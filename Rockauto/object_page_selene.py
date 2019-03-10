import time
import random
from selene.api import *
from selene.conditions import exist

from properties.prop_txt import Txt


txt = Txt()
read_file_path = r'C:\Users\Star\Desktop\rockauto_cars.txt'
write_file_path = r'C:\Users\Star\Desktop\rockauto_cars_model.txt'
make_file_path = r'C:\Users\Star\Desktop\make_cars.txt'

config.timeout = 15
config.hold_browser_open = True
config.browser_name = 'chrome'
browser.driver()
time.sleep(90)
browser.open_url('https://www.rockauto.com/')


def error_code():
    return s('.error-code').should_not(exist)


def time_sleep_random(min, max):
    sec = random.choice(range(min, max))
    time.sleep(sec)


def get_href():
    return set(a.get_attribute('href') for a in ss('.nlabel a'))


def click_a(prev):
    href_set = set()
    # import ipdb; ipdb.set_trace()
    with open(read_file_path, 'r', newline='') as tf:
        data = tf.readlines()
        for href in data:
            if href.find('\r\n'):
                href_set.add(href[:-2])
            else:
                href_set.add(href[:-1])

        prev = prev.union(href_set)
        # if error_code:
        for line in data:
            browser.open_url(line[:-1])
            time_sleep_random(1, 3)
            nxt = get_href()
            diff = difference_href(prev, nxt)
            txt.writer_file_txt(write_file_path, diff)
            with open(make_file_path, 'a', newline='\n') as tf:
                tf.write(line)
        # else:
        #     browser.close()


def difference_href(prev, nxt):
    return nxt.difference(prev)


href = get_href()
click_a(href)
