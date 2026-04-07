from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-014"
ADMIN_TALENTEN_URL = f"{BASE_URL}/admin/talenten"


def run(page: Page):
    """TC-014: Talent bewerken"""
    print("\n--- TC-014: Talent bewerken ---")

    if not login(page):
        result(TC_ID, "Talent bewerken", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=15000)

    if "/admin" not in page.url:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc014-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Talent bewerken", "GEBLOKKEERD",
               "Admin panel toegankelijk",
               f"Geen toegang tot admin panel — URL: {page.url}",
               screenshot=screenshot_path)
        return False

    # Zoek Test Talent en klik Edit
    try:
        row = page.locator("tr:has-text('Test'), tr:has-text('Talent')").first
        row.locator("button:has-text('Edit'), a:has-text('Edit'), button:has-text('Bewerken')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc014-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Talent bewerken", "GEBLOKKEERD",
               "Edit knop voor Test Talent aanwezig",
               f"Test Talent of Edit knop niet gevonden: {e}",
               screenshot=screenshot_path)
        return False

    # Wijzig woonplaats
    try:
        woonplaats_field = page.locator("input[formcontrolname='woonplaats'], input[placeholder*='oonplaats']").first
        woonplaats_field.triple_click(timeout=3000)
        woonplaats_field.fill("Gewijzigdstad")
        page.locator("button[type='submit'], button:has-text('Opslaan')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc014-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Talent bewerken", "GEBLOKKEERD",
               "Woonplaats wijzigbaar naar 'Gewijzigdstad'",
               f"Kon veld niet aanpassen: {e}",
               screenshot=screenshot_path)
        return False

    # Controleer in de lijst
    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=15000)
    updated = page.locator("text=Gewijzigdstad").count() > 0

    screenshot_path = f"{SCREENSHOTS_DIR}/tc014-{'geslaagd' if updated else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    if updated:
        result(TC_ID, "Talent bewerken", "GESLAAGD",
               "Woonplaats bijgewerkt naar 'Gewijzigdstad' in talentenlijst",
               "Woonplaats 'Gewijzigdstad' zichtbaar in lijst",
               screenshot=screenshot_path)
        return True
    else:
        result(TC_ID, "Talent bewerken", "GEFAALD",
               "Woonplaats bijgewerkt naar 'Gewijzigdstad' in talentenlijst",
               "Woonplaats 'Gewijzigdstad' niet gevonden in lijst",
               screenshot=screenshot_path)
        return False
