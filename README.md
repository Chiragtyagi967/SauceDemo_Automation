# SauceDemo Automation Testing Project

## 1. Project Overview

This project automates the testing of the SauceDemo (Swag Labs) e-commerce website using Python, Selenium WebDriver and Pytest.

The suite contains **110 automated test cases in 8 modules**. It covers login, product listing and sorting, product details, shopping cart, checkout, order completion, the side menu and the footer.

**Website:** https://www.saucedemo.com/

**Latest result:** 110 passed in 557.14 s (0:09:17).

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
│   └── config.py              # URL, users, checkout data
│
├── tests/
│   ├── test_login.py            # 15 tests
│   ├── test_products.py         # 25 tests
│   ├── test_product_details.py  # 5 tests
│   ├── test_cart.py             # 20 tests
│   ├── test_checkout.py         # 20 tests
│   ├── test_order.py            # 15 tests
│   ├── test_navigation.py       # 5 tests
│   └── test_footer.py           # 5 tests
│
├── utils/
│   └── helpers.py             # reusable wait/click/type/login helpers
│
├── screenshots/               # failure screenshots
├── reports/                   # HTML report
├── conftest.py                # driver fixture + failure screenshot hook
├── pytest.ini
├── requirements.txt
└── README.md
```

## 4. Features Tested

### 4.1 Login (15 tests)
- Valid login
- Invalid username and invalid password
- Empty username, empty password, both empty
- Locked-out user
- Username and password are case sensitive
- Leading/trailing spaces are rejected
- Password field is masked
- Login button is visible and enabled
- Error message can be closed
- Page title is "Swag Labs"

### 4.2 Products (25 tests)
- Products page and heading load
- 6 products with name, price, description, image and button
- Sort by price (low to high, high to low)
- Sort by name (A to Z, Z to A)
- Default sort and dropdown options (4 options, selected value)
- Names are unique, prices start with "$", descriptions not empty
- Page stays open after sorting

### 4.3 Product Details (5 tests)
- Details page opens
- Name, description and price are displayed
- Add to cart button is displayed and enabled

### 4.4 Cart (20 tests)
- Cart page and heading; cart empty at start
- Add one or multiple products
- Cart badge updates on add and remove
- Item name, price and quantity are correct
- Remove one or all products
- Continue Shopping and Checkout buttons and navigation

### 4.5 Checkout (20 tests)
- Checkout page, heading and all fields displayed
- Valid information moves to the overview
- Missing first name, last name or postal code shows an error
- All fields empty shows an error
- Input variations: numeric, alphanumeric, spaces, special characters
- Continue and Cancel buttons; Cancel returns to the cart

### 4.6 Order (15 tests)
- Order overview page, heading, product name and price
- Payment and shipping information
- Item total, tax and total labels
- Finish order shows the "Thank you" message
- Back Home returns to products

### 4.7 Navigation (5 tests)
- Menu button is displayed and the menu opens
- All Items navigation
- About link is displayed
- Logout returns to the login page

### 4.8 Footer (5 tests)
- Footer and copyright text are displayed
- Twitter, Facebook and LinkedIn links are displayed

**Total: 110 tests**

## 5. Framework Design

- **Configuration:** shared values (URL, users, password, checkout data) are kept in `config/config.py`.
- **Helpers:** `utils/helpers.py` provides `wait_for_element`, `click_element`, `enter_text`, `login`, `logout` and `get_error_message`, using explicit waits (10 seconds).
- **Fixture:** `conftest.py` starts a fresh Chrome browser for every test (password-manager pop-ups disabled, window maximised) and closes it afterwards.
- **Failure screenshots:** if a test fails, a screenshot is saved in `screenshots/` and attached to the HTML report.

## 6. Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install selenium==4.52.0 pytest==9.2.0 pytest-html==4.2.0
pip freeze > requirements.txt
```

To recreate the environment later: `pip install -r requirements.txt`

## 7. Running the Tests

Run all tests:

```bash
python -m pytest -v
```

Run all tests and create the HTML report:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

Run one module, one keyword or one test:

```bash
python -m pytest tests/test_login.py
python -m pytest -k checkout
python -m pytest tests/test_cart.py::test_add_single_product
```

A full run takes about 9 minutes because every test opens its own browser.

## 8. Test Results

| Total | Passed | Failed | Pass rate | Time |
|---|---|---|---|---|
| 110 | 110 | 0 | 100% | 557.14 s |
