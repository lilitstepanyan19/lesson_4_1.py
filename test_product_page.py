from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    basket = ProductPage(browser, link)
    basket.open()
    basket.add_product_to_basket()
    basket.solve_quiz_and_get_code()

    basket.should_be_added_product_to_basket_msg
    basket.product_name_message_to_match_added_product_name()

    basket.should_be_added_product_basket_price_msg()
    basket.product_price_message_to_match_added_basket_price()