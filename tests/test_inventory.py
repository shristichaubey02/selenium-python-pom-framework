from data.test_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    CUSTOMER_FIRST_NAME,
    CUSTOMER_LAST_NAME,
    CUSTOMER_POSTAL_CODE,
    PRODUCT_NAME,
)

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_backpack_to_cart(driver, config):

    timeout = int(config.fetch("TIMEOUT", "10"))

    login_page = LoginPage(driver, timeout)
    inventory_page = InventoryPage(driver, timeout)
    cart_page = CartPage(driver, timeout)
    checkout_page = CheckoutPage(driver, timeout)

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    inventory_page.add_product(PRODUCT_NAME)

    inventory_page.open_cart()

    assert "cart" in driver.current_url

    cart_page.click_checkout()

    assert "checkout-step-one" in driver.current_url

    checkout_page.enter_customer_information(
        CUSTOMER_FIRST_NAME,
        CUSTOMER_LAST_NAME,
        CUSTOMER_POSTAL_CODE
    )

    checkout_page.click_continue()
    checkout_page.click_finish()

    assert (
        checkout_page.get_confirmation_message()
        == "Thank you for your order!"
    )