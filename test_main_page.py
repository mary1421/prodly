import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        link = "https://stage.prodly.ru"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "https://stage.prodly.ru"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_logout(self, browser):
        link = "https://stage.prodly.ru/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        phone = "+79538906542"
        password = '1a2S3d4F5g6H7j'
        login_page.login_user(phone, password)
        login_page.logout()
        login_page.should_be_login_page()