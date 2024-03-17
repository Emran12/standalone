import multiprocessing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from openpyxl import Workbook
from multiprocessing import Manager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Function to scrape doctor's data from a page
def scrape_data(url, workbook, completed_pages):
    options = Options()
    options.headless = True  # Run Firefox in headless mode
    driver = webdriver.Firefox(options=options)

    driver.get(url)

    # Extract doctors' names and designations from the page
    try:
        names = driver.find_elements(By.XPATH, "//div[@class='doctor-container']//a[@class='search-item-doctor-name']")
        designations = driver.find_elements(By.XPATH, "//div[@class='doctor-container']//a[@class='search-item-specialty-text']")

        for name, designation in zip(names, designations):
            print(f"Name: {name.text}")
            print(f"Designation: {designation.text}")
            print("--------")
            workbook.active.append([name.text, designation.text])

    except NoSuchElementException:
        print("Error: Element not found on the page")

    driver.quit()
    completed_pages.append(url)


# Main function
def main():
    base_url = "https://www.ratemds.com/best-doctors/?page="
    num_pages = 200  # Total number of pages to scrape
    num_processes = multiprocessing.cpu_count()  # Number of processes to use

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Doctors Information"
    manager = Manager()
    completed_pages = manager.list()

    pool = multiprocessing.Pool(processes=num_processes)
    urls = [base_url + str(page) for page in range(1, num_pages + 1)]
    pool.starmap(scrape_data, [(url, workbook, completed_pages) for url in urls])
    pool.close()
    pool.join()
    workbook.save("doctors_data.xlsx")
    print("Completed Pages:", completed_pages)



# Execute the main function
if __name__ == "__main__":
    main()

#
#
# import time
# import concurrent.futures
# import pandas as pd
#
# from selenium import webdriver
# from selenium.common import StaleElementReferenceException, NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
#
# total_pages = 200
# num_processes = 100
#
#
# class SpecialistDoctors:
#     def __init__(self):
#         options = Options()
#         self.driver = webdriver.Firefox(service=Service(), options=options)
#
#     def scrape_pages(self, start_page, end_page):
#         data = []  # Initialize an empty list to store scraped data
#         for page in range(start_page, end_page + 1):
#             url = f"https://www.ratemds.com/best-doctors/?page={page}"
#             data.extend(self.fetch_data(url))  # Append the scraped data to the list
#
#         return data  # Return the data list for the current range of pages
#
#     def fetch_data(self, url):
#         print("url-------", url)
#         self.driver.get(url)
#         doctors_element = self.driver.find_elements(By.CLASS_NAME, 'doctor-container')
#         print(len(doctors_element))
#
#         data = []
#         for doctor in doctors_element:
#             retries = 3  # Number of retries for each element
#             while retries > 0:
#                 try:
#                     name = doctor.find_element(By.TAG_NAME, 'a').text
#                     designation = doctor.find_element(By.CLASS_NAME, 'search-item-specialty-text').text
#                     data.append({'Name': name, 'Designation': designation})  # Store the data as a dictionary
#                     break  # Break out of the retry loop if successful
#                 except (StaleElementReferenceException, NoSuchElementException):
#                     retries -= 1
#                     time.sleep(1)
#         return data  # Return the data list for the current page
#
#     def test(self):
#         with concurrent.futures.ThreadPoolExecutor(max_workers=num_processes) as executor:
#             pages_per_process = total_pages // num_processes
#             start_page = 1
#
#             futures = []
#             for _ in range(num_processes):
#                 end_page = start_page + pages_per_process - 1
#                 futures.append(executor.submit(self.scrape_pages, start_page, end_page))
#                 start_page = end_page + 1
#             # Wait for all tasks to complete
#             concurrent.futures.wait(futures)
#
#             # Retrieve the scraped data from the completed futures
#             scraped_data = []
#             for future in futures:
#                 scraped_data.extend(future.result())
#
#         self.driver.close()
#
#         # Export the scraped data to an Excel sheet
#         df = pd.DataFrame(scraped_data)
#         df.to_excel('specialist_doctors.xlsx', index=False)
#
#
# specialist_doctors = SpecialistDoctors()
# specialist_doctors.test()

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
#
# from scroll_page import ScrollPage
#
# class SpecialistDoctors(ScrollPage):
#     def __init__(self):
#         options = Options()
#         # options.add_argument('-headless')
#         options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0")
#         self.driver = webdriver.Firefox(service=Service(), options=options)
#         super().__init__(self.driver)
#
#     def test(self):
#         batch_size = 1000  # Number of pages to scrape in each batch
#         total_pages = 2  # Total number of pages to scrape
#
#         num_batches = (total_pages // batch_size) + 1
#         for batch_number in range(1, num_batches + 1):
#             start_page = (batch_number - 1) * batch_size + 1
#             end_page = min(batch_number * batch_size, total_pages)
#
#             print(f"Scraping batch {batch_number} of pages {start_page} to {end_page}")
#             for page_number in range(start_page, end_page + 1):
#                 url = f"https://www.ratemds.com/best-doctors/?page={page_number}"
#                 self.fetch_data(url)
#
#                 # Introduce a delay between consecutive page scrapes
#                 time.sleep(5)
#
#         self.driver.close()
#
#     def fetch_data(self, url):
#         print("URL:", url)
#         self.driver.get(url)
#         self.scroll_to_bottom()
#
#         # Rest of the code to scrape the data from the page
#
#         # Example code:
#         doctors_element = self.driver.find_elements(By.CLASS_NAME, 'doctor-container')
#         print(len(doctors_element))
#
#         wait = WebDriverWait(self.driver, 10)
#         for doctor in doctors_element:
#             name = doctor.find_element(By.TAG_NAME, 'a').text
#             designation = doctor.find_element(By.CLASS_NAME, 'search-item-specialty-text').text
#             address = doctor.find_element(By.XPATH, "./div[contains(@class, 'doctor-address')]").text
#             reviews = doctor.find_element(By.XPATH,
#                                           "(./div[@class='review-container ']//span[@class='reviews']//span)[4]").text
#             latest_comment = doctor.find_element(By.CLASS_NAME, "rating-comment").get_attribute('innerText').replace(
#                 "Read Full Review", "")
#             print(name)
#             print(designation)
#             print(address)
#             print(reviews)
#             print(latest_comment)
#
#
# specialist_doctors = SpecialistDoctors()
# specialist_doctors.test()
