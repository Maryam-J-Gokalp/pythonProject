# Created by mariajoana at 04/11/2022
Feature: BBC News para todos

Scenario: Verify that user can sign in with valid credentials

 Feature: I6_BBCNews app sign in feature
  User Story:
  As an HR user, I should be able to sign in; so that I can land on homepage.

  Background
    Given user is on the homePage

  ScenarioOutline:
    When user see England, N.Ireland and Scotland (sub sections of Home)
    When user clicks sign in button at the top of the screen
    And user enters "<email or username>"
    And user enters "<password>"
    And user clicks to sign in button
    Then user should see message "Need help signing in? (Enter a password of @@££@@££ in the password field and click Sign In) "

  ScenarioOutline:
    When user enters username "<username>"
    And user enters password "<password>"
    And user clicks to sign in button
    And user should not see dashboard instead this notice message : "Incorrect sign in or password."
    Then Sorry, that password is too short. It needs to be eight characters or more






