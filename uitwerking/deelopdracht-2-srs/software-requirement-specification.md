# 1. Inleiding

## 1.1 Doel van het Document

Dit **Software Requirement Specification (SRS)** document beschrijft de functionele en niet-functionele eisen voor **IT Showcase**. Het document dient als basis voor de ontwikkeling, testen en implementatie van het systeem.
## 1.2 Doel van het Project

Het doel van dit project is het ontwikkelen van **IT Showcase**, een professionele website waarop:

    Studenten van ICT opleidingen hun beste projecten kunnen presenteren
    Projecten op een aantrekkelijke en overzichtelijke manier worden getoond
    Studentenprofielen worden weergegeven met hun vaardigheden en ervaring
    Bezoekers (potentiële werkgevers, docenten, medestudenten) projecten en studenten kunnen ontdekken

## 1.3 Doelgroep van dit Document

Dit document is bedoeld voor:

    Ontwikkelaars die het systeem gaan bouwen
    Testers die het systeem gaan testen
    Projectmanagers die het project beheren
    Stakeholders die beslissingen nemen over het project
    Docenten en beheerders die het systeem gaan gebruiken

# 2. Scope

## 2.1 Wat valt binnen de scope

Het systeem omvat:

    Een publiek toegankelijke website voor het bekijken van projecten en studentprofielen
    Een beheerdersgedeelte voor het beheren van projecten, studenten en content
    Een studentgedeelte voor het aanmaken en beheren van eigen projecten en profiel
    Zoek- en filterfunctionaliteit voor projecten en studenten
    Responsive design voor verschillende apparaten (desktop, tablet, mobiel)
    Authenticatie en autorisatie voor verschillende gebruikersrollen

## 2.2 Wat valt buiten de scope

Het systeem omvat **NIET**:

    Integratie met externe leeromgevingen (zoals Moodle, Canvas)
    Betalingsfunctionaliteit
    Real-time chat of messaging tussen gebruikers
    Social media integraties (behalve mogelijk links naar externe profielen)
    Video streaming of live presentaties
    Geavanceerde analytics of rapportage tools
    Mobile apps (alleen responsive website)

# 3. Definities en Afkortingen

## 3.1 Afkortingen

- **SRS**: Software Requirement Specification
- **UI**: User Interface (Gebruikersinterface)
- **UX**: User Experience (Gebruikerservaring)
- **API**: Application Programming Interface
- **CMS**: Content Management System
- **CRUD**: Create, Read, Update, Delete
- **ICT**: Informatie- en Communicatietechnologie
- **GDPR**: General Data Protection Regulation (AVG)

3.2 Definities

    Portfolio: Een verzameling van projecten die een student heeft gemaakt
    Project: Een werkstuk, applicatie of opdracht die door een of meerdere studenten is gemaakt
    Studentprofiel: Een profielpagina met informatie over een student, inclusief vaardigheden en projecten
    Beheerder: Een gebruiker met volledige rechten om content te beheren
    Docent: Een gebruiker met rechten om projecten te beoordelen en goed te keuren
    Bezoeker: Een niet-ingelogde gebruiker die alleen publieke content kan bekijken

# 4. Overzicht

## 4.1 Productperspectief

**IT Showcase** is een webapplicatie die:

- Bestaat uit een **frontend** applicatie en een **backend** `API`
- Gebruik maakt van een aparte **Authenticatie API** voor authenticatie en gebruikersbeheer
- Gebruik maakt van een moderne webtechnologie stack
- **Responsive** is en werkt op verschillende apparaten en browsers
- Schaalbaar is om groeiende aantallen studenten en projecten te ondersteunen

## 4.2 Productfuncties

De belangrijkste functies van het systeem zijn:

    Projectbeheer: Studenten kunnen projecten aanmaken, bewerken en beheren
    Profielbeheer: Studenten kunnen hun profiel aanmaken en bijwerken
    Contentweergave: Publieke weergave van projecten en studentprofielen
    Dashboard Showcase: Docenten kunnen de beste projecten selecteren voor een showcase op het dashboard
    Zoeken en filteren: Bezoekers kunnen zoeken en filteren op verschillende criteria
    Beheerfunctionaliteit: Beheerders kunnen content modereren en beheren
    Authenticatie: Gebruikers kunnen inloggen en uitloggen

## 4.3 Gebruikersklassen

Het systeem kent de volgende gebruikersklassen:

- **Bezoeker**: Kan publieke projecten en profielen bekijken
- **Student**: Kan eigen projecten en profiel beheren, kan projecten bekijken
- **Docent**: Kan projecten beoordelen en goedkeuren, kan alle content bekijken
- **Beheerder**: Heeft volledige toegang tot alle functionaliteit

# 5. Gebruikersbeschrijving

## 5.1 Bezoeker

**Beschrijving**: Een bezoeker is een niet-ingelogde gebruiker die de website bezoekt om projecten en studentprofielen te bekijken.

**Kenmerken**:

- Geen technische kennis vereist
- Kan verschillende apparaten gebruiken (desktop, tablet, mobiel)
- Wil snel interessante projecten vinden

**Doelen**:

- Projecten van studenten bekijken
- Studentprofielen bekijken
- Zoeken naar specifieke projecten of vaardigheden
- Contact opnemen met studenten (via beschikbare contactgegevens)

## 5.2 Student

**Beschrijving**: Een student is een ingeschreven student van een ICT opleiding die projecten wil presenteren.

**Kenmerken**:

- Heeft basiskennis van computers en internet
- Wil zijn/haar werk professioneel presenteren
- Werkt mogelijk samen met andere studenten aan projecten

**Doelen**:

- Eigen projecten toevoegen en beheren
- Eigen profiel aanmaken en bijwerken (na ontvangst van account van beheerder)
- Projecten delen met anderen
- Feedback ontvangen op projecten

## 5.3 Docent

**Beschrijving**: Een docent is een begeleider die projecten beoordeelt en goedkeurt.

**Kenmerken**:

- Heeft uitgebreide kennis van de opleiding en projecten
- Moet projecten kunnen beoordelen op kwaliteit
- Werkt mogelijk met meerdere studenten

**Doelen**:

- Projecten beoordelen en goedkeuren
- Overzicht krijgen van alle projecten
- Studenten begeleiden bij het presenteren van projecten
- De beste projecten selecteren en toevoegen aan de dashboard showcase

## 5.4 Beheerder

**Beschrijving**: Een beheerder heeft volledige toegang tot het systeem voor beheer en onderhoud.

**Kenmerken**:

- Heeft technische kennis van het systeem
- Is verantwoordelijk voor de algemene werking van de website
- Moet content kunnen modereren

**Doelen**:

- Nieuwe gebruikersaccounts aanmaken voor studenten, docenten en andere beheerders
- Alle content beheren
- Gebruikers beheren
- Systeemconfiguratie aanpassen
- Problemen oplossen

# 6. Functionele Eisen

## 6.1 Authenticatie en Autorisatie

### FE1: Gebruikersaccount aanmaken

- **FE1.1**: Het systeem moet alleen beheerders in staat stellen nieuwe gebruikersaccounts aan te maken
- **FE1.2**: Bij het aanmaken van een account moet minimaal worden gevraagd: voornaam, achternaam, e-mailadres, wachtwoord, gebruikersrol
- **FE1.3**: Het systeem moet e-mailadres validatie uitvoeren (uniek en geldig formaat)
- **FE1.4**: Het systeem moet wachtwoordsterkte controleren (minimaal 8 karakters, combinatie van letters en cijfers)
- **FE1.5**: Het systeem moet een welkomstmail met inloggegevens sturen naar de nieuwe gebruiker

### FE2: Inloggen

- **FE2.1**: Het systeem moet gebruikers in staat stellen in te loggen met e-mailadres en wachtwoord
- **FE2.2**: Het systeem moet ongeldige inlogpogingen detecteren en een foutmelding tonen
- **FE2.3**: Het systeem moet een "Wachtwoord vergeten" functionaliteit bieden

### FE3: Uitloggen

- **FE3.1**: Het systeem moet gebruikers in staat stellen uit te loggen
- **FE3.2**: Na uitloggen moet de gebruiker worden doorgestuurd naar de homepage

### FE4: Autorisatie

- **FE4.1**: Het systeem moet verschillende gebruikersrollen ondersteunen (Bezoeker, Student, Docent, Beheerder)
- **FE4.2**: Het systeem moet toegang tot functionaliteit beperken op basis van gebruikersrol
- **FE4.3**: Alleen studenten kunnen hun eigen projecten en profiel bewerken
- **FE4.4**: Alleen docenten en beheerders kunnen projecten goedkeuren
- **FE4.5**: Alleen docenten en beheerders kunnen projecten toevoegen aan en verwijderen uit de showcase
- **FE4.6**: Alleen beheerders kunnen gebruikersaccounts aanmaken, beheren en systeeminstellingen aanpassen

## 6.2 Projectbeheer

### FE5: Project aanmaken

- **FE5.1**: Het systeem moet studenten in staat stellen een nieuw project aan te maken
- **FE5.2**: Bij het aanmaken moet minimaal worden gevraagd: projecttitel, beschrijving, categorie, technologieën
- **FE5.3**: Het systeem moet studenten in staat stellen afbeeldingen toe te voegen (minimaal 1, maximaal 10)
- **FE5.4**: Het systeem moet studenten in staat stellen een projectlink toe te voegen
- **FE5.5**: Het systeem moet studenten in staat stellen GitHub repository links toe te voegen (optioneel)
- **FE5.6**: Het systeem moet studenten in staat stellen meerdere studenten aan een project te koppelen
- **FE5.7**: Het systeem moet projecten opslaan als "concept" totdat ze worden gepubliceerd

### FE6: Project bewerken

- **FE6.1**: Het systeem moet studenten in staat stellen hun eigen projecten te bewerken
- **FE6.2**: Het systeem moet alle projectvelden bewerkbaar maken
- **FE6.3**: Het systeem moet een bewerkingsgeschiedenis bijhouden (optioneel)

### FE7: Project verwijderen

- **FE7.1**: Het systeem moet studenten in staat stellen hun eigen projecten te verwijderen
- **FE7.2**: Het systeem moet bevestiging vragen voordat een project wordt verwijderd
- **FE7.3**: Het systeem moet beheerders in staat stellen alle projecten te verwijderen

### FE8: Project publiceren

- **FE8.1**: Het systeem moet studenten in staat stellen projecten te publiceren
- **FE8.2**: Gepubliceerde projecten moeten zichtbaar zijn voor alle bezoekers
- **FE8.3**: Het systeem moet docenten in staat stellen projecten goed te keuren voordat ze publiek zichtbaar zijn (optioneel, afhankelijk van configuratie)
- **FE8.4**: Het systeem moet studenten in staat stellen projecten te publiceren op social media(LinkedIn, Twitter).

## 6.3 Profielbeheer

### FE9: Profiel aanmaken

- **FE9.1**: Het systeem moet studenten in staat stellen een profiel aan te maken na het ontvangen van een account
- **FE9.2**: Het profiel moet bevatten: voornaam, achternaam, profielfoto, bio, vaardigheden, contactgegevens
- **FE9.3**: Het systeem moet studenten in staat stellen links naar sociale media toe te voegen (LinkedIn, GitHub, IT Student in Actie)

### FE10: Profiel bewerken

- **FE10.1**: Het systeem moet studenten in staat stellen hun profiel te bewerken
- **FE10.2**: Alle profielvelden moeten bewerkbaar zijn
- **FE10.3**: Wijzigingen moeten direct zichtbaar zijn op het publieke profiel

### FE11: Profiel weergave

- **FE11.1**: Het systeem moet een publieke profielpagina tonen voor elke student
- **FE11.2**: Het profiel moet alle projecten van de student tonen
- **FE11.3**: Het profiel moet vaardigheden en contactgegevens tonen

## 6.4 Contentweergave

### FE12: Projectoverzicht

- **FE12.1**: Het systeem moet een overzichtspagina tonen met alle gepubliceerde projecten
- **FE12.2**: Projecten moeten worden weergegeven als kaarten met afbeelding, titel, korte beschrijving
- **FE12.3**: Het systeem moet paginering ondersteunen (bijvoorbeeld 12 projecten per pagina)
- **FE12.4**: Het systeem moet projecten sorteren op datum (nieuwste eerst) of populariteit

### FE13: Projectdetailpagina

- **FE13.1**: Het systeem moet een detailpagina tonen voor elk project
- **FE13.2**: De detailpagina moet tonen: volledige beschrijving, afbeeldingen, technologieën, betrokken studenten, links
- **FE13.3**: Het systeem moet een link naar het studentprofiel tonen voor elke betrokken student

### FE14: Studentoverzicht

- **FE14.1**: Het systeem moet een overzichtspagina tonen met alle studenten
- **FE14.2**: Studenten moeten worden weergegeven als kaarten met profielfoto, naam, korte bio
- **FE14.3**: Het systeem moet paginering ondersteunen

### FE14A: Dashboard Showcase

- **FE14A.1**: Het systeem moet een dashboard tonen met een showcase van de beste projecten binnen de opleiding
- **FE14A.2**: De showcase moet een beperkt aantal projecten tonen (bijvoorbeeld maximaal 12 projecten)
- **FE14A.3**: Projecten in de showcase moeten prominent worden weergegeven op het dashboard/homepage
- **FE14A.4**: Het systeem moet docenten in staat stellen projecten toe te voegen aan de showcase
- **FE14A.5**: Het systeem moet docenten in staat stellen projecten te verwijderen uit de showcase
- **FE14A.6**: Het systeem moet docenten in staat stellen de volgorde van projecten in de showcase aan te passen
- **FE14A.7**: Alleen gepubliceerde projecten kunnen aan de showcase worden toegevoegd
- **FE14A.8**: De showcase moet zichtbaar zijn voor alle bezoekers (inclusief niet-ingelogde gebruikers)

## 6.5 Zoeken en Filteren

### FE15: Zoekfunctionaliteit

- **FE15.1**: Het systeem moet een zoekbalk bieden op de homepage en projectoverzicht
- **FE15.2**: Zoeken moet werken op projecttitel, beschrijving en technologieën
- **FE15.3**: Zoeken moet werken op studentnaam en vaardigheden
- **FE15.4**: Zoekresultaten moeten worden weergegeven met relevante informatie

### FE16: Filterfunctionaliteit

- **FE16.1**: Het systeem moet filteren op projectcategorie mogelijk maken
- **FE16.2**: Het systeem moet filteren op technologieën mogelijk maken
- **FE16.3**: Het systeem moet filteren op opleidingsjaar mogelijk maken (indien beschikbaar)
- **FE16.4**: Het systeem moet meerdere filters tegelijk kunnen toepassen
- **FE16.5**: Het systeem moet filters kunnen resetten

## 6.6 Beheerfunctionaliteit

### FE17: Contentmoderatie

- **FE17.1**: Het systeem moet beheerders in staat stellen projecten te bekijken en te modereren
- **FE17.2**: Het systeem moet beheerders in staat stellen projecten te verwijderen of te verbergen
- **FE17.3**: Het systeem moet beheerders in staat stellen projecten te bewerken

### FE18: Gebruikersbeheer

- **FE18.1**: Het systeem moet beheerders in staat stellen nieuwe gebruikersaccounts aan te maken (zie FE1)
- **FE18.2**: Het systeem moet beheerders in staat stellen alle gebruikers te bekijken
- **FE18.3**: Het systeem moet beheerders in staat stellen gebruikersrollen aan te passen
- **FE18.4**: Het systeem moet beheerders in staat stellen gebruikers te deactiveren of verwijderen
- **FE18.5**: Het systeem moet beheerders in staat stellen wachtwoorden te resetten voor gebruikers

### FE19: Systeemconfiguratie

- **FE19.1**: Het systeem moet beheerders in staat stellen algemene instellingen aan te passen
- **FE19.2**: Het systeem moet beheerders in staat stellen categorieën en technologieën te beheren

## 6.7 Gebruikersinterface

### FE20: Responsive Design

- **FE20.1**: Het systeem moet goed werken op desktop computers (1920x1080 en hoger)
- **FE20.2**: Het systeem moet goed werken op tablets (768px - 1024px breedte)
- **FE20.3**: Het systeem moet goed werken op mobiele apparaten (320px - 767px breedte)
- **FE20.4**: Alle functionaliteit moet beschikbaar zijn op alle apparaten

### FE21: Navigatie

- **FE21.1**: Het systeem moet een duidelijke navigatiemenu bieden
- **FE21.2**: Het navigatiemenu moet aanpassen op basis van gebruikersrol
- **FE21.3**: Het systeem moet breadcrumbs tonen op detailpagina's

### FE22: Toegankelijkheid

- **FE22.1**: Het systeem moet voldoen aan `WCAG 2.1` niveau AA richtlijnen
- **FE22.2**: Het systeem moet navigeerbaar zijn met alleen het toetsenbord
- **FE22.3**: Het systeem moet alternatieve tekst bieden voor afbeeldingen

### FE23: Themakeuze
- **FE23.1**: Het systeem moet gebruikers in staat stellen tussen een licht en donker thema te kiezen

# 7. Niet-Functionele Eisen

## 7.1 Prestaties

### NFE1: Laadtijden

- **NFE1.1**: De homepage moet binnen 2 seconden laden op een gemiddelde internetverbinding
- **NFE1.2**: Projectoverzichtspagina's moeten binnen 3 seconden laden
- **NFE1.3**: Afbeeldingen moeten geoptimaliseerd zijn en niet groter dan 2MB per afbeelding
- **NFE1.4**: Het systeem moet lazy loading ondersteunen voor afbeeldingen

### NFE2: Schaalbaarheid

- **NFE2.1**: Het systeem moet minimaal 1000 gelijktijdige gebruikers kunnen ondersteunen
- **NFE2.2**: Het systeem moet minimaal 10.000 projecten kunnen beheren
- **NFE2.3**: Het systeem moet minimaal 5.000 studentprofielen kunnen beheren

## 7.2 Betrouwbaarheid

### NFE3: Beschikbaarheid

- **NFE3.1**: Het systeem moet 99% uptime hebben (maximaal 7,2 uur downtime per maand)
- **NFE3.2**: Het systeem moet automatische backups uitvoeren (dagelijks)
- **NFE3.3**: Het systeem moet een recovery plan hebben voor dataverlies

### NFE4: Foutafhandeling

- **NFE4.1**: Het systeem moet gebruiksvriendelijke foutmeldingen tonen
- **NFE4.2**: Het systeem moet technische fouten loggen voor ontwikkelaars
- **NFE4.3**: Het systeem moet niet crashen bij ongeldige gebruikersinvoer

## 7.3 Veiligheid

### NFE5: Dataveiligheid

- **NFE5.1**: Het systeem moet wachtwoorden hashen met een veilige hashfunctie (`bcrypt` of vergelijkbaar)
- **NFE5.2**: Het systeem moet `HTTPS` gebruiken voor alle communicatie
- **NFE5.3**: Het systeem moet bescherming bieden tegen `SQL injection` aanvallen
- **NFE5.4**: Het systeem moet bescherming bieden tegen `XSS` (Cross-Site Scripting) aanvallen
- **NFE5.5**: Het systeem moet `CSRF` (Cross-Site Request Forgery) bescherming bieden

### NFE6: Privacy

- **NFE6.1**: Het systeem moet voldoen aan `GDPR`/`AVG` wetgeving
- **NFE6.2**: Het systeem moet een privacybeleid en cookiebeleid hebben
- **NFE6.3**: Het systeem moet gebruikers in staat stellen hun data te exporteren
- **NFE6.4**: Het systeem moet gebruikers in staat stellen hun account te verwijderen

## 7.4 Gebruiksvriendelijkheid

### NFE7: Interface Design

- **NFE7.1**: Het systeem moet een moderne en professionele uitstraling hebben
- **NFE7.2**: Het systeem moet intuïtief te gebruiken zijn zonder training
- **NFE7.3**: Het systeem moet consistente navigatie en layout hebben
- **NFE7.4**: Het systeem moet duidelijke call-to-action buttons hebben

### NFE8: Internationalisatie

- **NFE8.1**: Het systeem moet primair Nederlands ondersteunen
- **NFE8.2**: Het systeem moet voorbereid zijn op uitbreiding naar Engels (optioneel)

## 7.5 Compatibiliteit

### NFE9: Browserondersteuning

- **NFE9.1**: Het systeem moet werken in Chrome (laatste 2 versies)
- **NFE9.2**: Het systeem moet werken in Firefox (laatste 2 versies)
- **NFE9.3**: Het systeem moet werken in Safari (laatste 2 versies)
- **NFE9.4**: Het systeem moet werken in Edge (laatste 2 versies)

### NFE10: Apparaatondersteuning

- **NFE10.1**: Het systeem moet werken op Windows computers
- **NFE10.2**: Het systeem moet werken op macOS computers
- **NFE10.3**: Het systeem moet werken op iOS apparaten (iPhone, iPad)
- **NFE10.4**: Het systeem moet werken op Android apparaten

## 7.6 Onderhoudbaarheid

### NFE11: Codekwaliteit

- **NFE11.1**: De code moet gestructureerd en gedocumenteerd zijn
- **NFE11.2**: De code moet modulair zijn en herbruikbare componenten bevatten
- **NFE11.3**: De code moet unit tests bevatten (minimaal 70% code coverage)

### NFE12: Documentatie

- **NFE12.1**: Het systeem moet technische documentatie hebben voor ontwikkelaars
- **NFE12.2**: Het systeem moet gebruikersdocumentatie hebben voor eindgebruikers
- **NFE12.3**: Het systeem moet `API` documentatie hebben (indien van toepassing)

# 8. Systeemarchitectuur

## 8.1 Algemene Architectuur

Het systeem bestaat uit de volgende componenten:

- **Frontend**: `React`-gebaseerde webapplicatie gebouwd met `Vite`
- **Backend**: `REST API` server gebouwd met `PHP` en `SLIM` framework
- **Authenticatie API**: Aparte `API` voor authenticatie en gebruikersbeheer (auth-api), gebouwd met `PHP` en `Slim Framework`
- **Database**: `MySQL` relationele database
- **File Storage**: Opslag voor afbeeldingen en bestanden (bijvoorbeeld `AWS S3` of lokale opslag)

## 8.2 Technologie Stack

### Frontend

- `React` (laatste versie)
- `Vite` als build tool en development server
- `TypeScript` (optioneel, aanbevolen)
- `CSS` framework (bijvoorbeeld `Tailwind CSS` of vergelijkbaar)
- `React Router` voor client-side navigatie

### Backend

- `PHP` (laatste stabiele versie)
- `SLIM Framework` voor `REST API` ontwikkeling
- `API`'s georganiseerd per functionaliteit (modulaire structuur)
- `JWT` (JSON Web Tokens) voor authenticatie
- `PDO` of `Eloquent ORM` voor database interactie

### Authenticatie API (aparte API)

- Aparte `API` service voor authenticatie en gebruikersbeheer
- `PHP` (laatste stabiele versie)
- `Slim Framework 4`
- `JWT` (JSON Web Tokens) voor access tokens en refresh tokens
- `RESTful API` endpoints voor login, gebruikersbeheer en rollenbeheer

### Database

- `MySQL` (laatste stabiele versie)
- Database migraties voor schema beheer

### API Structuur

`RESTful API` endpoints per functionaliteit:

- Authenticatie API (aparte API service voor login, gebruikersbeheer en rollenbeheer)
- Project API
- Profiel API
- Content API
- Zoek- en filter API

### Infrastructuur

- `Docker` voor containerisatie (optioneel)
- `CI/CD` pipeline voor automatische deployment

## 8.3 Data Model (Conceptueel)

**Entiteiten**:

- **User**: Gebruikersgegevens, authenticatie, rol
- **Project**: Projectgegevens, status, metadata
- **ProjectImage**: Afbeeldingen gekoppeld aan projecten
- **StudentProfile**: Uitgebreide profielgegevens van studenten
- **Category**: Projectcategorieën
- **Technology**: Technologieën/tools gebruikt in projecten
- **ProjectTechnology**: Koppeltabel tussen projecten en technologieën
- **ProjectStudent**: Koppeltabel tussen projecten en studenten

# 9. Aannames en Beperkingen

## 9.1 Aannames

- Studenten hebben toegang tot internet en een moderne webbrowser
- Studenten hebben basiskennis van het uploaden van bestanden en het invullen van formulieren
- De website wordt gehost op een betrouwbare server met voldoende resources
- Er is een beheerder beschikbaar voor contentmoderatie
- Studenten zijn gemotiveerd om hun projecten te presenteren

## 9.2 Beperkingen

- Het systeem ondersteunt geen real-time samenwerking tussen gebruikers
- Video-uploads zijn beperkt tot externe links (YouTube, Vimeo)
- Het systeem heeft geen geavanceerde versiebeheer functionaliteit voor projecten
- Externe integraties (zoals GitHub API) zijn optioneel en niet verplicht
- Het systeem heeft geen ingebouwde communicatiefunctionaliteit tussen gebruikers

## 9.3 Externe Afhankelijkheden

- **Authenticatie API**: Het systeem is afhankelijk van een aparte Authenticatie API service voor authenticatie en gebruikersbeheer
- **E-mailservice** voor het versturen van bevestigingsmails en wachtwoord reset emails
- **Hosting provider** voor het hosten van de website en de Authenticatie API
- **CDN** (Content Delivery Network) voor het snel serveren van afbeeldingen (optioneel)

# 10. Glossarium

- **Portfolio**: Een verzameling van projecten en werkstukken die een persoon heeft gemaakt
- **Project**: Een specifiek werkstuk, applicatie of opdracht die door studenten is ontwikkeld
- **Studentprofiel**: Een publieke pagina met informatie over een student, inclusief vaardigheden, bio en projecten
- **Categorie**: Een classificatie voor projecten (bijvoorbeeld: Web Development, Mobile App, Data Science)
- **Technologie**: Een tool, framework of programmeertaal gebruikt in een project
- **Moderatie**: Het proces van het controleren en goedkeuren van content voordat het publiek wordt gemaakt
- **Showcase**: Een selectie van de beste projecten die prominent worden getoond op het dashboard/homepage
- **Responsive Design**: Een ontwerpmethode waarbij de website zich aanpast aan verschillende schermgroottes
- **Authenticatie**: Het proces van het verifiëren van de identiteit van een gebruiker
- **Autorisatie**: Het proces van het bepalen welke rechten een gebruiker heeft in het systeem
- **GDPR/AVG**: Algemene Verordening Gegevensbescherming, Europese privacywetgeving

# Bijlagen

## Bijlage A: Prioritering (MoSCoW)

### **Must Have (M):**

- FE1 — Gebruikersaccount aanmaken
- FE2 — Inloggen met e-mailadres en wachtwoord
- FE3 — Uitloggen
- FE4 — Autorisatie op basis van gebruikersrol
- FE5 — Project aanmaken
- FE8 — Project publiceren (excl. FE8.4)
- FE12 — Projectoverzicht
- FE13 — Projectdetailpagina
- FE20 — Responsive design
- FE21 — Navigatie

### **Should Have (S):**

- FE6 — Project bewerken
- FE7 — Project verwijderen
- FE9 — Profiel aanmaken
- FE10 — Profiel bewerken
- FE11 — Profiel weergave
- FE14 — Studentoverzicht
- FE15 — Zoekfunctionaliteit
- FE16 — Filterfunctionaliteit
- FE23.1 — Themakeuze (dark mode)
- FE8.4 — Projecten delen op social media

### **Could Have (C):**

- FE14A — Dashboard Showcase
- FE17 — Contentmoderatie
- FE18 — Gebruikersbeheer
- FE19 — Systeemconfiguratie
- FE22 — Toegankelijkheid (WCAG 2.1 AA)

### **Won't Have (W):**

- Real-time chat of messaging tussen gebruikers
- Betalingsfunctionaliteit
- Video streaming of live presentaties
- Integratie met externe leeromgevingen (Moodle, Canvas)
- Mobiele apps (alleen responsive website)

---

**Document Status**: Concept
**Volgende Stap**: Review door stakeholders en goedkeuring voor ontwikkeling
