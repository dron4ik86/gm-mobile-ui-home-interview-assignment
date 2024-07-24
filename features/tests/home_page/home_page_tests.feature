Feature: Home Page

  Scenario Outline: Changes the Temperature
    Given The user is on the home page
    When The user enters <temperature> in the temperature text box
    Then The temperature should be updated to <temperature>
    When Sending the API request to get the audio file
    Then The audio file should contain the <temperature>

    Examples:
    | temperature |
    | 25          |
    | 20          |