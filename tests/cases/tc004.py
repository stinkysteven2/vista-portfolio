from helpers import login, result, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-004"


def run(page: Page):
    """TC-004: Uitloggen"""
    print("\n--- TC-004: Uitloggen ---")

    if not login(page):
        result(TC_ID, "Uitloggen", "GEBLOKKEERD",
               "Gebruiker is ingelogd voor aanvang van de test",
               "Inloggen mislukt — TC-004 kan niet worden uitgevoerd")
        return False

    try:
        page.locator("section#login i.material-icons:has-text('logout')").click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        result(TC_ID, "Klik op logout-icoon", "GEBLOKKEERD",
               "Logout-icoon klikbaar in navigatiebalk",
               f"Kon logout-knop niet vinden of klikken: {e}")
        return False

    has_login = page.locator("section#login i.material-icons:has-text('login')").count() > 0
    has_logout = page.locator("section#login i.material-icons:has-text('logout')").count() > 0

    if has_login and not has_logout:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc004-geslaagd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Uitloggen", "GESLAAGD",
               "Login-icoon zichtbaar; logout-icoon verdwenen",
               f"Login zichtbaar: {has_login} | Logout zichtbaar: {has_logout}",
               screenshot=screenshot_path)
        return True
    else:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc004-gefaald.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Uitloggen", "GEFAALD",
               "Login-icoon zichtbaar; logout-icoon verdwenen",
               f"Login zichtbaar: {has_login} | Logout zichtbaar: {has_logout}",
               screenshot=screenshot_path)
        return False
