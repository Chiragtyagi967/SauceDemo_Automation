\
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait

from utils.helpers import login, wait_for_element


# Helper function to open the products page
def open_products_page(driver):
    login(driver)

    wait_for_element(
        driver,
        (By.CLASS_NAME, "inventory_list")
    )


# Helper function to get all product cards
def get_products(driver):
    return driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )


# Helper function to get product names
def get_product_names(driver):
    return [
        product.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        ).text
        for product in get_products(driver)
    ]


# Helper function to get product prices
def get_product_prices(driver):
    return [
        float(
            product.find_element(
                By.CLASS_NAME,
                "inventory_item_price"
            ).text.replace("$", "")
        )
        for product in get_products(driver)
    ]


# Helper function to select sorting option
def select_sort_option(driver, value):
    dropdown = wait_for_element(
        driver,
        (By.CLASS_NAME, "product_sort_container")
    )

    Select(dropdown).select_by_value(value)

    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(
            By.CLASS_NAME,
            "product_sort_container"
        ).get_attribute("value") == value
    )


# 1. Verify products page loads successfully
def test_products_page_loads(driver):
    open_products_page(driver)

    assert "inventory" in driver.current_url


# 2. Verify products heading is displayed
def test_products_heading_displayed(driver):
    open_products_page(driver)

    heading = wait_for_element(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert heading.text == "Products"


# 3. Verify all six products are displayed
def test_all_six_products_displayed(driver):
    open_products_page(driver)

    assert len(get_products(driver)) == 6


# 4. Verify product names are displayed
def test_product_names_displayed(driver):
    open_products_page(driver)

    names = get_product_names(driver)

    assert len(names) == 6
    assert all(name.strip() for name in names)


# 5. Verify product prices are displayed
def test_product_prices_displayed(driver):
    open_products_page(driver)

    prices = get_product_prices(driver)

    assert len(prices) == 6
    assert all(price > 0 for price in prices)


# 6. Verify product descriptions are displayed
def test_product_descriptions_displayed(driver):
    open_products_page(driver)

    descriptions = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_desc"
    )

    assert len(descriptions) == 6
    assert all(item.text.strip() for item in descriptions)


# 7. Verify product images are displayed and loaded
def test_product_images_displayed(driver):
    open_products_page(driver)

    WebDriverWait(driver, 15).until(
        lambda d: len(
            d.find_elements(
                By.CSS_SELECTOR,
                ".inventory_item_img img"
            )
        ) == 6
    )

    WebDriverWait(driver, 15).until(
        lambda d: all(
            image.get_attribute("complete") == "true"
            and int(image.get_attribute("naturalWidth") or 0) > 0
            for image in d.find_elements(
                By.CSS_SELECTOR,
                ".inventory_item_img img"
            )
        )
    )

    images = driver.find_elements(
        By.CSS_SELECTOR,
        ".inventory_item_img img"
    )

    assert len(images) == 6

    for image in images:
        assert image.is_displayed()


# 8. Verify product add-to-cart buttons are displayed
def test_add_to_cart_buttons_displayed(driver):
    open_products_page(driver)

    buttons = driver.find_elements(
        By.CSS_SELECTOR,
        ".inventory_item button"
    )

    assert len(buttons) == 6

    for button in buttons:
        assert button.is_displayed()
        assert button.is_enabled()


# 9. Verify product prices are sorted from low to high
def test_sort_price_low_to_high(driver):
    open_products_page(driver)

    select_sort_option(driver, "lohi")

    prices = get_product_prices(driver)

    assert prices == sorted(prices)


# 10. Verify product prices are sorted from high to low
def test_sort_price_high_to_low(driver):
    open_products_page(driver)

    select_sort_option(driver, "hilo")

    prices = get_product_prices(driver)

    assert prices == sorted(prices, reverse=True)


# 11. Verify product names are sorted A to Z
def test_sort_name_a_to_z(driver):
    open_products_page(driver)

    select_sort_option(driver, "az")

    names = get_product_names(driver)

    assert names == sorted(names)


# 12. Verify product names are sorted Z to A
def test_sort_name_z_to_a(driver):
    open_products_page(driver)

    select_sort_option(driver, "za")

    names = get_product_names(driver)

    assert names == sorted(names, reverse=True)


# 13. Verify default product sorting is A to Z
def test_default_sorting_is_name_a_to_z(driver):
    open_products_page(driver)

    names = get_product_names(driver)

    assert names == sorted(names)


# 14. Verify sorting dropdown has four options
def test_sort_dropdown_has_four_options(driver):
    open_products_page(driver)

    dropdown = Select(
        wait_for_element(
            driver,
            (By.CLASS_NAME, "product_sort_container")
        )
    )

    assert len(dropdown.options) == 4


# 15. Verify default sorting option is selected
def test_default_sort_option_selected(driver):
    open_products_page(driver)

    dropdown = wait_for_element(
        driver,
        (By.CLASS_NAME, "product_sort_container")
    )

    assert dropdown.get_attribute("value") == "az"


# 16. Verify low-to-high sorting option is selected
def test_low_to_high_sort_option_selected(driver):
    open_products_page(driver)

    select_sort_option(driver, "lohi")

    dropdown = driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )

    assert dropdown.get_attribute("value") == "lohi"


# 17. Verify high-to-low sorting option is selected
def test_high_to_low_sort_option_selected(driver):
    open_products_page(driver)

    select_sort_option(driver, "hilo")

    dropdown = driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )

    assert dropdown.get_attribute("value") == "hilo"


# 18. Verify Z-to-A sorting option is selected
def test_z_to_a_sort_option_selected(driver):
    open_products_page(driver)

    select_sort_option(driver, "za")

    dropdown = driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )

    assert dropdown.get_attribute("value") == "za"


# 19. Verify product names are unique
def test_product_names_are_unique(driver):
    open_products_page(driver)

    names = get_product_names(driver)

    assert len(names) == len(set(names))


# 20. Verify product prices contain a dollar symbol
def test_product_prices_have_dollar_symbol(driver):
    open_products_page(driver)

    price_elements = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_price"
    )

    assert all(
        price.text.startswith("$")
        for price in price_elements
    )


# 21. Verify product descriptions are not empty
def test_product_descriptions_are_not_empty(driver):
    open_products_page(driver)

    descriptions = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_desc"
    )

    assert all(
        description.text.strip() != ""
        for description in descriptions
    )


# 22. Verify every product has an image source
def test_each_product_has_image_source(driver):
    open_products_page(driver)

    images = driver.find_elements(
        By.CSS_SELECTOR,
        ".inventory_item_img img"
    )

    assert len(images) == 6

    assert all(
        image.get_attribute("src")
        for image in images
    )


# 23. Verify product names are visible and enabled
def test_product_names_are_clickable(driver):
    open_products_page(driver)

    names = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item_name"
    )

    assert len(names) == 6

    for name in names:
        assert name.is_displayed()
        assert name.is_enabled()


# 24. Verify products page remains open after sorting
def test_products_page_remains_open_after_sorting(driver):
    open_products_page(driver)

    select_sort_option(driver, "hilo")

    assert "inventory" in driver.current_url
    assert len(get_products(driver)) == 6


# 25. Verify product cards contain complete information
def test_product_cards_contain_complete_information(driver):
    open_products_page(driver)

    products = get_products(driver)

    assert len(products) == 6

    for product in products:
        name = product.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        )

        description = product.find_element(
            By.CLASS_NAME,
            "inventory_item_desc"
        )

        price = product.find_element(
            By.CLASS_NAME,
            "inventory_item_price"
        )

        assert name.text.strip()
        assert description.text.strip()
        assert price.text.startswith("$")
