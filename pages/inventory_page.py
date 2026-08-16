from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):

    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    def add_product(self, product_name):
        product_id = product_name.lower().replace(" ", "-")

        locator = (
            By.ID,
            f"add-to-cart-{product_id}"
        )

        self.click(locator)

    def open_cart(self):
        self.click(self.CART_BUTTON)

        WebDriverWait(
            self.driver,
            self.timeout
        ).until(
            EC.url_contains("cart.html")
        )