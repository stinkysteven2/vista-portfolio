# Prioritering en planning verbetervoorstellen — IT Talenten Portaal

> Auteur: Steven
> Datum: april 2026
> Gebaseerd op: verbetervoorstellen deelopdracht 8

---

## 1. Inleiding

Dit document beschrijft de prioritering en planning van de vijf verbetervoorstellen uit deelopdracht 8. De prioritering is bepaald met de MoSCoW methode. De planning is opgesteld in sprints van twee weken, passend bij de werkwijze van het development team van het IT Talenten Portaal. Inschattingen zijn uitgedrukt in story points (Fibonacci), conform de inschattingsmethode van het team.

---

## 2. MoSCoW prioritering

Er zijn geen Must have voorstellen geïdentificeerd. Geen van de gevonden fouten vormt een functionele blokkade of een veiligheidsrisico. De voorstellen betreffen uitsluitend gebruikerservaring en uitbreidingen.

### Should have

| ID | Voorstel | Reden |
|---|---|---|
| VP-001 | Loginpagina vertalen naar Nederlands | Raakt alle gebruikers; staat onprofessioneel voor een Nederlandstalige applicatie |
| VP-003 | Bevestigingsmelding na formulieracties | Laag implementatie-inspanning (patroon bestaat al in de applicatie); verhoogt gebruikersvertrouwen |

### Could have

| ID | Voorstel | Reden |
|---|---|---|
| VP-004 | Layout admin tabel herzien | Visueel gebroken maar functioneel intact; raakt alleen interne gebruikers |
| VP-002 | Uitlogknop in admin panel | Workaround beschikbaar; kleine interne doelgroep |
| VP-005 | Gecombineerde reisafstand-filter | Zware feature (21 story points); gebruik en impact nog onbekend |

### Won't have

Geen voorstellen in deze categorie. VP-005 is bewust als Could have ingedeeld om de optie open te houden, ondanks de hoge complexiteit.

---

## 3. Volgorde en details per voorstel

| Volgorde | ID | Voorstel | MoSCoW | Story points | Benodigdheden |
|---|---|---|---|---|---|
| 1 | VP-001 | Loginpagina vertalen naar Nederlands | Should have | 3 | Keycloak admin |
| 2 | VP-003 | Bevestigingsmelding na formulieracties | Should have | 2 | Frontend developer |
| 3 | VP-004 | Layout admin tabel herzien | Could have | 5 | Frontend developer, designer |
| 4 | VP-002 | Uitlogknop in admin panel | Could have | 2 | Frontend developer |
| 5 | VP-005 | Gecombineerde reisafstand-filter | Could have | 21 | Backend developer, frontend developer, designer |

**Totaal: 33 story points**

---

## 4. Planning

De planning is opgesteld in sprints van twee weken. Het team heeft momenteel een volle backlog en weinig capaciteit. Implementatie start in juni. In juli is het team niet beschikbaar vanwege vakanties.

| Sprint | Periode | Voorstellen | Story points |
|---|---|---|---|
| Sprint 1 | Juni, eerste helft | VP-001, VP-003, VP-004 | 10 |
| Sprint 2 | Juni, tweede helft | VP-002 | 2 |
| — | Juli | Vakantie — geen ontwikkeling | — |
| Sprint 3 | Augustus | VP-005 | 21 |

---

## 5. Conclusie

De Should have voorstellen (VP-001 en VP-003) worden als eerste opgepakt omdat ze de meeste gebruikers raken en relatief weinig inspanning kosten. De Could have voorstellen volgen daarna op volgorde van impact en complexiteit. VP-005 is bewust naar augustus geschoven vanwege de hoge complexiteit (21 story points) en de vakantieperiode in juli.
