# Reflectie — Handmatig testen

## Observatie

Handmatig testen duurt langer dan geautomatiseerd testen. Toch leverde TC-003 een bevinding op die niet in het testplan stond: de loginpagina is volledig in het Engels, terwijl de applicatie gericht is op een Nederlands publiek. Een geautomatiseerde test had dit niet gevlagd, omdat het script alleen controleert wat het testplan voorschrijft.

## Conclusie

Handmatig testen blijft belangrijk, juist omdat een menselijke tester dingen opmerkt die buiten de testcases vallen.

## Conflict: geautomatiseerd vs. handmatig bij TC-006

Bij TC-006 (talentprofiel afgeschermd voor bezoekers) rapporteerde de geautomatiseerde test GEFAALD: de selector `[class*='contact']` pakte een element op dat als persoonsgegevens werd geïnterpreteerd. Handmatige inspectie liet zien dat de pagina wél correct afgeschermd was — de applicatie toonde een loginbericht en verborg naam en contactgegevens.

Dit zijn conflicterende resultaten: de geautomatiseerde test faalt, maar de handmatige test slaagt. De oorzaak is waarschijnlijk een te brede CSS-selector die een onschuldig element oppakt, maar dit verdient nader onderzoek.

Beide uitkomsten zijn vastgelegd in de screenshots-map. Dit benadrukt dat geautomatiseerde testresultaten niet blindelings vertrouwd mogen worden — een falende test is niet per definitie een bug in de applicatie.

## Aanpak voor de rest van het testplan

Als meerdere testcases sterk op elkaar lijken — zoals TC-001, TC-002 en TC-003 bij het inloggen — is het efficiënt om er één handmatig uit te voeren en de rest te automatiseren of met behulp van agentic AI (zoals Claude Code met Playwright) te draaien. Zo combineer ik de voordelen van beide methoden: de snelheid van automatisering en de breedte van handmatig testen.
