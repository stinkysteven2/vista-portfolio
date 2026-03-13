# Reflectie — Deelopdracht 5: Scope document

## Wat ging goed

Het scope document is goed ontvangen door de docenten. De opbouw was helder, niet te uitgebreid, maar wel met voldoende diepgang. De risico-analyse (sectie 3) en de onderbouwde browserkeuze op basis van Nederlands marktaandeel werden positief beoordeeld.

## Verbeterpunt: redenen om niet te testen

De docent gaf als feedback dat de redenen om onderdelen *niet* te testen te sterk leunden op MoSCoW-prioritering. Bijna alle uitsluitingen waren gebaseerd op "dit heeft geen prioriteit" of "dit valt buiten de huidige ontwikkelstrategie" — dus zakelijke keuzes.

Maar er zijn meer categorieën van redenen om iets niet te testen:

| Categorie | Voorbeeld |
|---|---|
| **Geen toegang** | Geen inloggegevens beschikbaar voor een bepaalde gebruikersrol |
| **Geen testomgeving** | Functionaliteit bestaat alleen in productie, testen brengt risico's mee |
| **Extern systeem** | Koppeling met UWV of sociale media — buiten ons beheer |
| **Testen zelf is risicovol** | Echte betalingen triggeren, echte e-mails versturen, productiedata beschadigen |
| **Functionaliteit nog niet gebouwd** | Er valt nog niets te testen |
| **Zakelijke keuze (MoSCoW)** | Geen prioriteit, buiten scope van huidige sprint of release |

In het document staat bij "koppeling met sociale media" al een aanzet in de goede richting: het risico voor persoonsgegevens is een inhoudelijke reden, niet alleen een prioriteitskeuze. Maar bij "filteren van vacatures" is de enige reden "geen prioriteit" — terwijl je ook had kunnen benoemen of er testdata of een testrol beschikbaar is.

## Eigen inzicht: efficiëntie als scopecriterium

Na de les realiseerde ik me dat er nog een dimensie ontbreekt in het scope document: mijn eigen positie als lerende. Het doel van dit project is tweeledig — leren en bewijzen dat ik heb geleerd. Als ik die twee dingen goed doe, ben ik tevreden.

Dat betekent dat "zo min mogelijk tijd besteden" een bewuste en legitieme keuze is. Niet uit luiheid, maar omdat ik gericht wil investeren: diepgang waar het leert, efficiëntie waar het kan. In een professionele context heet dat risico-gebaseerd testen. In mijn context heet het slim studeren.

Een volgende scope zou dit explicieter kunnen benoemen: wat test ik omdat ik er het meest van leer, en wat laat ik bewust weg omdat de leerwaarde niet opweegt tegen de tijdsinvestering?

## Wat ik een volgende keer anders doe

Bij het opstellen van een scope document kijk ik niet alleen naar wat de business wil testen, maar ook naar wat *haalbaar* is om te testen. Ontbrekende inloggegevens, het ontbreken van een testomgeving of de afhankelijkheid van externe systemen zijn zelfstandige uitsluitingsgronden — los van MoSCoW. En ik benoem expliciet welke keuzes ik maak vanuit mijn eigen leerdoelen en tijdsbudget.
