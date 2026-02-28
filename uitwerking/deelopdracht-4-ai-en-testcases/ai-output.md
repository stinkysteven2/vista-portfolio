# AI-gegenereerde testcases — FE2: Inloggen

> Dit is de originele output van Claude Code (AI-tool), gegenereerd op basis van de FE2-eisen uit het SRS document.
>
> **Gebruikte prompt:**
> "Genereer testcases voor de inlogfunctionaliteit van het IT Talenten Portaal op basis van de volgende eisen:
> - FE2.1: Het systeem moet gebruikers in staat stellen in te loggen met e-mailadres en wachtwoord.
> - FE2.2: Het systeem moet ongeldige inlogpogingen detecteren en een foutmelding tonen.
> - FE2.3: Het systeem moet een 'Wachtwoord vergeten' functionaliteit bieden.
> Zorg voor zowel positieve als negatieve testcases."

---

| TC-ID | Beschrijving | Precondities | Stappen | Verwacht resultaat | FE-ref |
|-------|-------------|--------------|---------|-------------------|--------|
| TC-01 | Succesvol inloggen met geldige gegevens | Gebruiker heeft een account | 1. Ga naar de loginpagina. 2. Vul een geldig e-mailadres in. 3. Vul het bijbehorende wachtwoord in. 4. Klik op "Inloggen". | Gebruiker wordt ingelogd en doorgestuurd naar de homepage. | FE2.1 |
| TC-02 | Inloggen met ongeldig e-mailadres | Gebruiker is niet ingelogd | 1. Ga naar de loginpagina. 2. Vul een ongeldig e-mailadres in (bijv. "geengeldigemail"). 3. Vul een wachtwoord in. 4. Klik op "Inloggen". | Er wordt een foutmelding getoond. | FE2.2 |
| TC-03 | Inloggen met verkeerd wachtwoord | Gebruiker heeft een account | 1. Ga naar de loginpagina. 2. Vul een geldig e-mailadres in. 3. Vul een verkeerd wachtwoord in. 4. Klik op "Inloggen". | Er wordt een foutmelding getoond. | FE2.2 |
| TC-04 | Inloggen met lege velden | Gebruiker is op de loginpagina | 1. Ga naar de loginpagina. 2. Laat beide velden leeg. 3. Klik op "Inloggen". | Er wordt een foutmelding getoond. | FE2.2 |
| TC-05 | Wachtwoord vergeten — e-mail versturen | Gebruiker heeft een account | 1. Ga naar de loginpagina. 2. Klik op "Wachtwoord vergeten". 3. Vul het e-mailadres in. 4. Klik op "Verstuur". | Gebruiker ontvangt een e-mail met een resetlink. | FE2.3 |
| TC-06 | Wachtwoord vergeten — onbekend e-mailadres | Gebruiker is op de wachtwoord-vergeten-pagina | 1. Klik op "Wachtwoord vergeten". 2. Vul een e-mailadres in dat niet bestaat. 3. Klik op "Verstuur". | Er wordt een foutmelding getoond dat het e-mailadres niet bekend is. | FE2.3 |
