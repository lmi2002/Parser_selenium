from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import params


class Driver(object):

    default_timeout = 30

    def __init__(self):
        self.driver = webdriver.Chrome(params.PATH_CHROME_DRIVER)
        self.wait = WebDriverWait(self.driver, self.default_timeout)

    def close(self):
        self.driver.quit()

    def maximize_window(self):
        self.driver.maximize_window()

