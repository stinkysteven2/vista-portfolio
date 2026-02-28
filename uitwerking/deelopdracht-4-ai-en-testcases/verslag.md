# Verslag — AI en testcases

## Gekozen functionaliteit

Ik heb gekozen voor **FE2: Inloggen**. Inloggen is een basisfunctionaliteit die in vrijwel elke applicatie voorkomt en veel te testen valt: geldige gegevens, ongeldige gegevens, lege velden, veiligheid en randgevallen. Het is daardoor een goede manier om te zien hoe ver AI-gegenereerde testcases reiken.

---

## Wat was goed aan de AI-testcases

De AI genereerde snel een bruikbare basisset testcases. Alle drie de FE2-eisen waren vertegenwoordigd (succesvol inloggen, foutafhandeling, wachtwoord vergeten). De structuur was helder en de stappen waren begrijpelijk geformuleerd. Voor een eerste opzet was het een goed startpunt.

---

## Wat heb ik aangepast en waarom

**Verwachte resultaten waren te vaag.** De AI schreef vaak "er wordt een foutmelding getoond", zonder te specificeren wat de melding moet zeggen. Een tester kan dan niet beoordelen of het systeem correct werkt. Ik heb alle verwachte resultaten concreter gemaakt.

**TC-06 bevatte een beveiligingsfout.** De AI verwachtte dat het systeem een foutmelding toont als een e-mailadres niet bekend is bij "Wachtwoord vergeten". Dit is een user enumeration kwetsbaarheid: een aanvaller kan zo uitvinden welke e-mailadressen in het systeem zitten. De correcte uitkomst is een neutrale melding, ongeacht of het adres bekend is.

**Ontbrekende testcases toegevoegd:**
- TC-04a en TC-04b: lege velden apart getest (de AI testte ze alleen samen).
- TC-07: accountblokkering na herhaalde mislukte pogingen (brute force bescherming).
- TC-08: sessie blijft actief bij navigeren.
- TC-09: speciale tekens in invoervelden (SQL injection en XSS).

---

## Mijn mening over AI voor testcases

AI is nuttig voor het snel opzetten van een basisstructuur. Het bespaart tijd en zorgt dat je de meest voor de hand liggende gevallen niet vergeet. Maar AI mist context: het weet niet hoe de applicatie er echt uitziet, welke beveiligingseisen er gelden, en welke edge cases specifiek voor dit systeem belangrijk zijn. De fout in TC-06 (user enumeration) is daar een goed voorbeeld van — de AI had niet door dat dit een beveiligingsrisico was.

Ik zou AI gebruiken als startpunt, maar nooit als eindproduct. Testcases altijd zelf doornemen en aanvullen.
