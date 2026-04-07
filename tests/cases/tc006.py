from helpers import result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-006"
PROFILE_URL = f"{BASE_URL}/talentprofile/1"


def run(page: Page):
    """TC-006: Talentprofiel afgeschermd voor bezoekers"""
    print("\n--- TC-006: Talentprofiel afgeschermd voor bezoekers ---")

    # Navigeer direct naar profiel zonder in te loggen
    try:
        page.goto(PROFILE_URL, wait_until="networkidle", timeout=15000)
    except Exception as e:
        result(TC_ID, "Navigeer naar talentprofiel zonder login", "GEBLOKKEERD",
               f"Talentprofiel laadt op {PROFILE_URL}",
               f"Navigatie mislukt: {e}")
        return False

    current_url = page.url

    # Zoek naar login call-to-action
    login_cta_visible = False
    for sel in ["text=Inloggen", "text=Log in", "[class*='login']", "a[href*='login']", "button:has-text('Inloggen')"]:
        try:
            el = page.locator(sel).first
            if el.count() > 0 and el.is_visible():
                login_cta_visible = True
                break
        except Exception:
            pass

    # Controleer of naam/contactgegevens NIET zichtbaar zijn
    # Zoek naar elementen die typisch persoonsgegevens bevatten
    personal_data_visible = False
    for sel in ["[class*='contact']", "[class*='phone']", "[class*='email']", "a[href^='mailto']", "a[href^='tel']"]:
        try:
            el = page.locator(sel).first
            if el.count() > 0 and el.is_visible():
                personal_data_visible = True
                break
        except Exception:
            pass

    screenshot_path = f"{SCREENSHOTS_DIR}/tc006-{'geslaagd' if login_cta_visible and not personal_data_visible else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    if login_cta_visible and not personal_data_visible:
        result(TC_ID, "Talentprofiel afgeschermd voor bezoekers", "GESLAAGD",
               "Naam en contactgegevens niet zichtbaar; login call-to-action aanwezig",
               f"URL: {current_url} | Login CTA: {login_cta_visible} | Persoonsgegevens zichtbaar: {personal_data_visible}",
               screenshot=screenshot_path)
        return True
    elif personal_data_visible:
        result(TC_ID, "Talentprofiel afgeschermd voor bezoekers", "GEFAALD",
               "Naam en contactgegevens niet zichtbaar; login call-to-action aanwezig",
               f"URL: {current_url} | Login CTA: {login_cta_visible} | Persoonsgegevens zichtbaar: {personal_data_visible}",
               screenshot=screenshot_path)
        return False
    else:
        result(TC_ID, "Talentprofiel afgeschermd voor bezoekers", "GEBLOKKEERD",
               "Naam en contactgegevens niet zichtbaar; login call-to-action aanwezig",
               f"URL: {current_url} | Login CTA: {login_cta_visible} | Persoonsgegevens zichtbaar: {personal_data_visible} — selectors mogelijk onjuist, handmatige controle nodig",
               screenshot=screenshot_path)
        return False
