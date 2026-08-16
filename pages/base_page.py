from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    def click(self, locator):
        element = WebDriverWait(
            self.driver,
            self.timeout
        ).until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    def type_text(self, locator, text):
        element = WebDriverWait(
            self.driver,
            self.timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = WebDriverWait(
            self.driver,
            self.timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

        return element.text