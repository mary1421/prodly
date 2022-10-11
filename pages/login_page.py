from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_link()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login is not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_link(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_LINK), "Register_link is not presented"

    def login_user(self, name, password):
        p_name = self.browser.find_element(*LoginPageLocators.LOGIN_NAME)
        p_name.send_keys(name)
        p_pas = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        p_pas.send_keys(password)
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.click()
