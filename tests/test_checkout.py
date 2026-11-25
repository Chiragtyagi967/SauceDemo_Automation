
from selenium.webdriver.common.by import By

from config.config import (
    FIRST_NAME,
    LAST_NAME,
    POSTAL_CODE
)

from utils.helpers import login, wait_for_element


# Helper function to start checkout
def start_checkout(driver):
    login(driver)

    wait_for_element(
        driver,
        (By.CLASS_NAME, "inventory_list")
    )

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    wait_for_element(
        driver,
        (By.ID, "checkout")
    )

    driver.find_element(
        By.ID,
        "checkout"
    ).click()

    wait_for_element(
        driver,
        (By.ID, "first-name")
    )


# Helper function to fill checkout information
def fill_checkout_information(
    driver,
    first_name=FIRST_NAME,
    last_name=LAST_NAME,
    postal_code=POSTAL_CODE
):
    first_name_field = wait_for_element(
        driver,
        (By.ID, "first-name")
    )

    first_name_field.clear()
    first_name_field.send_keys(first_name)

    last_name_field = wait_for_element(
        driver,
        (By.ID, "last-name")
    )

    last_name_field.clear()
    last_name_field.send_keys(last_name)

    postal_field = wait_for_element(
        driver,
        (By.ID, "postal-code")
    )

    postal_field.clear()
    postal_field.send_keys(postal_code)


# Helper function to get checkout error
def get_checkout_error(driver):
    return wait_for_element(
        driver,
        (By.CSS_SELECTOR, "[data-test='error']")
    ).text


# 1. Verify checkout information page opens
def test_checkout_page_opens(driver):
    start_checkout(driver)

    assert "checkout-step-one" in driver.current_url


# 2. Verify checkout page heading
def test_checkout_page_heading(driver):
    start_checkout(driver)

    heading = wait_for_element(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert heading.text == "Checkout: Your Information"


# 3. Verify first name field is displayed
def test_first_name_field_displayed(driver):
    start_checkout(driver)

    field = wait_for_element(
        driver,
        (By.ID, "first-name")
    )

    assert field.is_displayed()


# 4. Verify last name field is displayed
def test_last_name_field_displayed(driver):
    start_checkout(driver)

    field = wait_for_element(
        driver,
        (By.ID, "last-name")
    )

    assert field.is_displayed()


# 5. Verify postal code field is displayed
def test_postal_code_field_displayed(driver):
    start_checkout(driver)

    field = wait_for_element(
        driver,
        (By.ID, "postal-code")
    )

    assert field.is_displayed()


# 6. Verify all checkout fields are displayed
def test_checkout_information_fields_displayed(driver):
    start_checkout(driver)

    field_ids = [
        "first-name",
        "last-name",
        "postal-code"
    ]

    for field_id in field_ids:
        field = driver.find_element(
            By.ID,
            field_id
        )

        assert field.is_displayed()


# 7. Verify valid checkout information is accepted
def test_valid_checkout_information(driver):
    start_checkout(driver)

    fill_checkout_information(driver)

    driver.find_element(
        By.ID,
        "continue"
    ).click()

    assert "checkout-step-two" in driver.current_url


# 8. Verify checkout with empty first name
def test_missing_first_name(driver):
    start_checkout(driver)

    fill_checkout_information(
        driver,
        first_name=""
    )

    driver.find_element(
        By.ID,
        "continue"
    ).click()

    assert "First Name is required" in get_checkout_error(driver)


# 9. Verify checkout with empty last name
def test_missing_last_name(driver):
    start_checkout(driver)

    fill_checkout_information(
        driver,
        last_name=""
    )

    driver.find_element(
        By.ID,
        "continue"
    ).click()

    assert "Last Name is required" in get_checkout_error(driver)


# 10. Verify checkout with empty postal code
def test_missing_postal_code(driver):
    start_checkout(driver)

    fill_checkout_information(
        driver,
        postal_code=""
    )

    driver.find_element(
        By.ID,
        "continue"
    ).click()

    assert "Postal Code is required" in get_checkout_error(driver)


# 11. Verify checkout with all fields empty
def test_all_checkout_fields_empty(driver):
    start_checkout(driver)

    fill_checkout_information(
        driver,
        first_name="",
        last_name="",
        postal_code=""
    )

    driver.find_element(
        By.ID,
        "continue"
    ).click()

    assert "First Name is required" in get_checkout_error(driver)


# 12. Verify checkout with numeric first name
def test_numeric_first_name(driver):
    start_checkout(driver)

    fill_checkout_information(
        driver,
        first_name="12345"
    )

    driver.find_element(
        By.ID,
        "continue"
    ).click()

    assert "checkout-step-two" in driver.current_url


# 13. Verify checkout with numeric last name
def test_numeric_last_name(driver):
    start_checkout(driver)

    fill_checkout_information(
        driver,
        last_name="12345"
    )

    driver.find_element(
        By.ID,
        "continue"
    ).click()

    assert "checkout-step-two" in driver.current_url


# 14. Verify checkout with alphanumeric postal code
def test_alphanumeric_postal_code(driver):
    start_checkout(driver)

    fill_checkout_information(
        driver,
        postal_code="ABC123"
    )

    driver.find_element(
        By.ID,
        "continue"
    ).click()

    assert "checkout-step-two" in driver.current_url


# 15. Verify checkout with spaces in first name
def test_first_name_with_spaces(driver):
    start_checkout(driver)

    fill_checkout_information(
        driver,
        first_name="Test Student"
    )

    driver.find_element(
        By.ID,
        "continue"
    ).click()

    assert "checkout-step-two" in driver.current_url


# 16. Verify checkout with special characters in name
def test_special_characters_in_first_name(driver):
    start_checkout(driver)

    fill_checkout_information(
        driver,
        first_name="Test@123"
    )

    driver.find_element(
        By.ID,
        "continue"
    ).click()

    assert "checkout-step-two" in driver.current_url


# 17. Verify Continue button is displayed and enabled
def test_continue_button_displayed_and_enabled(driver):
    start_checkout(driver)

    button = wait_for_element(
        driver,
        (By.ID, "continue")
    )

    assert button.is_displayed()
    assert button.is_enabled()


# 18. Verify Cancel button is displayed and enabled
def test_cancel_button_displayed_and_enabled(driver):
    start_checkout(driver)

    button = wait_for_element(
        driver,
        (By.ID, "cancel")
    )

    assert button.is_displayed()
    assert button.is_enabled()


# 19. Verify Cancel button returns to cart
def test_cancel_checkout_returns_to_cart(driver):
    start_checkout(driver)

    driver.find_element(
        By.ID,
        "cancel"
    ).click()

    assert "cart" in driver.current_url


# 20. Verify checkout form fields accept entered values
def test_checkout_fields_accept_input(driver):
    start_checkout(driver)

    fill_checkout_information(
        driver,
        first_name="Chirag",
        last_name="Student",
        postal_code="140301"
    )

    assert driver.find_element(
        By.ID,
        "first-name"
    ).get_attribute("value") == "Chirag"

    assert driver.find_element(
        By.ID,
        "last-name"
    ).get_attribute("value") == "Student"

    assert driver.find_element(
        By.ID,
        "postal-code"
    ).get_attribute("value") == "140301"
