
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import (
    USERNAME,
    PASSWORD,
    LOCKED_USER,
    INVALID_PASSWORD
)

from utils.helpers import (
    login,
    get_error_message,
    wait_for_element
)


# 1. Verify login with valid credentials
def test_valid_login(driver):
    login(driver)

    assert "inventory" in driver.current_url


# 2. Verify login with an invalid username
def test_invalid_username(driver):
    login(driver, username="wrong_user", password=PASSWORD)

    assert "Username and password do not match" in get_error_message(driver)


# 3. Verify login with an invalid password
def test_invalid_password(driver):
    login(driver, username=USERNAME, password=INVALID_PASSWORD)

    assert "Username and password do not match" in get_error_message(driver)


# 4. Verify login with an empty username
def test_empty_username(driver):
    login(driver, username="", password=PASSWORD)

    assert get_error_message(driver) == "Epic sadface: Username is required"


# 5. Verify login with an empty password
def test_empty_password(driver):
    login(driver, username=USERNAME, password="")

    assert get_error_message(driver) == "Epic sadface: Password is required"


# 6. Verify login with both fields empty
def test_both_fields_empty(driver):
    login(driver, username="", password="")

    assert get_error_message(driver) == "Epic sadface: Username is required"


# 7. Verify login with a locked-out user
def test_locked_out_user(driver):
    login(driver, username=LOCKED_USER, password=PASSWORD)

    assert "Sorry, this user has been locked out" in get_error_message(driver)


# 8. Verify that the username is case-sensitive
def test_username_case_sensitivity(driver):
    login(driver, username="Standard_user", password=PASSWORD)

    assert "Username and password do not match" in get_error_message(driver)


# 9. Verify that the password is case-sensitive
def test_password_case_sensitivity(driver):
    login(driver, username=USERNAME, password="Secret_sauce")

    assert "Username and password do not match" in get_error_message(driver)


# 10. Verify login with leading and trailing spaces in username
def test_username_with_spaces(driver):
    login(driver, username=" " + USERNAME + " ", password=PASSWORD)

    assert "Username and password do not match" in get_error_message(driver)


# 11. Verify login with leading and trailing spaces in password
def test_password_with_spaces(driver):
    login(driver, username=USERNAME, password=" " + PASSWORD + " ")

    assert "Username and password do not match" in get_error_message(driver)


# 12. Verify that the password field hides entered characters
def test_password_field_is_masked(driver):
    driver.get("https://www.saucedemo.com/")

    password_field = wait_for_element(
        driver,
        (By.ID, "password")
    )

    assert password_field.get_attribute("type") == "password"


# 13. Verify that the login button is visible and enabled
def test_login_button_is_visible_and_enabled(driver):
    driver.get("https://www.saucedemo.com/")

    login_button = wait_for_element(
        driver,
        (By.ID, "login-button")
    )

    assert login_button.is_displayed()
    assert login_button.is_enabled()


# 14. Verify that the login error message can be closed
def test_error_message_can_be_closed(driver):
    login(driver, username="wrong_user", password=PASSWORD)

    close_button = wait_for_element(
        driver,
        (By.CSS_SELECTOR, "[data-test='error-button']")
    )

    close_button.click()

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )


# 15. Verify the login page title
def test_login_page_title(driver):
    driver.get("https://www.saucedemo.com/")

    assert driver.title == "Swag Labs"
