from selene import config
from selene import browser


class Browser:
    def __init__(self, browser_name='chrome', url=None):
        self.browser_name = browser_name
        self.url = url

        config.browser_name = browser_name
        config.start_maximized = True
        config.hold_browser_open = False
        config.cash_elements = True
        browser.open_url(url)

