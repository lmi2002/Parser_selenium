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
        list_item_brand = function.delete_all_spec_symbol(brand)
        brand_no_sym = list_item_brand[0]
        list_brand_lower = function.lower_register(brand_no_sym)
        brand_lower = list_brand_lower[0]
        span_list = self.ss('div span').should(appear)
        print(span_list)
        for el in span_list:
            txt = el.span_list
            txt_no_sym = function.delete_all_spec_symbol(txt)
            print(txt_no_sym)




browser = Browser('chrome', 'https://avto.pro/')
page_object = PageObjectAvtopro()
input_search = page_object.get_input_search()
input_search.send_keys(12659)
page_object.get_choice_num('Fe-bi')
#print(function.lower_register('Metelli', 12345))
#print(function.delete_all_spec_symbol('Me//te-l+li/', '12!3+4-5'))