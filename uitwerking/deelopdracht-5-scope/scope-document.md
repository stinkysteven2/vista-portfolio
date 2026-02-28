# Scope document — Testen IT Talenten Portaal

> Opgesteld op: 28 februari 2026
> Applicatie: [IT Talenten Portaal](https://it-talenten-portaal-test-it-talenten-webapp-test.iapmkw.easypanel.host/talent)
> Gebaseerd op: SRS document (deelopdracht 2), bevindingen uit deelopdracht 1

---

## 1. Gebruikersrollen

Het IT Talenten Portaal kent drie gebruikersrollen:

| Rol | Omschrijving |
|-----|-------------|
| **Bezoeker** | Niet-ingelogde gebruiker die talenten en vacatures bekijkt |
| **Talent** | Ingelogde gebruiker die zijn eigen profiel beheert en deelt |
| **Beheerder** | Beheert gebruikers, content en systeeminstellingen |

---

## 2. Wat wordt WEL getest

| # | Functionaliteit | Gebruikersrol | Reden |
|---|----------------|---------------|-------|
| 1 | Inloggen (FE2) | Talent, Beheerder | Kernfunctionaliteit. Als inloggen niet werkt, hebben talenten en beheerders geen toegang tot het systeem. Hoog risico. |
| 2 | Uitloggen (FE3) | Talent, Beheerder | Veiligheidscriterium: sessie moet correct worden afgesloten. |
| 3 | Autorisatie per rol (FE4) | Alle rollen | Als rollen niet correct worden afgedwongen, kunnen bezoekers bij beheerdersfuncties. Hoog beveiligingsrisico. |
| 4 | Talentenoverzicht bekijken (FE12) | Bezoeker | Primaire functie van de applicatie — de meest bezochte pagina. |
| 5 | Talentprofiel bekijken (FE13) | Bezoeker | Bezoekers willen individuele talenten bekijken. Hoge gebruiksfrequentie. |
| 6 | Talentprofiel beheren (FE9, FE10) | Talent | Talenten moeten hun eigen profiel kunnen aanmaken en bijwerken. |
| 7 | Vacatures bekijken en filteren (FE15, FE16) | Bezoeker | Vacaturepagina is een kernpagina. De provincie-filter toont al bekende problemen (zie deelopdracht 1, bug #2). |
| 8 | Social media delen (FE8.4) | Talent | Nieuwe feature. Bevat privacyrisico's rondom welke data gedeeld wordt. |
| 9 | Dark mode (FE23.1) | Bezoeker, Talent | Nieuwe feature. Toegankelijkheids- en compatibiliteitseisen zijn meetbaar (WCAG contrast). |
| 10 | Responsive design (FE20) | Bezoeker, Talent | De applicatie moet werken op desktop, tablet en mobiel. Al gedeeltelijk getest in opdracht 1. |
| 11 | Navigatie en links (FE21) | Bezoeker | In opdracht 1 is een kapotte navigatielink gevonden (/linknaarittalenten). Navigatie moet volledig getest worden. |
| 12 | Privacypagina (NFE6) | Bezoeker | In opdracht 1 bevatte de privacypagina placeholder-tekst (lorem ipsum). Wettelijk verplichte content moet correct zijn. |

---

## 3. Wat wordt NIET getest

| Functionaliteit | Reden |
|----------------|-------|
| Real-time chat of messaging | Valt expliciet buiten de scope van het SRS (sectie 2.2). |
| Betalingsfunctionaliteit | Niet aanwezig in de applicatie en buiten scope (SRS 2.2). |
| Video streaming | Buiten scope (SRS 2.2). Externe videolinks vallen onder navigatietest. |
| Integratie met leeromgevingen (Moodle, Canvas) | Buiten scope (SRS 2.2). |
| Mobiele apps | Er is alleen een responsive website, geen native app. |
| E-mailbezorging wachtwoord-reset | Vereist toegang tot een externe mailserver. Niet testbaar zonder infrastructuurrechten; wordt aangenomen dat de mailservice correct werkt. |
| Geavanceerde prestatietests (load testing) | Vereist testinfrastructuur en valt buiten de middelen van dit testtraject. Basisresponstijden worden wel gecontroleerd. |
| Beheerderspaneel (FE17–FE19) | Geen beheerdersaccount beschikbaar voor de testomgeving. Wordt gedocumenteerd als buiten scope voor dit testtraject. |

---

## 4. Risico-analyse

| Risico | Ernst | Kans | Toelichting |
|--------|-------|------|-------------|
| Inloggen werkt niet | Hoog | Laag | Alle functionaliteit voor ingelogde gebruikers valt weg. Gevonden: 401-fouten op /home (opdracht 1, bug #4). |
| Autorisatie niet correct afgedwongen | Hoog | Laag | Bezoekers kunnen bij privé-profieldata. Direct beveiligingsrisico. |
| Social media sharing stuurt privédata door | Hoog | Gemiddeld | Als de implementatie niet goed gefilterd is, kan persoonlijke data lekken naar externe platforms. |
| Provincie-filter onleesbaar | Gemiddeld | Hoog | Al bevestigd in opdracht 1 (bug #2). Treft alle bezoekers die op vacatures zoeken. |
| Kapotte navigatielink (/linknaarittalenten) | Gemiddeld | Hoog | Al bevestigd in opdracht 1 (bug #4). Treft alle bezoekers op alle pagina's. |
| Lorem ipsum op privacypagina | Gemiddeld | Hoog | Al bevestigd in opdracht 1 (bug #3). Een lege privacyverklaring is een AVG/GDPR-risico. |
| Dark mode voldoet niet aan WCAG-contrast | Gemiddeld | Gemiddeld | Donkere thema's mislukken vaak op contrastvereisten. Meetbaar en testbaar. |
| Afbeeldingen zonder src-attribuut | Laag | Hoog | Al bevestigd in opdracht 1 (bug #5). Visuele fout op alle pagina's, maar geen functioneel risico. |

---

## 5. Motivatie van de keuzes

De scope is bepaald op basis van drie criteria:

1. **Gebruiksfrequentie** — Functies die door alle bezoekers gebruikt worden (talentenoverzicht, navigatie, vacatures) krijgen prioriteit, ongeacht rol.
2. **Risico** — Functies met een beveiligings- of AVG-risico (authenticatie, autorisatie, social media delen, privacypagina) worden altijd getest, ook als de kans op een fout klein is.
3. **Bekende bevindingen** — Bugs die al in opdracht 1 zijn gevonden worden expliciet opgenomen in de scope, zodat ze in het testplan en testrapport terugkomen.

Functies die buiten scope vallen zijn ofwel expliciet uitgesloten in het SRS, niet beschikbaar in de testomgeving, of vereisen infrastructuur die buiten dit testtraject valt.
