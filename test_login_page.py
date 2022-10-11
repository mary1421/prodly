import pytest, time
from .pages.login_page import LoginPage

@pytest.mark.login_logout
class TestUserLogin():
    def test_user_login(self, browser):
        link = "https://stage.prodly.ru/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        phone = "+79538906542"
        password = '1a2S3d4F5g6H7j'
        login_page.login_user(phone, password)
        time.sleep(5)
        name = 'Manya'
        login_page.should_be_authorized_user(name)
