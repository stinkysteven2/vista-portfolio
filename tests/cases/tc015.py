from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-015"
ADMIN_TALENTEN_URL = f"{BASE_URL.replace('/talent', '')}/admin/talenten"


def run(page: Page):
    """TC-015: Talent verwijderen"""
    print("\n--- TC-015: Talent verwijderen ---")

    if not login(page):
        result(TC_ID, "Talent verwijderen", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=15000)

    if "/admin" not in page.url:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc015-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Talent verwijderen", "GEBLOKKEERD",
               "Admin panel toegankelijk",
               f"Geen toegang tot admin panel — URL: {page.url}",
               screenshot=screenshot_path)
        return False

    # Zoek Test Talent en klik Delete
    try:
        row = page.locator("tr:has-text('Test'), tr:has-text('Talent')").first
        row.locator("button:has-text('Delete'), button:has-text('Verwijderen')").first.click(timeout=5000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc015-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Talent verwijderen", "GEBLOKKEERD",
               "Delete knop voor Test Talent aanwezig",
               f"Test Talent of Delete knop niet gevonden: {e}",
               screenshot=screenshot_path)
        return False

    # Bevestig indien gevraagd
    try:
        confirm = page.locator("button:has-text('Ja'), button:has-text('Bevestig'), button:has-text('OK'), button:has-text('Verwijderen')").first
        if confirm.count() > 0 and confirm.is_visible():
            confirm.click(timeout=3000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception:
        pass

    # Controleer dat Test Talent weg is
    talent_gone = page.locator("text=Test Talent").count() == 0

    screenshot_path = f"{SCREENSHOTS_DIR}/tc015-{'geslaagd' if talent_gone else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    if talent_gone:
        result(TC_ID, "Talent verwijderen", "GESLAAGD",
               "Test Talent niet meer zichtbaar in talentenlijst",
               "Test Talent niet gevonden in lijst na verwijdering",
               screenshot=screenshot_path)
        return True
    else:
        result(TC_ID, "Talent verwijderen", "GEFAALD",
               "Test Talent niet meer zichtbaar in talentenlijst",
               "Test Talent nog steeds aanwezig in lijst",
               screenshot=screenshot_path)
        return False
