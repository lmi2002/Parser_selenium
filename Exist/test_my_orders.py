import time

import self as self
from selene import config, browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selene.api import s, ss
from selene.browser import open_url, driver
from selene.support.conditions import have

from Exist.object_page_my_orders import MyOrders
from Exist.object_page_persona_cabinet import PersonalCabinet

config.timeout = 4
config.hold_browser_open = False
config.browser_name = 'chrome'
browser.driver()
browser.open_url('https://exist.ua/')

pc = PersonalCabinet()
mo = MyOrders
pc.log_in()
mo.click_my_orders()
time.sleep(15)

# -----------------------------------------------
# office_select = mo.office_list()[0]
# mo.click_office_sale()
# mo.click_select_office_sale(office=office_select)
# mo.click_btn_blue()
# time.sleep(1)
# office = list(set(mo.office_list()))
# assert len(office) == 1 and office[0] == office_select
# print(mo.get_current_count(), len(mo.office_list()))
# assert mo.get_current_count() == len(mo.office_list())
# mo.click_select_clear()
# mo.click_btn_blue()

# ------------------------------------------------
# status_select = mo.status_list()[0]
# mo.click_status()
# mo.click_select_status(status=status_select)
# mo.click_btn_blue()
# time.sleep(1)
# status = list(set(mo.status_list()))
# assert mo.get_price_list() == mo.get_orders_total()
# assert len(status) == 1 and status[0] == status_select
# assert mo.get_current_count() == len(mo.status_list())
# mo.click_select_clear()
# mo.click_btn_blue()

# ---------------------------------------------------
# order_select = mo.order_num_list()[0]
# mo.get_order_number_input().send_keys(order_select)
# mo.click_btn_blue()
# time.sleep(1)
# order = list(mo.order_num_list())
# assert len(order) == 1 and order[0] == order_select
# assert mo.get_current_count() == len(mo.order_num_list())
# mo.get_order_number_input().send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
# mo.click_btn_blue()
# # ----------------------------------------------------
# brand_select = mo.get_brand_text_list()[0]
# mo.get_num_input().send_keys(brand_select)
# mo.click_btn_blue()
# time.sleep(1)
# brand = list(set(mo.get_brand_text_list()))
# assert len(brand) == 1 and brand[0] == brand_select
# assert mo.get_current_count() == len(mo.get_brand_text_list())
# mo.get_num_input().send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
# mo.click_btn_blue()
# ------------------------------------------------------
# mo.get_number_list()[0].click()
# time.sleep(7)

# -------------------------------------------------------
# mo.click_review_link()
# mo.have_modal()
# mo.click_reorder_link()
# mo.click_button_payment()
# mo.click_button_balance()

print(len(mo.get_rows_order_part()))
time.sleep(7)