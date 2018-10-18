from selene.api import *
from selene.conditions import appear, text

from properties.prop_browser import Browser
from base_function import function


class PageObjectAvtopro:

    def __init__(self):
        self.s = s
        self.ss = ss

    def get_input_search(self):
        return self.s('#ap-search-query').should(appear)

    # Search in list elements element with text
    def get_choice_num(self, brand):
        brand_no_sym = function.delete_all_spec_symbol(brand)
        brand_lower = function.lower_register(brand_no_sym[0])

        try:
            list_span = self.ss('span')

            for el in list_span:
                try:
                    txt = function.lower_register(el.text)
                    txt_no_sym = function.delete_all_spec_symbol(txt)
                    if brand_lower[0] in txt_no_sym[0]:
                        self.s(by.text(el.text)).click()
                except Exception:
                    pass
        except Exception:
            pass


_browser = Browser('chrome', 'https://avto.pro/')
page_object = PageObjectAvtopro()
input_search = page_object.get_input_search()
input_search.send_keys(12659)
page_object.get_choice_num('febi')