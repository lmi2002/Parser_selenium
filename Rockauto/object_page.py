import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

from properties.prop_driver import Driver


class PageObjectRockauto(Driver):

    def __init__(self):
        super().__init__()

    def open_site(self, url):
        return self.driver.get(url)

    def get_href(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'2019')")))




#por = PageObjectRockauto()

#por.open_site('https://www.rockauto.com/en/catalog/bmw')
#els = por.get_href()
#for el in els:
    #print(el.get_attribute('href'))

#por.close()

with open(r'C:\Users\anokhin\Desktop\marka.txt', 'r') as fl:
    reader = fl.readlines()
    href = [href.lower() for href in reader]


for el in href:
    response = requests.get('https://www.rockauto.com/en/catalog/' + href[0])
    soup = BeautifulSoup(response.content, 'html.parser')
    a = soup.find_all('a')
    lst = [elm.get('href') for elm in a if re.search('en/catalog/'+href, el.get('href'), re.I)]

print(lst)

with open(r'C:\Users\anokhin\Desktop\marka_1.txt', 'w') as flw:
    writer = flw.writelines(lst)



