import re
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from properties.prop_driver import Driver
from base_function import helper


class PageObjectAvtopro(Driver):

    url = 'https://avto.pro/'

    def __init__(self):
        super().__init__()

    def open_site(self):
        return self.driver.get(self.url)

    def get_search_query(self):
        return self.driver.find_element_by_id('ap-search-query')

    def get_choice_num(self, brand_exist):
        brand_exist = brand_exist
        brand_no_sym = helper.delete_all_spec_symbol(brand_exist)

        list_brand = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[2]/span/span")))

        for brand in list_brand:
            brand_avtopro = brand.text
            brand_avtopro_no_sym = helper.delete_all_spec_symbol(brand_avtopro)
            if re.search(brand_no_sym[0], brand_avtopro_no_sym[0], re.I):
                brand.click()
                break






r = PageObjectAvtopro()
r.open_site()
r.maximize_window()
r.get_search_query().send_keys(12345)
time.sleep(3)
r.get_choice_num('Feb')
time.sleep(3)
r.close()


