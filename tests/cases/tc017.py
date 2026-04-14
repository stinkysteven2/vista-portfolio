from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-017"
ADMIN_TALENTEN_URL = f"{BASE_URL.replace('/talent', '')}/admin/talenten"


def dismiss_cookie_banner(page: Page):
    try:
        page.locator("app-cookie-banner .btn.decline").click(timeout=3000)
        page.wait_for_timeout(300)
    except Exception:
        pass


def fill_description_js(page: Page, text: str):
    """Vul beschrijving textarea in via JS (visibility: hidden door Angular CDK)."""
    page.evaluate(f"""() => {{
        const els = document.querySelectorAll("textarea[formcontrolname='description']");
        for (const el of els) {{
            const setter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
            setter.call(el, '{text}');
            el.dispatchEvent(new Event('input', {{bubbles: true}}));
            el.dispatchEvent(new Event('change', {{bubbles: true}}));
        }}
    }}""")


def enter_edit(page: Page):
    """Navigeer naar admin en open edit-modus voor eerste talent."""
    page.goto(ADMIN_TALENTEN_URL, wait_until="networkidle", timeout=30000)
    dismiss_cookie_banner(page)
    page.locator("button:has-text('Edit')").first.click(timeout=5000)
    page.wait_for_timeout(2000)


def run(page: Page):
    """TC-017: Werkervaring bewerken"""
    print("\n--- TC-017: Werkervaring bewerken ---")

    if not login(page):
        result(TC_ID, "Werkervaring bewerken", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    enter_edit(page)

    page.locator("mat-expansion-panel-header:has-text('Werkervaring')").first.click(timeout=3000)
    page.wait_for_timeout(800)

    # Als er geen werkervaring is, eerst toevoegen
    if page.locator("text=Nog geen werkervaring").count() > 0:
        page.locator("button:has-text('ervaring toevoegen')").first.click(timeout=5000)
        page.wait_for_timeout(800)
        page.locator("input[formcontrolname='function']:visible").first.fill("Tester", timeout=3000)
        page.locator("input[formcontrolname='company']:visible").first.fill("Test BV", timeout=3000)
        page.locator("input[formcontrolname='dateFrom']:visible").first.fill("01-2023", timeout=3000)
        page.locator("input[formcontrolname='dateTill']:visible").first.fill("12-2024", timeout=3000)
        fill_description_js(page, "Testbeschrijving werkervaring")
        page.locator("button:has-text('Talent Bijwerken'), button:has-text('Update')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=15000)
        page.wait_for_timeout(1000)
        enter_edit(page)
        page.locator("mat-expansion-panel-header:has-text('Werkervaring')").first.click(timeout=3000)
        page.wait_for_timeout(800)

    # Klik op de werkervaring entry om het sub-panel te openen
    try:
        page.locator("mat-expansion-panel-header:has-text('Tester'), mat-expansion-panel-header:has-text('Test BV')").first.click(timeout=3000)
        page.wait_for_timeout(800)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc017-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring bewerken", "GEBLOKKEERD",
               "Werkervaring entry uitklappen", f"Entry niet gevonden: {e}",
               screenshot=screenshot_path)
        return False

    # Bewerk functietitel
    try:
        page.locator("input[formcontrolname='function']:visible").first.fill("Senior Tester", timeout=3000)
        fill_description_js(page, "Bijgewerkte beschrijving werkervaring")
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc017-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring bewerken", "GEBLOKKEERD",
               "Functietitel bewerkbaar", f"Kon niet bewerken: {e}",
               screenshot=screenshot_path)
        return False

    page.locator("button:has-text('Talent Bijwerken'), button:has-text('Update')").first.click(timeout=5000)
    page.wait_for_load_state("networkidle", timeout=15000)
    page.wait_for_timeout(1000)

    # Verifieer: opnieuw edit openen
    enter_edit(page)
    page.locator("mat-expansion-panel-header:has-text('Werkervaring')").first.click(timeout=3000)
    page.wait_for_timeout(800)

    senior_visible = page.locator("text=Senior Tester").count() > 0
    screenshot_path = f"{SCREENSHOTS_DIR}/tc017-{'geslaagd' if senior_visible else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    if senior_visible:
        result(TC_ID, "Werkervaring bewerken", "GESLAAGD",
               "Functietitel gewijzigd naar 'Senior Tester'",
               f"Senior Tester zichtbaar: {senior_visible}",
               screenshot=screenshot_path)
        return True
    else:
        result(TC_ID, "Werkervaring bewerken", "GEFAALD",
               "Functietitel gewijzigd naar 'Senior Tester'",
               "Gewijzigde functietitel niet gevonden",
               screenshot=screenshot_path)
        return False
