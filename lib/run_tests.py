"""
Test runner voor IT Talenten Portaal
Voert testcases uit het testplan geautomatiseerd uit en geeft gestructureerde output.
Credentials worden geladen uit .env (niet in git).
"""

import os
import json
from datetime import datetime
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Page

load_dotenv()

BASE_URL = "https://it-talenten-portaal-test-it-talenten-webapp-test.iapmkw.easypanel.host/talent"
USERNAME = os.getenv("TALENTEN_USERNAME", "")
PASSWORD = os.getenv("TALENTEN_PASSWORD", "")
SCREENSHOTS_DIR = "uitwerking/deelopdracht-7-testrapportage/screenshots"

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

results: list[dict] = []


def result(tc_id: str, description: str, status: str, expected: str, actual: str, notes: str = ""):
    entry = {
        "tc_id": tc_id,
        "description": description,
        "status": status,       # GESLAAGD / GEFAALD / GEBLOKKEERD
        "expected": expected,
        "actual": actual,
        "notes": notes,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    results.append(entry)
    icon = {"GESLAAGD": "V", "GEFAALD": "X", "GEBLOKKEERD": "!"}.get(status, "?")
    print(f"  [{icon} {status}] {tc_id}: {description}")
    if actual:
        print(f"    Werkelijk: {actual}")
    if notes:
        print(f"    Notitie: {notes}")


def tc001(page: Page):
    """TC-001: Inloggen met geldige gegevens"""
    print("\n--- TC-001: Inloggen met geldige gegevens ---")

    # Stap 1: Navigeer naar startpagina
    page.goto(BASE_URL, wait_until="networkidle", timeout=15000)

    # Stap 2: Klik op het login-icoon in de navigatiebalk (section#login > i.material-icons)
    try:
        page.locator("section#login i.material-icons").click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        result("TC-001", "Klik op login-icoon", "GEBLOKKEERD",
               "Login-icoon klikbaar in navigatiebalk",
               f"Kon login-knop niet vinden of klikken: {e}")
        return False

    # Stap 3 & 4: Vul credentials in op de Keycloak loginpagina
    try:
        page.locator("input[type='text']").first.fill(USERNAME, timeout=5000)
        page.locator("input[type='password']").first.fill(PASSWORD, timeout=5000)
    except Exception as e:
        result("TC-001", "Invullen credentials", "GEBLOKKEERD",
               "Invoervelden voor gebruikersnaam en wachtwoord aanwezig",
               f"Kon velden niet vinden: {e}")
        return False

    # Stap 5: Klik op Sign In en wacht op redirect terug naar portaal
    try:
        page.locator("button[type='submit'], input[type='submit']").first.click(timeout=5000)
        page.wait_for_url(f"{BASE_URL}**", timeout=15000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        result("TC-001", "Klik op Sign In", "GEFAALD",
               "Doorgestuurd terug naar IT Talenten Portaal na inloggen",
               f"Redirect mislukt of timeout: {e}")
        return False

    # Verwacht resultaat: terug op portaal, logout-icoon zichtbaar, login-icoon verdwenen
    current_url = page.url
    has_logout = page.locator("section#login i.material-icons:has-text('logout')").count() > 0
    has_login = page.locator("section#login i.material-icons:has-text('login')").count() > 0

    if has_logout and not has_login:
        screenshot_path = f"{SCREENSHOTS_DIR}/tc001-geslaagd.png"
        page.screenshot(path=screenshot_path)
        result("TC-001", "Inloggen met geldige gegevens", "GESLAAGD",
               "Doorgestuurd naar startpagina; logout-knop zichtbaar; login-knop verdwenen",
               f"URL: {current_url} | Logout zichtbaar: {has_logout} | Login zichtbaar: {has_login}",
               notes=f"Screenshot: {screenshot_path}")
        return True
    else:
        # Controleer op foutmelding
        error_msg = ""
        for sel in ["[class*='error']", ".alert", "[class*='alert']", "mat-error"]:
            el = page.locator(sel).first
            if el.count() > 0 and el.is_visible():
                error_msg = el.inner_text().strip()
                break

        screenshot_path = f"{SCREENSHOTS_DIR}/tc001-gefaald.png"
        page.screenshot(path=screenshot_path)
        result("TC-001", "Inloggen met geldige gegevens", "GEFAALD",
               "Doorgestuurd naar startpagina; logout-knop zichtbaar",
               f"URL: {current_url} | Logout zichtbaar: {has_logout} | Login zichtbaar: {has_login}" +
               (f" | Foutmelding: '{error_msg}'" if error_msg else ""),
               notes=f"Screenshot: {screenshot_path}")
        return False


def tc002(page: Page):
    """TC-002: Inloggen met onjuist wachtwoord"""
    print("\n--- TC-002: Inloggen met onjuist wachtwoord ---")

    # Stap 1: Navigeer naar startpagina
    page.goto(BASE_URL, wait_until="networkidle", timeout=15000)

    # Stap 2: Klik op login-icoon
    try:
        page.locator("section#login i.material-icons").click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        result("TC-002", "Klik op login-icoon", "GEBLOKKEERD",
               "Login-icoon klikbaar in navigatiebalk",
               f"Kon login-knop niet vinden of klikken: {e}")
        return False

    # Stap 3 & 4: Vul geldige gebruikersnaam + fout wachtwoord in
    try:
        page.locator("input[type='text']").first.fill(USERNAME, timeout=5000)
        page.locator("input[type='password']").first.fill("ditiseenonjuistwachtwoord123!", timeout=5000)
    except Exception as e:
        result("TC-002", "Invullen credentials", "GEBLOKKEERD",
               "Invoervelden aanwezig",
               f"Kon velden niet vinden: {e}")
        return False

    # Stap 5: Klik op Sign In
    try:
        page.locator("button[type='submit'], input[type='submit']").first.click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception as e:
        result("TC-002", "Klik op Sign In", "GEBLOKKEERD",
               "Sign In knop aanwezig en klikbaar",
               f"Kon Sign In knop niet vinden: {e}")
        return False

    # Verwacht resultaat: nog steeds op Keycloak-pagina, foutmelding zichtbaar
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
        result("TC-002", "Inloggen met onjuist wachtwoord", "GESLAAGD",
               f"Blijft op loginpagina; foutmelding '{expected_msg}' zichtbaar",
               f"URL: {current_url} | Foutmelding: '{error_msg}'",
               notes=f"Screenshot: {screenshot_path}")
        return True
    else:
        result("TC-002", "Inloggen met onjuist wachtwoord", "GEFAALD",
               f"Blijft op loginpagina; foutmelding '{expected_msg}' zichtbaar",
               f"URL: {current_url} | Nog op Keycloak: {still_on_keycloak} | Foutmelding: '{error_msg or '(geen)'}'")
        return False


def print_summary():
    print("\n" + "=" * 60)
    print(f"SAMENVATTING — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)
    geslaagd = sum(1 for r in results if r["status"] == "GESLAAGD")
    gefaald = sum(1 for r in results if r["status"] == "GEFAALD")
    geblokkeerd = sum(1 for r in results if r["status"] == "GEBLOKKEERD")
    print(f"  Totaal:      {len(results)}")
    print(f"  Geslaagd:    {geslaagd}")
    print(f"  Gefaald:     {gefaald}")
    print(f"  Geblokkeerd: {geblokkeerd}")
    if results:
        pct = round(geslaagd / len(results) * 100)
        print(f"  Slaagpercentage: {pct}%")
    return results


def main():
    if not USERNAME or not PASSWORD:
        print("FOUT: Geen credentials gevonden. Controleer je .env bestand.")
        return

    print("=" * 60)
    print("TEST RUNNER — IT Talenten Portaal")
    print("=" * 60)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        ctx1 = browser.new_context()
        tc001(ctx1.new_page())
        ctx1.close()

        ctx2 = browser.new_context()
        tc002(ctx2.new_page())
        ctx2.close()

        browser.close()

    return print_summary()


if __name__ == "__main__":
    results_data = main()
    # Sla ruwe resultaten op als JSON voor de rapportage
    with open("lib/last_run.json", "w", encoding="utf-8") as f:
        json.dump(results_data, f, ensure_ascii=False, indent=2)
    print("\nResultaten opgeslagen in lib/last_run.json")
