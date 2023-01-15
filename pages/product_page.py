from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_be_disappeared_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_ADDED_TO_BASKET), \
            "Success message is not disappeared"

    def add_book_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def check_book_is_added_to_basket(self):
        alerts = self.browser.find_elements(*ProductPageLocators.ALERT_ADDED_TO_BASKET)
        assert len(alerts) > 0, 'Alerts "book is added to basket" is not presented'

        basket_total_price = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_BASKET).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert book_price == basket_total_price, \
            f"Basket total {basket_total_price} is not equal book price {book_price}"

        alert_book_title = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_TITLE).text
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        assert alert_book_title == book_title, \
            f'Book title in alert "{alert_book_title}" is not equal book title on page "{book_title}"'
