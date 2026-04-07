from helpers import result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-011"
PROFILE_URL = f"{BASE_URL}/talentprofile/1"


def run(page: Page):
    """TC-011: Talentprofiel gedeeltelijk zichtbaar voor bezoeker"""
    print("\n--- TC-011: Talentprofiel gedeeltelijk zichtbaar voor bezoeker ---")

    page.goto(PROFILE_URL, wait_until="networkidle", timeout=15000)

    # Moet zichtbaar zijn voor bezoeker
    public_visible = False
    for sel in ["[class*='skill']", "[class*='vaardigheid']", "[class*='beschikbaar']", "[class*='availability']", "[class*='province']", "[class*='provincie']"]:
        try:
            el = page.locator(sel).first
            if el.count() > 0 and el.is_visible():
                public_visible = True
                break
        except Exception:
            pass

    # Mag NIET zichtbaar zijn voor bezoeker
    personal_visible = False
    for sel in ["a[href^='mailto']", "a[href^='tel']", "[class*='contact-detail']", "[class*='phone']", "[class*='email']"]:
        try:
            el = page.locator(sel).first
            if el.count() > 0 and el.is_visible():
                personal_visible = True
                break
        except Exception:
            pass

    # Login CTA moet aanwezig zijn
    login_cta = False
    for sel in ["text=Inloggen", "button:has-text('Inloggen')", "a:has-text('Inloggen')", "[class*='login']"]:
        try:
            el = page.locator(sel).first
            if el.count() > 0 and el.is_visible():
                login_cta = True
                break
        except Exception:
            pass

    screenshot_path = f"{SCREENSHOTS_DIR}/tc011-resultaat.png"
    page.screenshot(path=screenshot_path)

    actual = f"Publieke content zichtbaar: {public_visible} | Persoonsgegevens zichtbaar: {personal_visible} | Login CTA: {login_cta}"

    if not personal_visible and login_cta:
        result(TC_ID, "Talentprofiel gedeeltelijk zichtbaar voor bezoeker", "GESLAAGD",
               "Persoonsgegevens verborgen; publieke attributen en login CTA zichtbaar",
               actual, screenshot=screenshot_path)
        return True
    elif personal_visible:
        result(TC_ID, "Talentprofiel gedeeltelijk zichtbaar voor bezoeker", "GEFAALD",
               "Persoonsgegevens verborgen; publieke attributen en login CTA zichtbaar",
               actual, screenshot=screenshot_path)
        return False
    else:
        result(TC_ID, "Talentprofiel gedeeltelijk zichtbaar voor bezoeker", "GEBLOKKEERD",
               "Persoonsgegevens verborgen; publieke attributen en login CTA zichtbaar",
               actual + " — selectors aanpassen na inspectie",
               screenshot=screenshot_path)
        return False
