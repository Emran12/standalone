
import time

import pandas as pd
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SpeakerScraper:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def scrape_speakers(self):
        url = 'https://www.synbiobeta.com/attend/synbiobeta-2023/speakers'
        self.driver.get(url)
        i = 1
        while i < 15:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)
            i += 1
        speakers_xpath = "//div[@class='speakers-collection w-dyn-list']" \
                         "//div[@class='collection-list-13 w-dyn-items w-row']" \
                         "//div[@class='collection-item-16 w-dyn-item w-col w-col-3']//a"
        speaker_elements = self.driver.find_elements(By.XPATH, speakers_xpath)
        print(len(speaker_elements))
        data = {
            'Speaker Name': [],
            'Speaker Title': [],
            'Company Name': []
        }

        for index in range(0, len(speaker_elements), 2):
            element = speaker_elements[index]
            print("element------------", element)
            self.driver.execute_script("arguments[0].setAttribute('target', '_blank');", element)
            print("speaker element--------------------------", index, element)
            link_url = element.get_attribute('href')
            print("href-----------", link_url)
            self.driver.execute_script("window.open(arguments[0], '_blank');", link_url)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            wait = WebDriverWait(self.driver, 10)
            speaker_name_element = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='master-section wf-section']//h1[@class='speaker-headline']")))
            speaker_title_element = self.driver.find_element(By.XPATH,
                                                             "//div[@class='master-section wf-section']//div[contains(@class, 'job-title')]")
            company_name_element = self.driver.find_element(By.XPATH,
                                                            "//div[@class='master-section wf-section']//div[@class='company-name']")
            speaker_name = speaker_name_element.text
            speaker_title = speaker_title_element.text
            company_name = company_name_element.text
            print('speaker name', speaker_name)
            print('speaker title', speaker_title)
            print('company name', company_name)
            data['Speaker Name'].append(speaker_name)
            data['Speaker Title'].append(speaker_title)
            data['Company Name'].append(company_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        df = pd.DataFrame(data)

        # Write the DataFrame to an Excel file
        df.to_excel('speaker_details.xlsx', index=False)

        self.driver.close()


scraper = SpeakerScraper()
scraper.scrape_speakers()

