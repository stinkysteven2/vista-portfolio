"""
Authenticated crawl script for IT Talenten Portaal
Explores both public and authenticated pages.
Goal: discover actual functionality for SRS writing.
"""

import os
import time
from urllib.parse import urljoin, urlparse
from playwright.sync_api import sync_playwright, Page
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://talenten-portaal-tp-test-webapp.iapmkw.easypanel.host"
USERNAME = os.getenv("TALENTEN_USERNAME", "admin")
PASSWORD = os.getenv("TALENTEN_PASSWORD")

visited: set[str] = set()
pages_found: list[dict] = set()
findings: list[dict] = []


def log(msg):
    print(str(msg).encode("utf-8", errors="replace").decode("utf-8"))


def get_page_info(page: Page, url: str, label: str) -> dict:
    info = {
        "url": url,
        "label": label,
        "title": "",
        "headings": [],
        "forms": [],
        "links": [],
        "buttons": [],
        "errors": [],
    }

    try:
        page.goto(url, wait_until="networkidle", timeout=20000)
    except Exception as e:
        info["errors"].append(f"Laden mislukt: {e}")
        return info

    info["title"] = page.title()

    # Headings — give us a sense of page structure
    for tag in ["h1", "h2", "h3"]:
        els = page.locator(tag).all()
        for el in els:
            try:
                text = el.inner_text().strip()
                if text:
                    info["headings"].append(f"{tag}: {text}")
            except Exception:
                pass

    # Forms — what inputs exist?
    forms = page.locator("form").all()
    for i, form in enumerate(forms, 1):
        form_info = {"index": i, "inputs": []}
        inputs = form.locator("input, textarea, select").all()
        for inp in inputs:
            try:
                input_type = inp.get_attribute("type") or "text"
                name = inp.get_attribute("name") or inp.get_attribute("id") or inp.get_attribute("placeholder") or "?"
                form_info["inputs"].append(f"{input_type}: {name}")
            except Exception:
                pass
        info["forms"].append(form_info)

    # Buttons
    buttons = page.locator("button, [role='button']").all()
    for btn in buttons:
        try:
            text = btn.inner_text().strip()
            if text:
                info["buttons"].append(text)
        except Exception:
            pass

    # Internal links
    links = page.locator("a[href]").all()
    for link in links:
        try:
            href = link.get_attribute("href") or ""
            text = link.inner_text().strip() or href
            full = urljoin(BASE_URL, href)
            parsed = urlparse(full)
            base_parsed = urlparse(BASE_URL)
            if parsed.netloc == base_parsed.netloc and full not in visited:
                info["links"].append((full, text[:60]))
        except Exception:
            pass

    return info


def print_page_info(info: dict):
    log(f"\n{'='*60}")
    log(f"PAGINA: {info['label']}")
    log(f"URL:    {info['url']}")
    log(f"Titel:  {info['title']}")

    if info["headings"]:
        log("Koppen:")
        for h in info["headings"][:10]:
            log(f"  {h}")

    if info["forms"]:
        log("Formulieren:")
        for f in info["forms"]:
            log(f"  Formulier {f['index']}: {', '.join(f['inputs'])}")

    if info["buttons"]:
        unique_buttons = list(dict.fromkeys(info["buttons"]))
        log(f"Knoppen: {', '.join(unique_buttons[:15])}")

    if info["errors"]:
        log(f"FOUTEN: {info['errors']}")


KEYCLOAK_BASE = "https://keycloak-test-keycloak-test-instance.iapmkw.easypanel.host"
KEYCLOAK_REALM = "talentenportaal-test"


def try_login(page: Page) -> bool:
    log("\n--- Inloggen via Keycloak ---")
    try:
        # Navigate to a protected route — app will redirect to Keycloak
        page.goto(BASE_URL + "/talenten", wait_until="domcontentloaded", timeout=20000)
        page.wait_for_timeout(3000)
        log(f"URL na navigatie naar /talenten: {page.url}")

        # If not on Keycloak yet, try forcing login via the auth endpoint
        if "keycloak" not in page.url:
            keycloak_login = f"{KEYCLOAK_BASE}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/auth"
            page.goto(keycloak_login, wait_until="domcontentloaded", timeout=20000)
            page.wait_for_timeout(2000)
            log(f"URL na directe navigatie naar Keycloak: {page.url}")

        if page.locator("input[type='password']").count() == 0:
            log("Geen wachtwoordveld gevonden op Keycloak-pagina.")
            log(f"Huidige URL: {page.url}, titel: {page.title()}")
            return False

        # Fill credentials on Keycloak login form
        for selector in ["input[id='username']", "input[name='username']", "input[type='text']"]:
            if page.locator(selector).count() > 0:
                page.locator(selector).first.fill(USERNAME)
                log(f"Gebruikersnaam ingevuld via: {selector}")
                break

        page.locator("input[type='password']").first.fill(PASSWORD)
        log("Wachtwoord ingevuld")

        for selector in ["input[type='submit']", "button[type='submit']", "#kc-login"]:
            if page.locator(selector).count() > 0:
                page.locator(selector).first.click()
                log(f"Formulier ingediend via: {selector}")
                break

        page.wait_for_load_state("networkidle", timeout=15000)
        log(f"URL na inloggen: {page.url}")
        log(f"Titel na inloggen: {page.title()}")

        if "keycloak" in page.url.lower():
            # Check for error messages
            error = page.locator(".alert-error, #input-error, .kc-feedback-text").first
            if error.count() > 0:
                log(f"Keycloak foutmelding: {error.inner_text()}")
            log("WAARSCHUWING: Nog op Keycloak — inloggen mislukt?")
            return False

        log("Inloggen geslaagd.")
        return True

    except Exception as e:
        log(f"Inloggen mislukt: {e}")
        return False


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        log("=" * 60)
        log("AUTHENTICATED CRAWL — IT Talenten Portaal")
        log("=" * 60)

        # Step 1: Public pages
        log("\n\n### FASE 1: PUBLIEKE PAGINA'S ###")
        public_info = get_page_info(page, BASE_URL, "Startpagina (publiek)")
        print_page_info(public_info)
        visited.add(BASE_URL)

        # Follow one level of public links
        for link_url, link_text in public_info["links"][:10]:
            if link_url not in visited:
                visited.add(link_url)
                info = get_page_info(page, link_url, link_text)
                print_page_info(info)

        # Step 2: Login
        log("\n\n### FASE 2: INLOGGEN ###")
        logged_in = try_login(page)

        if logged_in:
            # Step 3: Authenticated pages
            log("\n\n### FASE 3: INGELOGDE PAGINA'S ###")
            current_url = page.url
            visited.add(current_url)

            # Get info on landing page after login
            info = get_page_info(page, current_url, "Landingspagina na login")
            print_page_info(info)

            # Follow links from authenticated landing page
            all_links = info["links"][:]
            visited_count = 0
            while all_links and visited_count < 20:
                link_url, link_text = all_links.pop(0)
                if link_url not in visited:
                    visited.add(link_url)
                    visited_count += 1
                    link_info = get_page_info(page, link_url, link_text)
                    print_page_info(link_info)
                    # Add newly discovered links
                    for new_link in link_info["links"]:
                        if new_link[0] not in visited:
                            all_links.append(new_link)

        log("\n\n### SAMENVATTING ###")
        log(f"Totaal bezochte pagina's: {len(visited)}")
        for url in sorted(visited):
            log(f"  {url}")

        browser.close()


if __name__ == "__main__":
    main()
