Feature: FE8.4 Share Project
    As a student I would like to share my projects on social media to showcase
    my work to potential employers.

Background:
    Given I am on a project page

Scenario: Share project on Twitter
    When I click the "Share on Twitter" button
    Then I should see a Twitter share dialog with the project link

Scenario: Share project on LinkedIn
    When I click the "Share on LinkedIn" button
    Then I should see a LinkedIn share dialog with the project link
