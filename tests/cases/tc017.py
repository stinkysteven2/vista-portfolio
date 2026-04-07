from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-017"
ADMIN_TALENTEN_URL = f"{BASE_URL}/admin/talenten"


def run(page: Page):
    """TC-017: Werkervaring bewerken"""
    print("\n--- TC-017: Werkervaring bewerken ---")

    if not login(page):
        result(TC_ID, "Werkervaring bewerken", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=15000)

    try:
        page.locator("button:has-text('Edit'), a:has-text('Edit')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc017-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring bewerken", "GEBLOKKEERD",
               "Edit knop aanwezig", f"Edit knop niet gevonden: {e}", screenshot=screenshot_path)
        return False

    try:
        page.locator("text=Werkervaring, mat-expansion-panel:has-text('Werkervaring')").first.click(timeout=3000)
        page.wait_for_timeout(500)
        functie_field = page.locator("input[formcontrolname*='functie'], input[placeholder*='unctie']").first
        functie_field.triple_click(timeout=3000)
        functie_field.fill("Senior Tester")
        page.locator("button[type='submit'], button:has-text('Opslaan')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc017-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring bewerken", "GEBLOKKEERD",
               "Functietitel wijzigbaar naar 'Senior Tester'",
               f"Kon werkervaring niet bewerken: {e} — selectors aanpassen na inspectie",
               screenshot=screenshot_path)
        return False

    screenshot_path = f"{SCREENSHOTS_DIR}/tc017-resultaat.png"
    page.screenshot(path=screenshot_path)
    result(TC_ID, "Werkervaring bewerken", "GEBLOKKEERD",
           "'Senior Tester' zichtbaar in profiel",
           "Functietitel aangepast — handmatige verificatie of profiel correct bijgewerkt",
           screenshot=screenshot_path)
    return False
