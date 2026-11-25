
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import login, wait_for_element


# Helper function to open the menu
def open_menu(driver):
    login(driver)

    wait_for_element(
        driver,
        (By.CLASS_NAME, "inventory_list")
    )

    driver.find_element(
        By.ID,
        "react-burger-menu-btn"
    ).click()

    wait_for_element(
        driver,
        (By.ID, "inventory_sidebar_link")
    )


# 1. Verify menu button is displayed and enabled
def test_menu_button_displayed_and_enabled(driver):
    login(driver)

    menu_button = wait_for_element(
        driver,
        (By.ID, "react-burger-menu-btn")
    )

    assert menu_button.is_displayed()
    assert menu_button.is_enabled()


# 2. Verify menu opens successfully
def test_menu_opens(driver):
    open_menu(driver)

    menu = wait_for_element(
        driver,
        (By.CLASS_NAME, "bm-menu")
    )

    assert menu.is_displayed()


# 3. Verify All Items menu link navigates to products
def test_all_items_navigation(driver):
    open_menu(driver)

    driver.find_element(
        By.ID,
        "inventory_sidebar_link"
    ).click()

    assert "inventory" in driver.current_url


# 4. Verify About menu link is displayed and enabled
def test_about_link_displayed_and_enabled(driver):
    open_menu(driver)

    about_link = wait_for_element(
        driver,
        (By.ID, "about_sidebar_link")
    )

    assert about_link.is_displayed()
    assert about_link.is_enabled()


# 5. Verify Logout menu link returns to login page
def test_logout_from_menu(driver):
    open_menu(driver)

    driver.find_element(
        By.ID,
        "logout_sidebar_link"
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "login-button")
        )
    )

    assert "saucedemo.com" in driver.current_url
    assert driver.find_element(
        By.ID,
        "login-button"
    ).is_displayed()
