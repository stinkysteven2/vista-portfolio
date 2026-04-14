from helpers import result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-009"
MIN_HOURS = 20
MAX_HOURS = 32


def count_talents(page: Page) -> int:
    """Lees het aantal talenten uit de 'Zoekresultaten (X)' kop."""
    import re
    try:
        tekst = page.locator("h1:has-text('Zoekresultaten')").first.inner_text(timeout=5000)
        match = re.search(r'\((\d+)\)', tekst)
        if match:
            return int(match.group(1))
    except Exception:
        pass
    return -1


def run(page: Page):
    """TC-009: Filteren op beschikbaarheid (grenswaarden)"""
    print("\n--- TC-009: Filteren op beschikbaarheid (grenswaarden) ---")

    page.goto(BASE_URL, wait_until="networkidle", timeout=15000)

    # Cookie banner wegklikken
    try:
        page.locator("app-cookie-banner .btn.decline").click(timeout=3000)
        page.wait_for_timeout(300)
    except Exception:
        pass

    total_before = count_talents(page)

    try:
        # Beschikbaarheid accordion openen
        header = page.locator(".accordion-item-header:has-text('Beschikbaarheid')").first
        if header.count() == 0:
            raise Exception("Beschikbaarheid accordion niet gevonden")
        header.click(timeout=3000)
        page.wait_for_timeout(500)

        # Vul de start-waarde in
        start_input = page.locator("input[name='start-value']").first
        if start_input.count() == 0:
            raise Exception("Start-value input niet gevonden")
        start_input.click(timeout=3000, click_count=3)
        start_input.fill(str(MIN_HOURS))
        start_input.dispatch_event("change")
        page.wait_for_timeout(300)

        # Vul de end-waarde in
        end_input = page.locator("input[name='end-value']").first
        if end_input.count() == 0:
            raise Exception("End-value input niet gevonden")
        end_input.click(timeout=3000, click_count=3)
        end_input.fill(str(MAX_HOURS))
        end_input.dispatch_event("change")
        page.keyboard.press("Tab")
        page.wait_for_load_state("networkidle", timeout=10000)

        # Wacht tot Zoekresultaten-teller verandert (Angular update)
        page.wait_for_function(
            "before => { const h1 = document.querySelector('h1'); const m = h1 && h1.innerText.match(/\\((\\d+)\\)/); return m && parseInt(m[1]) !== before; }",
            arg=total_before,
            timeout=5000
        )

    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc009-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Filteren op beschikbaarheid (grenswaarden)", "GEBLOKKEERD",
               f"Beschikbaarheidsfilter invulbaar met {MIN_HOURS}–{MAX_HOURS} uur",
               f"Kon filter niet activeren: {e}",
               screenshot=screenshot_path)
        return False

    total_after = count_talents(page)
    filtered_correctly = total_after != -1 and (total_after <= total_before or total_before == -1)

    screenshot_path = f"{SCREENSHOTS_DIR}/tc009-{'geslaagd' if filtered_correctly else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    if filtered_correctly:
        result(TC_ID, "Filteren op beschikbaarheid (grenswaarden)", "GESLAAGD",
               f"Alleen talenten beschikbaar {MIN_HOURS}–{MAX_HOURS} uur getoond; aantal ≤ totaal",
               f"Voor filter: {total_before} | Na filter ({MIN_HOURS}–{MAX_HOURS} uur): {total_after}",
               screenshot=screenshot_path)
        return True
    else:
        result(TC_ID, "Filteren op beschikbaarheid (grenswaarden)", "GEFAALD",
               f"Alleen talenten beschikbaar {MIN_HOURS}–{MAX_HOURS} uur getoond; aantal ≤ totaal",
               f"Voor filter: {total_before} | Na filter ({MIN_HOURS}–{MAX_HOURS} uur): {total_after}",
               screenshot=screenshot_path)
        return False
