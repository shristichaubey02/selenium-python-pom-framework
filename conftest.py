import os

import pytest

from utils.config_factory import ConfigFactory
from utils.driver_factory import DriverFactory


@pytest.fixture
def config():
    return ConfigFactory()


@pytest.fixture
def driver(config):
    driver = DriverFactory(config).get_driver()

    driver.get(config.fetch("BASE_URL"))

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_name = (
                f"screenshots/{item.name}.png"
            )

            driver.save_screenshot(screenshot_name)

            print(
                f"\nScreenshot saved: {screenshot_name}"
            )