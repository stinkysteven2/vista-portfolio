from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-024"
ADMIN_TALENTEN_URL = f"{BASE_URL}/admin/talenten"


def run(page: Page):
    """TC-024: Hobby/interesse sorteren"""
    print("\n--- TC-024: Hobby/interesse sorteren ---")

    if not login(page):
        result(TC_ID, "Hobby/interesse sorteren", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=15000)

    try:
        page.locator("button:has-text('Edit'), a:has-text('Edit')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
        page.locator("text=Hobby, mat-expansion-panel:has-text('Hobby')").first.click(timeout=3000)
        page.wait_for_timeout(500)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc024-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Hobby/interesse sorteren", "GEBLOKKEERD",
               "Hobbylijst met meerdere items aanwezig",
               f"Admin panel of Hobby paneel niet bereikbaar: {e}",
               screenshot=screenshot_path)
        return False

    # Sorteerinteractie — afhankelijk van UI (slepen of pijltjesknop)
    hobbies = page.locator("[class*='hobby'] [cdkdrag], [class*='sortable'] li, [class*='hobby'] tr").all()
    if len(hobbies) < 2:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc024-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Hobby/interesse sorteren", "GEBLOKKEERD",
               "Minimaal twee hobby's aanwezig om volgorde te wijzigen",
               f"Minder dan 2 hobby's gevonden ({len(hobbies)}) — voeg eerst hobby's toe via TC-022",
               screenshot=screenshot_path)
        return False

    # Probeer via prioriteitsknop
    try:
        page.locator("button[aria-label*='omhoog'], button:has-text('↑'), button[class*='up']").first.click(timeout=3000)
        page.locator("button[type='submit'], button:has-text('Opslaan')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc024-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Hobby/interesse sorteren", "GEBLOKKEERD",
               "Volgorde van hobby's aanpasbaar",
               f"Sorteerfunctionaliteit niet gevonden: {e} — selectors aanpassen na inspectie",
               screenshot=screenshot_path)
        return False

    screenshot_path = f"{SCREENSHOTS_DIR}/tc024-resultaat.png"
    page.screenshot(path=screenshot_path)
    result(TC_ID, "Hobby/interesse sorteren", "GEBLOKKEERD",
           "Nieuwe volgorde van hobby's zichtbaar in profiel",
           "Sorteervolgorde aangepast — handmatige verificatie nodig",
           screenshot=screenshot_path)
    return False
