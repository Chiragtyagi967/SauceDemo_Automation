
from selenium.webdriver.common.by import By

from utils.helpers import login, wait_for_element


# Helper function to open the cart
def open_cart(driver):
    login(driver)

    wait_for_element(
        driver,
        (By.CLASS_NAME, "inventory_list")
    )

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    wait_for_element(
        driver,
        (By.CLASS_NAME, "cart_list")
    )


# Helper function to get cart products
def get_cart_products(driver):
    return driver.find_elements(
        By.CLASS_NAME,
        "cart_item"
    )


# Helper function to add the first product
def add_first_product(driver):
    button = wait_for_element(
        driver,
        (By.ID, "add-to-cart-sauce-labs-backpack")
    )
    button.click()


# 1. Verify cart page opens successfully
def test_cart_page_opens(driver):
    open_cart(driver)

    assert "cart" in driver.current_url


# 2. Verify cart heading is displayed
def test_cart_heading_displayed(driver):
    open_cart(driver)

    heading = wait_for_element(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert heading.text == "Your Cart"


# 3. Verify cart is empty initially
def test_cart_is_empty_initially(driver):
    open_cart(driver)

    assert len(get_cart_products(driver)) == 0


# 4. Verify one product can be added to cart
def test_add_single_product(driver):
    login(driver)
    add_first_product(driver)

    assert driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    ).text == "1"


# 5. Verify multiple products can be added to cart
def test_add_multiple_products(driver):
    login(driver)

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-bike-light"
    ).click()

    assert driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    ).text == "2"


# 6. Verify added product appears in cart
# 6. Verify added product appears in cart
def test_added_product_appears_in_cart(driver):
    login(driver)
    add_first_product(driver)

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    wait_for_element(
        driver,
        (By.CLASS_NAME, "cart_item")
    )

    products = get_cart_products(driver)

    assert len(products) == 1


# 7. Verify correct product name appears in cart
def test_cart_displays_correct_product_name(driver):
    login(driver)
    add_first_product(driver)

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    name = wait_for_element(
        driver,
        (By.CLASS_NAME, "inventory_item_name")
    )

    assert name.text == "Sauce Labs Backpack"


# 8. Verify product price appears in cart
def test_cart_displays_product_price(driver):
    login(driver)
    add_first_product(driver)

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    price = wait_for_element(
        driver,
        (By.CLASS_NAME, "inventory_item_price")
    )

    assert price.text.startswith("$")


# 9. Verify product quantity is displayed
def test_cart_displays_product_quantity(driver):
    login(driver)
    add_first_product(driver)

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    quantity = wait_for_element(
        driver,
        (By.CLASS_NAME, "cart_quantity")
    )

    assert quantity.text == "1"


# 10. Verify product can be removed from cart
def test_remove_product_from_cart(driver):
    login(driver)
    add_first_product(driver)

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    wait_for_element(
        driver,
        (By.CLASS_NAME, "cart_item")
    )

    driver.find_element(
        By.ID,
        "remove-sauce-labs-backpack"
    ).click()

    assert len(get_cart_products(driver)) == 0


# 11. Verify cart badge updates after adding a product
def test_cart_badge_updates_after_adding(driver):
    login(driver)
    add_first_product(driver)

    badge = driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert badge.text == "1"


# 12. Verify cart badge updates after removing a product
def test_cart_badge_updates_after_removing(driver):
    login(driver)
    add_first_product(driver)

    driver.find_element(
        By.ID,
        "remove-sauce-labs-backpack"
    ).click()

    badges = driver.find_elements(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert len(badges) == 0


# 13. Verify cart badge counts multiple products
def test_cart_badge_counts_multiple_products(driver):
    login(driver)

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-bike-light"
    ).click()

    assert driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    ).text == "2"


# 14. Verify all added products appear in cart

# Check that all added products appear in cart
def test_all_added_products_appear_in_cart(driver):
    login(driver)

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bike-light"
    ).click()

    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    wait_for_element(
        driver, (By.CLASS_NAME, "cart_item")
    )

    cart_products = driver.find_elements(
        By.CLASS_NAME, "cart_item"
    )

    assert len(cart_products) == 2



# 15. Verify one product can be removed while another remains
def test_remove_one_product_from_multiple_items(driver):
    login(driver)

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-bike-light"
    ).click()

    driver.find_element(
        By.ID,
        "remove-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    products = get_cart_products(driver)

    assert len(products) == 1

    name = products[0].find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    )

    assert name.text == "Sauce Labs Bike Light"


# 16. Verify cart remains empty after removing all products
def test_cart_empty_after_removing_all_products(driver):
    login(driver)

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-bike-light"
    ).click()

    driver.find_element(
        By.ID,
        "remove-sauce-labs-backpack"
    ).click()

    driver.find_element(
        By.ID,
        "remove-sauce-labs-bike-light"
    ).click()

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    assert len(get_cart_products(driver)) == 0


# 17. Verify Continue Shopping button is displayed
def test_continue_shopping_button_displayed(driver):
    open_cart(driver)

    button = wait_for_element(
        driver,
        (By.ID, "continue-shopping")
    )

    assert button.is_displayed()
    assert button.is_enabled()


# 18. Verify Continue Shopping returns to products page
def test_continue_shopping_navigation(driver):
    open_cart(driver)

    driver.find_element(
        By.ID,
        "continue-shopping"
    ).click()

    assert "inventory" in driver.current_url


# 19. Verify Checkout button is displayed in cart
def test_checkout_button_displayed(driver):
    open_cart(driver)

    button = wait_for_element(
        driver,
        (By.ID, "checkout")
    )

    assert button.is_displayed()
    assert button.is_enabled()


# 20. Verify checkout button opens checkout information page

# 20. Checkout button navigation
def test_checkout_button_navigation(driver):
    login(driver)
    add_first_product(driver)

    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    checkout_button = wait_for_element(
        driver, (By.ID, "checkout")
    )

    assert checkout_button.is_displayed()
    assert checkout_button.is_enabled()

    checkout_button.click()

    wait_for_element(
        driver, (By.ID, "first-name")
    )

    assert "checkout-step-one" in driver.current_url

