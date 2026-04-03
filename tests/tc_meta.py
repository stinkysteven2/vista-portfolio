"""
Metadata per testcase: beschrijving, eis, prioriteit, teststappen en conclusie-templates.
Wordt gebruikt door manual_entry.py, generate_report.py en save_results() in helpers.py.
"""

TC_META = {
    "TC-001": {
        "description": "Inloggen met geldige gegevens",
        "eis": "FE1",
        "prioriteit": "Hoog",
        "stappen": [
            "Navigeer naar de startpagina (`/talent`)",
            "Klik op het login-icoon (`section#login i.material-icons`) in de navigatiebalk",
            "Keycloak-loginpagina laadt op extern domein",
            "Vul geldige gebruikersnaam en wachtwoord in",
            'Klik op "Sign In"',
        ],
        "conclusie_geslaagd": "Inloggen werkt correct. De applicatie stuurt de gebruiker terug naar de startpagina en toont het logout-icoon.",
        "conclusie_gefaald": "Inloggen werkt niet correct.",
    },
    "TC-002": {
        "description": "Inloggen met onjuist wachtwoord",
        "eis": "FE1",
        "prioriteit": "Hoog",
        "stappen": [
            "Navigeer naar de startpagina (`/talent`) — frisse sessie (niet ingelogd)",
            "Klik op het login-icoon in de navigatiebalk",
            "Keycloak-loginpagina laadt",
            "Vul geldige gebruikersnaam in, maar een onjuist wachtwoord",
            'Klik op "Sign In"',
        ],
        "conclusie_geslaagd": "Het systeem toont de juiste foutmelding en stuurt de gebruiker niet door. Werkt correct.",
        "conclusie_gefaald": "Het systeem geeft geen of onjuiste foutmelding.",
    },
    "TC-003": {
        "description": "Inloggen met onbekend e-mailadres",
        "eis": "FE1",
        "prioriteit": "Gemiddeld",
        "stappen": [
            "Navigeer naar de startpagina (`/talent`) — handmatig, Firefox",
            "Klik op het login-icoon in de navigatiebalk",
            "Keycloak-loginpagina laadt",
            "Vul een onbekend e-mailadres in (`ditbestaaniet@test.nl`) en willekeurig wachtwoord",
            'Klik op "Sign In"',
        ],
        "conclusie_geslaagd": "Het systeem maakt geen onderscheid tussen onbekend account en fout wachtwoord. Werkt correct.",
        "conclusie_gefaald": "Het systeem geeft een onverwachte of ontbrekende foutmelding.",
    },
    "TC-004": {
        "description": "Uitloggen",
        "eis": "FE2",
        "prioriteit": "Hoog",
        "stappen": [
            "Log in met geldige gegevens (zie TC-001)",
            "Klik op het logout-icoon in de navigatiebalk",
        ],
        "conclusie_geslaagd": "Uitloggen werkt correct. De applicatie toont het login-icoon en verbergt het logout-icoon.",
        "conclusie_gefaald": "Uitloggen werkt niet correct.",
    },
}
