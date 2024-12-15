"""
asd
"""

import time
# from bs4 import BeautifulSoup, PageElement
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://vplates.com.au/"
# BASE_URL = "https://vplates.com.au/create/check-combination"


def check_combo_availability(driver: webdriver, combo: str):
    input_box = driver.find_element(By.ID, "quick-combo__combo")
    input_box.send_keys(combo)
    button = driver.find_element(By.CLASS_NAME, "quick-combo__submit")
    button.click()

    # time.sleep(5)

    # WebDriverWait(driver, 10).until(
    #     EC.text_to_be_present_in_element(
    #         locator=(By.CLASS_NAME, "quick-combo__title"),
    #         text_="available"
    #     )
    # )

    # result_raw = driver.find_element(By.CLASS_NAME, "quick-combo__title").text
    # print(f"{result_raw=}")


    max_wait_time = 20
    for _ in range(max_wait_time):
        time.sleep(1)

        result_raw = driver.find_element(By.CLASS_NAME, "quick-combo__title").text
        print(f"{result_raw=}")

        if "available" in result_raw:

            ### Reset for the next check
            button = driver.find_element(By.CLASS_NAME, "quick-combo__reset")
            button.click()

            break

    result = result_raw == "This combo is unavailable."
    print(f"{result=}")

    return result



def main():

    ### Boilerplate
    ff_opts = FirefoxOptions()
    ff_opts.add_argument('-headless')

    driver = webdriver.Firefox(
        service=Service(executable_path="/usr/local/bin/geckodriver"),
        options=ff_opts,
    )
    driver.get(BASE_URL)



    ### Submit form
    # input_box = driver.find_element(By.CLASS_NAME, "class name")
    # input_box.send_keys("IS003")
    is_001_available = check_combo_availability(driver, "IS001") ### Not available
    is_003_available = check_combo_availability(driver, "IS003") ### Available

    print(f"{is_001_available=}")
    print(f"{is_003_available=}")



    ### SOUP
    # soup = BeautifulSoup(
    #     markup=driver.page_source,
    #     features="html.parser"
    # )

    # # # soup.get("quick-combo__title")
    # # element = soup.find(class_='quick-combo__title')
    # # print(element.text.strip())

    # input_box = soup.find(class_="quick-combo__combo")
    # input_box.

    # check_availability_button = soup.find(class_="quick-combo__submit")






    ### TODO: copy generation code from phone





if __name__ == "__main__":
    main()
