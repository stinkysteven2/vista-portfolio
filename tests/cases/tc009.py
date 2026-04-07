from helpers import result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-009"
MIN_HOURS = 20
MAX_HOURS = 32


def run(page: Page):
    """TC-009: Filteren op beschikbaarheid (grenswaarden)"""
    print("\n--- TC-009: Filteren op beschikbaarheid (grenswaarden) ---")

    page.goto(BASE_URL, wait_until="networkidle", timeout=15000)

    # Zoek beschikbaarheidsfilter (slider of invoervelden)
    filter_found = False
    for sel in [
        "[class*='beschikbaarheid']",
        "[class*='availability']",
        "mat-slider",
        "[placeholder*='uur']",
        "[placeholder*='beschikbaar']",
    ]:
        el = page.locator(sel).first
        if el.count() > 0 and el.is_visible():
            filter_found = True
            break

    if not filter_found:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc009-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Filteren op beschikbaarheid (grenswaarden)", "GEBLOKKEERD",
               f"Beschikbaarheidsfilter aanwezig; talenten met {MIN_HOURS}–{MAX_HOURS} uur worden getoond",
               "Beschikbaarheidsfilter niet gevonden — selector aanpassen na inspectie",
               screenshot=screenshot_path)
        return False

    # Probeer min/max in te vullen als er invoervelden zijn
    inputs = page.locator("input[type='number']")
    if inputs.count() >= 2:
        try:
            inputs.nth(0).fill(str(MIN_HOURS))
            inputs.nth(1).fill(str(MAX_HOURS))
            page.keyboard.press("Enter")
            page.wait_for_load_state("networkidle", timeout=10000)
        except Exception as e:
            screenshot_path = f"{SCREENSHOTS_DIR}/tc009-geblokkeerd.png"
            page.screenshot(path=screenshot_path)
            result(TC_ID, "Filteren op beschikbaarheid (grenswaarden)", "GEBLOKKEERD",
                   f"Grenswaarden {MIN_HOURS}–{MAX_HOURS} uur invulbaar",
                   f"Kon filter niet invullen: {e}",
                   screenshot=screenshot_path)
            return False

    screenshot_path = f"{SCREENSHOTS_DIR}/tc009-resultaat.png"
    page.screenshot(path=screenshot_path)

    result(TC_ID, "Filteren op beschikbaarheid (grenswaarden)", "GEBLOKKEERD",
           f"Talenten buiten {MIN_HOURS}–{MAX_HOURS} uur vallen af",
           "Filter gevonden maar resultaatvalidatie vereist handmatige controle — zie screenshot",
           screenshot=screenshot_path)
    return False
