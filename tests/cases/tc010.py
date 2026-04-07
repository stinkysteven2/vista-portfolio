from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-010"
PROFILE_URL = f"{BASE_URL}/talentprofile/1"

EXPECTED_ELEMENTS = [
    ("Naam", ["[class*='name']", "[class*='naam']", "h1", "h2"]),
    ("Functietitel", ["[class*='title']", "[class*='functie']", "[class*='job']"]),
    ("Locatie", ["[class*='location']", "[class*='locatie']", "[class*='city']"]),
    ("Vaardigheden", ["[class*='skill']", "[class*='vaardigheid']"]),
    ("Contactknop", ["button:has-text('Contact')", "a:has-text('Contact')", "[class*='contact']"]),
]


def run(page: Page):
    """TC-010: Talentprofiel volledig zichtbaar voor ingelogde gebruiker"""
    print("\n--- TC-010: Talentprofiel volledig zichtbaar voor ingelogde gebruiker ---")

    if not login(page):
        result(TC_ID, "Talentprofiel volledig zichtbaar", "GEBLOKKEERD",
               "Gebruiker is ingelogd",
               "Inloggen mislukt")
        return False

    page.goto(PROFILE_URL, wait_until="networkidle", timeout=15000)

    found = []
    missing = []
    for label, selectors in EXPECTED_ELEMENTS:
        visible = False
        for sel in selectors:
            try:
                el = page.locator(sel).first
                if el.count() > 0 and el.is_visible():
                    visible = True
                    break
            except Exception:
                pass
        if visible:
            found.append(label)
        else:
            missing.append(label)

    screenshot_path = f"{SCREENSHOTS_DIR}/tc010-{'geslaagd' if not missing else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    actual = f"Gevonden: {', '.join(found) or '(geen)'} | Ontbreekt: {', '.join(missing) or '(geen)'}"

    if not missing:
        result(TC_ID, "Talentprofiel volledig zichtbaar voor ingelogde gebruiker", "GESLAAGD",
               "Alle verwachte profielattributen zijn zichtbaar",
               actual, screenshot=screenshot_path)
        return True
    elif found:
        result(TC_ID, "Talentprofiel volledig zichtbaar voor ingelogde gebruiker", "GEBLOKKEERD",
               "Alle verwachte profielattributen zijn zichtbaar",
               actual + " — ontbrekende elementen: selectors aanpassen na inspectie",
               screenshot=screenshot_path)
        return False
    else:
        result(TC_ID, "Talentprofiel volledig zichtbaar voor ingelogde gebruiker", "GEFAALD",
               "Alle verwachte profielattributen zijn zichtbaar",
               actual, screenshot=screenshot_path)
        return False
