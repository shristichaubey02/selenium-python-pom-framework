from pathlib import Path
import os

from jproperties import Properties


class ConfigFactory:

    def __init__(self, file_path="resources/config.properties"):
        self.path = Path(file_path)

        if not self.path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.path}"
            )

        self.configs = Properties()

        with self.path.open("rb") as config_file:
            self.configs.load(config_file)

    def fetch(self, key, default=None):
        value = os.getenv(key)

        if value is not None:
            return value

        item = self.configs.get(key)

        if item is None:
            if default is not None:
                return default

            raise KeyError(
                f"Missing configuration property: {key}"
            )

        return item[0]
# if __name__ == "__main__":

#     config = ConfigFactory()

#     print("URL:", config.fetch("BASE_URL"))
#     print("Browser:", config.fetch("BROWSER"))
#     print("Headless:", config.fetch("HEADLESS"))
#     print("Timeout:", config.fetch("TIMEOUT"))