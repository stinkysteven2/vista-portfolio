# Testplan — IT Talenten Portaal

> Auteur: Steven
> Datum: maart 2026
> Applicatie: [IT Talenten Portaal](https://talenten-portaal-tp-test-webapp.iapmkw.easypanel.host)
> Gebaseerd op: `software-requirement-specification.md` (in deze map)

---

## 1. Inleiding

Dit testplan beschrijft hoe we het IT Talenten Portaal gaan testen. Het helpt om er zeker van te zijn dat de applicatie goed werkt en voldoet aan de eisen uit het SRS.

---

## 2. Wat wordt getest

Op basis van het SRS en het scope document worden de volgende eisen getest:

| Eis | Omschrijving | Reden |
|---|---|---|
| FE1 | Inloggen (alle gevallen) | Kernfunctionaliteit, goed testbaar |
| FE2 | Uitloggen + sessiebeëindiging | Veiligheid |
| FE3 | Autorisatie per rol | AVG, veiligheid |
| FE4 | Filteren op provincie en beschikbaarheid | Kernfunctionaliteit, twee verschillende interactiemechanismen |
| FE5 | Talentprofiel bekijken | Kernfunctionaliteit |
| FE11 | Talentenbeheer (admin) | Kernfunctionaliteit admin |
| FE14 | Property labels beheren (admin) | Beheerfunctionaliteit |
| NFE1/NFE3 | IDOR-test: talentprofiel zonder login | AVG, veiligheid |

**Niet getest:**

| Eis | Reden |
|---|---|
| FE6 — Favorieten | Lage prioriteit, geen leerwaarde |
| FE7/FE8 — Vacatures | Geen business prioriteit |
| FE9.1 — Talentregistratie | Functionaliteit niet aanwezig in de applicatie |
| FE9.2 — Beheerder melding binnen 24 uur | Extern proces, niet te testen |
| FE10 — Gebruikersbeheer | Buiten scope van deze testronde |
| FE12/FE13 — Organisaties, bedrijven, vacaturesbeheer | Buiten scope van deze testronde |
| Vaardigheden & Eigenschappen (talentprofiel) | Oogt onafgemaakt; verwachting is dat dit onderdeel nog gaat veranderen. Bevindingen worden wel opgenomen in het testrapport. |
| Bekende bugs (B1-B5) | Al gedocumenteerd in deelopdracht 1 |

---

## 3. Hoe wordt getest

### 3.1 Testmethoden

**Geautomatiseerd** — via Playwright (Python) op Chrome. Geautomatiseerde testen dekken de functionele eisen en worden herhaald bij elke wijziging.

**Handmatig** — aanvullend op Chrome (desktop), Edge (desktop) en Safari (mobiel) voor visuele correctheid en gebruiksvriendelijkheid.

### 3.2 Testvolgorde

Testen worden uitgevoerd per gebruikersrol, van minste naar meeste rechten:

1. **Bezoeker** (niet ingelogd) — filters, publieke pagina's, IDOR-test
2. **Ingelogde gebruiker** — talentprofiel, uitloggen, sessiebeëindiging
3. **Admin** — talentenbeheer, property labels
4. **Talent** — *(vervalt: registratiefunctionaliteit niet aanwezig)*

De reden voor deze volgorde: elke rol bouwt voort op de vorige. Bovendien vereist de talent-rol een door de admin goedgekeurd account, dus de admin moet eerst werken.

### 3.3 Overlap tussen testcases

Sommige testcases testen dezelfde pagina of functionaliteit vanuit een andere invalshoek. Dit is bewust — een testcase die autorisatie test vertelt een ander verhaal dan een testcase die profielinhoud test, ook als ze dezelfde URL bezoeken. Overlap wordt niet actief vermeden.

### 3.4 Verwijzing naar testcases

De gedetailleerde testcases staan in `testcases.md` (in deze map). Elke testcase verwijst terug naar een FE- of NFE-eis uit het SRS.

| TC | Eis | Omschrijving | Prioriteit |
|---|---|---|---|
| [TC-001](testcases.md#tc-001-inloggen-met-geldige-gegevens) | [FE1](software-requirement-specification.md#41-authenticatie-en-autorisatie) | Inloggen met geldige gegevens | Hoog |
| [TC-002](testcases.md#tc-002-inloggen-met-onjuist-wachtwoord) | [FE1](software-requirement-specification.md#41-authenticatie-en-autorisatie) | Inloggen met onjuist wachtwoord | Hoog |
| [TC-003](testcases.md#tc-003-inloggen-met-onbekend-e-mailadres) | [FE1](software-requirement-specification.md#41-authenticatie-en-autorisatie) | Inloggen met onbekend e-mailadres | Gemiddeld |
| [TC-004](testcases.md#tc-004-uitloggen) | [FE2](software-requirement-specification.md#41-authenticatie-en-autorisatie) | Uitloggen | Hoog |
| [TC-005](testcases.md#tc-005-sessie-beëindigd-na-uitloggen) | [FE2](software-requirement-specification.md#41-authenticatie-en-autorisatie) | Sessie beëindigd na uitloggen | Hoog |
| [TC-006](testcases.md#tc-006-talentprofiel-afgeschermd-voor-bezoekers) | [FE3](software-requirement-specification.md#41-authenticatie-en-autorisatie) | Talentprofiel afgeschermd voor bezoekers | Hoog |
| [TC-007](testcases.md#tc-007-admin-panel-toegankelijkheid-per-rol) | [FE3](software-requirement-specification.md#41-authenticatie-en-autorisatie) | Admin panel toegankelijkheid per rol | Hoog |
| [TC-008](testcases.md#tc-008-filteren-op-provincie) | [FE4](software-requirement-specification.md#42-talenten-zoeken-en-filteren) | Filteren op provincie | Hoog |
| [TC-009](testcases.md#tc-009-filteren-op-beschikbaarheid-grenswaarden) | [FE4](software-requirement-specification.md#42-talenten-zoeken-en-filteren) | Filteren op beschikbaarheid (grenswaarden) | Hoog |
| [TC-010](testcases.md#tc-010-talentprofiel-volledig-zichtbaar-voor-ingelogde-gebruiker) | [FE5](software-requirement-specification.md#42-talenten-zoeken-en-filteren) | Talentprofiel volledig zichtbaar voor ingelogde gebruiker | Hoog |
| [TC-011](testcases.md#tc-011-talentprofiel-gedeeltelijk-zichtbaar-voor-bezoeker) | [FE5](software-requirement-specification.md#42-talenten-zoeken-en-filteren) | Talentprofiel gedeeltelijk zichtbaar voor bezoeker | Hoog |
| [TC-012](testcases.md#tc-012-idor--talentprofiel-via-url-manipulatie) | [NFE1/NFE3](software-requirement-specification.md#51-veiligheid) | IDOR — talentprofiel via URL-manipulatie | Hoog |
| [TC-013](testcases.md#tc-013-talent-aanmaken) | [FE11](software-requirement-specification.md#46-admin-panel) | Talent aanmaken | Hoog |
| [TC-014](testcases.md#tc-014-talent-bewerken) | [FE11](software-requirement-specification.md#46-admin-panel) | Talent bewerken | Hoog |
| [TC-015](testcases.md#tc-015-talent-verwijderen) | [FE11](software-requirement-specification.md#46-admin-panel) | Talent verwijderen | Hoog |
| [TC-016](testcases.md#tc-016-werkervaring-toevoegen) | [FE11](software-requirement-specification.md#46-admin-panel) | Werkervaring toevoegen | Gemiddeld |
| [TC-017](testcases.md#tc-017-werkervaring-bewerken) | [FE11](software-requirement-specification.md#46-admin-panel) | Werkervaring bewerken | Gemiddeld |
| [TC-018](testcases.md#tc-018-werkervaring-verwijderen) | [FE11](software-requirement-specification.md#46-admin-panel) | Werkervaring verwijderen | Gemiddeld |
| [TC-019](testcases.md#tc-019-opleiding-toevoegen) | [FE11](software-requirement-specification.md#46-admin-panel) | Opleiding toevoegen | Gemiddeld |
| [TC-020](testcases.md#tc-020-opleiding-bewerken) | [FE11](software-requirement-specification.md#46-admin-panel) | Opleiding bewerken | Gemiddeld |
| [TC-021](testcases.md#tc-021-opleiding-verwijderen) | [FE11](software-requirement-specification.md#46-admin-panel) | Opleiding verwijderen | Gemiddeld |
| [TC-022](testcases.md#tc-022-hobbyinteresse-toevoegen) | [FE11](software-requirement-specification.md#46-admin-panel) | Hobby/interesse toevoegen | Laag |
| [TC-023](testcases.md#tc-023-hobbyinteresse-verwijderen) | [FE11](software-requirement-specification.md#46-admin-panel) | Hobby/interesse verwijderen | Laag |
| [TC-024](testcases.md#tc-024-hobbyinteresse-sorteren) | [FE11](software-requirement-specification.md#46-admin-panel) | Hobby/interesse sorteren | Laag |

---

## 4. Planning

De exacte deadline voor deelopdracht 6 is nog niet bekend. De planning wordt ingevuld zodra deze beschikbaar is. De testvolgorde staat vast (zie sectie 3.2).

| Fase | Inhoud |
|---|---|
| Fase 1 | Bezoeker: filters en IDOR |
| Fase 2 | Ingelogde gebruiker: talentprofiel, uitloggen |
| Fase 3 | Admin: talentenbeheer, property labels |
| Fase 4 | *(vervalt)* |

---

## 5. Wat is nodig

### 5.1 Testomgeving

| Omgeving | URL |
|---|---|
| Applicatie (frontend) | https://talenten-portaal-tp-test-webapp.iapmkw.easypanel.host |
| API (backend) | https://talenten-portaal-tp-test-api.iapmkw.easypanel.host |
| Authenticatie (Keycloak) | https://keycloak-test-keycloak-test-instance.iapmkw.easypanel.host |

### 5.2 Testdata

| Gegeven | Waarde | Opmerking |
|---|---|---|
| Admin account | `admin` / `[REDACTED]` | Beschikbaar |
| Talent account | nader te bepalen | Aan te maken door admin vóór testuitvoering |
| Bestaand talentprofiel-ID | nader te bepalen | Op te zoeken via talentenoverzicht |

### 5.3 Tools

| Tool | Doel |
|---|---|
| Playwright (Python) | Geautomatiseerde functionele testen |
| Chrome | Primaire testbrowser |
| Edge | Handmatig testen desktop |
| Safari (mobiel) | Handmatig testen mobiel |

### 5.4 Mensen

- De admin moet vóór testfase 4 een testaccount voor een talent aanmaken.
- Geen andere externe afhankelijkheden.

---

## 6. Risico's en oplossingen

| Risico | Kans | Impact | Oplossing |
|---|---|---|---|
| Testomgeving niet beschikbaar | Laag | Hoog | Opnieuw proberen na 24 uur; contact opnemen met beheerder |
| Geen inloggegevens voor talent-rol | Gemiddeld | Gemiddeld | Admin maakt testaccount aan vóór testfase 4 |
| Keycloak sessie verloopt tijdens testen | Gemiddeld | Laag | Opnieuw inloggen; Playwright script houdt rekening met re-authenticatie |
| Testdata wordt overschreven door andere testers | Laag | Gemiddeld | Aparte testaccounts gebruiken; naamconventie hanteren (bijv. `test-talent-steven`) |
| Applicatie bevat bekende bugs die testuitvoering blokkeren | Gemiddeld | Gemiddeld | Bevinding documenteren, test markeren als geblokkeerd, doorgaan met volgende testcase |
