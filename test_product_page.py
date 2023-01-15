from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
import time

URL = 'http://selenium1py.pythonanywhere.com/zh-cn/catalogue/coders-at-work_207/'
URL_PROMO = URL + '?promo=newYear2019'


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@mail.org"
        user_page = LoginPage(browser, URL_PROMO)
        user_page.open()
        user_page.register_new_user(email, 'GjitkYf[eq')

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, URL_PROMO)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, URL_PROMO)
        page.open()
        page.add_book_to_basket()
        page.solve_quiz_and_get_code()
        page.check_book_is_added_to_basket()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', [f"{URL}?promo=offer0", f"{URL}?promo=offer1", f"{URL}?promo=offer2",
                                  f"{URL}?promo=offer3", f"{URL}?promo=offer4", f"{URL}?promo=offer5",
                                  f"{URL}?promo=offer6",
                                  pytest.param(f"{URL}?promo=offer7", marks=pytest.mark.xfail),
                                  f"{URL}?promo=offer8", f"{URL}?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.solve_quiz_and_get_code()
    page.check_book_is_added_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.add_book_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.add_book_to_basket()
    page.should_be_disappeared_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.present_text_of_the_basket_is_empty()
