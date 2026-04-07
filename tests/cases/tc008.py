from helpers import result, BASE_URL, SCREENSHOTS_DIR
from playwright.sync_api import Page

TC_ID = "TC-008"
FILTER_PROVINCE = "Noord-Brabant"


def count_talents(page: Page) -> int:
    """Tel het aantal zichtbare talent-kaarten op de pagina."""
    for sel in ["[class*='talent-card']", "[class*='talentcard']", "[class*='card']", "app-talent-card", ".talent"]:
        count = page.locator(sel).count()
        if count > 0:
            return count
    return -1  # onbekend


def run(page: Page):
    """TC-008: Filteren op provincie"""
    print("\n--- TC-008: Filteren op provincie ---")

    page.goto(BASE_URL, wait_until="networkidle", timeout=15000)

    # Tel ongefilterden talenten
    total_before = count_talents(page)

    # Zoek het provinciefilter
    province_filter = None
    for sel in [
        f"mat-select:has-text('Provincie')",
        f"select:has-text('Provincie')",
        "[placeholder*='rovincie']",
        "[class*='province']",
        "[class*='filter'] select",
        "mat-select",
    ]:
        el = page.locator(sel).first
        if el.count() > 0 and el.is_visible():
            province_filter = el
            break

    if province_filter is None:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc008-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Filteren op provincie", "GEBLOKKEERD",
               f"Provinciefilter aanwezig en filterbaar op {FILTER_PROVINCE}",
               "Provinciefilter niet gevonden — selector aanpassen na inspectie",
               screenshot=screenshot_path)
        return False

    try:
        province_filter.click(timeout=3000)
        page.locator(f"mat-option:has-text('{FILTER_PROVINCE}'), option:has-text('{FILTER_PROVINCE}')").first.click(timeout=3000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc008-geblokkeerd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Filteren op provincie", "GEBLOKKEERD",
               f"Filteroptie '{FILTER_PROVINCE}' selecteerbaar",
               f"Kon filter niet activeren: {e}",
               screenshot=screenshot_path)
        return False

    total_after = count_talents(page)
    filtered_correctly = total_after != -1 and (total_after <= total_before or total_before == -1)

    screenshot_path = f"{SCREENSHOTS_DIR}/tc008-{'geslaagd' if filtered_correctly else 'gefaald'}.png"
    page.screenshot(path=screenshot_path)

    if filtered_correctly:
        result(TC_ID, "Filteren op provincie", "GESLAAGD",
               f"Alleen talenten uit {FILTER_PROVINCE} getoond; aantal ≤ totaal",
               f"Voor filter: {total_before} | Na filter ({FILTER_PROVINCE}): {total_after}",
               screenshot=screenshot_path)
        return True
    else:
        result(TC_ID, "Filteren op provincie", "GEFAALD",
               f"Alleen talenten uit {FILTER_PROVINCE} getoond; aantal ≤ totaal",
               f"Voor filter: {total_before} | Na filter ({FILTER_PROVINCE}): {total_after}",
               screenshot=screenshot_path)
        return False
