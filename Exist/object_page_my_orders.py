import re
from functools import reduce

from selene import browser
from selene.api import ss, s
from selene.support import by
from selene.support.conditions import have
from selene.support.conditions.be import visible


class MyOrders:

    @staticmethod
    def get_number_list():
        return ss('tbody .name a')

    @staticmethod
    def order_num_list():
        return [el.text for el in ss('tbody p strong:not([class]').should(have.size_at_least(1))]

    @staticmethod
    def office_list():
        return [el.text for el in ss('tbody .order-office').should(have.size_at_least(1))]

    @staticmethod
    def status_list():
        return [el.text for el in ss('tbody .order-status').should(have.size_at_least(1))]

    @staticmethod
    def get_brand_text_list():
        return [el.text for el in ss('tbody .name > strong').should(have.size_at_least(1))]

    @staticmethod
    def get_price_list():
        return reduce((lambda x, y: x + y), [int(el.text[:-4]) for el in ss('tbody .price')])

    @staticmethod
    def click_office_sale():
        ss('.react-select-container')[0].click()

    @staticmethod
    def click_select_office_sale(office=None):
        for el in ss('.react-select__menu div'):
            if re.match(el.text, office, re.I):
                el.click()
                break

    @staticmethod
    def click_status():
        ss('.react-select-container')[2].click()

    @staticmethod
    def click_select_status(status=None):
        for el in ss('.react-select__menu div'):
            if re.match(el.text, status, re.I):
                el.click()
                break

    @staticmethod
    def get_select_delivery_type():
        ss('.react-select-container')[1].click()

    @staticmethod
    def click_btn_blue():
        s('.orders-filter .btn-blue ').click()

    @staticmethod
    def click_my_orders():
        ss('.user-menu-profile-body ul a')[2].click()

    @staticmethod
    def click_select_clear():
        s('.react-select__clear-indicator').click()

    @staticmethod
    def get_order_number_input():
        return s('.order-number-input')

    @staticmethod
    def get_num_input():
        return s('.order-number-input ~ input')

    @staticmethod
    def click_review_link():
        s('.order-item-links button').click()

    @staticmethod
    def click_reorder_link():
        s('.order-item-links a').click()

    @staticmethod
    def have_modal():
        browser.driver().switch_to_window('.supportDesktop')

    @staticmethod
    def get_current_count():
        return int(s('.current').text.split('(')[1][:-1])

    @staticmethod
    def get_orders_total():
        return int(s('.orders-total strong').text[:-4])

    @staticmethod
    def click_button_payment():
        ss('.nested-row-header .btn-blue')[0].click()

    @staticmethod
    def click_button_balance():
        s('.personal-data-wrapper .btn-green').click()

    @staticmethod
    def get_rows_order_part():
        return ss(by.xpath('//tr [@class=" "]')).should_be(have.size_at_least(1))
