from helpers import login, login_regular, result, BASE_URL, SCREENSHOTS_DIR, REGULAR_USERNAME
from playwright.sync_api import Page

TC_ID = "TC-007"
ADMIN_URL = f"{BASE_URL.replace('/talent', '')}/admin"


def is_on_admin_panel(page: Page) -> bool:
    return "/admin" in page.url and page.locator("[class*='admin'], nav, table").count() > 0


def run(page: Page):
    """TC-007: Admin panel toegankelijkheid per rol"""
    print("\n--- TC-007: Admin panel toegankelijkheid per rol ---")

    if not REGULAR_USERNAME:
        result(TC_ID, "Admin panel toegankelijkheid per rol", "GEBLOKKEERD",
               "Niet-admin credentials beschikbaar",
               "TALENTEN_REGULAR_USERNAME niet ingesteld in .env")
        return False

    # Scenario 1: bezoeker (niet ingelogd)
    page.goto(ADMIN_URL, wait_until="networkidle", timeout=15000)
    visitor_blocked = not is_on_admin_panel(page)
    screenshot_visitor = f"{SCREENSHOTS_DIR}/tc007-bezoeker.png"
    page.screenshot(path=screenshot_visitor)

    # Scenario 2: ingelogde gebruiker (niet-admin)
    if not login_regular(page):
        result(TC_ID, "Admin panel — niet-admin gebruiker", "GEBLOKKEERD",
               "Inloggen als niet-admin lukt",
               "Login als niet-admin mislukt")
        return False

    page.goto(ADMIN_URL, wait_until="networkidle", timeout=15000)
    regular_blocked = not is_on_admin_panel(page)
    screenshot_regular = f"{SCREENSHOTS_DIR}/tc007-niet-admin.png"
    page.screenshot(path=screenshot_regular)

    # Scenario 3: beheerder — sessie wissen zodat we opnieuw kunnen inloggen
    page.context.clear_cookies()
    if not login(page):
        result(TC_ID, "Admin panel — beheerder", "GEBLOKKEERD",
               "Inloggen als beheerder lukt",
               "Login als beheerder mislukt")
        return False

    page.goto(ADMIN_URL, wait_until="networkidle", timeout=15000)
    admin_has_access = is_on_admin_panel(page)
    screenshot_admin = f"{SCREENSHOTS_DIR}/tc007-admin.png"
    page.screenshot(path=screenshot_admin)

    actual = (
        f"Bezoeker geblokkeerd: {visitor_blocked} | "
        f"Niet-admin geblokkeerd: {regular_blocked} | "
        f"Beheerder heeft toegang: {admin_has_access}"
    )

    if visitor_blocked and regular_blocked and admin_has_access:
        result(TC_ID, "Admin panel toegankelijkheid per rol", "GESLAAGD",
               "Bezoeker en niet-admin omgeleid; beheerder heeft toegang",
               actual, screenshot=screenshot_admin,
               notes=f"Bezoeker: {screenshot_visitor} | Niet-admin: {screenshot_regular}")
        return True
    else:
        result(TC_ID, "Admin panel toegankelijkheid per rol", "GEFAALD",
               "Bezoeker en niet-admin omgeleid; beheerder heeft toegang",
               actual, screenshot=screenshot_admin)
        return False
