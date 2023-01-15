import time

from .pages.product_page import ProductPage
import pytest

URL = 'http://selenium1py.pythonanywhere.com/zh-cn/catalogue/coders-at-work_207/'
URL_PROMO = URL + '?promo=newYear2019'

@pytest.mark.parametrize('link', [f"{URL}?promo=offer0",
                                  f"{URL}?promo=offer1",
                                  f"{URL}?promo=offer2",
                                  f"{URL}?promo=offer3",
                                  f"{URL}?promo=offer4",
                                  f"{URL}?promo=offer5",
                                  f"{URL}?promo=offer6",
                                  pytest.param(f"{URL}?promo=offer7", marks=pytest.mark.xfail),
                                  f"{URL}?promo=offer8",
                                  f"{URL}?promo=offer9"])
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


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, URL)
    page.open()
    page.add_book_to_basket()
    page.should_be_disappeared_of_success_message()
