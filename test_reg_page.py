import pytest, time
from .pages.register_page import RegisterPage

@pytest.mark.register
class TestUserRegister():
    '''
    Тест на регистрацию нового пользователя, необходимо запускать с параметром -s.
    Номер телефона и код из СМС требуется вводить в консоли теста
    '''
    def test_register_new_user(self, browser):
        link = "https://stage.prodly.ru/register"
        register_page = RegisterPage(browser, link)
        register_page.open()
        name = 'Manya'
        print('Введите номер телефона в формате +7ХХХХХХХХХХ')
        phone = input()
        email = str(time.time()) + "@fakemail.org"
        register_page.register_new_user(name, phone, email, '1a2S3d4F5g6H7j', '')
        time.sleep(15)
        print('Введите код из SMS')
        register_page.register_verification(input())
        time.sleep(5)
        register_page.should_be_authorized_user(name)

    '''
    Негативный тест
    Тест на регистрацию пользователя с ранее зарегистрированным номером телефона.
    Проверяется наличие сообщения об ошибке
    '''
    def test_register_not_new_user(self, browser):
        link = "https://stage.prodly.ru/register"
        register_page = RegisterPage(browser, link)
        register_page.open()
        name = 'Manya'
        phone = '89538906542'
        email = str(time.time()) + "@fakemail.org"
        register_page.register_new_user(name, phone, email, '1a2S3d4F5g6H7j', '')
        time.sleep(5)
        register_page.should_be_error_msg_register()

