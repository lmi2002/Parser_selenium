from selene.api import *

config.timeout = 4
config.hold_browser_open = False
config.browser_name = 'chrome'
browser.driver()
browser.open_url('https://exist.ua/')
base_url = browser.driver().current_url

pages = {
    'settings': 'settings/',
    'notepad': 'notepad/',
    # 'orders': 'orders/',
    'balance': 'balance/'
}

for value in pages.values():
    browser.open_url(base_url + value)
    s('.no-access-wrapper-title').should(have.exact_text('ДАННЫЙ ФУНКЦИОНАЛ ДОСТУПЕН ЗАРЕГИСТРИРОВАННЫМ ПОЛЬЗОВАТЕЛЯМ'))
