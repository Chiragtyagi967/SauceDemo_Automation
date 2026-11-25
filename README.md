
# SauceDemo Automation Testing Project

## 1. Project Overview

This project is an automation testing framework developed to test the SauceDemo e-commerce website using Python, Selenium WebDriver, and Pytest.

The main objective is to automate important website functionalities and verify that they work as expected.

The project covers login, product details, product sorting, shopping cart operations, checkout, order processing, navigation, and footer links.

**Website:** https://www.saucedemo.com/

## 2. Technologies Used

- Python 3.14
- Selenium WebDriver 4.52.0
- Pytest 9.2.0
- pytest-html 4.2.0
- Google Chrome
- Visual Studio Code
- Windows 11

## 3. Project Structure

```text
SauceDemo_Automation/
│
├── config/
│   └── config.py
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_order.py
│   ├── test_navigation.py
│   ├── test_product_details.py
│   └── test_footer.py
│
├── utils/
│   └── helpers.py
│
├── screenshots/
├── reports/
│   └── report.html
│
├── venv/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## 4. Features Tested

### 4.1 Login Testing
- Valid login
- Invalid username
- Invalid password
- Empty username
- Empty password
- Both fields empty
- Locked-out user
- Username and password case sensitivity
- Input fields with spaces
- Password masking
- Login button visibility and functionality
- Error message handling
- Login page title

### 4.2 Product Testing
- Products page loading
- Products heading
- Display of all six products
- Product names and prices
- Product descriptions
- Product images
- Add-to-cart buttons
- Sorting products by price
- Sorting products alphabetically
- Default sorting option
- Sorting dropdown options
- Unique product names
- Product price format
- Product card information

### 4.3 Shopping Cart Testing
- Open shopping cart
- Display cart heading
- Initially empty cart
- Add single product
- Add multiple products
- Verify added products
- Verify product names and prices
- Verify product quantity
- Remove products
- Update cart badge
- Verify cart badge count
- Remove one product from multiple products
- Empty cart after removing products
- Continue shopping functionality
- Checkout button visibility
- Checkout navigation

### 4.4 Checkout Testing
- Open checkout page
- Verify checkout heading
- First name field
- Last name field
- Postal code field
- Display all checkout fields
- Valid checkout information
- Missing first name
- Missing last name
- Missing postal code
- All fields empty
- Numeric and alphanumeric input
- Input containing spaces and special characters
- Continue button visibility and functionality
- Cancel checkout functionality

### 4.5 Order Testing
- Open order summary page
- Verify order summary heading
- Display ordered product
- Verify product name and price
- Display payment information
- Verify payment information
- Display shipping information
- Verify shipping information
- Verify item total
- Verify tax amount
- Verify order total
- Finish button visibility and functionality
- Complete order successfully
- Return to products page

### 4.6 Navigation and Menu Testing
- Menu button visibility
- Open navigation menu
- All Items navigation
- About link visibility
- Logout functionality

### 4.7 Product Details Testing
- Open product details page
- Verify product name
- Verify product description
- Verify product price
- Add-to-cart button visibility and functionality

### 4.8 Footer and Social Links Testing
- Footer visibility
- Copyright information
- Twitter/X social link
- Facebook social link
- LinkedIn social link

## 5. Framework Features

- Selenium WebDriver for browser automation.
- Pytest for test case execution.
- Reusable helper functions to reduce code duplication.
- Pytest fixtures for browser setup and cleanup.
- Explicit waits to handle page loading and element visibility.
- Assertions to verify expected results.
- HTML reporting using pytest-html.
- Screenshot capture for test failures through the pytest configuration.

## 6. Test Execution

### Step 1: Activate Virtual Environment

Open the project folder in CMD and execute:

```cmd
venv\Scripts\activate.bat
```

### Step 2: Run All Test Cases

```cmd
python -m pytest -v
```

### Step 3: Run a Specific Test Module

Example:

```cmd
python -m pytest tests/test_login.py -v
```

### Step 4: Generate HTML Test Report

```cmd
python -m pytest -v --html=reports/report.html --self-contained-html
```

After execution, open `reports/report.html` in a browser to view the test results.

## 7. Test Results

The project contains eight test modules covering the major functionalities of the SauceDemo website.

**Latest full execution results:**

| Result | Count |
|---|---:|
| Total collected tests | 88 |
| Passed | 87 |
| Failed | 1 |
| Pass rate | 98.86% |

The remaining failed test was related to verifying that multiple added products appeared in the shopping cart. It is being investigated.

*Update this section after the final successful execution.*

## 8. Reports and Screenshots

The project uses pytest-html to generate an HTML test report.

- HTML reports are stored in the `reports` folder.
- Failure screenshots are captured through the Pytest configuration when a test fails during execution.
- Reports help identify passed and failed test cases.

## 9. Conclusion

The SauceDemo Automation Testing Project demonstrates how Selenium WebDriver and Pytest can be used to automate the testing of an e-commerce website.

The framework covers major application functionalities, including authentication, product management, shopping cart operations, checkout, order processing, and website navigation.

It also demonstrates reusable functions, browser fixtures, explicit waits, assertions, and HTML test reporting.

The project provides practical experience in software test automation and helps identify functional issues through automated test execution.

## 10. Future Enhancements

- Add more test scenarios for different user conditions.
- Improve test execution stability.
- Expand browser compatibility testing.
- Enhance HTML reports with additional test details.
- Integrate automated testing into a CI/CD pipeline.
