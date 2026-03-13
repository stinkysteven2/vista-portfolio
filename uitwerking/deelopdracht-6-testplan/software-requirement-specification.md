# Software Requirement Specification — IT Talenten Portaal

> Versie: 1.0 — opgesteld op basis van verkennende crawl (maart 2026)
> Applicatie: [IT Talenten Portaal](https://talenten-portaal-tp-test-webapp.iapmkw.easypanel.host)
> Gebaseerd op: deelopdracht 2 SRS (IT Showcase), aangepast voor het Talenten Portaal

---

## 1. Inleiding

### 1.1 Doel van het document

Dit SRS beschrijft de functionele en niet-functionele eisen voor het **IT Talenten Portaal**. Het document dient als basis voor het testplan en de bijbehorende testcases.

### 1.2 Doel van het project

Het IT Talenten Portaal is een webapplicatie waarop:

- IT-talenten een profiel aanmaken en beheren
- Organisaties/recruiters talenten kunnen zoeken en filteren
- Vacatures kunnen worden geplaatst en bekeken
- Beheerders het systeem en de gebruikers kunnen administreren

### 1.3 Doelgroep van dit document

- Testers die het systeem gaan testen
- Ontwikkelaars die het systeem onderhouden

---

## 2. Scope

### 2.1 Wat valt binnen de scope

- Publieke talentenpagina met zoek- en filterfunctionaliteit
- Talentprofiel (detailpagina)
- Vacatureoverzicht en vacaturedetail
- Inloggen en uitloggen (via Keycloak)
- Favorieten beheren (ingelogde gebruikers)
- Talentregistratie (aanvraagflow)
- Admin panel: gebruikersbeheer, talentenbeheer, organisatiebeheer, vacaturesbeheer

### 2.2 Wat valt buiten de scope

- White-label thema's voor organisaties
- Koppeling met externe systemen (UWV, sociale media)
- Geolocatiefilters
- Registratie van organisaties (extern proces)

---

## 3. Gebruikersklassen

| Rol | Omschrijving |
|---|---|
| **Bezoeker** | Niet-ingelogde gebruiker; kan talenten en vacatures bekijken |
| **Ingelogde gebruiker** | Heeft toegang tot talentprofielen en favorieten |
| **Talent** | Heeft een eigen profiel dat door de admin is aangemaakt of goedgekeurd |
| **Beheerder (admin)** | Volledige toegang tot het admin panel |

---

## 4. Functionele Eisen

### 4.1 Authenticatie en autorisatie

**FE1 — Inloggen**
- FE1.1: Het systeem moet gebruikers in staat stellen in te loggen via Keycloak (e-mail + wachtwoord)
- FE1.2: Na succesvol inloggen wordt de gebruiker doorgestuurd naar de startpagina
- FE1.3: Bij onjuiste inloggegevens toont het systeem een foutmelding

**FE2 — Uitloggen**
- FE2.1: Het systeem moet ingelogde gebruikers in staat stellen uit te loggen
- FE2.2: Na uitloggen wordt de sessie beëindigd en is beschermde content niet meer toegankelijk

**FE3 — Autorisatie**
- FE3.1: Talentprofielen zijn alleen volledig zichtbaar voor ingelogde gebruikers
- FE3.2: Het admin panel is alleen toegankelijk voor beheerders
- FE3.3: Niet-ingelogde gebruikers worden omgeleid bij toegang tot beveiligde pagina's

### 4.2 Talenten zoeken en filteren

**FE4 — Zoeken**
- FE4.1: De talentenpagina toont een overzicht van beschikbare talenten met zoekresultaatteller
- FE4.2: Talenten zijn doorzoekbaar en filterbaar op: provincie, werkniveau, beschikbaarheid (uren/week), methoden & technieken, softwarepakketten, programmeer- & scriptingtalen, frameworks & databases, talen, werklocatie, rijbewijs, reisafstand

**FE5 — Talentprofiel**
- FE5.1: Elk talent heeft een detailpagina met: naam, functietitel, locatie, werkervaring, kernkwaliteiten, vaardigheden
- FE5.2: De pagina bevat een contactknop en een terugknop naar het overzicht

### 4.3 Favorieten

**FE6 — Favorieten**
- FE6.1: Ingelogde gebruikers kunnen talenten opslaan als favoriet
- FE6.2: De favorietenpagina toont een overzicht van opgeslagen talenten
- FE6.3: Favorieten zijn leeg totdat de gebruiker er actief mee werkt

### 4.4 Vacatures

**FE7 — Vacatureoverzicht**
- FE7.1: De vacaturespagina toont een overzicht van openstaande vacatures met filter-panel
- FE7.2: Filters bevatten: provincie, werkniveau, methoden & technieken, softwarepakketten, talen, programmeerniveau, bedrijven

**FE8 — Vacaturedetail**
- FE8.1: Elke vacature heeft een detailpagina met: functietitel, salaris, locatie, publicatiedatum, uren, programmeerniveau, beschrijving
- FE8.2: De pagina bevat een sollicitatieknop en een contactknop

### 4.5 Talentregistratie

**FE9 — Registratie**
- FE9.1: Talenten kunnen zich aanmelden via een registratieformulier
- FE9.2: Na registratie ontvangt de beheerder een melding en neemt binnen 24 uur contact op

### 4.6 Admin panel

**FE10 — Gebruikersbeheer**
- FE10.1: De beheerder kan gebruikers aanmaken, wijzigen en verwijderen
- FE10.2: De beheerder kan gebruikersrechten instellen

**FE11 — Talentenbeheer**
- FE11.1: De beheerder kan talentprofielen beheren (aanmaken, bewerken, verwijderen)

**FE12 — Organisaties en bedrijven**
- FE12.1: De beheerder kan organisaties en bedrijven/instanties beheren

**FE13 — Vacaturesbeheer**
- FE13.1: De beheerder kan vacatures aanmaken, bewerken en verwijderen

**FE14 — Property labels**
- FE14.1: De beheerder kan eigenschappenlabels en subkeuzes beheren

---

## 5. Niet-Functionele Eisen

### 5.1 Veiligheid

- NFE1: Persoonsgegevens van talenten zijn alleen zichtbaar voor ingelogde gebruikers (AVG)
- NFE2: Authenticatie verloopt via Keycloak met PKCE (OAuth 2.0)
- NFE3: Het systeem moet beschermd zijn tegen IDOR (profieldata van anderen ophalen via URL-manipulatie)

### 5.2 Beschikbaarheid en prestaties

- NFE4: De applicatie moet beschikbaar zijn via HTTPS
- NFE5: Pagina's moeten laden binnen een redelijke tijd (< 5 seconden op normale verbinding)

### 5.3 Compatibiliteit

- NFE6: De applicatie werkt in Chrome (desktop en mobiel)
- NFE7: De applicatie werkt in Edge (desktop)
- NFE8: De applicatie werkt in Safari (mobiel)

### 5.4 Bruikbaarheid

- NFE9: Filterpanelen zijn leesbaar en bedienbaar op desktop
- NFE10: Navigatie werkt correct en alle links verwijzen naar bestaande pagina's

---

## 6. Bekende Issues (uit deelopdracht 1)

| # | Pagina | Bevinding |
|---|---|---|
| B1 | `/` | Carousel leeg zonder login |
| B2 | `/vacatures` | Provincie-filter onleesbaar |
| B3 | `/Privacy` | Lorem ipsum placeholder aanwezig |
| B4 | Alle pagina's | Kapotte navigatielink → `/linknaarittalenten` |
| B5 | Alle pagina's | Afbeeldingen zonder `src`-attribuut |

---

## 7. Systeemsarchitectuur (globaal)

- **Frontend**: Angular SPA
- **Backend API**: `https://talenten-portaal-tp-test-api.iapmkw.easypanel.host`
- **Authenticatie**: Keycloak — realm `talentenportaal-test`, client `angular-app-client`
- **Hosting**: Easypanel (containerized)
