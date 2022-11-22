from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTR_FORM = (By.CSS_SELECTOR, '.register_form')

class BasketLocators():
    ADD_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')

class ProductLocators():
    PRODUCT_NAME_MSG = (By.CSS_SELECTOR, '.alertinner')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner>strong')

class BasketPriceLocators():
    BASKET_PRICE_MSG = (By.CSS_SELECTOR, 'alertinner>p')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main>p')
    ADDED_BASKET_PRICE = (By.CSS_SELECTOR, 'alertinner>p>strong')