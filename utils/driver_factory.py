from selenium import webdriver

from utils.config_factory import ConfigFactory


class DriverFactory:

    def __init__(self, config):
        self.config = config

    def get_driver(self):

        browser = self.config.fetch("BROWSER").lower()

        headless = self.config.fetch(
            "HEADLESS",
            "false"
        ).lower() == "true"

        if browser == "chrome":

            options = webdriver.ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":

            options = webdriver.FirefoxOptions()

            if headless:
                options.add_argument("-headless")

            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

            driver = webdriver.Firefox(options=options)

        else:
            raise ValueError(
                f"Unsupported browser: {browser}"
            )

        return driver
    
# if __name__ == "__main__":

#     config = ConfigFactory()

#     driver = DriverFactory(config).get_driver()

#     driver.get(config.fetch("BASE_URL"))

#     input("Press Enter to close the browser...")

#     driver.quit()