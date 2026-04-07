from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-016"
ADMIN_TALENTEN_URL = f"{BASE_URL}/admin/talenten"


def run(page: Page):
    """TC-016: Werkervaring toevoegen"""
    print("\n--- TC-016: Werkervaring toevoegen ---")

    if not login(page):
        result(TC_ID, "Werkervaring toevoegen", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=15000)

    if "/admin" not in page.url:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc016-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring toevoegen", "GEBLOKKEERD",
               "Admin panel toegankelijk", f"Geen toegang — URL: {page.url}",
               screenshot=screenshot_path)
        return False

    # Open eerste talent via Edit
    try:
        page.locator("button:has-text('Edit'), a:has-text('Edit')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc016-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring toevoegen", "GEBLOKKEERD",
               "Edit knop voor een talent aanwezig", f"Edit knop niet gevonden: {e}",
               screenshot=screenshot_path)
        return False

    # Open Werkervaring paneel
    try:
        page.locator("text=Werkervaring, [class*='werkervaring'], mat-expansion-panel:has-text('Werkervaring')").first.click(timeout=3000)
        page.wait_for_timeout(500)
    except Exception:
        pass

    # Voeg werkervaring toe
    try:
        page.locator("button:has-text('Toevoegen'), button:has-text('Werkervaring toevoegen'), button[class*='add']").first.click(timeout=5000)
        page.wait_for_timeout(500)
        page.locator("input[placeholder*='erkgever'], input[formcontrolname*='werkgever']").first.fill("Test BV", timeout=3000)
        page.locator("input[placeholder*='unctie'], input[formcontrolname*='functie']").first.fill("Tester", timeout=3000)
        page.locator("button[type='submit'], button:has-text('Opslaan')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc016-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring toevoegen", "GEBLOKKEERD",
               "Werkervaring toevoegbaar via admin panel",
               f"Kon werkervaring niet toevoegen: {e} — selectors aanpassen na inspectie",
               screenshot=screenshot_path)
        return False

    screenshot_path = f"{SCREENSHOTS_DIR}/tc016-resultaat.png"
    page.screenshot(path=screenshot_path)
    result(TC_ID, "Werkervaring toevoegen", "GEBLOKKEERD",
           "Werkervaring 'Test BV / Tester' zichtbaar in profiel",
           "Werkervaring-formulier ingevuld en opgeslagen — handmatige verificatie nodig",
           screenshot=screenshot_path)
    return False
