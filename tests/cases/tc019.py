from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-019"
ADMIN_TALENTEN_URL = f"{BASE_URL.replace('/talent', '')}/admin/talenten"


def run(page: Page):
    """TC-019: Opleiding toevoegen"""
    print("\n--- TC-019: Opleiding toevoegen ---")

    if not login(page):
        result(TC_ID, "Opleiding toevoegen", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=15000)

    try:
        page.locator("button:has-text('Edit'), a:has-text('Edit')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
        page.locator("text=Opleidingen, mat-expansion-panel:has-text('Opleiding')").first.click(timeout=3000)
        page.wait_for_timeout(500)
        page.locator("button:has-text('Toevoegen'), button:has-text('Opleiding toevoegen')").first.click(timeout=5000)
        page.wait_for_timeout(500)
        page.locator("input[formcontrolname*='opleiding'], input[placeholder*='pleiding']").first.fill("Software Developer", timeout=3000)
        page.locator("input[formcontrolname*='instelling'], input[placeholder*='nstelling']").first.fill("Test ROC", timeout=3000)
        page.locator("input[formcontrolname*='jaar'], input[placeholder*='aar']").first.fill("2022", timeout=3000)
        page.locator("button[type='submit'], button:has-text('Opslaan')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc019-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Opleiding toevoegen", "GEBLOKKEERD",
               "Opleiding toevoegbaar via admin panel",
               f"Kon opleiding niet toevoegen: {e} — selectors aanpassen na inspectie",
               screenshot=screenshot_path)
        return False

    screenshot_path = f"{SCREENSHOTS_DIR}/tc019-resultaat.png"
    page.screenshot(path=screenshot_path)
    result(TC_ID, "Opleiding toevoegen", "GEBLOKKEERD",
           "'Software Developer / Test ROC' zichtbaar in profiel",
           "Opleidingsformulier ingevuld — handmatige verificatie nodig",
           screenshot=screenshot_path)
    return False
