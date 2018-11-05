from properties.prop_driver import Driver


class PageObjectAvtopro(Driver):
    super().__init__()


    def get_input_search(self):
        self.

        ('#ap-search-query')

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

    def get_table(self, table):
        for tr in table.find_elements_by_xpath('tbody/tr'):
            row = [td.text for idx, td in enumerate(tr.find_elements_by_xpath('td'), start=1) if idx in (1, 2, 3, 5)]
            return row


_browser = Browser('chrome', 'https://avto.pro/part-12345-FEBI-178/')
_browser.i

#page_object = PageObjectAvtopro()
#input_search = page_object.get_input_search()
#input_search.send_keys(12345)
#page_object.get_choice_num('febi')
#page_object.s(by.css('h3')).should(appear).click()
print('ata')