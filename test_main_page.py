from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    # page = MainPage(browser, link)
    # page.open
    # page.go_to_login_page()

# def test_guest_should_see_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#     page = MainPage(browser, link)
#     page.open
    # page.should_by_login_link()
    login = LoginPage(browser, link)
    login.open
    login.should_be_login_form()

if __name__ == '__main__':
    pytest.main()