
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import BASE_URL, USERNAME, PASSWORD


WAIT_TIME = 10


def wait_for_element(driver, locator):
    return WebDriverWait(driver, WAIT_TIME).until(
        EC.visibility_of_element_located(locator)
    )


def click_element(driver, locator):
    element = WebDriverWait(driver, WAIT_TIME).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()


def enter_text(driver, locator, text):
    element = wait_for_element(driver, locator)
    element.clear()
    element.send_keys(text)


def login(driver, username=USERNAME, password=PASSWORD):
    driver.get(BASE_URL)

    enter_text(
        driver,
        (By.ID, "user-name"),
        username
    )

    enter_text(
        driver,
        (By.ID, "password"),
        password
    )

    click_element(
        driver,
        (By.ID, "login-button")
    )


def logout(driver):
    click_element(
        driver,
        (By.ID, "react-burger-menu-btn")
    )

    click_element(
        driver,
        (By.ID, "logout_sidebar_link")
    )


def get_error_message(driver):
    error = wait_for_element(
        driver,
        (By.CSS_SELECTOR, "[data-test='error']")
    )
    return error.text
