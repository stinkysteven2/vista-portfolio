from helpers import login, result, BASE_URL, SCREENSHOTS_DIR, USERNAME, PASSWORD
from playwright.sync_api import Page

TC_ID = "TC-001"


def run(page: Page):
    """TC-001: Inloggen met geldige gegevens"""
    print("\n--- TC-001: Inloggen met geldige gegevens ---")

    page.goto(BASE_URL, wait_until="networkidle", timeout=15000)

    try:
        page.locator("section#login i.material-icons").click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        result(TC_ID, "Klik op login-icoon", "GEBLOKKEERD",
               "Login-icoon klikbaar in navigatiebalk",
               f"Kon login-knop niet vinden of klikken: {e}")
        return False

    try:
        page.locator("input[type='text']").first.fill(USERNAME, timeout=5000)
        page.locator("input[type='password']").first.fill(PASSWORD, timeout=5000)
    except Exception as e:
        result(TC_ID, "Invullen credentials", "GEBLOKKEERD",
               "Invoervelden voor gebruikersnaam en wachtwoord aanwezig",
               f"Kon velden niet vinden: {e}")
        return False

    try:
        page.locator("button[type='submit'], input[type='submit']").first.click(timeout=5000)
        page.wait_for_url(f"{BASE_URL}**", timeout=15000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        result(TC_ID, "Klik op Sign In", "GEFAALD",
               "Doorgestuurd terug naar IT Talenten Portaal na inloggen",
               f"Redirect mislukt of timeout: {e}")
        return False

    current_url = page.url
    has_logout = page.locator("section#login i.material-icons:has-text('logout')").count() > 0
    has_login = page.locator("section#login i.material-icons:has-text('login')").count() > 0

    if has_logout and not has_login:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc001-geslaagd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Inloggen met geldige gegevens", "GESLAAGD",
               "Doorgestuurd naar startpagina; logout-knop zichtbaar; login-knop verdwenen",
               f"URL: {current_url} | Logout zichtbaar: {has_logout} | Login zichtbaar: {has_login}",
               screenshot=screenshot_path)
        return True
    else:
        error_msg = ""
        for sel in ["[class*='error']", ".alert", "[class*='alert']", "mat-error"]:
            el = page.locator(sel).first
            if el.count() > 0 and el.is_visible():
                error_msg = el.inner_text().strip()
                break

        screenshot_path = f"{SCREENSHOTS_DIR}/tc001-gefaald.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Inloggen met geldige gegevens", "GEFAALD",
               "Doorgestuurd naar startpagina; logout-knop zichtbaar",
               f"URL: {current_url} | Logout zichtbaar: {has_logout} | Login zichtbaar: {has_login}" +
               (f" | Foutmelding: '{error_msg}'" if error_msg else ""),
               screenshot=screenshot_path)
        return False
