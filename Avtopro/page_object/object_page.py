import re
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


from properties.prop_driver import Driver
from base_function import func


class PageObjectAvtopro(Driver):

    url = 'https://avto.pro/'

    def __init__(self):
        super().__init__()

    def open_site(self):
        return self.driver.get(self.url)

    def get_search_query(self):
        return self.driver.find_element_by_id('ap-search-query')

    def get_choice_num(self, brand):
        brand_no_sym = func.delete_all_spec_symbol(brand)
        brand_lower = func.lower_register(brand_no_sym[0])

        list_brand = [el for el in self.driver.find_elements_by_xpath('//div[2]/span/span')]

        for brand_avtopro in list_brand:
            brand_avtopro_no_sym = func.delete_all_spec_symbol(brand_avtopro.text)
            brand_avtopro_lower = func.lower_register(brand_avtopro_no_sym[0])
            if brand_lower == brand_avtopro_lower:
                self.driver.find_element_by_xpath('//div[2]/span/span').click()
                print()



r = PageObjectAvtopro()
r.open_site()
r.maximize_window()
r.get_search_query().send_keys(12345)
time.sleep(3)
r.get_choice_num('Febi')
time.sleep(3)
r.close()


