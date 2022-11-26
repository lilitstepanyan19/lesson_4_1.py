from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def go_to_basket_page(self):
        self.go_to_basket(*BasketPageLocators.BTN_BASKET)

    def no_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.NO_PTODUCT), 'There is product in basket'

    def no_product_in_basket_msg(self):
        assert self.is_element_present(*BasketPageLocators.NO_PRODUCT_MSG), 'No message that basket is empty'

    def should_see_no_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NO_PTODUCT), 'There is not product in basket'

    def should_see_no_product_in_basket_msg(self):
        assert self.is_not_element_present(*BasketPageLocators.NO_PRODUCT_MSG), 'Was message that basket is empty'
