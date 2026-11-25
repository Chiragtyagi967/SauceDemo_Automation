
from selenium.webdriver.common.by import By
from utils.helpers import login, wait_for_element


def open_products_page(driver):
    login(driver)
    wait_for_element(driver, (By.CLASS_NAME, "inventory_list"))


def get_social_link(driver, platform):
    links = driver.find_elements(
        By.CSS_SELECTOR, ".social a"
    )

    for link in links:
        href = (link.get_attribute("href") or "").lower()

        if platform in href:
            return link

    return None


# 1. Footer is displayed
def test_footer_displayed(driver):
    open_products_page(driver)

    footer = wait_for_element(
        driver, (By.CLASS_NAME, "footer")
    )

    assert footer.is_displayed()


# 2. Footer contains copyright text
def test_footer_copyright_text(driver):
    open_products_page(driver)

    copyright_text = wait_for_element(
        driver, (By.CLASS_NAME, "footer_copy")
    )

    assert copyright_text.is_displayed()
    assert "Sauce Labs" in copyright_text.text


# 3. Twitter link is displayed

# 3. Twitter / X link is displayed
def test_twitter_link_displayed(driver):
    open_products_page(driver)

    links = driver.find_elements(
        By.CSS_SELECTOR, ".social a"
    )

    twitter_link = None

    for link in links:
        href = (link.get_attribute("href") or "").lower()

        if "twitter.com" in href or "x.com" in href:
            twitter_link = link
            break

    assert twitter_link is not None, "Twitter/X link was not found"
    assert twitter_link.is_displayed()



# 4. Facebook link is displayed
def test_facebook_link_displayed(driver):
    open_products_page(driver)

    facebook = get_social_link(driver, "facebook")

    assert facebook is not None, "Facebook link was not found"
    assert facebook.is_displayed()


# 5. LinkedIn link is displayed
def test_linkedin_link_displayed(driver):
    open_products_page(driver)

    linkedin = get_social_link(driver, "linkedin")

    assert linkedin is not None, "LinkedIn link was not found"
    assert linkedin.is_displayed()
