import time

import pandas as pd
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
        i = 1
        data = []
        while i <= 400:
            self.scroll_to_bottom()
            products_element = self.driver.find_elements(By.XPATH, "//div[@class='a-section a-spacing-base']")
            print(len(products_element))
            time.sleep(15)
            self.get_product_details(products_element, data)
            df = pd.DataFrame(data, columns=["Product Name", "Price", "Ratings", "Reviews"])
            df.to_excel("amazon_electronics_info.xlsx", index=False)
            self.driver.find_element(By.XPATH, "//a[@class='s-pagination-item s-pagination-next"
                                               " s-pagination-button s-pagination-separator']").click()
            print("page No:--------------------", i)
            i += 1
        self.driver.close()

    @staticmethod
    def get_product_details(products_element, data):
        print("product details ---------------------------------")
        for index in range(0, (len(products_element)) - 1):
            try:
                name = products_element[index].find_element(By.TAG_NAME, 'h2').text
                ratings = products_element[index].find_element(By.XPATH,
                                                               f"(//span[@class = 'a-icon-alt'])[{index + 1}]").get_attribute(
                    'innerText')
                reviews = products_element[index].find_element(By.XPATH,
                                                               f"(//span[@class = 'a-size-base s-underline-text'])[{index + 1}]").get_attribute(
                    'innerText')
                price = products_element[index].find_element(By.XPATH, f"(//span[@class = 'a-price'])[{index + 1}]") \
                    .text.replace('\n', '.')
                print("product name", name)
                print("product ratings", ratings)
                print("reviews", reviews)
                print("Price", price)
                data.append([name, price, ratings, reviews])
            except Exception as e:
                print("an error occurred as", e)


amazon_electronics = AmazonElectronics()
amazon_electronics.scrape_electronics_info()
