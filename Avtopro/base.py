import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from exception import ElementNotFoundException


class BasePage(object):
    default_timeout = 10
    default_delay = 1

    def __init__(self, driver):
        super(BasePage, self).__init__()
        self.driver = driver
        self.timeout = self.default_timeout
        self.delay = self.default_delay
        self.wait = WebDriverWait(self.driver, self.timeout)

    def impliti_wait_sec(self, sec):
        self.impliti_wait(sec)

    def get_web_element(self, item):
        try:
            element = self.wait.until(
                expected_conditions.presence_of_element_located(item)
            )
            return element
        except TimeoutException as e:
            raise ElementNotFoundException(item, e)

    def get_web_elements(self, item):
        try:
            element = self.wait.until(
                expected_conditions.presence_of_all_elements_located(item)
            )
            return element
        except TimeoutException as e:
            raise ElementNotFoundException(item, e)

    def get_visible_element(self, item):
        try:
            element = self.wait.until(
                expected_conditions.visibility_of_element_located(item)
            )
            return element
        except TimeoutException as e:
            raise ElementNotFoundException(item, e)

    def get_visible_elements(self, item):
        try:
            elements = self.wait.until(
                expected_conditions.visibility_of_any_elements_located(item)
            )
        except TimeoutException:
            elements = []

        return elements

    def get_first_visible_element(self, item):
        elements = self.get_visible_elements(item)
        if not elements:
            raise ElementNotFoundException(item)
        return elements[0]

    def get_alert(self):
        return self.wait.until(
            expected_conditions.alert_is_present()
        )

    def check_text_present_in_element(self, item, text):
        element = self.wait.until(
            expected_conditions.text_to_be_present_in_element(item, text)
        )
        return element

    def delay_test(self, delay=None):
        time.sleep(delay or self.delay)

    def locate(self, item):
        self.delay_test()
        return self.get_web_element(item)

    def click(self, item, delay=None):
        try:
            element = self.wait.until(
                expected_conditions.element_to_be_clickable(item)
            )
        except TimeoutException as e:
            raise ElementNotFoundException(item, e)

        element.click()
        self.delay_test(delay=delay)
        return element

    def go_back(self, qnt):
        self.driver.execute_script("window.history.go(" + str(qnt) + ")")

    def refresh(self):
        self.driver.execute_script("location.reload()")