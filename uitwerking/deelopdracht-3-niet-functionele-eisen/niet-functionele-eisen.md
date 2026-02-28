# Deelopdracht 3 — Niet-functionele eisen: donkere modus & social media delen

> Geteste applicatie: [IT Talenten Portaal](https://it-talenten-portaal-test-it-talenten-webapp-test.iapmkw.easypanel.host/talent)
> Gebaseerd op user stories FE23.1 (donkere modus) en FE8.4 (social media delen) uit deelopdracht 2.

---

## 1. Niet-functionele eisen — Donkere modus (FE23.1)

De IT Talenten Portaal is een Angular-applicatie met een bestaand themasysteem (standaard- en leerwerkloket-thema). Een donkere modus zou als derde thema in deze bestaande architectuur worden opgenomen.

| # | Categorie | Eis | Motivatie |
|---|-----------|-----|-----------|
| NFE13.1 | Prestaties | De themawisseling vindt plaats binnen 200 milliseconden, zonder pagina-herlaad. | Een trage switch voelt als een fout. In Angular is dit een CSS class toggle en hoort bijna onmiddellijk te zijn. |
| NFE13.2 | Gebruiksvriendelijkheid | De themakeuze wordt opgeslagen in localStorage van de browser, zodat de voorkeur bewaard blijft bij een volgend bezoek. | Zonder opslag moeten gebruikers elke keer opnieuw kiezen — dat is vervelend. |
| NFE13.3 | Toegankelijkheid | Alle tekst- en achtergrondkleurencombinaties in het donkere thema voldoen aan een minimale contrastverhouding van 4,5:1 (WCAG 2.1 AA) voor normale tekst en 3:1 voor grote tekst. | Donkere thema's mislukken vaak op contrast. Dit is meetbaar en controleerbaar. |
| NFE13.4 | Compatibiliteit | Het donkere thema werkt correct in Chrome, Firefox, Safari en Edge (laatste 2 versies) en op mobiele browsers (iOS Safari, Android Chrome). | De applicatie heeft een responsive design; het thema moet op alle ondersteunde apparaten werken. |
| NFE13.5 | Betrouwbaarheid | Als localStorage niet beschikbaar is (bijv. in incognito-modus of bij geblokkeerde opslag), valt het systeem terug op de systeemvoorkeur van het apparaat via `prefers-color-scheme`. | De feature mag niet crashen bij ontbrekende opslagrechten. Een graceful fallback zorgt voor altijd correct gedrag. |

---

## 2. Niet-functionele eisen — Social media delen (FE8.4)

Talenten kunnen hun profiel delen op LinkedIn en Twitter om zichzelf te presenteren aan potentiële werkgevers.

| # | Categorie | Eis | Motivatie |
|---|-----------|-----|-----------|
| NFE14.1 | Veiligheid | Alleen publiek zichtbare profielinformatie (naam, functietitel, openbare bio) wordt doorgegeven aan het externe platform. Inloggegevens, e-mailadressen en andere privégegevens worden nooit meegestuurd. | Gebruikers moeten erop kunnen vertrouwen dat alleen publieke data gedeeld wordt. |
| NFE14.2 | Prestaties | De share-dialoog opent binnen 1 seconde na het klikken op de deelknop. Als het externe platform meer dan 3 seconden nodig heeft om te reageren, toont het systeem een laadstatus. | Een onreagerende knop zonder feedback voelt als een kapotte interface. |
| NFE14.3 | Betrouwbaarheid | Als LinkedIn of Twitter niet bereikbaar is, verschijnt er binnen 5 seconden een begrijpelijke foutmelding. Het systeem biedt dan een alternatief: de profiellink kopiëren naar het klembord. | Externe platforms kunnen down zijn. De core-functionaliteit (profiel delen) mag daar niet volledig door geblokkeerd worden. |
| NFE14.4 | Privacy | Voordat het profiel daadwerkelijk gedeeld wordt, ziet de talent een preview van wat er gedeeld wordt (naam, URL, eventuele beschrijving), zodat er bewust gedeeld wordt. | Dit sluit aan op GDPR-principes rondom transparantie en toestemming. |
| NFE14.5 | Foutafhandeling | Als de share-actie mislukt (bijv. door een geblokkeerde pop-up of een API-fout), ontvangt de gebruiker een duidelijke melding in begrijpelijke taal, zonder technische foutcodes. | Technische foutmeldingen zijn niet bruikbaar voor eindgebruikers. |

---

## 3. Categorisatie — overzicht

| Categorie | Eisen |
|-----------|-------|
| Prestaties | NFE13.1, NFE14.2 |
| Gebruiksvriendelijkheid | NFE13.2, NFE14.4 |
| Toegankelijkheid | NFE13.3 |
| Compatibiliteit | NFE13.4 |
| Betrouwbaarheid | NFE13.5, NFE14.3 |
| Veiligheid | NFE14.1 |
| Privacy | NFE14.4, NFE14.5 |

---

## 4. Testideeën voor 3 niet-functionele eisen

### NFE13.3 — WCAG contrastverhouding in dark mode

| | |
|---|---|
| **Wat meten** | Of alle tekst- en achtergrondkleurencombinaties in dark mode voldoen aan de minimale contrastverhouding. |
| **Hoe meten** | Geautomatiseerd met de axe-core library via Playwright (dezelfde tool die al in dit project gebruikt wordt). Aanvullend handmatig checken met de WebAIM Contrast Checker voor dynamisch gegenereerde content. |
| **Acceptatiecriterium** | Alle combinaties scoren minimaal 4,5:1 voor normale tekst en 3:1 voor grote tekst. Nul axe-core violations op niveau AA. |
| **Edge case** | Profielfoto's met tekst overlay (bijv. naam over een achtergrondafbeelding) vallen buiten automatische contrast-checks en moeten handmatig beoordeeld worden. |

---

### NFE13.2 — Persistentie van themakeuze via localStorage

| | |
|---|---|
| **Wat meten** | Of de themakeuze na het sluiten en heropenen van de browser nog actief is, en of de fallback correct werkt als localStorage niet beschikbaar is. |
| **Hoe meten** | Handmatig: dark mode aanzetten → browser sluiten → heropenen → controleren of dark mode actief is. Incognito-test: dark mode aanzetten → nieuw incognitovenster openen → controleren of systeemvoorkeur (`prefers-color-scheme`) gevolgd wordt. |
| **Acceptatiecriterium** | In een normale browsersessie blijft de keuze bewaard na herstart. In incognito of bij geblokkeerde localStorage wordt de OS-voorkeur gevolgd zonder foutmelding. |
| **Edge case** | localStorage volledig gevuld of geblokkeerd via privacyinstellingen van de browser (bijv. Firefox "Strict" tracking protection). |

---

### NFE14.3 — Betrouwbaarheid bij extern platform onbereikbaar

| | |
|---|---|
| **Wat meten** | Of het systeem correct reageert als LinkedIn of Twitter niet bereikbaar is, en of het alternatief (link kopiëren) beschikbaar is. |
| **Hoe meten** | Netwerk-simulatie in Chrome DevTools: externe domeinen (linkedin.com, twitter.com) blokkeren via "Request blocking". Meten hoe lang het duurt voordat de foutmelding verschijnt en of de kopieerknop zichtbaar is. |
| **Acceptatiecriterium** | Foutmelding verschijnt binnen 5 seconden. De knop "Link kopiëren naar klembord" is zichtbaar en functioneel. De foutmelding bevat geen technische codes. |
| **Edge case** | Gedeeltelijke verbinding: platform bereikbaar maar reageert extreem traag (simuleer via "Slow 3G" throttling). Het systeem mag niet oneindig blijven laden. |
