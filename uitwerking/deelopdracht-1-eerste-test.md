# Deelopdracht 1 — Eerste test van het IT Talenten Portaal

## Gevonden fouten

> Getest op: [datum]
> Geteste applicatie: [IT Talenten Portaal](https://it-talenten-portaal-test-it-talenten-webapp-test.iapmkw.easypanel.host/talent)
> Browser: Chromium (via Playwright) + handmatig in [browser]

| # | Wat ik deed | Wat ik verwachtte | Wat er gebeurde | Waar op de site | Ernst |
|---|-------------|-------------------|-----------------|-----------------|-------|
| 1 | Homepage bezoeken(niet ingelogd) | Ik zie talenten in de carrousel | er zijn geen talenten te zien | / | midden |
| 2 | open zoekcriteria > Provincie op de vacatures pagina | Ik verwacht een selectiemenu | veel van de selectie items in het menu zijn onleesbaar | /vacatures | midden |
| 3 | Privacy pagina lezen | Een statement over privacy | een lorem ipsum text | Privacy |  midden |
| 4 | Klikken op de "it-talenten.nl" link in de navigatiebalk | Doorverwijzing naar de externe website it-talenten.nl | De pagina navigeert naar /linknaarittalenten en toont een lege foutpagina (Angular routingfout: route bestaat niet) | Navigatiebalk (alle pagina's) | midden |
| 5 | Pagina's laden en de afbeeldingen bekijken | Alle afbeeldingen worden correct weergegeven | Op elke pagina zijn 2 afbeeldingen zonder src-attribuut — ze worden niet geladen en tonen een gebroken afbeeldingsicoon | Alle pagina's | laag |

---

## Reflectie

**Wat is software testen volgens jou na deze eerste ervaring?**

Software testen is het proces waarbij je fouten in een computerprogramma opspoort.

---

**Wat vond je moeilijk of makkelijk aan het vinden van fouten?**

Ik vind software testen een saai proces dus mijn aandacht erbij houden is lastig. Ik denk dat ik goed ben in het helder omschrijven wat voor fouten ik vind.

---

**Waarom denk je dat testen belangrijk is?**

Testen is belangrijk omdat software vrijwel altijd problemen bevat. Door middel van testen kan je fouten opsporen, wat als signaal kan worden gebruikt om die fouten te verbeteren.

---

**Wat zou je de volgende keer anders doen?**

Nu weet ik wel wat er slecht gaat maar niet wat er goed gaat. Ik zou planmatiger werken als ik een website zou testen. Wellicht eerst documentatie of een sitemap of iets dergelijks gebruiken om de te testen oppervlakte in kaart te brengen om die vervolgens systematisch af te werken. Willy-nilly testen vindt wel fouten maar geeft geen garanties over "kwaliteitsbodem".
