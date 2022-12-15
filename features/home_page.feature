Feature: Home Page
#  Given I am a customer
#  When I navigate to the demoblaze website
#  Then A home page is open
#  And I have access from it to all website functionalities

  Scenario: Carousel images from homepage stop when keep cursor on it
    Given I am on the homepage
    When I keep the mouse cursor on the carousel images
    Then The carousel image stop at the current images

  Scenario: Carousel images from homepage move automatically when don't keep cursor on it
    Given I am on the homepage
    When I don't keep the mouse cursor on the carousel images
    Then The carousel image move automatically

  Scenario: Carousel images from homepage can be changed using right arrow
    Given I am on the homepage
    When I press the right arrow from the carousel images
    Then The carousel image change to next image

  Scenario: Carousel images from homepage can be changed using right arrow
    Given I am on the homepage
    When I press the left arrow from the carousel images
    Then The carousel image change to previous image

  Scenario Outline: Carousel images slide button work properly
    Given I am on the homepage
    When I press <position> slide button
    Then The carousel image is <image>

  Examples: Slide position and images:
    |position | image        |
    |first    | Samsung1.jpg |
    |second   | nexus1.jpg   |
    |third    | iphone1.jpg  |