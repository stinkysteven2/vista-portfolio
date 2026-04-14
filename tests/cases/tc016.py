from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-016"
ADMIN_TALENTEN_URL = f"{BASE_URL.replace('/talent', '')}/admin/talenten"


def dismiss_cookie_banner(page: Page):
    try:
        page.locator("app-cookie-banner .btn.decline").click(timeout=3000)
        page.wait_for_timeout(300)
    except Exception:
        pass


def fill_description(page: Page, text: str):
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
    """TC-016: Werkervaring toevoegen"""
    print("\n--- TC-016: Werkervaring toevoegen ---")

    if not login(page):
        result(TC_ID, "Werkervaring toevoegen", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    enter_edit(page)

    if "/admin" not in page.url:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc016-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring toevoegen", "GEBLOKKEERD",
               "Admin panel toegankelijk", f"Geen toegang — URL: {page.url}",
               screenshot=screenshot_path)
        return False

    # Open Werkervaring panel
    try:
        page.locator("mat-expansion-panel-header:has-text('Werkervaring')").first.click(timeout=3000)
        page.wait_for_timeout(800)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc016-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring toevoegen", "GEBLOKKEERD",
               "Werkervaring panel opent", f"Panel niet gevonden: {e}",
               screenshot=screenshot_path)
        return False

    # Klik "ervaring toevoegen"
    try:
        page.locator("button:has-text('ervaring toevoegen')").first.click(timeout=5000)
        page.wait_for_timeout(800)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc016-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring toevoegen", "GEBLOKKEERD",
               "Toevoegen-knop aanwezig", f"Knop niet gevonden: {e}",
               screenshot=screenshot_path)
        return False

    # Vul werkervaringsvelden in
    try:
        page.locator("input[formcontrolname='function']:visible").first.fill("Tester", timeout=3000)
        page.locator("input[formcontrolname='company']:visible").first.fill("Test BV", timeout=3000)
        page.locator("input[formcontrolname='dateFrom']:visible").first.fill("01-2023", timeout=3000)
        page.locator("input[formcontrolname='dateTill']:visible").first.fill("12-2024", timeout=3000)
        fill_description(page, "Testbeschrijving werkervaring")
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc016-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring toevoegen", "GEBLOKKEERD",
               "Werkervaringsvelden invulbaar", f"Kon velden niet invullen: {e}",
               screenshot=screenshot_path)
        return False

    # Opslaan
    try:
        page.locator("button:has-text('Talent Bijwerken'), button:has-text('Update')").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=15000)
        page.wait_for_timeout(1000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc016-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Werkervaring toevoegen", "GEBLOKKEERD",
               "Opslaan knop klikbaar", f"Kon niet opslaan: {e}",
               screenshot=screenshot_path)
        return False

    # Verifieer: opnieuw edit openen (pagina redirect naar lijst na save)
    enter_edit(page)
    page.locator("mat-expansion-panel-header:has-text('Werkervaring')").first.click(timeout=3000)
    page.wait_for_timeout(800)

    test_bv_visible = page.locator("text=Test BV").count() > 0
    tester_visible = page.locator("text=Tester").count() > 0

    screenshot_path = f"{SCREENSHOTS_DIR}/tc016-{'geslaagd' if test_bv_visible else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    actual = f"Test BV zichtbaar: {test_bv_visible} | Tester zichtbaar: {tester_visible}"

    if test_bv_visible:
        result(TC_ID, "Werkervaring toevoegen", "GESLAAGD",
               "Werkervaring 'Test BV / Tester' zichtbaar na opslaan",
               actual, screenshot=screenshot_path)
        return True
    else:
        result(TC_ID, "Werkervaring toevoegen", "GEFAALD",
               "Werkervaring 'Test BV / Tester' zichtbaar na opslaan",
               actual, screenshot=screenshot_path)
        return False
