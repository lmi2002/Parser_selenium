from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from properties.prop_driver import Driver


class PageObjectPartsRightToyota(Driver):

    url = 'https://parts.righttoyota.com/'

    def __init__(self):
        super().__init__()

    def open_site(self, url):
        return self.driver.get(url)

    def get_input(self):
        try:
            return self.wait.until(EC.presence_of_element_located((By.ID, 'main_search_2')))
        except:
            return False

    def get_submit(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//form[@id='search-box']/button/i)[2]")))

    def get_secondary_images(self):
        try:
            return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'secondary-images')))
        except:
            return False

    def get_main_image(self):
        try:
            return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.main-image > a img')))
        except:
            return False

    def get_product_details_inner(self):
        try:
            return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-details-inner')))
        except:
            return False

    def get_no_results_found(self):
        try:
            self.default_timeout = 5
            return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.no-results-found')))
        except:
            return False

    def get_product_title_module(self):
        try:
            return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-title-module > h1')))
        except:
            return False

