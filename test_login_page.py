import pytest, time
from .pages.login_page import LoginPage

@pytest.mark.login_logout
class TestUserLogin():
    '''
    Тест на авторизацию пользователя.
    Проверяется наличие сообщения об успешном входе.
    '''
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

    '''
    Негативный тест
    Тест на авторизацию пользователя с некорректным паролем.
    Проверяется наличие сообщения об ошибке.
    '''
    def test_user_login_incorrect(self, browser):
        link = "https://stage.prodly.ru/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        phone = "+79538906542"
        password = '123456'
        login_page.login_user(phone, password)
        time.sleep(5)
        login_page.should_be_error_msg_login()