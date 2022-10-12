from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".login")
    USER_GREETING = (By.CSS_SELECTOR, "#main-form > div.top > h3")
    #OUTLETS_WRAP = (By.CSS_SELECTOR, ".outlets-wrap")
    #CLOSE_OUTLETS = (By.CSS_SELECTOR, ".close-icon")
    LOGOUT_LINK = (By.XPATH, "/html/body/div[3]/div/div[1]/div[2]/div/div/div[2]/ul/li[6]/a")
    ERROR_MSG = (By.CSS_SELECTOR, "#main-form > div.input-wrap.password-wrap > p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".sign-in-wrapper")
    REGISTER_LINK = (By.CSS_SELECTOR, "#main-form > div.top > a")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_NAME = (By.CSS_SELECTOR, ".phone-number-input")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#loginPassword")
    LOGIN_BTN = (By.CSS_SELECTOR, ".send")

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