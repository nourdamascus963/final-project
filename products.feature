Feature: Product Management

  Scenario: Get all products
    Given the product service is running
    When I request all products
    Then I should receive a list of products

  Scenario: Add a new product
    Given the product service is running
    When I add a new product
    Then the product should be added successfully

  Scenario: Delete a product
    Given the product service is running
    When I delete a product
    Then the product should be removed
