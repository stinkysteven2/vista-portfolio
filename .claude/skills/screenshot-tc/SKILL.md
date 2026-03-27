---
name: screenshot-tc
description: Voeg automatische screenshots toe aan een Playwright-testfunctie in run_tests.py
---

Voeg een automatische screenshot toe aan de Playwright-testfunctie voor de opgegeven TC in `lib/run_tests.py`.

**TC-ID:** $ARGUMENTS

**Stappen:**

1. Lees `lib/run_tests.py` en zoek de functie voor TC-ID $ARGUMENTS.
2. Bepaal het juiste moment voor de screenshot: vlak na het verwachte resultaat (geslaagd of gefaald).
3. Voeg `page.screenshot(path=...)` toe op dat moment. Sla de screenshot op in `uitwerking/deelopdracht-7-testrapportage/screenshots/` met bestandsnaam `<TC-ID-lowercase>-<status>.png` (bijv. `tc001-geslaagd.png`).
4. Zorg dat de map bestaat door `os.makedirs(..., exist_ok=True)` toe te voegen indien dat nog niet in het script staat.
5. Voeg het pad naar de screenshot toe aan de `result()`-aanroep als extra notitie.
6. Voer het script uit om te controleren dat de screenshot correct wordt aangemaakt.
7. Bevestig aan de gebruiker welke screenshot is opgeslagen en op welk pad.
