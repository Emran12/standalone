
from selenium import webdriver
from selenium.webdriver.common.by import By

from scroll_page import ScrollPage


class AmazonElectronics(ScrollPage):
    def __init__(self):
        self.driver = webdriver.Firefox()
        super().__init__(self.driver)

    def scrape_electronics_info(self):
        url = 'https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456&ref' \
              '=nav_em__nav_desktop_sa_intl_computer_accessories_and_peripherals_0_2_6_2'
        self.driver.get(url)
        self.scroll_to_bottom()
        products_element = self.driver.find_elements(By.XPATH, "//div[@class='a-section a-spacing-base']")
        print(len(products_element))
        for product_element in products_element:
            innertext = product_element.get_attribute('innerText')
            print(innertext)
        self.driver.close()


amazon_electronics = AmazonElectronics()
amazon_electronics.scrape_electronics_info()
