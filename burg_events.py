
import time

import pandas as pd
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from scroll_page import ScrollPage


class EventsScraper(ScrollPage):
    def __init__(self):
        self.driver = webdriver.Firefox()
        super().__init__(self.driver)

    def scrape_burg_events(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            url = 'https://ilovetheburg.com/events/'
            self.driver.get(url)
            self.scroll_to_bottom()
            wait.until(ec.element_to_be_clickable((By.XPATH,
                                                   "(//nav[@class='tribe-events-calendar-list-nav tribe-events-c-nav']//ul//li//a)[1]"))).click()
            wait.until(ec.staleness_of(self.driver.find_element(By.XPATH,
                                                                "(//nav[@class='tribe-events-calendar-list-nav tribe-events-c-nav']//ul//li//a)[1]")))

            self.scroll_to_bottom()
            time.sleep(5)
        except TimeoutException as e:
            print(str(e))
        self.driver.close()


scraper = EventsScraper()
scraper.scrape_burg_events()

