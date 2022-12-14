from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest
import time

@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    basket = ProductPage(browser, link)
    basket.open()
    basket.add_product_to_basket()
    basket.solve_quiz_and_get_code()

    basket.should_be_added_product_to_basket_msg
    basket.product_name_message_to_match_added_product_name()

    basket.should_be_added_product_basket_price_msg()
    basket.product_price_message_to_match_added_basket_price()

@pytest.mark.parametrize('link', [pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0', marks=pytest.mark.xfail)])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link): 
    not_page = ProductPage(browser, link)
    not_page.open()
    not_page.add_product_to_basket()
    not_page.solve_quiz_and_get_code()
    not_page.should_not_be_success_message()

@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'])
def test_guest_cant_see_success_message(browser, link): 
    not_page = ProductPage(browser, link)
    not_page.open()
    not_page.should_not_be_success_message()

@pytest.mark.parametrize('link', [pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0', marks=pytest.mark.xfail)])
def test_message_disappeared_after_adding_product_to_basket(browser, link): 
    not_page = ProductPage(browser, link)
    not_page.open()
    not_page.add_product_to_basket()
    not_page.solve_quiz_and_get_code()
    not_page.should_not_be_disappeared()

@pytest.mark.xfail
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.no_product_in_basket()
    page.no_product_in_basket_msg()
    page.should_see_no_product_in_basket()
    page.should_see_no_product_in_basket_msg()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

@pytest.mark.login
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = MainPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login = LoginPage(browser, browser.current_url)
        login.open()
        email = str(time.time()) + "@fakemail.org"
        login.register_new_user(email, time.time())
        login.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser): 
        not_page = ProductPage(browser, self.link)
        not_page.open()
        not_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        basket = ProductPage(browser, self.link)
        basket.open()
        basket.add_product_to_basket()
        basket.solve_quiz_and_get_code()

        basket.should_be_added_product_to_basket_msg
        basket.product_name_message_to_match_added_product_name()

        basket.should_be_added_product_basket_price_msg()
        basket.product_price_message_to_match_added_basket_price()

