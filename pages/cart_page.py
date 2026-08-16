from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class CartPage(BasePage):

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

        WebDriverWait(
            self.driver,
            self.timeout
        ).until(
            lambda driver: "checkout-step-one" in driver.current_url
        )