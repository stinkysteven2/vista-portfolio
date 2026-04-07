from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-013"
ADMIN_TALENTEN_URL = f"{BASE_URL}/admin/talenten"

TEST_TALENT = {
    "initialen": "T.",
    "voornaam": "Test",
    "tussenvoegsel": "",
    "achternaam": "Talent",
    "geboortedatum": "01-01-2000",
    "straat": "Teststraat",
    "huisnummer": "1",
    "postcode": "1234 AB",
    "woonplaats": "Teststad",
    "telefoon": "+31612345678",
    "email": "test.talent@example.com",
}


def fill_if_exists(page: Page, selector: str, value: str):
    try:
        el = page.locator(selector).first
        if el.count() > 0 and el.is_visible():
            el.fill(value)
    except Exception:
        pass


def run(page: Page):
    """TC-013: Talent aanmaken"""
    print("\n--- TC-013: Talent aanmaken ---")

    if not login(page):
        result(TC_ID, "Talent aanmaken", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=15000)

    if "/admin" not in page.url:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc013-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Talent aanmaken", "GEBLOKKEERD",
               "Admin panel toegankelijk",
               f"Geen toegang tot admin panel — URL: {page.url}",
               screenshot=screenshot_path)
        return False

    # Klik op "Talent toevoegen"
    try:
        page.locator("button:has-text('Talent toevoegen'), button:has-text('Toevoegen'), a:has-text('Talent toevoegen')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc013-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Talent aanmaken", "GEBLOKKEERD",
               '"Talent toevoegen" knop aanwezig',
               f"Knop niet gevonden: {e}",
               screenshot=screenshot_path)
        return False

    # Vul verplichte velden in
    fill_if_exists(page, "input[formcontrolname='initialen'], input[placeholder*='nitialen']", TEST_TALENT["initialen"])
    fill_if_exists(page, "input[formcontrolname='voornaam'], input[placeholder*='oornaam']", TEST_TALENT["voornaam"])
    fill_if_exists(page, "input[formcontrolname='achternaam'], input[placeholder*='chternaam']", TEST_TALENT["achternaam"])
    fill_if_exists(page, "input[formcontrolname='geboortedatum'], input[type='date'], input[placeholder*='eboorte']", TEST_TALENT["geboortedatum"])
    fill_if_exists(page, "input[formcontrolname='straat'], input[placeholder*='traat']", TEST_TALENT["straat"])
    fill_if_exists(page, "input[formcontrolname='huisnummer'], input[placeholder*='uisnummer']", TEST_TALENT["huisnummer"])
    fill_if_exists(page, "input[formcontrolname='postcode'], input[placeholder*='ostcode']", TEST_TALENT["postcode"])
    fill_if_exists(page, "input[formcontrolname='woonplaats'], input[placeholder*='oonplaats']", TEST_TALENT["woonplaats"])
    fill_if_exists(page, "input[formcontrolname='telefoon'], input[type='tel'], input[placeholder*='elefoon']", TEST_TALENT["telefoon"])
    fill_if_exists(page, "input[formcontrolname='email'], input[type='email'], input[placeholder*='mail']", TEST_TALENT["email"])

    # Opslaan
    try:
        page.locator("button[type='submit'], button:has-text('Opslaan'), button:has-text('Aanmaken')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc013-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Talent aanmaken", "GEBLOKKEERD",
               "Opslaan knop aanwezig en klikbaar",
               f"Kon niet opslaan: {e}",
               screenshot=screenshot_path)
        return False

    # Controleer of Test Talent in de lijst staat
    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=15000)
    talent_present = page.locator("text=Test Talent, text=Talent Test, td:has-text('Test')").count() > 0

    screenshot_path = f"{SCREENSHOTS_DIR}/tc013-{'geslaagd' if talent_present else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    if talent_present:
        result(TC_ID, "Talent aanmaken", "GESLAAGD",
               "Test Talent verschijnt in de talentenlijst",
               f"Talent 'Test Talent' gevonden in lijst: {talent_present}",
               screenshot=screenshot_path)
        return True
    else:
        result(TC_ID, "Talent aanmaken", "GEFAALD",
               "Test Talent verschijnt in de talentenlijst",
               f"Talent 'Test Talent' niet gevonden in lijst",
               screenshot=screenshot_path)
        return False
