Feature: Google.com Demo

  Scenario: Search google
    Given I load "http://www.google.com"
    When Fill in the form with "clown"
    Then  I can see that page title starts with "clown"
