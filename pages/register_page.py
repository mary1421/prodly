from .base_page import BasePage
from .locators import BasePageLocators, RegisterPageLocators

class RegisterPage(BasePage):
    def register_new_user(self, name, phone, email, password, reg_id):
        p_name = self.browser.find_element(*RegisterPageLocators.REGISTER_NAME)
        p_name.send_keys(name)
        p_phone = self.browser.find_element(*RegisterPageLocators.REGISTER_PHONE)
        p_phone.send_keys(phone)
        p_mail = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL)
        p_mail.send_keys(email)
        p_pas = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD)
        p_pas.send_keys(password)
        p_reg_id = self.browser.find_element(*RegisterPageLocators.REGISTER_REG_ID)
        p_reg_id.send_keys(reg_id)
        register_btn = self.browser.find_element(*RegisterPageLocators.REGISTER_BTN)
        register_btn.click()

    def register_verification(self, code):
        p_ver = self.browser.find_element(*RegisterPageLocators.REGISTER_VER_CODE)
        p_ver.send_keys(code)
        ver_btn = self.browser.find_element(*RegisterPageLocators.REGISTER_VER_BTN)
        ver_btn.click()

    def should_be_error_msg_register(self):
       text = self.browser.find_element(*BasePageLocators.ERROR_MSG).text
       assert self.browser.find_element(*BasePageLocators.ERROR_MSG).text == \
              'Номер телефона уже зарегистрирован в системе.', "User error-message is not presented"

