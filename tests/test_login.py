from pages.login_page import LoginPage


def test_valid_login(driver, config):
    timeout = int(config.fetch("TIMEOUT", "10"))

    login_page = LoginPage(driver, timeout)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory" in driver.current_url
    # assert "THIS_WILL_FAIL" in driver.current_url

def test_invalid_login(driver, config):

    timeout = int(config.fetch("TIMEOUT", "10"))

    login_page = LoginPage(driver, timeout)

    login_page.login(
        "invalid_user",
        "wrong_password"
    )

    error_message = login_page.get_error_message()

    assert "Username and password do not match" in error_message