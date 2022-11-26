from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
])
def test_guest_can_add_product_to_basket(browser, link):
    basket = ProductPage(browser, link)
    basket.open()
    basket.add_product_to_basket()
    basket.solve_quiz_and_get_code()

    basket.should_be_added_product_to_basket_msg
    basket.product_name_message_to_match_added_product_name()

    basket.should_be_added_product_basket_price_msg()
    basket.product_price_message_to_match_added_basket_price()

@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'])
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

@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'])
def test_message_disappeared_after_adding_product_to_basket(browser, link): 
    not_page = ProductPage(browser, link)
    not_page.open()
    not_page.add_product_to_basket()
    not_page.solve_quiz_and_get_code()
    not_page.should_not_be_disappeared()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.no_product_in_basket()
    page.no_product_in_basket_msg()
    page.should_see_no_product_in_basket()
    page.should_see_no_product_in_basket_msg()



