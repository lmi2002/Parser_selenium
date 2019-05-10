from selene.api import *


class PersonalCabinet:

    @staticmethod
    def click_personal_cabinet():
        s('.profile').s('button').click()

    @staticmethod
    def get_input_phone_field():
        return s('#phone-field')

    @staticmethod
    def get_input_password():
        return s(by.name('password'))

    @staticmethod
    def click_btn_blue():
        s('.btn-blue').click()

    def log_in(self):
        self.click_personal_cabinet()
        self.get_input_phone_field().send_keys('688074444')
        self.get_input_password().send_keys('vaz21099')
        self.click_btn_blue()
        self.click_personal_cabinet()
