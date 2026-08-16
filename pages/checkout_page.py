from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)

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
        self.click(self.CONTINUE_BUTTON)

        WebDriverWait(
            self.driver,
            self.timeout
        ).until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

        WebDriverWait(
            self.driver,
            self.timeout
        ).until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        )

    def get_confirmation_message(self):
        return self.get_text(self.COMPLETE_HEADER)