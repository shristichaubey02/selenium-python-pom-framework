# Selenium Python POM Automation Framework

## 1. Project Overview

This project is a Selenium WebDriver automation framework developed using Python and Pytest.

The framework follows the **Page Object Model (POM)** design pattern to keep test cases clean, reusable, and maintainable.

The project automates the SauceDemo application and currently covers:

- Valid login
- Invalid login
- Adding a product to the cart
- Cart navigation

The framework also includes HTML reporting, failure screenshots, configuration management, and GitHub Actions CI.

---

## 2. Technologies Used

### 2.1 Python

Python is used as the primary programming language for the automation framework.

### 2.2 Selenium WebDriver

Selenium WebDriver is used to automate browser interactions.

### 2.3 Pytest

Pytest is used as the testing framework for:

- Test execution
- Fixtures
- Assertions
- Test discovery

### 2.4 Page Object Model

The Page Object Model is used to separate:

- Test logic
- Page locators
- Page actions

This makes the framework easier to maintain and reuse.

### 2.5 pytest-html

`pytest-html` is used to generate HTML test reports.

### 2.6 jproperties

`jproperties` is used to read configuration values from the `config.properties` file.

### 2.7 Git and GitHub

Git is used for version control and GitHub is used to store the project repository.

### 2.8 GitHub Actions

GitHub Actions is used to automatically execute the test suite in CI.

---

## 3. Project Structure

### 3.1 .github

#### 3.1.1 workflows

##### 3.1.1.1 tests.yml

Contains the GitHub Actions CI workflow used to automatically install dependencies and execute the Pytest test suite.

### 3.2 data

#### 3.2.1 test_data.py

Contains test data used by the automation tests, such as usernames, passwords, and product names.

### 3.3 pages

#### 3.3.1 __init__.py

Marks the `pages` directory as a Python package.

#### 3.3.2 base_page.py

Contains reusable Selenium operations such as:

- Click
- Enter text
- Get text
- Explicit waits

#### 3.3.3 login_page.py

Contains locators and actions related to the login page.

#### 3.3.4 inventory_page.py

Contains actions related to the inventory page, including:

- Adding products to the cart
- Opening the cart

#### 3.3.5 cart_page.py

Contains actions and validations related to the shopping cart.

#### 3.3.6 checkout_page.py

Contains actions related to the checkout process.

### 3.4 resources

#### 3.4.1 config.properties

Contains framework configuration values such as:

- Application URL
- Browser
- Timeout
- Headless execution settings

### 3.5 tests

#### 3.5.1 __init__.py

Marks the `tests` directory as a Python package.

#### 3.5.2 test_login.py

Contains login test cases:

- Valid login
- Invalid login

#### 3.5.3 test_inventory.py

Contains the inventory and cart test case.

### 3.6 utils

#### 3.6.1 __init__.py

Marks the `utils` directory as a Python package.

#### 3.6.2 config_factory.py

Reads configuration values from `config.properties`.

#### 3.6.3 driver_factory.py

Creates and configures the Selenium WebDriver.

### 3.7 conftest.py

Contains Pytest fixtures used to initialize and clean up the WebDriver for tests.

### 3.8 pytest.ini

Contains Pytest configuration, including the test directory and test execution settings.

### 3.9 requirements.txt

Contains the Python dependencies required to run the framework.

### 3.10 README.md

Contains project documentation and instructions for running the framework.

---

## 4. Framework Design

### 4.1 Page Object Model

The framework follows the Page Object Model design pattern.

Each application page has a dedicated Python class.

For example:

```text
LoginPage
InventoryPage
CartPage
CheckoutPage