"""
Exploratory crawl script for IT Talenten Portaal
Simulates a tester doing an unplanned first pass: navigates pages,
clicks through content, checks for visible errors, broken links, and
console/network issues. Outputs findings to stdout.
"""

import re
import time
from urllib.parse import urljoin, urlparse
from playwright.sync_api import sync_playwright, Page

BASE_URL = "https://it-talenten-portaal-test-it-talenten-webapp-test.iapmkw.easypanel.host/talent"

visited: set[str] = set()
findings: list[dict] = []
console_errors: list[dict] = []
network_errors: list[dict] = []


def log_finding(severity: str, page_url: str, action: str, expected: str, actual: str, location: str = ""):
    finding = {
        "severity": severity,       # Hoog / Gemiddeld / Laag
        "page": page_url,
        "action": action,
        "expected": expected,
        "actual": actual,
        "location": location,
    }
    findings.append(finding)
    print(f"  [{severity.upper()}] {action} -> {actual}")


def check_page(page: Page, url: str, label: str):
    print(f"\n--- Pagina: {label} ({url}) ---")

    # Collect console errors on this page
    page_console_errors = []
    page.on("console", lambda msg: page_console_errors.append(msg) if msg.type == "error" else None)

    # Collect failed network requests
    page_network_errors = []
    page.on("requestfailed", lambda req: page_network_errors.append(req))

    try:
        resp = page.goto(url, wait_until="networkidle", timeout=15000)
    except Exception as e:
        log_finding("Hoog", url, f"Pagina laden: {label}", "Pagina laadt succesvol", f"Fout bij laden: {e}")
        return []

    # Check HTTP status
    if resp and resp.status >= 400:
        log_finding("Hoog", url, f"HTTP status voor {label}", "2xx of 3xx", f"HTTP {resp.status}")

    # Check page title
    title = page.title()
    if not title or title.strip() == "":
        log_finding("Laag", url, "Paginatitel", "Beschrijvende titel aanwezig", "Geen paginatitel (leeg <title>)")
    else:
        print(f"  Titel: {title}")

    # Check for visible error messages in the DOM
    for selector in ["[class*='error']", "[class*='Error']", "[id*='error']", ".alert-danger", ".toast-error"]:
        try:
            els = page.locator(selector).all()
            for el in els:
                if el.is_visible():
                    text = el.inner_text().strip()
                    if text:
                        log_finding("Gemiddeld", url, f"Foutmelding zichtbaar op pagina ({selector})",
                                    "Geen foutmeldingen op een normale pagina", f"Tekst: '{text}'")
        except Exception:
            pass

    # Check images for broken src or missing alt
    images = page.locator("img").all()
    for img in images:
        try:
            src = img.get_attribute("src") or ""
            alt = img.get_attribute("alt")
            if not src:
                log_finding("Gemiddeld", url, "Afbeelding zonder src", "src attribuut aanwezig", "Afbeelding heeft geen src")
            if alt is None:
                log_finding("Laag", url, "Afbeelding zonder alt-tekst", "alt attribuut aanwezig voor toegankelijkheid",
                            f"Afbeelding '{src[:60]}' mist alt attribuut")
        except Exception:
            pass

    # Check all links — collect internal ones for follow-up
    internal_links = []
    links = page.locator("a[href]").all()
    for link in links:
        try:
            href = link.get_attribute("href") or ""
            text = link.inner_text().strip() or "(geen tekst)"
            if not href or href == "#":
                log_finding("Laag", url, f"Link zonder bestemming: '{text}'",
                            "Link verwijst naar een pagina", f"href='{href}'")
                continue
            full = urljoin(url, href)
            parsed = urlparse(full)
            if parsed.netloc in urlparse(BASE_URL).netloc or parsed.netloc == urlparse(url).netloc:
                if full not in visited:
                    internal_links.append((full, text))
        except Exception:
            pass

    # Check buttons without accessible text
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text().strip()
            aria = btn.get_attribute("aria-label") or ""
            if not text and not aria:
                log_finding("Laag", url, "Knop zonder tekst of aria-label",
                            "Knop heeft zichtbare tekst of aria-label", "Knop is niet toegankelijk")
        except Exception:
            pass

    # Check forms for basic issues
    forms = page.locator("form").all()
    for i, form in enumerate(forms, 1):
        inputs = form.locator("input, textarea, select").all()
        for inp in inputs:
            try:
                input_type = inp.get_attribute("type") or "text"
                label_for = inp.get_attribute("id")
                placeholder = inp.get_attribute("placeholder") or ""
                # Check if there's an associated label
                if label_for:
                    lbl = page.locator(f"label[for='{label_for}']")
                    if lbl.count() == 0 and not placeholder:
                        log_finding("Gemiddeld", url, f"Formulierveld zonder label (type={input_type})",
                                    "Elk veld heeft een <label> of placeholder",
                                    f"Input id='{label_for}' heeft geen label en geen placeholder")
            except Exception:
                pass

    # Report console errors
    time.sleep(0.5)  # let late console messages arrive
    for msg in page_console_errors:
        log_finding("Gemiddeld", url, "JavaScript console error",
                    "Geen JS-fouten in de console", f"{msg.text[:200]}")

    # Report network failures
    for req in page_network_errors:
        log_finding("Gemiddeld", url, f"Netwerk request mislukt: {req.url[:80]}",
                    "Alle resources laden succesvol", f"Fout: {req.failure}")

    return internal_links


def check_responsiveness(page: Page, url: str):
    print(f"\n--- Responsiviteit check ---")
    viewports = [
        ("Desktop (1280x800)", 1280, 800),
        ("Tablet (768x1024)", 768, 1024),
        ("Mobiel (390x844)", 390, 844),
    ]
    for name, width, height in viewports:
        page.set_viewport_size({"width": width, "height": height})
        page.goto(url, wait_until="networkidle", timeout=15000)
        # Check for horizontal overflow (common mobile bug)
        overflow = page.evaluate("""() => {
            return document.body.scrollWidth > window.innerWidth;
        }""")
        if overflow:
            scroll_width = page.evaluate("document.body.scrollWidth")
            log_finding("Gemiddeld", url, f"Horizontale scroll op {name}",
                        "Geen horizontale scroll — responsive layout",
                        f"scrollWidth={scroll_width}px > viewportWidth={width}px",
                        location=name)
        else:
            print(f"  {name}: OK (geen horizontale scroll)")


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        print("=" * 60)
        print("EXPLORATORY TEST — IT Talenten Portaal")
        print("=" * 60)

        # --- Pass 1: home page ---
        visited.add(BASE_URL)
        internal_links = check_page(page, BASE_URL, "Startpagina")

        # --- Pass 2: follow internal links (one level deep) ---
        to_visit = internal_links[:20]  # cap at 20 to keep it manageable
        for link_url, link_text in to_visit:
            if link_url not in visited:
                visited.add(link_url)
                check_page(page, link_url, link_text[:50])

        # --- Pass 3: responsiveness on home page ---
        check_responsiveness(page, BASE_URL)

        browser.close()

    # --- Summary ---
    print("\n" + "=" * 60)
    print(f"SAMENVATTING: {len(findings)} bevindingen gevonden op {len(visited)} pagina's")
    print("=" * 60)
    severities = {"Hoog": [], "Gemiddeld": [], "Laag": []}
    for f in findings:
        severities.get(f["severity"], []).append(f)

    for sev in ["Hoog", "Gemiddeld", "Laag"]:
        items = severities[sev]
        if items:
            print(f"\n[{sev.upper()}] ({len(items)}x)")
            for f in items:
                print(f"  • Pagina: {f['page']}")
                print(f"    Actie:  {f['action']}")
                print(f"    Verwacht: {f['expected']}")
                print(f"    Werkelijk: {f['actual']}")
                if f['location']:
                    print(f"    Locatie: {f['location']}")


if __name__ == "__main__":
    main()
