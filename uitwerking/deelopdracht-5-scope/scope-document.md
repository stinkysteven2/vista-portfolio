# Scope document — Testen IT Talenten Portaal

> Opgesteld op: 28 februari 2026
> Applicatie: [IT Talenten Portaal](https://it-talenten-portaal-test-it-talenten-webapp-test.iapmkw.easypanel.host/talent)
> Gebaseerd op: SRS document (deelopdracht 2), bevindingen deelopdracht 1

---

## 1. Wat wordt WEL getest

| Functionaliteit | Reden |
|---|---|
| **Inloggen** | Kernfunctionaliteit. Gebruikers maken objecten aan die gekoppeld zijn aan hun organisatie of persoon. Ongeauthenticeerde gebruikers mogen geen toegang krijgen tot zulke gegevens. |
| **Uitloggen** | Veiligheid. Een sessie moet correct kunnen worden afgesloten — wat als iemand achter een publieke computer zit? |
| **Aanmaken talentenprofiel** | Kernfunctionaliteit van de applicatie. Het doel van de app is talenten doorzoekbaar te maken; zonder profiel werkt niets. |
| **Talenten filteren en zoeken** | Kernfunctionaliteit. Zonder werkende zoekfunctie is de applicatie nutteloos voor organisaties die op zoek zijn naar talent. |
| **Aanmaken organisatie** | Organisaties hebben een account nodig om toegang te krijgen tot de talenten-zoek-interface en om vacatures aan te kunnen maken. |
| **Aanmaken vacature** | Toekomstgericht. In de business zien we de omgekeerde vraag vaker langskomen — organisaties die talent zoeken. Dit heeft nu geen prioriteit, maar het is handig om hier alvast een voet tussen de deur te hebben voor gesprekken met toekomstige partners en stakeholders. |
| **Afschermen van NaW-gegevens** | Wettelijke verplichting (AVG/GDPR). Persoonsgegevens mogen niet zomaar publiek beschikbaar worden gesteld en mogen alleen worden gedeeld met vertrouwde partijen. |

---

## 2. Wat wordt NIET getest

| Functionaliteit | Reden |
|---|---|
| **Filteren van vacatures** | Ontwikkeling hiervan heeft geen prioriteit. In de business zien we vaker de omgekeerde vraag — vacatures die talent aantrekken — dan actief zoekend talent. |
| **Koppeling met externe sociale media** | Op dit moment te risicovol. Onduidelijk wat externe platforms doen met persoonsgegevens van talenten. Dit vereist nader onderzoek voordat het getest kan worden. |
| **White-label thema's voor detacheringspartijen** | Er worden (nog) geen thema's ontwikkeld voor partijen die de applicatie als white-label oplossing willen gebruiken. |
| **Automatische koppeling met UWV-systemen** | Buiten de huidige scope. Integratie met externe overheidssystemen vereist aparte afspraken en infrastructuur. |
| **Geolocatie-afstandsfilters** | Er worden geen geolocatiefilters ontwikkeld binnen het zoekprofiel van gebruikers. |

---

## 3. Risico's

### 3.1 Datalekken

Datalekken vormen het grootste risico voor deze applicatie. De app bevat persoonsgegevens van talenten (NaW-gegevens, werkervaring, opleidingsachtergrond). Een lek heeft directe juridische consequenties onder de AVG. We onderscheiden de volgende typen:

| Type | Omschrijving |
|---|---|
| **XSS (Cross-Site Scripting)** | Een kwaadwillende plaatst uitvoerbare code in een talentenprofiel of vacature. Die code voert uit in de browser van andere gebruikers. Gevaarlijk omdat profielen publiek zichtbaar zijn. |
| **Authentication bypass** | Inloggen omzeilen zonder geldige inloggegevens, bijvoorbeeld via SQL injection in het loginformulier. Geeft directe toegang tot persoonsgegevens. |
| **Brute force / account takeover** | Wachtwoorden raden via herhaalde inlogpogingen. Relevant omdat accounts NaW-gegevens bevatten die bij een overname direct blootgesteld worden. |
| **IDOR (Insecure Direct Object Reference)** | Profieldata van een ander talent opvragen door een getal in de URL te veranderen (bijv. `/talent/123` → `/talent/124`). Een veelvoorkomende fout in dit type applicaties. |
| **Phishing** | Nep-loginpagina's die eruitzien als het Talenten Portaal. Het risico wordt vergroot door de gebroken navigatielink die in deelopdracht 1 is gevonden — gebruikers zijn al gewend aan onverwachte redirects. |
| **Session hijacking** | Een actieve sessie stelen van een ingelogde talent, bijvoorbeeld via een onbeveiligde verbinding. |

### 3.2 Outages

Als de applicatie niet beschikbaar is, kunnen talenten geen profiel aanmaken of beheren en kunnen organisaties geen talenten zoeken. Dit schaadt de betrouwbaarheid van het platform en het vertrouwen van zowel talenten als partnerorganisaties.

### 3.3 Data-integriteit

Als het aanmaken van een talentenprofiel of vacature niet correct opslaat — bijvoorbeeld door een formulierfout of API-probleem — werken alle afhankelijke functies ook niet. Een talent dat denkt ingeschreven te zijn maar dat niet is, is een concreet en moeilijk te traceren probleem.

### 3.4 Reputatieschade

Als de zoekfunctie niet werkt of profielen niet zichtbaar zijn, verlaten organisaties de applicatie en zoeken zij elders. Het vertrouwen van de doelgroep is moeilijk terug te winnen.

---

## 4. Testmiddelen

### 4.1 Doelgroep en browserkeuze

De applicatie richt zich primair op **Nederlandse professionele gebruikers**: IT-talenten en HR-medewerkers of recruiters bij Nederlandse organisaties. Deze doelgroep werkt overwegend op Windows in een zakelijke omgeving, wat de browserkeuze direct beïnvloedt.

De browserkeuze is gebaseerd op marktaandeel-data van StatCounter voor **Nederland** (januari 2026):

| Browser | Marktaandeel NL |
|---------|----------------|
| Chrome | 62,43% |
| Safari | 18,12% |
| Edge | 6,70% |
| Firefox | 3,73% |

Voor een Nederlandse professionele doelgroep is **Edge** relevanter dan Firefox: Nederlandse bedrijven draaien grotendeels op Windows en Microsoft 365, waarbij Edge de standaardbrowser is die vaak via groepsbeleid wordt uitgerold. Firefox wordt in zakelijke omgevingen nauwelijks actief ingezet.

### 4.2 Testmethoden

**Geautomatiseerd** — via Playwright (Python) op Chrome en Firefox. Geautomatiseerde testen dekken de volledige scope en worden herhaald bij elke wijziging. Dit is de primaire testmethode voor functionele eisen.

**Handmatig** — de kernfunctionaliteit (inloggen, uitloggen, aanmaken talentenprofiel, zoeken) wordt aanvullend handmatig getest op de meest gebruikte browsers binnen de doelgroep:

| Browser / Platform | Marktaandeel NL | Methode |
|---|---|---|
| Chrome — desktop | 62,43% | Handmatig + geautomatiseerd |
| Edge — desktop | 6,70% | Handmatig |
| Chrome — mobiel | — | Handmatig + geautomatiseerd |
| Safari — mobiel | 18,12% | Handmatig |
| Firefox — desktop | 3,73% | Alleen geautomatiseerd |

Handmatig testen is met name relevant voor gebruiksvriendelijkheid en visuele correctheid, die moeilijk automatisch te beoordelen zijn.

---

## 5. Motivatie van de keuzes

De scope is bepaald op basis van drie criteria:

1. **Kernfunctionaliteit** — functies zonder welke de applicatie haar doel niet kan vervullen (talenten doorzoekbaar maken, organisaties laten zoeken) krijgen altijd prioriteit.
2. **Wet- en regelgeving** — functies met een AVG/GDPR-dimensie worden getest ongeacht prioriteit, omdat non-compliance directe juridische consequenties heeft.
3. **Businessperspectief** — sommige functies (zoals vacatures) worden getest vanwege toekomstige waarde voor partners en stakeholders, ook als de urgentie nu laag is. Functies die buiten de huidige ontwikkelstrategie vallen worden bewust uitgesloten.
