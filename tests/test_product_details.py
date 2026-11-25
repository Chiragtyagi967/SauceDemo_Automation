
from selenium.webdriver.common.by import By
from utils.helpers import login, wait_for_element


def open_products_page(driver):
    login(driver)
    wait_for_element(driver, (By.CLASS_NAME, "inventory_list"))


def open_first_product_details(driver):
    open_products_page(driver)

    product_name = wait_for_element(
        driver, (By.CLASS_NAME, "inventory_item_name")
    )
    product_name.click()

    wait_for_element(driver, (By.CLASS_NAME, "inventory_details"))


# 1. Product details page opens
def test_product_details_page_opens(driver):
    open_first_product_details(driver)

    assert driver.find_element(
        By.CLASS_NAME, "inventory_details"
    ).is_displayed()


# 2. Product name is displayed
def test_product_name_displayed(driver):
    open_first_product_details(driver)

    name = wait_for_element(
        driver, (By.CLASS_NAME, "inventory_details_name")
    )

    assert name.is_displayed()
    assert name.text.strip() != ""


# 3. Product description is displayed
def test_product_description_displayed(driver):
    open_first_product_details(driver)

    description = wait_for_element(
        driver, (By.CLASS_NAME, "inventory_details_desc")
    )

    assert description.is_displayed()
    assert description.text.strip() != ""


# 4. Product price is displayed
def test_product_price_displayed(driver):
    open_first_product_details(driver)

    price = wait_for_element(
        driver, (By.CLASS_NAME, "inventory_details_price")
    )

    assert price.is_displayed()
    assert "$" in price.text


# 5. Add to cart button is displayed and enabled
def test_add_to_cart_button_displayed_and_enabled(driver):
    open_first_product_details(driver)

    button = wait_for_element(
        driver, (By.CLASS_NAME, "btn_inventory")
    )

    assert button.is_displayed()
    assert button.is_enabled()
