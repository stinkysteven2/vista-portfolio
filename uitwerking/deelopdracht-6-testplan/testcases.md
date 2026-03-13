# Testcases — IT Talenten Portaal

> Gebaseerd op: `uitgangspunten/software-requirement-specification.md` en `testplan.md`
> Format geïnspireerd op: testplan SensorShip (mbogodigital.nl)

---

## FE1 — Inloggen

### TC-001: Inloggen met geldige gegevens

**Doel:** Verifiëren dat een gebruiker met geldige inloggegevens succesvol kan inloggen.

**Stappen:**
1. Navigeer naar de startpagina
2. Klik op het login-icoon in de navigatiebalk
3. Vul een geldig e-mailadres in
4. Vul het bijbehorende wachtwoord in
5. Klik op "Sign In"

**Verwacht resultaat:** De gebruiker wordt doorgestuurd naar de startpagina. De navigatiebalk toont de `logout`-knop en admin-iconen.

**Prioriteit:** Hoog

---

### TC-002: Inloggen met onjuist wachtwoord

**Doel:** Verifiëren dat het systeem een foutmelding toont bij een onjuist wachtwoord.

**Stappen:**
1. Navigeer naar de startpagina
2. Klik op het login-icoon in de navigatiebalk
3. Vul een geldig e-mailadres in
4. Vul een onjuist wachtwoord in
5. Klik op "Sign In"

**Verwacht resultaat:** De gebruiker blijft op de loginpagina. De foutmelding *"Invalid username or password."* wordt getoond.

**Prioriteit:** Hoog

---

### TC-003: Inloggen met onbekend e-mailadres

**Doel:** Verifiëren dat het systeem een foutmelding toont bij een onbekend e-mailadres.

**Stappen:**
1. Navigeer naar de startpagina
2. Klik op het login-icoon in de navigatiebalk
3. Vul een onbekend e-mailadres in (bijv. `onbekend@test.nl`)
4. Vul een willekeurig wachtwoord in
5. Klik op "Sign In"

**Verwacht resultaat:** De gebruiker blijft op de loginpagina. De foutmelding *"Invalid username or password."* wordt getoond. Het systeem maakt geen onderscheid tussen onbekend account en fout wachtwoord.

**Prioriteit:** Gemiddeld

---

## FE2 — Uitloggen

### TC-004: Uitloggen

**Doel:** Verifiëren dat een ingelogde gebruiker succesvol kan uitloggen.

**Stappen:**
1. Log in met geldige gegevens (zie TC-001)
2. Klik op het logout-icoon in de navigatiebalk

**Verwacht resultaat:** De gebruiker is uitgelogd. De navigatiebalk toont het login-icoon en niet langer de logout-knop.

**Prioriteit:** Hoog

---

### TC-005: Sessie beëindigd na uitloggen

**Doel:** Verifiëren dat beschermde content niet meer toegankelijk is na uitloggen.

**Stappen:**
1. Log in met geldige gegevens (zie TC-001)
2. Navigeer naar een talentprofiel
3. Klik op het logout-icoon in de navigatiebalk
4. Klik op de terugknop van de browser

**Verwacht resultaat:** Het talentprofiel met persoonsgegevens is niet meer zichtbaar. De gebruiker wordt omgeleid of ziet geen beschermde content.

**Prioriteit:** Hoog

---

## FE3 — Autorisatie

### TC-006: Talentprofiel afgeschermd voor bezoekers

**Doel:** Verifiëren dat persoonsgegevens van een talent niet zichtbaar zijn voor niet-ingelogde gebruikers.

**Stappen:**
1. Zorg dat je niet ingelogd bent
2. Navigeer direct naar een talentprofiel via de URL (bijv. `/talent/talentprofile/1`)

**Verwacht resultaat:** De pagina laadt, maar naam en contactgegevens zijn niet zichtbaar. Er is een "Inloggen" call-to-action zichtbaar.

**Prioriteit:** Hoog

---

### TC-007: Admin panel toegankelijkheid per rol

**Doel:** Verifiëren dat het admin panel alleen toegankelijk is voor beheerders.

**Stappen:**
1. Navigeer als **bezoeker** (niet ingelogd) naar `/admin`
2. Navigeer als **ingelogde gebruiker** (niet-admin) naar `/admin`
3. Navigeer als **beheerder** naar `/admin`

**Verwacht resultaat:**
- Bezoeker: wordt omgeleid, geen toegang tot admin panel
- Ingelogde gebruiker (niet-admin): wordt omgeleid, geen toegang tot admin panel
- Beheerder: admin panel is zichtbaar en toegankelijk

**Prioriteit:** Hoog

---

## FE4 — Filteren

### TC-008: Filteren op provincie

**Doel:** Verifiëren dat het provinciefilter alleen talenten toont uit de geselecteerde provincie.

**Stappen:**
1. Navigeer naar de talentenpagina (`/talent`)
2. Noteer het aantal getoonde talenten
3. Selecteer een provincie via het provinciefilter (bijv. Noord-Brabant)
4. Bekijk de gefilterde resultaten

**Verwacht resultaat:** Alleen talenten uit de geselecteerde provincie worden getoond. Het aantal resultaten is kleiner dan of gelijk aan het oorspronkelijke aantal.

**Prioriteit:** Hoog

---

### TC-009: Filteren op beschikbaarheid (grenswaarden)

**Doel:** Verifiëren dat het beschikbaarheidsfilter talenten correct uitsluit op basis van een minimum- en maximumwaarde.

**Stappen:**
1. Navigeer naar de talentenpagina (`/talent`)
2. Noteer welke talenten beschikbaar zijn en hoeveel uur zij beschikbaar zijn
3. Stel een ondergrens en bovengrens in voor beschikbaarheid (bijv. 20–32 uur)
4. Controleer de gefilterde resultaten

**Verwacht resultaat:** Talenten met een beschikbaarheid onder de ondergrens vallen af. Talenten met een beschikbaarheid boven de bovengrens vallen af. Alleen talenten binnen het opgegeven bereik worden getoond.

**Prioriteit:** Hoog

---

## FE5 — Talentprofiel

### TC-010: Talentprofiel volledig zichtbaar voor ingelogde gebruiker

**Doel:** Verifiëren dat alle verwachte profielattributen zichtbaar zijn voor een ingelogde gebruiker.

**Stappen:**
1. Log in met geldige gegevens (zie TC-001)
2. Navigeer naar een talentprofiel (bijv. `/talent/talentprofile/1`)

**Verwacht resultaat:** De volgende attributen zijn zichtbaar:
- Naam
- Functietitel
- Locatie
- Werkervaring (datums, werkgever, rol)
- Kernkwaliteiten
- Vaardigheden (methoden, tools, talen, etc.)
- Contactknop
- Terugknop naar overzicht

**Prioriteit:** Hoog

---

### TC-011: Talentprofiel gedeeltelijk zichtbaar voor bezoeker

**Doel:** Verifiëren dat persoonsgegevens verborgen zijn voor niet-ingelogde gebruikers en dat publieke attributen wel zichtbaar zijn.

**Stappen:**
1. Zorg dat je niet ingelogd bent
2. Navigeer direct naar een talentprofiel via de URL (bijv. `/talent/talentprofile/1`)

**Verwacht resultaat:**
- De volgende attributen zijn **niet** zichtbaar: naam, contactgegevens
- De volgende attributen zijn **wel** zichtbaar: vaardigheden, werkniveau, beschikbaarheid, provincie
- Er is een "Inloggen" call-to-action zichtbaar

**Prioriteit:** Hoog

---

## NFE1/NFE3 — IDOR

### TC-012: IDOR — talentprofiel via URL-manipulatie

**Doel:** Verifiëren dat persoonsgegevens van talenten niet toegankelijk zijn via directe URL-manipulatie zonder login.

**Stappen:**
1. Zorg dat je niet ingelogd bent
2. Navigeer naar `/talent/talentprofile/1`
3. Noteer welke gegevens zichtbaar zijn
4. Verander het ID in de URL naar `/talent/talentprofile/2`, `/talent/talentprofile/3`, etc.
5. Controleer per profiel welke gegevens zichtbaar zijn

**Verwacht resultaat:** Voor geen enkel profiel zijn naam of contactgegevens zichtbaar zonder login. De applicatie toont voor elk ID dezelfde beperkte weergave als voor niet-ingelogde gebruikers.

**Prioriteit:** Hoog

---

## FE11 — Talentenbeheer (admin)

### TC-013: Talent aanmaken

**Doel:** Verifiëren dat een beheerder een nieuw talent kan aanmaken via het admin panel.

**Stappen:**
1. Log in als beheerder (zie TC-001)
2. Navigeer naar `/admin/talenten`
3. Klik op "Talent toevoegen"
4. Vul de verplichte velden in met de volgende testdata:
   - Initialen: `T.`
   - Voornaam: `Test`
   - Tussenvoegsel: *(leeg)*
   - Achternaam: `Talent`
   - Geboortedatum: `01-01-2000`
   - Opleidingsniveau: `MBO`
   - Straat: `Teststraat`
   - Huisnummer: `1`
   - Toevoeging: *(leeg)*
   - Postcode: `1234 AB`
   - Woonplaats: `Teststad`
   - Telefoonnummer: `+31612345678`
   - E-mail: `test.talent@example.com`
5. Sla het talent op

**Verwacht resultaat:** Het nieuwe talent verschijnt in de talentenlijst op `/admin/talenten`.

**Prioriteit:** Hoog

---

### TC-014: Talent bewerken

**Doel:** Verifiëren dat een beheerder een bestaand talent kan bewerken.

**Stappen:**
1. Log in als beheerder (zie TC-001)
2. Navigeer naar `/admin/talenten`
3. Klik op "Edit" bij het talent aangemaakt in TC-013 (Test Talent)
4. Wijzig de woonplaats van `Teststad` naar `Gewijzigdstad`
5. Sla de wijziging op

**Verwacht resultaat:** De woonplaats van het talent is bijgewerkt naar `Gewijzigdstad` in de talentenlijst.

**Prioriteit:** Hoog

---

### TC-015: Talent verwijderen

**Doel:** Verifiëren dat een beheerder een talent kan verwijderen.

**Stappen:**
1. Log in als beheerder (zie TC-001)
2. Navigeer naar `/admin/talenten`
3. Klik op "Delete" bij het talent aangemaakt in TC-013 (Test Talent)
4. Bevestig de verwijdering indien gevraagd

**Verwacht resultaat:** Het talent is niet meer zichtbaar in de talentenlijst op `/admin/talenten`.

**Prioriteit:** Hoog

---

### TC-016: Werkervaring toevoegen

**Doel:** Verifiëren dat een beheerder werkervaring kan toevoegen aan een talentprofiel.

**Stappen:**
1. Log in als beheerder en navigeer naar `/admin/talenten`
2. Klik op "Edit" bij een bestaand talent
3. Open het paneel "Werkervaring"
4. Voeg een nieuwe werkervaringsregel toe met testdata (bijv. werkgever: `Test BV`, functie: `Tester`, periode: `2023–2024`)
5. Sla het talent op

**Verwacht resultaat:** De werkervaring is zichtbaar in het profiel van het talent.

**Prioriteit:** Gemiddeld

---

### TC-017: Werkervaring bewerken

**Doel:** Verifiëren dat een beheerder bestaande werkervaring kan bewerken.

**Stappen:**
1. Log in als beheerder en navigeer naar het bewerkscherm van een talent met werkervaring
2. Open het paneel "Werkervaring"
3. Bewerk de functietitel van een bestaande regel (bijv. van `Tester` naar `Senior Tester`)
4. Sla het talent op

**Verwacht resultaat:** De gewijzigde functietitel is zichtbaar in het profiel van het talent.

**Prioriteit:** Gemiddeld

---

### TC-018: Werkervaring verwijderen

**Doel:** Verifiëren dat een beheerder werkervaring kan verwijderen van een talentprofiel.

**Stappen:**
1. Log in als beheerder en navigeer naar het bewerkscherm van een talent met werkervaring
2. Open het paneel "Werkervaring"
3. Verwijder een werkervaringsregel
4. Sla het talent op

**Verwacht resultaat:** De verwijderde werkervaring is niet meer zichtbaar in het profiel van het talent.

**Prioriteit:** Gemiddeld

---

### TC-019: Opleiding toevoegen

**Doel:** Verifiëren dat een beheerder een opleiding kan toevoegen aan een talentprofiel.

**Stappen:**
1. Log in als beheerder en navigeer naar het bewerkscherm van een talent
2. Open het paneel "Opleidingen"
3. Voeg een opleiding toe met testdata (bijv. opleiding: `Software Developer`, instelling: `Test ROC`, jaar: `2022`)
4. Sla het talent op

**Verwacht resultaat:** De opleiding is zichtbaar in het profiel van het talent.

**Prioriteit:** Gemiddeld

---

### TC-020: Opleiding bewerken

**Doel:** Verifiëren dat een beheerder een bestaande opleiding kan bewerken.

**Stappen:**
1. Log in als beheerder en navigeer naar het bewerkscherm van een talent met een opleiding
2. Open het paneel "Opleidingen"
3. Wijzig het afstudeerjaar (bijv. van `2022` naar `2023`)
4. Sla het talent op

**Verwacht resultaat:** Het gewijzigde jaar is zichtbaar in het profiel van het talent.

**Prioriteit:** Gemiddeld

---

### TC-021: Opleiding verwijderen

**Doel:** Verifiëren dat een beheerder een opleiding kan verwijderen van een talentprofiel.

**Stappen:**
1. Log in als beheerder en navigeer naar het bewerkscherm van een talent met een opleiding
2. Open het paneel "Opleidingen"
3. Verwijder een opleiding
4. Sla het talent op

**Verwacht resultaat:** De verwijderde opleiding is niet meer zichtbaar in het profiel van het talent.

**Prioriteit:** Gemiddeld

---

### TC-022: Hobby/interesse toevoegen

**Doel:** Verifiëren dat een beheerder een hobby of interesse kan toevoegen aan een talentprofiel.

**Stappen:**
1. Log in als beheerder en navigeer naar het bewerkscherm van een talent
2. Open het paneel "Hobby's (& Interesses)"
3. Voeg een hobby toe (bijv. `Schaken`)
4. Sla het talent op

**Verwacht resultaat:** De hobby is zichtbaar in het profiel van het talent.

**Prioriteit:** Laag

---

### TC-023: Hobby/interesse verwijderen

**Doel:** Verifiëren dat een beheerder een hobby of interesse kan verwijderen van een talentprofiel.

**Stappen:**
1. Log in als beheerder en navigeer naar het bewerkscherm van een talent met een hobby
2. Open het paneel "Hobby's (& Interesses)"
3. Verwijder een hobby
4. Sla het talent op

**Verwacht resultaat:** De verwijderde hobby is niet meer zichtbaar in het profiel van het talent.

**Prioriteit:** Laag

---

### TC-024: Hobby/interesse sorteren

**Doel:** Verifiëren dat een beheerder de volgorde van hobby's en interesses kan aanpassen.

**Stappen:**
1. Log in als beheerder en navigeer naar het bewerkscherm van een talent met meerdere hobby's
2. Open het paneel "Hobby's (& Interesses)"
3. Verander de volgorde van twee hobby's (bijv. via slepen of prioriteitsknop)
4. Sla het talent op

**Verwacht resultaat:** De nieuwe volgorde van hobby's is zichtbaar in het profiel van het talent.

**Prioriteit:** Laag

---
