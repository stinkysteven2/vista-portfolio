"""
Test runner voor IT Talenten Portaal
Ontdekt automatisch alle testcases in tests/cases/ en voert ze uit.
Credentials worden geladen uit .env (niet in git).
"""

import sys
import json
import argparse
import importlib.util
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright

# Zorg dat helpers.py vindbaar is voor de case-bestanden
sys.path.insert(0, str(Path(__file__).parent))

import helpers


def discover_cases() -> dict:
    """Laad alle testcases uit de cases/ map. Geeft {TC_ID: run_functie} terug."""
    cases_dir = Path(__file__).parent / "cases"
    all_tests = {}
    for path in sorted(cases_dir.glob("*.py")):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, "TC_ID") and hasattr(mod, "run"):
            all_tests[mod.TC_ID] = mod.run
    return all_tests


def print_summary():
    print("\n" + "=" * 60)
    print(f"SAMENVATTING — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)
    geslaagd = sum(1 for r in helpers.results if r["status"] == "GESLAAGD")
    gefaald = sum(1 for r in helpers.results if r["status"] == "GEFAALD")
    geblokkeerd = sum(1 for r in helpers.results if r["status"] == "GEBLOKKEERD")
    print(f"  Totaal:      {len(helpers.results)}")
    print(f"  Geslaagd:    {geslaagd}")
    print(f"  Gefaald:     {gefaald}")
    print(f"  Geblokkeerd: {geblokkeerd}")
    if helpers.results:
        pct = round(geslaagd / len(helpers.results) * 100)
        print(f"  Slaagpercentage: {pct}%")
    return helpers.results


def main():
    all_tests = discover_cases()

    parser = argparse.ArgumentParser(description="Test runner — IT Talenten Portaal")
    parser.add_argument("tests", nargs="*", metavar="TC-ID",
                        help=f"Testcases om uit te voeren (bijv. TC-001 TC-004). Zonder argument: alles. Beschikbaar: {', '.join(all_tests)}")
    args = parser.parse_args()

    if not helpers.USERNAME or not helpers.PASSWORD:
        print("FOUT: Geen credentials gevonden. Controleer je .env bestand.")
        return

    to_run = {k: v for k, v in all_tests.items()
              if not args.tests or k in [t.upper() for t in args.tests]}

    if not to_run:
        print(f"Geen geldige testcases gevonden. Beschikbaar: {', '.join(all_tests)}")
        return

    print("=" * 60)
    print("TEST RUNNER — IT Talenten Portaal")
    print("=" * 60)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        for tc_fn in to_run.values():
            ctx = browser.new_context()
            tc_fn(ctx.new_page())
            ctx.close()

        browser.close()

    return print_summary()


if __name__ == "__main__":
    main()
    helpers.save_results()
