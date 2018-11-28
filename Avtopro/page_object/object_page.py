import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from properties.prop_driver import Driver
from helper import base_func


class PageObjectAvtopro(Driver):
    url = 'https://avto.pro/'

    header = ['Производитель', 'Код', 'Описание', 'Цена,ГРН']

    def __init__(self):
        super().__init__()

    def open_site(self):
        return self.driver.get(self.url)

    def get_search_query(self):
        return self.driver.find_element_by_id('ap-search-query')

    def get_element_no_found(self):
        self.default_timeout = 4
        try:
            return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "LWFNSBrEZM8occTp6tJPU")))
        except Exception:
            return None

    def get_choice_num(self, brand_exist):
        try:
            brand_exist = brand_exist
            brand_no_sym = base_func.delete_all_spec_symbol(brand_exist)

            list_brand = self.wait.until(
                EC.presence_of_all_elements_located((
                    By.XPATH, "//div[@class='_1a3Xi3YWVfR_VZuP6CmJIS']/span/span")))

            for brand in list_brand:
                brand_avtopro = brand.text
                brand_avtopro_no_sym = base_func.delete_all_spec_symbol(brand_avtopro)
                if re.search(brand_no_sym[0], brand_avtopro_no_sym[0], re.I):
                    return brand
            else:
                return None
        except Exception:
            return None

    def get_table(self):
        return self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//table[@id='js-partslist-primary']/tbody/tr")))

    def record_to_file_csv(self, table):
        lst = []
        keys = ['Производитель', 'Код', 'Описание', 'Цена,ГРН']
        dct_key = dict.fromkeys(keys)

        for tr in table:
            dct_value = [td.text for idx, td in enumerate(tr.find_elements_by_xpath('td'), start=1) if
                         idx in (1, 2, 3, 5)]
            dct = dict(zip(dct_key, dct_value))
            lst.append(dct)
        return lst

    def page_404(self):
        if '404' in self.driver.title:
            return True

    def get_el_refer_to_main(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".er_text a")))
