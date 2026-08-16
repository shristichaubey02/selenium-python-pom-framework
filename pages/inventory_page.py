from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):

    CART_BUTTON = (By.CSS_SELECTOR, "a.shopping_cart_link")

    def add_product(self, product_name):
        product_id = product_name.lower().replace(" ", "-")

        locator = (
            By.ID,
            f"add-to-cart-{product_id}"
        )

        self.click(locator)

    def open_cart(self):
        cart = self.wait.until(
            EC.element_to_be_clickable(self.CART_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            cart
        )