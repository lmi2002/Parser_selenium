import re
import time

from numpy.core.defchararray import lower
from selene import config, browser
from selene.api import s, ss
from selene.support.conditions import have
from selene.support.conditions.be import visible

config.timeout = 4
config.hold_browser_open = False
config.browser_name = 'chrome'
browser.driver()
browser.open_url('https://exist.ua/')


def get_search_input():
    return ss('.search-input')[1]


def get_search_results():
    return [el for el in s('.search-results.modal').should(visible).ss('div .title').should(have.size_at_least(1))]


string = 'Hydroblocks components and antiblocking systems (ABS)'
s('.lang-dd-button button').click()
time.sleep(1)
s('.lang-select').ss('button')[1].click()
get_search_input().send_keys(string)
st_s = get_search_results()[0]

for el in get_search_results():
    if el.text == string:
        el.click()
        time.sleep(10)

re.sub('components', 'com', string, count=0)
