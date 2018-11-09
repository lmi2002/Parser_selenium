import time

from Avtopro.page_object.object_page import PageObjectAvtopro
from properties.prop_csv import Csv

ob_csv = Csv()
poa = PageObjectAvtopro()

poa.open_site()
poa.maximize_window()

lst_from_ex = ob_csv.read_to_csv(r'C:\Users\anokhin\Desktop\KNS2018-11-06.csv')

for item in lst_from_ex:
    time.sleep(1)
    poa.get_search_query().send_keys(item['num'])
    time.sleep(3)
    poa.get_choice_num(item['brand_avtopro'])
    data = poa.record_to_file_csv(poa.get_table())
    if data:
        ob_csv.record_to_csv(item['index'] + "_" + item['brand_ex'] + "_" + item['num'], poa.header, data, r'C:\parser\correct')
    else:
        ob_csv.record_to_csv(item['index'] + "_" + item['brand_ex'] + "_" + item['num'] + "_undefined", r'C:\parser\uncorrect')

poa.close()
