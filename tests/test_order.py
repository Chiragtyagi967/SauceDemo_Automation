
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import login, wait_for_element


# Helper function to open order summary
def open_order_summary(driver):
    login(driver)

    # Wait for products page
    wait_for_element(
        driver,
        (By.CLASS_NAME, "inventory_list")
    )

    # Add product to cart
    wait_for_element(
        driver,
        (By.ID, "add-to-cart-sauce-labs-backpack")
    ).click()

    # Open cart
    wait_for_element(
        driver,
        (By.CLASS_NAME, "shopping_cart_link")
    ).click()

    # Wait for cart page
    wait_for_element(
        driver,
        (By.ID, "checkout")
    )

    # Open checkout
    driver.find_element(
        By.ID,
        "checkout"
    ).click()

    # Wait for checkout information page
    wait_for_element(
        driver,
        (By.ID, "first-name")
    )

    # Enter checkout information
    driver.find_element(
        By.ID,
        "first-name"
    ).send_keys("Test")

    driver.find_element(
        By.ID,
        "last-name"
    ).send_keys("Student")

    driver.find_element(
        By.ID,
        "postal-code"
    ).send_keys("140301")

    # Continue to order summary
    driver.find_element(
        By.ID,
        "continue"
    ).click()

    # Wait for order summary page
    WebDriverWait(driver, 15).until(
        EC.url_contains("checkout-step-two")
    )

    wait_for_element(
        driver,
        (By.CLASS_NAME, "summary_info")
    )


# 1. Verify order summary page opens
def test_order_summary_page_opens(driver):
    open_order_summary(driver)

    assert "checkout-step-two" in driver.current_url


# 2. Verify order summary heading
def test_order_summary_heading(driver):
    open_order_summary(driver)

    heading = wait_for_element(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert heading.text == "Checkout: Overview"


# 3. Verify ordered product appears in summary
def test_order_product_displayed(driver):
    open_order_summary(driver)

    products = driver.find_elements(
        By.CLASS_NAME,
        "cart_item"
    )

    assert len(products) == 1


# 4. Verify correct product name in summary
def test_order_product_name(driver):
    open_order_summary(driver)

    name = wait_for_element(
        driver,
        (By.CLASS_NAME, "inventory_item_name")
    )

    assert name.text == "Sauce Labs Backpack"


# 5. Verify product price in order summary
def test_order_product_price(driver):
    open_order_summary(driver)

    price = wait_for_element(
        driver,
        (By.CLASS_NAME, "inventory_item_price")
    )

    assert price.text == "$29.99"


# 6. Verify payment information is displayed
def test_payment_information_displayed(driver):
    open_order_summary(driver)

    payment = driver.find_elements(
        By.CLASS_NAME,
        "summary_value_label"
    )

    assert len(payment) >= 2
    assert payment[0].is_displayed()


# 7. Verify payment information value
def test_payment_information_value(driver):
    open_order_summary(driver)

    payment = driver.find_elements(
        By.CLASS_NAME,
        "summary_value_label"
    )

    assert payment[0].text.startswith("SauceCard")


# 8. Verify shipping information is displayed
def test_shipping_information_displayed(driver):
    open_order_summary(driver)

    shipping = driver.find_elements(
        By.CLASS_NAME,
        "summary_value_label"
    )

    assert len(shipping) >= 2
    assert shipping[1].is_displayed()
    assert shipping[1].text.strip() != ""


# 9. Verify shipping information value
def test_shipping_information_value(driver):
    open_order_summary(driver)

    shipping = driver.find_elements(
        By.CLASS_NAME,
        "summary_value_label"
    )

    assert shipping[1].text == "Free Pony Express Delivery!"


# 10. Verify item total is displayed
def test_item_total_displayed(driver):
    open_order_summary(driver)

    item_total = wait_for_element(
        driver,
        (By.CLASS_NAME, "summary_subtotal_label")
    )

    assert item_total.text.startswith("Item total:")


# 11. Verify tax amount is displayed
def test_tax_amount_displayed(driver):
    open_order_summary(driver)

    tax = wait_for_element(
        driver,
        (By.CLASS_NAME, "summary_tax_label")
    )

    assert tax.text.startswith("Tax:")


# 12. Verify total amount is displayed
def test_order_total_displayed(driver):
    open_order_summary(driver)

    total = wait_for_element(
        driver,
        (By.CLASS_NAME, "summary_total_label")
    )

    assert total.text.startswith("Total:")


# 13. Verify Finish button is displayed and enabled
def test_finish_button_displayed_and_enabled(driver):
    open_order_summary(driver)

    finish_button = wait_for_element(
        driver,
        (By.ID, "finish")
    )

    assert finish_button.is_displayed()
    assert finish_button.is_enabled()


# 14. Verify order can be completed successfully
def test_finish_order_successfully(driver):
    open_order_summary(driver)

    driver.find_element(
        By.ID,
        "finish"
    ).click()

    confirmation = wait_for_element(
        driver,
        (By.CLASS_NAME, "complete-header")
    )

    assert confirmation.text == "Thank you for your order!"


# 15. Verify Back Home button returns to products page
def test_back_home_after_order(driver):
    open_order_summary(driver)

    driver.find_element(
        By.ID,
        "finish"
    ).click()

    wait_for_element(
        driver,
        (By.CLASS_NAME, "complete-header")
    )

    driver.find_element(
        By.ID,
        "back-to-products"
    ).click()

    assert "inventory" in driver.current_url
