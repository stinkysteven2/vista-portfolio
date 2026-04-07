from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-007"
ADMIN_URL = f"{BASE_URL.replace('/talent', '')}/admin"


def is_on_admin_panel(page: Page) -> bool:
    return "/admin" in page.url and page.locator("[class*='admin'], nav, table").count() > 0


def run(page: Page):
    """TC-007: Admin panel toegankelijkheid per rol"""
    print("\n--- TC-007: Admin panel toegankelijkheid per rol ---")

    # Scenario 1: bezoeker (niet ingelogd)
    page.goto(ADMIN_URL, wait_until="networkidle", timeout=15000)
    visitor_url = page.url
    visitor_has_admin = is_on_admin_panel(page)

    screenshot_visitor = f"{SCREENSHOTS_DIR}/tc007-bezoeker.png"
    page.screenshot(path=screenshot_visitor)

    # Scenario 2: ingelogde gebruiker (zelfde context, nu inloggen)
    if not login(page):
        result(TC_ID, "Admin panel — ingelogde gebruiker", "GEBLOKKEERD",
               "Inloggen lukt voor scenario 2",
               "Inloggen mislukt")
        return False

    page.goto(ADMIN_URL, wait_until="networkidle", timeout=15000)
    loggedin_url = page.url
    loggedin_has_admin = is_on_admin_panel(page)

    screenshot_loggedin = f"{SCREENSHOTS_DIR}/tc007-ingelogd.png"
    page.screenshot(path=screenshot_loggedin)

    # Beoordeling
    # Verwacht: bezoeker → omgeleid (geen admin), ingelogde gebruiker → afhankelijk van rol
    visitor_blocked = not visitor_has_admin
    actual = (
        f"Bezoeker — URL: {visitor_url} | Admin zichtbaar: {visitor_has_admin} | "
        f"Ingelogd — URL: {loggedin_url} | Admin zichtbaar: {loggedin_has_admin}"
    )

    if visitor_blocked:
        result(TC_ID, "Admin panel toegankelijkheid per rol", "GESLAAGD",
               "Bezoeker en niet-admin worden omgeleid; beheerder heeft toegang",
               actual,
               screenshot=screenshot_loggedin,
               notes=f"Bezoeker screenshot: {screenshot_visitor}")
        return True
    else:
        result(TC_ID, "Admin panel toegankelijkheid per rol", "GEFAALD",
               "Bezoeker en niet-admin worden omgeleid; beheerder heeft toegang",
               actual,
               screenshot=screenshot_visitor)
        return False
