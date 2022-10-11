from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-group a")
    LOGIN_LINK = (By.CSS_SELECTOR, ".login")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".sign-in-wrapper")
    REGISTER_LINK = (By.CSS_SELECTOR, "#main-form > div.top > a")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD2 = (By.NAME, "registration-password2")
    LOGIN_BTN = (By.NAME, "registration_submit")

class RegisterPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_NAME = (By.CSS_SELECTOR, "#main-form > div.info-inputs > div:nth-child(1) > input[type=text]")
    REGISTER_PHONE = (By.CSS_SELECTOR, "#main-form > div.info-inputs > div:nth-child(2) > input")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#main-form > div.info-inputs > div:nth-child(3) > input[type=email]")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, \
                             "#main-form > div.info-inputs > div.input-wrap.password-wrap > input[type=password]")
    REGISTER_REG_ID = (By.CSS_SELECTOR, "#main-form > div.info-inputs > div:nth-child(5) > input")
    REGISTER_BTN = (By.CSS_SELECTOR, ".send")
    REGISTER_VER_CODE = (By.NAME, "verificationCode")
    REGISTER_VER_BTN = (By.CSS_SELECTOR, "#globalDialog > div.dialog-body > div > div > form > div.form-code > button")