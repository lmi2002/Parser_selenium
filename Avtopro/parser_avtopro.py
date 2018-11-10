import time
from selenium.webdriver.common.keys import Keys

from Avtopro.page_object.object_page import PageObjectAvtopro
from properties.prop_csv import Csv

ob_csv = Csv()
poa = PageObjectAvtopro()

poa.open_site()
poa.maximize_window()

lst_from_ex = ob_csv.read_to_csv(r'C:\Users\anokhin\Desktop\KNS2018-11-06.csv')

for item in lst_from_ex:
    try:
        time.sleep(1)

        el_input = poa.get_search_query()
        el_input.send_keys(Keys.CONTROL + Keys.SHIFT + Keys.HOME)
        el_input.send_keys(Keys.DELETE)

        if '/' in item['num']:
            num = item['num'].replace('/', '$')
        else:
            num = item['num']

        if '/' in item['brand_ex']:
            brand_ex = item['brand_ex'].replace('/', '$')
        else:
            brand_ex = item['brand_ex']

        el_input.send_keys(num)

        time.sleep(3)
        el = poa.get_choice_num(item['brand_avtopro'])

        if el:
            el.click()

            if poa.get_element_no_found():
                ob_csv.create_empty_csv(item['index'] + "_" + brand_ex + "_" + num + "_undefined", r'C:\parser\uncorrect')

            data = poa.record_to_file_csv(poa.get_table())

            if data:
                ob_csv.record_to_csv(item['index'] + "_" + brand_ex + "_" + num, poa.header, data, r'C:\parser\correct')
            else:
                ob_csv.create_empty_csv(item['index'] + "_" + brand_ex + "_" + num + "_undefined", r'C:\parser\uncorrect')

        else:
            ob_csv.create_empty_csv(item['index'] + "_" + brand_ex + "_" + num + "_undefined", r'C:\parser\uncorrect')

    except Exception:
        ob_csv.create_empty_csv(item['index'] + "_" + brand_ex + "_" + num + "_error", r'C:\parser\uncorrect')

poa.close()
