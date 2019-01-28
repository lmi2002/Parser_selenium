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
import urllib.request

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

    def get_main_image(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.main-image > a img')))

    def get_product_details_inner(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-details-inner')))


if __name__ == "__main__":

    # add path to save images
    path_to_save_img = 'C:\\Users\\anokhin\\Desktop\\'
    art = '43512-06150'
    pop = PageObjectPartsRightToyota()
    pop.open_site(pop.url)
    pop.maximize_window()
    pop.get_input().send_keys(art)
    pop.get_input().send_keys(Keys.ENTER)

    secondary_images = pop.get_secondary_images()

    images_list = [img.get_attribute('src') for img in secondary_images.find_elements_by_css_selector('li > a img')]

    # save to folder img
    for ind, href_img in enumerate(images_list, start=1):
        urllib.request.urlretrieve(href_img, path_to_save_img + art + '_' + str(ind) +
                                   href_img[href_img.rfind("."):])

    # save to folder main_img
    main_image = pop.get_main_image().get_attribute('src')
    urllib.request.urlretrieve(main_image, path_to_save_img + art + '_' + str(0) +
                               href_img[href_img.rfind("."):])

    product_details = pop.get_product_details_inner()

    for detail in product_details.find_elements_by_css_selector('li'):
            print(detail.find_element_by_css_selector('label').text)
            print(detail.find_element_by_css_selector('span').text)





pop.close()