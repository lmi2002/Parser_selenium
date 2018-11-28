from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
import os
import csv
import logging

from helper import logger
from properties.prop_driver import Driver
from properties.prop_csv import Csv


class PageObjectCaralarm(Driver):
    url = 'http://www.caralarm.com.ua/fo.php'

    def __init__(self):
        super().__init__()

    def open_site(self, url):
        return self.driver.get(url)

    def get_list_href_category(self):
        return list(set(item.get_attribute('href') for item in self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.box_category a')))))

    def select_all(self):
        Select(self.wait.until(EC.presence_of_element_located((By.ID, 'pl_onpage')))).select_by_index(2)

    def get_list_href_prod(self):
        return list(set(item.get_attribute('href') for item in self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.prod_info11 a')))))

    def get_href_image(self):
        el = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#big_image img')))
        return el.get_attribute('src')

    def get_name_item(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#description h1'))).text

    def get_num_and_brand(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.prod_info_25'))).text

    def get_description_full(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.prod_info_26'))).text

    def get_category(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'brdcrmb'))).text

    def get_li_property(self):
        try:
            self.wait = WebDriverWait(self.driver, 1)
            return self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"Характеристики")]')))
        except Exception:
            return False

    def get_text_property(self):
        table = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#tabs-2 tr')))
        return [tr.text for tr in table]


poc = PageObjectCaralarm()
obj_csv = Csv()

#poc.open_site(poc.url)

#list_href_category = poc.get_list_href_category()

#with open(r'C:\Users\anokhin\Desktop\caralarm\assortiment.txt', 'a') as f:
    #for href in list_href_category:
        #poc.open_site(href)
        #base_name = os.path.basename(href)
        #name_category = base_name.split('?')
        #poc.select_all()
        #time.sleep(30)
        #list_href_prod = poc.get_list_href_prod()
        #for item in list_href_prod:
            #f.write(item + '\n')

with open(r'C:\Users\anokhin\Desktop\caralarm\assortiment.txt', 'r', newline='') as f:
    while True:
        try:
            data = f.readline()

            poc.open_site(data)

            lst = []
            lst.append({'key': 'href', 'value': poc.get_href_image()})
            name_sym = poc.get_name_item()
            name = name_sym.replace('/', '$')
            lst.append({'key': 'name', 'value': name_sym})
            lst.append({'key': 'num_brand', 'value': poc.get_num_and_brand()})
            lst.append({'key': 'description_full', 'value': poc.get_description_full()})
            lst.append({'key': 'category', 'value': poc.get_category()})
            with open('C:\\Users\\anokhin\\Desktop\\caralarm\\product\\' + name + '.csv', 'w', newline='', errors='ignore') as csvfile:
                fieldnames = ['key', 'value']
                writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
                for row in lst:
                    writer.writerow(row)

            if poc.get_li_property():
                poc.get_li_property().click()
                with open('C:\\Users\\anokhin\\Desktop\\caralarm\\property\\' + name + '.csv', 'w', newline='', errors='ignore') as csvfile:
                    txt = poc.get_text_property()
                    for row in txt:
                        csvfile.writelines(row)

        except Exception as er:
            logging.basicConfig(filename=r'C:\Users\anokhin\Desktop\caralarm\error.txt', level=logging.INFO)
            logging.info(er)

