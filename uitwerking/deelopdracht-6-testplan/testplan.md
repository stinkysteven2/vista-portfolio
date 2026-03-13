# Testplan — IT Talenten Portaal

> Auteur: Steven
> Datum: maart 2026
> Applicatie: [IT Talenten Portaal](https://talenten-portaal-tp-test-webapp.iapmkw.easypanel.host)
> Gebaseerd op: `software-requirement-specification.md` (in deze map)

---

## 1. Inleiding

Dit testplan beschrijft hoe we het IT Talenten Portaal gaan testen. Het helpt om er zeker van te zijn dat de applicatie goed werkt en voldoet aan de eisen uit het SRS.

Het testplan is een werkinstructie: ongeacht wie de testen uitvoert, zouden de bevindingen zo veel mogelijk hetzelfde moeten zijn.

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
| TC-001 | FE1 | Inloggen met geldige gegevens | Hoog |
| TC-002 | FE1 | Inloggen met onjuist wachtwoord | Hoog |
| TC-003 | FE1 | Inloggen met onbekend e-mailadres | Gemiddeld |
| TC-004 | FE2 | Uitloggen | Hoog |
| TC-005 | FE2 | Sessie beëindigd na uitloggen | Hoog |
| TC-006 | FE3 | Talentprofiel afgeschermd voor bezoekers | Hoog |
| TC-007 | FE3 | Admin panel toegankelijkheid per rol | Hoog |
| TC-008 | FE4 | Filteren op provincie | Hoog |
| TC-009 | FE4 | Filteren op beschikbaarheid (grenswaarden) | Hoog |
| TC-010 | FE5 | Talentprofiel volledig zichtbaar voor ingelogde gebruiker | Hoog |
| TC-011 | FE5 | Talentprofiel gedeeltelijk zichtbaar voor bezoeker | Hoog |
| TC-012 | NFE1/NFE3 | IDOR — talentprofiel via URL-manipulatie | Hoog |
| TC-013 | FE11 | Talent aanmaken | Hoog |
| TC-014 | FE11 | Talent bewerken | Hoog |
| TC-015 | FE11 | Talent verwijderen | Hoog |
| TC-016 | FE11 | Werkervaring toevoegen | Gemiddeld |
| TC-017 | FE11 | Werkervaring bewerken | Gemiddeld |
| TC-018 | FE11 | Werkervaring verwijderen | Gemiddeld |
| TC-019 | FE11 | Opleiding toevoegen | Gemiddeld |
| TC-020 | FE11 | Opleiding bewerken | Gemiddeld |
| TC-021 | FE11 | Opleiding verwijderen | Gemiddeld |
| TC-022 | FE11 | Hobby/interesse toevoegen | Laag |
| TC-023 | FE11 | Hobby/interesse verwijderen | Laag |
| TC-024 | FE11 | Hobby/interesse sorteren | Laag |

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
