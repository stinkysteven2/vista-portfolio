Feature: FE23.1 Dark mode
    As a visitor I would like to be able to switch the application to
    dark mode so that the website is comfortable to read in low-light
    environments.

Background:
    Given a visitor is on the homepage

Scenario: Toggle dark mode on
    Given the page is currently in light mode
    When I open the "settings" menu
    And I toggle the dark mode switch
    Then I see the dark mode color design.

Scenario: Toggle dark mode off
    Given the page is currently in dark mode
    When I open the "settings" menu
    And I toggle the dark mode switch
    Then I see the light mode color design.
