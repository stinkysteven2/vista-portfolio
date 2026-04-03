import os
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from playwright.sync_api import Page
from tc_meta import TC_META

load_dotenv()

BASE_URL = "https://it-talenten-portaal-test-it-talenten-webapp-test.iapmkw.easypanel.host/talent"
USERNAME = os.getenv("TALENTEN_USERNAME", "")
PASSWORD = os.getenv("TALENTEN_PASSWORD", "")
SCREENSHOTS_DIR = "uitwerking/deelopdracht-7-testrapportage/screenshots"
RESULTS_JSON = Path(__file__).parent / "results.json"

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

results: list[dict] = []


def result(
    tc_id: str,
    description: str,
    status: str,
    expected: str,
    actual: str,
    notes: str = "",
    screenshot: str = "",
    testomgeving: str = "geautomatiseerd",
):
    entry = {
        "tc_id": tc_id,
        "description": description,
        "status": status,
        "expected": expected,
        "actual": actual,
        "notes": notes,
        "screenshot": screenshot,
        "testomgeving": testomgeving,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    results.append(entry)
    icon = {"GESLAAGD": "V", "GEFAALD": "X", "GEBLOKKEERD": "!"}.get(status, "?")
    print(f"  [{icon} {status}] {tc_id}: {description}")
    if actual:
        print(f"    Werkelijk: {actual}")
    if screenshot:
        print(f"    Screenshot: {screenshot}")
    if notes:
        print(f"    Notitie: {notes}")


def save_results():
    """Sla de resultaten van deze testrun op in results.json."""
    data = {}
    if RESULTS_JSON.exists():
        with open(RESULTS_JSON, encoding="utf-8") as f:
            data = json.load(f)

    for r in results:
        tc_id = r["tc_id"]
        meta = TC_META.get(tc_id, {})
        conclusie_key = f"conclusie_{r['status'].lower()}"
        data[tc_id] = {
            **r,
            "eis": meta.get("eis", ""),
            "prioriteit": meta.get("prioriteit", ""),
            "conclusie": meta.get(conclusie_key, ""),
        }

    with open(RESULTS_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\nResultaten opgeslagen in {RESULTS_JSON}")


def login(page: Page) -> bool:
    """Helper: log in met geldige credentials. Geeft True terug bij succes."""
    page.goto(BASE_URL, wait_until="networkidle", timeout=15000)
    try:
        page.locator("section#login i.material-icons").click(timeout=5000)
        page.wait_for_load_state("networkidle", timeout=10000)
        page.locator("input[type='text']").first.fill(USERNAME, timeout=5000)
        page.locator("input[type='password']").first.fill(PASSWORD, timeout=5000)
        page.locator("button[type='submit'], input[type='submit']").first.click(timeout=5000)
        page.wait_for_url(f"{BASE_URL}**", timeout=15000)
        page.wait_for_load_state("networkidle", timeout=10000)
        return True
    except Exception:
        return False
