from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-005"
PROFILE_URL = f"{BASE_URL}/talentprofile/1"


def run(page: Page):
    """TC-005: Sessie beëindigd na uitloggen"""
    print("\n--- TC-005: Sessie beëindigd na uitloggen ---")

    # Stap 1: Log in
    if not login(page):
        result(TC_ID, "Sessie beëindigd na uitloggen", "GEBLOKKEERD",
               "Gebruiker is ingelogd voor aanvang van de test",
               "Inloggen mislukt — TC-005 kan niet worden uitgevoerd")
        return False

    # Stap 2: Navigeer naar een talentprofiel
    try:
        page.goto(PROFILE_URL, wait_until="networkidle", timeout=15000)
    except Exception as e:
        result(TC_ID, "Navigeer naar talentprofiel", "GEBLOKKEERD",
               f"Talentprofiel laadt op {PROFILE_URL}",
               f"Navigatie mislukt: {e}")
        return False

    # Stap 3: Uitloggen
    try:
        page.locator("section#login i.material-icons:has-text('logout')").click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        result(TC_ID, "Klik op logout-icoon", "GEBLOKKEERD",
               "Logout-icoon klikbaar na navigeren naar profiel",
               f"Kon logout-knop niet vinden of klikken: {e}")
        return False

    # Stap 4: Terugknop
    try:
        page.go_back(wait_until="networkidle", timeout=10000)
    except Exception as e:
        result(TC_ID, "Terugknop browser", "GEBLOKKEERD",
               "Browser navigeert terug naar talentprofiel",
               f"go_back mislukt: {e}")
        return False

    # Controleer: is de gebruiker uitgelogd (login-icoon zichtbaar)?
    current_url = page.url
    still_on_profile = "/talentprofile/" in current_url
    has_logout = page.locator("section#login i.material-icons:has-text('logout')").count() > 0
    has_login_icon = page.locator("section#login i.material-icons:has-text('login')").count() > 0

    # Zoek naar een login call-to-action op de profielpagina
    login_cta_visible = False
    for sel in ["text=Inloggen", "[class*='login']", "a[href*='login']"]:
        try:
            el = page.locator(sel).first
            if el.count() > 0 and el.is_visible():
                login_cta_visible = True
                break
        except Exception:
            pass

    screenshot_path = f"{SCREENSHOTS_DIR}/tc005-{'geslaagd' if not has_logout else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    session_ended = not has_logout
    if session_ended:
        result(TC_ID, "Sessie beëindigd na uitloggen", "GESLAAGD",
               "Beschermde content niet meer zichtbaar na uitloggen en terugknop",
               f"URL: {current_url} | Nog op profiel: {still_on_profile} | "
               f"Logout zichtbaar: {has_logout} | Login CTA zichtbaar: {login_cta_visible}",
               screenshot=screenshot_path)
        return True
    else:
        result(TC_ID, "Sessie beëindigd na uitloggen", "GEFAALD",
               "Beschermde content niet meer zichtbaar na uitloggen en terugknop",
               f"URL: {current_url} | Nog op profiel: {still_on_profile} | "
               f"Logout zichtbaar: {has_logout} — sessie lijkt actief na terugknop",
               screenshot=screenshot_path)
        return False
