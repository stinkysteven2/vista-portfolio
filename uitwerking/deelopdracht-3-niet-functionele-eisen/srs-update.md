# SRS Update — Niet-functionele eisen deelopdracht 3

> Dit document bevat de aanvullingen op het SRS uit deelopdracht 2. De nieuwe secties NFE13 en NFE14 worden toegevoegd aan hoofdstuk 7 (Niet-Functionele Eisen).

---

## 7.7 Donkere modus (FE23.1)

### NFE13: Dark mode specificaties

- **NFE13.1**: De themawisseling vindt plaats binnen 200 milliseconden, zonder pagina-herlaad.
- **NFE13.2**: De themakeuze wordt opgeslagen in `localStorage` van de browser, zodat de voorkeur bewaard blijft bij een volgend bezoek.
- **NFE13.3**: Alle tekst- en achtergrondkleurencombinaties in het donkere thema voldoen aan een minimale contrastverhouding van 4,5:1 (WCAG 2.1 AA) voor normale tekst en 3:1 voor grote tekst.
- **NFE13.4**: Het donkere thema werkt correct in Chrome, Firefox, Safari en Edge (laatste 2 versies) en op mobiele browsers (iOS Safari, Android Chrome).
- **NFE13.5**: Als `localStorage` niet beschikbaar is (bijv. in incognito-modus), valt het systeem terug op de systeemvoorkeur van het apparaat via `prefers-color-scheme`.

## 7.8 Social media delen (FE8.4)

### NFE14: Social media delen specificaties

- **NFE14.1**: Alleen publiek zichtbare profielinformatie wordt doorgegeven aan het externe platform. Inloggegevens, e-mailadressen en andere privégegevens worden nooit meegestuurd.
- **NFE14.2**: De share-dialoog opent binnen 1 seconde na het klikken op de deelknop. Als het externe platform meer dan 3 seconden nodig heeft om te reageren, toont het systeem een laadstatus.
- **NFE14.3**: Als LinkedIn of Twitter niet bereikbaar is, verschijnt er binnen 5 seconden een begrijpelijke foutmelding en biedt het systeem een alternatief: de profiellink kopiëren naar het klembord.
- **NFE14.4**: Voordat het profiel gedeeld wordt, ziet de talent een preview van wat er gedeeld wordt (naam, URL, eventuele beschrijving).
- **NFE14.5**: Als de share-actie mislukt, ontvangt de gebruiker een duidelijke melding in begrijpelijke taal, zonder technische foutcodes.
