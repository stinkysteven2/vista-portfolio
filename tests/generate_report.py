"""
Genereert de testrapportage-secties op basis van tests/results.json
en vervangt de gemarkeerde blokken in testrapport.md.

Markers in testrapport.md:
  <!-- GENERATED:OVERZICHT:START --> ... <!-- GENERATED:OVERZICHT:END -->
  <!-- GENERATED:DETAILS:START -->  ... <!-- GENERATED:DETAILS:END -->
  <!-- GENERATED:STATISTIEKEN:START --> ... <!-- GENERATED:STATISTIEKEN:END -->
"""

import sys
import re
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tc_meta import TC_META

RESULTS_JSON = Path(__file__).parent / "results.json"
REPORT_PATH = (
    Path(__file__).parent.parent
    / "uitwerking/deelopdracht-7-testrapportage/testrapport.md"
)


def load_results() -> dict:
    with open(RESULTS_JSON, encoding="utf-8") as f:
        return json.load(f)


def replace_section(content: str, marker: str, new_content: str) -> str:
    pattern = rf"<!-- GENERATED:{marker}:START -->.*?<!-- GENERATED:{marker}:END -->"
    replacement = (
        f"<!-- GENERATED:{marker}:START -->\n"
        f"{new_content}\n"
        f"<!-- GENERATED:{marker}:END -->"
    )
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def format_actual(actual: str) -> str:
    """Splits pipe-separated actual values into bullet points."""
    parts = [p.strip() for p in actual.split(" | ") if p.strip()]
    if len(parts) == 1:
        return parts[0]
    return "\n".join(f"- {p}" for p in parts)


def generate_overzicht(results: dict) -> str:
    header = (
        "| TC-ID | Omschrijving | Eis | Prioriteit | Status | Uitgevoerd om |\n"
        "|---|---|---|---|---|---|"
    )
    rows = []
    for tc_id in sorted(results):
        r = results[tc_id]
        anchor = tc_id.lower() + "--detail"
        status = f"**{r['status']}**"
        rows.append(
            f"| [{tc_id}](#{anchor}) | {r['description']} "
            f"| {r.get('eis', '-')} | {r.get('prioriteit', '-')} "
            f"| {status} | {r['timestamp']} |"
        )
    return header + "\n" + "\n".join(rows)


def generate_details(results: dict) -> str:
    sections = []
    for tc_id in sorted(results):
        r = results[tc_id]
        meta = TC_META.get(tc_id, {})
        stappen = meta.get("stappen", [])

        lines = [f"### {tc_id} — Detail", ""]

        if stappen:
            lines.append("**Teststappen:**")
            for i, stap in enumerate(stappen, 1):
                lines.append(f"{i}. {stap}")
            lines.append("")

        lines.append(f"**Verwacht resultaat:** {r['expected']}")
        lines.append("")
        lines.append("**Werkelijk resultaat:**")
        lines.append(format_actual(r["actual"]))
        lines.append("")

        if r.get("conclusie"):
            lines.append(f"**Conclusie:** {r['conclusie']}")
            lines.append("")

        if r.get("screenshot"):
            lines.append("**Bewijs:**")
            lines.append(f"![{tc_id} {r['status'].lower()}]({r['screenshot']})")

        sections.append("\n".join(lines))

    return "\n\n---\n\n".join(sections)


def generate_statistieken(results: dict) -> str:
    totaal = len(results)
    geslaagd = sum(1 for r in results.values() if r["status"] == "GESLAAGD")
    gefaald = sum(1 for r in results.values() if r["status"] == "GEFAALD")
    geblokkeerd = sum(1 for r in results.values() if r["status"] == "GEBLOKKEERD")
    pct = round(geslaagd / totaal * 100) if totaal else 0

    return (
        "| Maat | Waarde |\n|---|---|\n"
        f"| Totaal aantal testen | {totaal} |\n"
        f"| Geslaagd | {geslaagd} |\n"
        f"| Gefaald | {gefaald} |\n"
        f"| Geblokkeerd | {geblokkeerd} |\n"
        f"| Slaagpercentage | {pct}% |"
    )


def main():
    results = load_results()

    with open(REPORT_PATH, encoding="utf-8") as f:
        content = f.read()

    content = replace_section(content, "OVERZICHT", generate_overzicht(results))
    content = replace_section(content, "DETAILS", generate_details(results))
    content = replace_section(content, "STATISTIEKEN", generate_statistieken(results))

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Testrapport bijgewerkt: {REPORT_PATH}")
    print(f"  {len(results)} testcase(s) verwerkt: {', '.join(sorted(results))}")


if __name__ == "__main__":
    main()
