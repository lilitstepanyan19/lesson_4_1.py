from .base_page import BasePage
from .locators import BasketLocators, ProductLocators, BasketPriceLocators
from cgitb import text

class ProductPage(BasePage):
    def add_product_to_basket(self):
        product = self.browser.find_element(*BasketLocators.ADD_BASKET)
        product.click()

    def should_be_added_product_to_basket_msg(self):
        assert self.is_element_present(*ProductLocators.PRODUCT_NAME_MSG), 'No message that the product has been added to the bascet'

    def product_name_message_to_match_added_product_name(self):
        product_name = self.browser.find_element(*ProductLocators.PRODUCT_NAME).text 
        added_product_name = self.browser.find_element(*ProductLocators.ADDED_PRODUCT_NAME).text

        assert product_name == added_product_name, 'Something went wrong'

    def should_be_added_product_basket_price_msg(self):
        assert self.is_element_present(*BasketPriceLocators.BASKET_PRICE_MSG), 'No message about added product basket'
    
    def product_price_message_to_match_added_basket_price(self):
        product_price = self.browser.find_element(*BasketPriceLocators.PRODUCT_PRICE).text
        added_basket_price = self.browser.find_element(*BasketPriceLocators.ADDED_BASKET_PRICE).text
        
        assert product_price == added_basket_price, 'Something went wrong'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductLocators.PRODUCT_NAME_MSG), \
            "Success message is presented, but should not be"

    def should_not_be_disappeared(self):
        assert self.is_disappeared(*ProductLocators.PRODUCT_NAME_MSG), \
            "Success message is presented, but should not be"



