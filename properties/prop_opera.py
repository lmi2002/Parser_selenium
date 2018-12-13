import time

from selenium import webdriver
from selenium.webdriver.chrome import service


webdriver_service = service.Service(r'C:\Users\anokhin\PycharmProjects\Parser_site\drivers\operadriver.exe')
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

driver.get('https://www.google.com/')


time.sleep(5) #see the result
driver.quit()
