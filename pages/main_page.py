from .base_page import BasePage
from .locators import BasePageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    #def should_be_outlets_wrap(self):
    #    assert self.is_element_present(*BasePageLocators.OUTLETS_WRAP), "Outlets_wrap is not presented"
    #    close_btn = self.browser.find_element(*BasePageLocators.CLOSE_OUTLETS)
    #    close_btn.click()