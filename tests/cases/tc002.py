from helpers import result, BASE_URL, SCREENSHOTS_DIR, USERNAME
from playwright.sync_api import Page

TC_ID = "TC-002"


def run(page: Page):
    """TC-002: Inloggen met onjuist wachtwoord"""
    print("\n--- TC-002: Inloggen met onjuist wachtwoord ---")

    page.goto(BASE_URL, wait_until="networkidle", timeout=15000)

    try:
        page.locator("section#login i.material-icons").click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        result(TC_ID, "Klik op login-icoon", "GEBLOKKEERD",
               "Login-icoon klikbaar in navigatiebalk",
               f"Kon login-knop niet vinden of klikken: {e}")
        return False

    try:
        page.locator("input[type='text']").first.fill(USERNAME, timeout=5000)
        page.locator("input[type='password']").first.fill("ditiseenonjuistwachtwoord123!", timeout=5000)
    except Exception as e:
        result(TC_ID, "Invullen credentials", "GEBLOKKEERD",
               "Invoervelden aanwezig",
               f"Kon velden niet vinden: {e}")
        return False

    try:
        page.locator("button[type='submit'], input[type='submit']").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        result(TC_ID, "Klik op Sign In", "GEBLOKKEERD",
               "Sign In knop aanwezig en klikbaar",
               f"Kon Sign In knop niet vinden: {e}")
        return False

    current_url = page.url
    still_on_keycloak = "bee-ids-test.azurewebsites.net" in current_url

    error_msg = ""
    for sel in ["[class*='alert']", "[class*='error']", "#input-error", "span.pf-v5-c-alert__title", ".kc-feedback-text"]:
        try:
            el = page.locator(sel).first
            if el.count() > 0 and el.is_visible():
                error_msg = el.inner_text().strip()
                break
        except Exception:
            pass

    expected_msg = "Invalid username or password."
    msg_correct = expected_msg.lower() in error_msg.lower() if error_msg else False

    if still_on_keycloak and msg_correct:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc002-geslaagd.png"
        page.screenshot(path=screenshot_path)
        result(TC_ID, "Inloggen met onjuist wachtwoord", "GESLAAGD",
               f"Blijft op loginpagina; foutmelding '{expected_msg}' zichtbaar",
               f"URL: {current_url} | Foutmelding: '{error_msg}'",
               screenshot=screenshot_path)
        return True
    else:
        result(TC_ID, "Inloggen met onjuist wachtwoord", "GEFAALD",
               f"Blijft op loginpagina; foutmelding '{expected_msg}' zichtbaar",
               f"URL: {current_url} | Nog op Keycloak: {still_on_keycloak} | Foutmelding: '{error_msg or '(geen)'}'")
        return False
