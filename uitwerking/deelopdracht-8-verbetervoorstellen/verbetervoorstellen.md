# Verbetervoorstellen — IT Talenten Portaal

> Auteur: Steven
> Datum: april 2026
> Gebaseerd op: testrapport deelopdracht 7

---

## 1. Inleiding

Dit document bevat verbetervoorstellen op basis van de testresultaten uit deelopdracht 7. Alle 19 testcases zijn geslaagd, maar tijdens het testen zijn vier fouten gevonden en één verbetermogelijkheid geïdentificeerd. De voorstellen zijn onderverdeeld in correctieve voorstellen (op basis van gevonden fouten) en proactieve voorstellen (verbeteringen voor functionaliteit die werkt maar beter kan).

---

## 2. Analyse van de fouten

Van de vier gevonden fouten (F-001 t/m F-004) zijn drie fouten terug te vinden in het admin panel. Dit wijst erop dat het admin panel als geheel minder aandacht heeft gekregen bij de ontwikkeling op het gebied van gebruikerservaring. F-001 staat op zichzelf en betreft de externe Keycloak-loginpagina.

---

## 3. Overzicht verbetervoorstellen

| ID | Omschrijving | Type | Belang | Gebruikersrol |
|---|---|---|---|---|
| VP-001 | Loginpagina vertalen naar Nederlands | Correctief | Middel | Alle gebruikers |
| VP-002 | Uitlogknop toevoegen aan admin panel | Correctief | Laag | Beheerder |
| VP-003 | Bevestigingsmelding toevoegen na formulieracties | Correctief | Laag | Beheerder |
| VP-004 | Layout admin tabel herzien voor middelgrote viewports | Correctief | Laag | Beheerder |
| VP-005 | Gecombineerde reisafstand-filter op basis van geolocatie | Proactief | Laag | Organisatie |

---

## 4. Verbetervoorstellen per fout

### VP-001 — Loginpagina vertalen naar Nederlands

**Probleem:** De loginpagina wordt beheerd door Keycloak en toont alle teksten in het Engels ("Sign in to your account", "Username or email", "Password", "Sign In", "New user? Register"). Dit terwijl de applicatie gericht is op een Nederlandstalige doelgroep.

**Functionaliteit:** Authenticatie (FE1)

**Voorstel:** Stel de Nederlandse taalinstelling in binnen de Keycloak-configuratie voor dit realm. Keycloak ondersteunt meertaligheid via ingebouwde localisation-instellingen.

**Waarom:** Een Engelstalige loginpagina oogt onprofessioneel voor een applicatie die expliciet gericht is op de Nederlandse markt. De meeste gebruikers zullen de Engelse teksten begrijpen, maar de inconsistentie in taalgebruik ondermijnt de uitstraling van het product.

**Belang:** Middel — raakt alle gebruikers, maar vormt geen functionele blokkade.

**Gebruikersrol:** Alle gebruikers

---

### VP-002 — Uitlogknop toevoegen aan admin panel

**Probleem:** Het admin panel (`/admin`) heeft geen uitlogknop of -icoon. Een beheerder die uitwil loggen moet handmatig navigeren naar de hoofdapplicatie om daar uit te loggen.

**Functionaliteit:** Sessiebeheer (FE2), Admin panel

**Voorstel:** Voeg een uitlogknop toe aan de navigatiebalk of header van het admin panel.

**Waarom:** Hoewel er via een extra klik een uitlogmogelijkheid beschikbaar is, is dit niet intuïtief. Een uitlogknop hoort standaard aanwezig te zijn in elke beveiligde omgeving.

**Belang:** Laag — raakt uitsluitend interne beheerders, en er is een workaround beschikbaar.

**Gebruikersrol:** Beheerder

---

### VP-003 — Bevestigingsmelding toevoegen na formulieracties

**Probleem:** Na het aanmaken of bewerken van een talent in het admin panel verdwijnt het formulier zonder zichtbare bevestiging. Het is voor de beheerder niet direct duidelijk of de actie geslaagd is.

**Functionaliteit:** Talentbeheer (FE11), Admin panel

**Voorstel:** Voeg een tijdelijke bevestigingsmelding toe (snackbar of toast notification, gangbaar patroon in Angular Material) die verschijnt na het succesvol opslaan van een talent. Bijvoorbeeld: "Talent succesvol aangemaakt" of "Wijzigingen opgeslagen".

**Waarom:** Gebruikersfeedback na formulierverwerking is een basisverwachting in moderne webapplicaties. Het ontbreken ervan leidt tot onzekerheid bij de gebruiker.

**Belang:** Laag — raakt uitsluitend interne beheerders.

**Gebruikersrol:** Beheerder

---

### VP-004 — Layout admin tabel herzien voor middelgrote viewports

**Probleem:** De delete-knop in de talentenlijst (`/admin/talenten`) wordt visueel afgesneden bij viewportbreedtes groter dan ~950px en kleiner dan ~1560px. Alles werkt functioneel nog wel, maar de layout is zichtbaar gebroken.

**Functionaliteit:** Talentbeheer (FE11), Admin panel

**Voorstel:** Herzie het tabelontwerp voor het admin panel. Mogelijke oplossingen zijn het aanpassen van UI-breakpoints, het smaller maken van tabelcellen, of het herzien van het gehele tabelontwerp zodat knoppen altijd volledig zichtbaar blijven.

**Waarom:** Een gebroken layout ondermijnt het vertrouwen in de applicatie, ook als de functionaliteit intact is.

**Belang:** Laag — raakt uitsluitend interne beheerders; functionaliteit is niet aangetast.

**Gebruikersrol:** Beheerder

---

## 5. Proactief verbetervoorstel

### VP-005 — Gecombineerde reisafstand-filter op basis van geolocatie

**Situatie:** De talentenpagina biedt momenteel losse filters voor werklocatie en reisafstand. Deze filters zijn alleen samen zinvol: een organisatie wil weten welke talenten bereikbaar zijn vanuit hun locatie.

**Functionaliteit:** Talentenzoeken (FE4)

**Voorstel:** Vervang de losse filters door één gecombineerde reisafstand-filter. De gebruiker voert een locatie in (adres, postcode of geolocatie) en stelt een maximale reisafstand in. De applicatie filtert vervolgens talenten op basis van de reisafstand tussen het adres van het talent en de opgegeven locatie.

**Waarom:** Dit sluit beter aan bij de daadwerkelijke behoefte van organisaties: zij zoeken niet op provincie of abstracte afstand, maar op bereikbaarheid vanuit hun eigen vestiging.

**Belang:** Laag — de huidige filters werken, maar dit zou de bruikbaarheid voor organisaties aanzienlijk verbeteren.

**Gebruikersrol:** Organisatie

---

## 6. Conclusie

De vier gevonden fouten zijn geen functionele blokkades maar betreffen taalgebruik, ontbrekende gebruikersfeedback en een layoutprobleem — alle drie geconcentreerd in het admin panel. Het proactieve voorstel (VP-005) raakt de zoekfunctionaliteit voor organisaties en vraagt om een heroverweging van het filterontwerp. Geen van de voorstellen is urgent; het admin panel verdient als geheel de meeste aandacht.
