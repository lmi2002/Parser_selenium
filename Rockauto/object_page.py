import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from properties.prop_driver import Driver


class PageObjectRockauto(Driver):


    def __init__(self):
        super().__init__()

    def open_site(self, url):
        return self.driver.get(url)

    def get_href(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'2019')")))




por = PageObjectRockauto()

por.open_site('https://www.rockauto.com/en/catalog/bmw')
els = por.get_href()
els
for el in els:
    print(el.get_attribute('href'))

por.close()