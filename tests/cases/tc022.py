from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-022"
ADMIN_TALENTEN_URL = f"{BASE_URL}/admin/talenten"


def run(page: Page):
    """TC-022: Hobby/interesse toevoegen"""
    print("\n--- TC-022: Hobby/interesse toevoegen ---")

    if not login(page):
        result(TC_ID, "Hobby/interesse toevoegen", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=15000)

    try:
        page.locator("button:has-text('Edit'), a:has-text('Edit')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
        page.locator("text=Hobby, mat-expansion-panel:has-text('Hobby')").first.click(timeout=3000)
        page.wait_for_timeout(500)
        page.locator("button:has-text('Toevoegen'), button:has-text('Hobby toevoegen')").first.click(timeout=5000)
        page.wait_for_timeout(500)
        page.locator("input[formcontrolname*='hobby'], input[formcontrolname*='interesse'], input[placeholder*='obby']").first.fill("Schaken", timeout=3000)
        page.locator("button[type='submit'], button:has-text('Opslaan')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc022-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Hobby/interesse toevoegen", "GEBLOKKEERD",
               "Hobby 'Schaken' toevoegbaar via admin panel",
               f"Kon hobby niet toevoegen: {e} — selectors aanpassen na inspectie",
               screenshot=screenshot_path)
        return False

    screenshot_path = f"{SCREENSHOTS_DIR}/tc022-resultaat.png"
    page.screenshot(path=screenshot_path)
    result(TC_ID, "Hobby/interesse toevoegen", "GEBLOKKEERD",
           "'Schaken' zichtbaar in profiel",
           "Hobbyformulier ingevuld — handmatige verificatie nodig",
           screenshot=screenshot_path)
    return False
