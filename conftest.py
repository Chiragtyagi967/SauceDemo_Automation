from pathlib import Path
import re

import pytest
import pytest_html

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


SCREENSHOT_DIR = Path(__file__).parent / "screenshots"


@pytest.fixture
def driver():
    options = Options()

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
    )

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver is not None:
            SCREENSHOT_DIR.mkdir(exist_ok=True)

            safe_name = re.sub(
                r"[^a-zA-Z0-9_-]",
                "_",
                item.nodeid
            )

            screenshot_path = (
                SCREENSHOT_DIR / f"{safe_name}.png"
            )

            try:
                driver.save_screenshot(str(screenshot_path))

                report.extras = getattr(report, "extras", [])
                report.extras.append(
                    pytest_html.extras.image(
                        str(screenshot_path),
                        mime_type="image/png",
                        name="Failure Screenshot"
                    )
                )

            except Exception as error:
                print(f"Could not save failure screenshot: {error}")