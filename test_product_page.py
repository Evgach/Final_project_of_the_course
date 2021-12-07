from .pages.product_page import PageObject
from .pages.base_page import BasePage
import time
import pytest

@pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=offer{offer}"
    page = PageObject(browser, link)
    page.open()
    page.book_add_to_bucket()
    browser.implicitly_wait(1)
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(1)
    page.message_about_item_added_to_basket()
    page.message_about_price_of_the_basket()
    
@pytest.mark.parametrize('offer', [*range(0,7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, offer):
   link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}'