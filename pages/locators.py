from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTR_FORM = (By.CSS_SELECTOR, '.register_form')
    USER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    USER_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    USER_PASS_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTR_BTN = (By.XPATH, '//button[@name="registration_submit"]')

class BasketLocators():
    ADD_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')

class ProductLocators():
    PRODUCT_NAME_MSG = (By.CSS_SELECTOR, '.alertinner:nth-child(1)')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner>strong')

class BasketPriceLocators():
    BASKET_PRICE_MSG = (By.CSS_SELECTOR, '.alertinner>p')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>p')
    ADDED_BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong')

class BasketPageLocators():
    BTN_BASKET = (By.CSS_SELECTOR, '.btn-group>.btn.btn-default')
    NO_PTODUCT = (By.CSS_SELECTOR, '#content_inner')
    NO_PRODUCT_MSG = (By.CSS_SELECTOR, '.content>#content_inner>p')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")