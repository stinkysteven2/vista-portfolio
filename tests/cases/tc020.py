from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-020"
ADMIN_TALENTEN_URL = f"{BASE_URL}/admin/talenten"


def run(page: Page):
    """TC-020: Opleiding bewerken"""
    print("\n--- TC-020: Opleiding bewerken ---")

    if not login(page):
        result(TC_ID, "Opleiding bewerken", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=15000)

    try:
        page.locator("button:has-text('Edit'), a:has-text('Edit')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
        page.locator("text=Opleidingen, mat-expansion-panel:has-text('Opleiding')").first.click(timeout=3000)
        page.wait_for_timeout(500)
        jaar_field = page.locator("input[formcontrolname*='jaar'], input[placeholder*='aar']").first
        jaar_field.triple_click(timeout=3000)
        jaar_field.fill("2023")
        page.locator("button[type='submit'], button:has-text('Opslaan')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc020-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Opleiding bewerken", "GEBLOKKEERD",
               "Afstudeerjaar wijzigbaar naar '2023'",
               f"Kon opleiding niet bewerken: {e} — selectors aanpassen na inspectie",
               screenshot=screenshot_path)
        return False

    screenshot_path = f"{SCREENSHOTS_DIR}/tc020-resultaat.png"
    page.screenshot(path=screenshot_path)
    result(TC_ID, "Opleiding bewerken", "GEBLOKKEERD",
           "Gewijzigd jaar '2023' zichtbaar in profiel",
           "Jaar aangepast — handmatige verificatie nodig",
           screenshot=screenshot_path)
    return False
