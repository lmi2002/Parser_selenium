import time
import random
from selene.api import *

from properties.prop_txt import Txt

txt = Txt()
file_path = r'C:\Users\Star\Desktop\rockauto_cars.txt'

config.timeout = 15
config.hold_browser_open = False
config.browser_name = 'chrome'
browser.open_url('https://www.rockauto.com')


def time_sleep_random(min, max):
    sec = random.choice(range(min, max))
    time.sleep(sec)


def get_href():
    return set(a.get_attribute('href') for a in ss('.nlabel a'))


def click_a(elements, prev):
    # import ipdb; ipdb.set_trace()
    for element in elements:
        browser.open_url(element)
        time_sleep_random(3, 12)
        nxt = get_href()
        diff = difference_href(prev, nxt)
        txt.writer_file_txt(file_path, diff)


def difference_href(prev, nxt):
    return nxt.difference(prev)


href = get_href()
click_a(href, href)
