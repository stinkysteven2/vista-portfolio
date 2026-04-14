from helpers import result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-008"
FILTER_PROVINCE = "Gelderland"


def count_talents(page: Page) -> int:
    """Lees het aantal talenten uit de 'Zoekresultaten (X)' kop."""
    import re
    try:
        tekst = page.locator("h1:has-text('Zoekresultaten')").first.inner_text(timeout=5000)
        match = re.search(r'\((\d+)\)', tekst)
        if match:
            return int(match.group(1))
    except Exception:
        pass
    return -1  # onbekend


def run(page: Page):
    """TC-008: Filteren op provincie"""
    print("\n--- TC-008: Filteren op provincie ---")

    page.goto(BASE_URL, wait_until="networkidle", timeout=15000)

    # Cookie banner wegklikken indien aanwezig
    try:
        page.locator("app-cookie-banner .btn.decline").click(timeout=3000)
        page.wait_for_timeout(300)
    except Exception:
        pass

    # Tel ongefilterde talenten
    total_before = count_talents(page)

    try:
        # Provincie accordion openen (zit al in de sidebar, geen extra panel nodig)
        provincie_header = page.locator(".accordion-item-header:has-text('Provincie')").first
        if provincie_header.count() == 0:
            raise Exception("Provincie accordion header niet gevonden")
        provincie_header.click(timeout=3000)
        page.wait_for_timeout(500)

        # Klik de provincie radio button
        radio = page.locator(f"mat-radio-button:has-text('{FILTER_PROVINCE}')").first
        if radio.count() == 0:
            raise Exception(f"Radio button '{FILTER_PROVINCE}' niet gevonden")
        radio.click(timeout=3000)
        page.wait_for_load_state("networkidle", timeout=10000)

        # Wacht tot Zoekresultaten-teller verandert (Angular update)
        page.wait_for_function(
            "before => { const h1 = document.querySelector('h1'); const m = h1 && h1.innerText.match(/\\((\\d+)\\)/); return m && parseInt(m[1]) !== before; }",
            arg=total_before,
            timeout=5000
        )

    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc008-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Filteren op provincie", "GEBLOKKEERD",
               f"Filteroptie '{FILTER_PROVINCE}' selecteerbaar",
               f"Kon filter niet activeren: {e}",
               screenshot=screenshot_path)
        return False

    total_after = count_talents(page)
    filtered_correctly = total_after != -1 and (total_after <= total_before or total_before == -1)

    screenshot_path = f"{SCREENSHOTS_DIR}/tc008-{'geslaagd' if filtered_correctly else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    if filtered_correctly:
        result(TC_ID, "Filteren op provincie", "GESLAAGD",
               f"Alleen talenten uit {FILTER_PROVINCE} getoond; aantal ≤ totaal",
               f"Voor filter: {total_before} | Na filter ({FILTER_PROVINCE}): {total_after}",
               screenshot=screenshot_path)
        return True
    else:
        result(TC_ID, "Filteren op provincie", "GEFAALD",
               f"Alleen talenten uit {FILTER_PROVINCE} getoond; aantal ≤ totaal",
               f"Voor filter: {total_before} | Na filter ({FILTER_PROVINCE}): {total_after}",
               screenshot=screenshot_path)
        return False
