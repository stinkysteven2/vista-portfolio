# Verbeterde testcases — FE2: Inloggen

> Gebaseerd op de AI-output in `ai-output.md`, aangevuld en gecorrigeerd na beoordeling.

---

## Wat was goed aan de AI-output

- Goede basisstructuur met positieve én negatieve testcases.
- Alle drie de FE2-eisen (FE2.1, FE2.2, FE2.3) waren vertegenwoordigd.
- Stappen waren begrijpelijk geformuleerd.

## Wat ontbrak of was onvoldoende

| Probleem | Toelichting |
|----------|-------------|
| Verwachte resultaten te vaag | "Er wordt een foutmelding getoond" zegt niets over de inhoud. Een tester weet niet wat de juiste melding is. |
| TC-06 is een privacyprobleem | Het tonen van een foutmelding bij een onbekend e-mailadres geeft informatie weg aan aanvallers (user enumeration). De correct verwachte uitkomst is een neutrale melding. |
| Ontbrekend: lege velden individueel | TC-04 test beide velden leeg, maar niet elk veld afzonderlijk. |
| Ontbrekend: account blokkering | Geen test voor meerdere opeenvolgende mislukte inlogpogingen (brute force bescherming). |
| Ontbrekend: sessie na inloggen | Geen test of de sessie actief blijft bij navigeren, of correct afloopt bij uitloggen. |
| Ontbrekend: speciale tekens in invoer | Geen test voor SQL injection of XSS-tekens in de invoervelden. |

---

## Verbeterde testcases

| TC-ID | Beschrijving | Precondities | Stappen | Verwacht resultaat | FE-ref |
|-------|-------------|--------------|---------|-------------------|--------|
| TC-01 | Succesvol inloggen met geldige gegevens | Gebruiker heeft een actief account | 1. Ga naar /login. 2. Vul geldig e-mailadres in. 3. Vul correct wachtwoord in. 4. Klik op "Inloggen". | Gebruiker wordt doorgestuurd naar /home. Naam van gebruiker is zichtbaar in de navigatiebalk. | FE2.1 |
| TC-02 | Inloggen met ongeldig e-mailformaat | Gebruiker is niet ingelogd | 1. Ga naar /login. 2. Vul "geengeldigemail" in het e-mailveld. 3. Vul een wachtwoord in. 4. Klik op "Inloggen". | Formulier toont: "Vul een geldig e-mailadres in." Inloggen mislukt. | FE2.2 |
| TC-03 | Inloggen met verkeerd wachtwoord | Gebruiker heeft een actief account | 1. Ga naar /login. 2. Vul geldig e-mailadres in. 3. Vul een onjuist wachtwoord in. 4. Klik op "Inloggen". | Foutmelding: "E-mailadres of wachtwoord is onjuist." Wachtwoordveld wordt leeggemaakt. | FE2.2 |
| TC-04a | Inloggen met leeg e-mailveld | Gebruiker is op /login | 1. Laat e-mailveld leeg. 2. Vul een wachtwoord in. 3. Klik op "Inloggen". | Foutmelding bij e-mailveld: "Dit veld is verplicht." Inloggen mislukt. | FE2.2 |
| TC-04b | Inloggen met leeg wachtwoordveld | Gebruiker is op /login | 1. Vul een e-mailadres in. 2. Laat wachtwoordveld leeg. 3. Klik op "Inloggen". | Foutmelding bij wachtwoordveld: "Dit veld is verplicht." Inloggen mislukt. | FE2.2 |
| TC-05 | Wachtwoord vergeten — e-mail versturen | Gebruiker heeft een actief account | 1. Ga naar /login. 2. Klik op "Wachtwoord vergeten". 3. Vul het bekende e-mailadres in. 4. Klik op "Verstuur". | Bevestigingsbericht: "Als dit e-mailadres bekend is, ontvang je een resetlink." Gebruiker ontvangt e-mail met geldige resetlink. | FE2.3 |
| TC-06 | Wachtwoord vergeten — onbekend e-mailadres | Gebruiker is op de wachtwoord-vergeten-pagina | 1. Klik op "Wachtwoord vergeten". 2. Vul een e-mailadres in dat niet bestaat. 3. Klik op "Verstuur". | Zelfde neutrale bevestigingsbericht als TC-05: "Als dit e-mailadres bekend is, ontvang je een resetlink." Geen onderscheid met TC-05 zichtbaar voor de gebruiker. | FE2.3 |
| TC-07 | Accountblokkering na herhaalde mislukte pogingen | Gebruiker heeft een actief account | 1. Ga naar /login. 2. Voer 5x achter elkaar een onjuist wachtwoord in. 3. Probeer opnieuw in te loggen. | Account is tijdelijk geblokkeerd. Melding: "Te veel mislukte pogingen. Probeer het later opnieuw." | FE2.2 |
| TC-08 | Sessie blijft actief bij navigeren | Gebruiker is ingelogd (TC-01 geslaagd) | 1. Log in. 2. Navigeer naar /vacatures. 3. Navigeer terug naar /home. | Gebruiker blijft ingelogd. Naam is zichtbaar in navigatiebalk op alle pagina's. | FE2.1 |
| TC-09 | Speciale tekens in invoervelden | Gebruiker is op /login | 1. Vul `' OR 1=1; --` in het e-mailveld. 2. Vul `<script>alert(1)</script>` in het wachtwoordveld. 3. Klik op "Inloggen". | Inloggen mislukt. Geen SQL-fout of scriptuitvoering zichtbaar. Foutmelding: "E-mailadres of wachtwoord is onjuist." | FE2.2 |
