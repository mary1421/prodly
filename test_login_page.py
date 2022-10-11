import pytest, time
from .pages.login_page import LoginPage

#@pytest.mark.skip
class TestUserAddToBasketFromProductPage():
    #@pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, '1a2S3d4F5g6H7j')
        time.sleep(5)
        login_page.should_be_authorized_user()
