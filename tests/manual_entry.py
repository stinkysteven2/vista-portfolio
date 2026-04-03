"""
Formulier voor het invoeren van handmatige testresultaten.
Schrijft het resultaat naar tests/results.json.
"""

import sys
import json
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))
from tc_meta import TC_META

RESULTS_JSON = Path(__file__).parent / "results.json"


def load_results() -> dict:
    if RESULTS_JSON.exists():
        with open(RESULTS_JSON, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_results(data: dict):
    with open(RESULTS_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def prompt(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    val = input(f"{label}{suffix}: ").strip()
    return val if val else default


def main():
    print("=== Handmatige testresultaten invoeren ===\n")
    print("Beschikbare TC-IDs:", ", ".join(sorted(TC_META)))
    print()

    tc_id = prompt("TC-ID (bijv. TC-003)").upper()
    if tc_id not in TC_META:
        print(f"Onbekend TC-ID: {tc_id}. Beschikbaar: {', '.join(sorted(TC_META))}")
        return

    meta = TC_META[tc_id]
    print(f"\n  Omschrijving : {meta['description']}")
    print(f"  Eis          : {meta['eis']}  |  Prioriteit: {meta['prioriteit']}")
    print(f"\n  Teststappen:")
    for i, stap in enumerate(meta["stappen"], 1):
        print(f"    {i}. {stap}")
    print()

    testomgeving = prompt("Testomgeving (bijv. Firefox op Windows 10)", "handmatig")

    print("\nStatus opties: GESLAAGD / GEFAALD / GEBLOKKEERD")
    status = prompt("Status").upper()
    if status not in ("GESLAAGD", "GEFAALD", "GEBLOKKEERD"):
        print(f"Ongeldige status: '{status}'")
        return

    expected = prompt("Verwacht resultaat")
    actual = prompt("Werkelijk resultaat")
    conclusie = prompt("Conclusie", meta.get(f"conclusie_{status.lower()}", ""))
    screenshot = prompt("Schermafbeelding (pad relatief aan screenshots/, optioneel)")
    notes = prompt("Notities (optioneel)")

    entry = {
        "tc_id": tc_id,
        "description": meta["description"],
        "eis": meta["eis"],
        "prioriteit": meta["prioriteit"],
        "status": status,
        "expected": expected,
        "actual": actual,
        "conclusie": conclusie,
        "screenshot": screenshot,
        "testomgeving": testomgeving,
        "notes": notes,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    data = load_results()
    data[tc_id] = entry
    save_results(data)

    print(f"\nOpgeslagen: {tc_id} — {status}")
    print("Voer 'python tests/generate_report.py' uit om het testrapport bij te werken.")


if __name__ == "__main__":
    main()
