from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class ScrollPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_bottom(self):
        while True:
            current_height = self.driver.execute_script("return document.body.scrollHeight")

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            while True:
                current_height = self.driver.execute_script("return document.body.scrollHeight")

                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

                try:
                    WebDriverWait(self.driver, 3).until(
                        lambda _: self.driver.execute_script("return document.body.scrollHeight") != current_height
                    )
                except TimeoutException:
                    break

                new_height = self.driver.execute_script("return document.body.scrollHeight")

                if new_height == current_height:
                    break

            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == current_height:
                break
