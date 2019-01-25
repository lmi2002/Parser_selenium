from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os
import csv
import logging
from functools import reduce

from helper import logger
from properties.prop_driver import Driver
from properties.prop_csv import Csv


class PageObjectPartsRightToyota(Driver):

    url = 'https://parts.righttoyota.com/'

    def __init__(self):
        super().__init__()

    def open_site(self, url):
        return self.driver.get(url)

    def get_input(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, 'main_search_2')))

    def get_submit(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[@id='search-box']/button/i)[2]")))

    def get_secondary_images(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'secondary-images')))


if __name__ == "__main__":

    pop = PageObjectPartsRightToyota()
    pop.open_site(pop.url)
    pop.maximize_window()
    pop.get_input().send_keys('43512-06150')
    pop.get_input().send_keys(Keys.ENTER)
    print(pop.get_secondary_images())


