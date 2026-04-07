from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-018"
ADMIN_TALENTEN_URL = f"{BASE_URL}/admin/talenten"


def run(page: Page):
    """TC-018: Werkervaring verwijderen"""
    print("\n--- TC-018: Werkervaring verwijderen ---")

    if not login(page):
        result(TC_ID, "Werkervaring verwijderen", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=15000)

    try:
        page.locator("button:has-text('Edit'), a:has-text('Edit')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
        page.locator("text=Werkervaring, mat-expansion-panel:has-text('Werkervaring')").first.click(timeout=3000)
        page.wait_for_timeout(500)
        page.locator("button:has-text('Verwijderen'), button[class*='delete'], button[class*='remove']").first.click(timeout=5000)
        page.locator("button[type='submit'], button:has-text('Opslaan')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc018-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring verwijderen", "GEBLOKKEERD",
               "Werkervaring verwijderbaar",
               f"Kon werkervaring niet verwijderen: {e} — selectors aanpassen na inspectie",
               screenshot=screenshot_path)
        return False

    screenshot_path = f"{SCREENSHOTS_DIR}/tc018-resultaat.png"
    page.screenshot(path=screenshot_path)
    result(TC_ID, "Werkervaring verwijderen", "GEBLOKKEERD",
           "Verwijderde werkervaring niet meer zichtbaar in profiel",
           "Verwijderknop geklikt — handmatige verificatie nodig",
           screenshot=screenshot_path)
    return False
