import time

from Avtopro.page_object.object_page import PageObjectAvtopro
from properties.prop_csv import Csv



poa = PageObjectAvtopro()
poa.open_site()
poa.maximize_window()
poa.get_search_query().send_keys(12345)
time.sleep(2)
poa.get_choice_num('Feb')
data = poa.record_to_file_csv(poa.get_table())
ob_csv = Csv()
ob_csv.record_to_csv('Feb' + '12345', poa.header, data, r'C:\parser\correct')
poa.close()


