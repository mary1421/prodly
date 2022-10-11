import pytest, time
from .pages.register_page import RegisterPage

@pytest.mark.register
class TestUserRegister():
    #@pytest.fixture(scope="function", autouse=True)
    def test_register_new_user(self, browser):
        link = "https://stage.prodly.ru/register"
        register_page = RegisterPage(browser, link)
        register_page.open()
        name = 'Manya'
        phone = '89538906542'
        email = str(time.time()) + "@fakemail.org"
        register_page.register_new_user(name, phone, email, '1a2S3d4F5g6H7j', '')
        time.sleep(15)
        register_page.register_verification(input())
        time.sleep(5)
        #register_page.should_be_authorized_user()

