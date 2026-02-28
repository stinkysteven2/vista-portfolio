# Reflectie met Claude Code na afronding

## Verbeterpunten

Tijdens het nakijken van het werk zijn een aantal punten opgemerkt die verbeterd kunnen worden. Deze zijn bewust nog niet aangepast, maar worden hier gedocumenteerd.

### 1. Tegenstrijdigheid scope en FE8.4

Sectie 2.2 van het SRS ("Wat valt buiten de scope") vermeldt expliciet:
> *"Social media integraties (behalve mogelijk links naar externe profielen)"*

Dit staat direct in conflict met FE8.4, dat social media sharing toevoegt als functionele eis. Dit is ontstaan doordat FE8.4 later is toegevoegd als klantwens zonder de scope-sectie bij te werken. Oplossing: sectie 2.2 aanpassen zodat de social media deelfunctionaliteit expliciet binnen scope valt.

### 2. FE23 (dark mode) is beperkt uitgewerkt

FE23 heeft momenteel slechts één sub-eis (FE23.1). Vergeleken met andere secties in het SRS is dit erg summier. Mogelijke uitbreidingen:
- FE23.2: De voorkeur wordt opgeslagen in de browser (localStorage), zodat de keuze bewaard blijft bij een volgend bezoek.
- FE23.3: Het systeem volgt de systeemvoorkeur van het apparaat (`prefers-color-scheme`) als standaard.
- FE23.4: Kleuren in dark mode voldoen aan de contrastnormen van WCAG 2.1 AA.

### 3. FE4 actor in de backlog is "Systeem"

In de backlog staat bij FE4 (autorisatie op basis van gebruikersrol) als actor "Systeem". Een user story heeft altijd een persoon als actor. Dit zou herschreven moeten worden vanuit het perspectief van de beheerder:
> *"Als beheerder wil ik gebruikersrollen kunnen instellen zodat elke gebruiker alleen toegang heeft tot functionaliteit die bij zijn rol past."*
