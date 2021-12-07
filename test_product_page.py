from .pages.product_page import PageObject
from .pages.base_page import BasePage
import time
import pytest

@pytest.mark.parametrize('offer', ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", "promo=offer4", "promo=offer5", "promo=offer6", "promo=offer7", "promo=offer8", "promo=offer9"])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?{offer}"
    page = PageObject(browser, link)
    page.open()
    page.book_add_to_bucket()
    browser.implicitly_wait(1)
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(1)
    page.message_about_item_added_to_basket()
    page.message_about_price_of_the_basket()