from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def enter_customer_information(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        self.wait.until(
            EC.url_contains("checkout-step-two")
        )

    def click_finish(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        self.wait.until(
            EC.url_contains("checkout-complete")
        )

    def get_confirmation_message(self):
        return self.get_text(self.COMPLETE_HEADER)