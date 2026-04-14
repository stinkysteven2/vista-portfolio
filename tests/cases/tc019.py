from helpers import login, result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-019"
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
    """TC-019: Opleiding toevoegen"""
    print("\n--- TC-019: Opleiding toevoegen ---")

    if not login(page):
        result(TC_ID, "Opleiding toevoegen", "GEBLOKKEERD", "Ingelogd als beheerder", "Inloggen mislukt")
        return False

    enter_edit(page)

    try:
        page.locator("mat-expansion-panel-header:has-text('Opleidingen')").first.click(timeout=5000)
        page.wait_for_timeout(800)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc019-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Opleiding toevoegen", "GEBLOKKEERD",
               "Opleidingen panel opent", f"Panel niet gevonden: {e}",
               screenshot=screenshot_path)
        return False

    try:
        page.locator("button:has-text('opleiding toevoegen')").first.click(timeout=5000)
        page.wait_for_timeout(800)
        page.locator("input[formcontrolname='name']:visible").first.fill("Software Developer", timeout=3000)
        page.locator("input[formcontrolname='institution']:visible").first.fill("Test ROC", timeout=3000)
        page.locator("input[formcontrolname='dateFrom']:visible").first.fill("09-2020", timeout=3000)
        page.locator("input[formcontrolname='dateTill']:visible").first.fill("06-2022", timeout=3000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc019-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Opleiding toevoegen", "GEBLOKKEERD",
               "Opleidingsvelden invulbaar", f"Kon velden niet invullen: {e}",
               screenshot=screenshot_path)
        return False

    # Beschrijving werkervaring invullen (verplicht veld kan save blokkeren)
    fill_description(page, "Beschrijving werkervaring")

    page.locator("button:has-text('Talent Bijwerken'), button:has-text('Update')").first.click(timeout=5000)
    page.wait_for_load_state("networkidle", timeout=15000)
    page.wait_for_timeout(1000)

    # Verifieer: opnieuw edit openen (redirect na save)
    enter_edit(page)
    page.locator("mat-expansion-panel-header:has-text('Opleidingen')").first.click(timeout=5000)
    page.wait_for_timeout(800)

    opleiding_visible = page.locator("text=Software Developer").count() > 0 or page.locator("text=Test ROC").count() > 0
    screenshot_path = f"{SCREENSHOTS_DIR}/tc019-{'geslaagd' if opleiding_visible else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    if opleiding_visible:
        result(TC_ID, "Opleiding toevoegen", "GESLAAGD",
               "Opleiding 'Software Developer / Test ROC' zichtbaar na opslaan",
               f"Opleiding zichtbaar: {opleiding_visible}",
               screenshot=screenshot_path)
        return True
    else:
        result(TC_ID, "Opleiding toevoegen", "GEFAALD",
               "Opleiding 'Software Developer / Test ROC' zichtbaar na opslaan",
               "Opleiding niet gevonden na opslaan",
               screenshot=screenshot_path)
        return False
