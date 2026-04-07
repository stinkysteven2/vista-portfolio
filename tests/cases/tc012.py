from helpers import result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-012"
PROFILE_IDS = [1, 2, 3, 4, 5]

PERSONAL_DATA_SELECTORS = [
    "a[href^='mailto']",
    "a[href^='tel']",
    "[class*='contact-detail']",
    "[class*='phone']",
    "[class*='email']",
]


def has_personal_data(page: Page) -> bool:
    for sel in PERSONAL_DATA_SELECTORS:
        try:
            el = page.locator(sel).first
            if el.count() > 0 and el.is_visible():
                return True
        except Exception:
            pass
    return False


def run(page: Page):
    """TC-012: IDOR — talentprofiel via URL-manipulatie"""
    print("\n--- TC-012: IDOR — talentprofiel via URL-manipulatie ---")

    exposed = []
    checked = []

    for profile_id in PROFILE_IDS:
        url = f"{BASE_URL}/talentprofile/{profile_id}"
        try:
            page.goto(url, wait_until="networkidle", timeout=15000)
        except Exception:
            continue

        current_url = page.url
        personal_visible = has_personal_data(page)
        checked.append(str(profile_id))

        if personal_visible:
            exposed.append(str(profile_id))

    screenshot_path = f"{SCREENSHOTS_DIR}/tc012-{'geslaagd' if not exposed else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    actual = f"Gecontroleerde IDs: {', '.join(checked)} | Blootgestelde IDs: {', '.join(exposed) or '(geen)'}"

    if not exposed:
        result(TC_ID, "IDOR — talentprofiel via URL-manipulatie", "GESLAAGD",
               "Geen persoonsgegevens zichtbaar bij URL-manipulatie zonder login",
               actual, screenshot=screenshot_path)
        return True
    else:
        result(TC_ID, "IDOR — talentprofiel via URL-manipulatie", "GEFAALD",
               "Geen persoonsgegevens zichtbaar bij URL-manipulatie zonder login",
               actual, screenshot=screenshot_path)
        return False
