from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_by_login_link()

    login = LoginPage(browser, browser.current_url)
    login.open()
    login.should_be_login_url()
    login.should_be_login_form()
    login.should_be_register_form()

@pytest.mark.xfail
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.no_product_in_basket()
    page.no_product_in_basket_msg()
    page.should_see_no_product_in_basket()
    page.should_see_no_product_in_basket_msg()





