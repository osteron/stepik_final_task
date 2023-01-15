from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty'

    def present_text_of_the_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), 'Basket is not empty'
