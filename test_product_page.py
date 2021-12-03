from .pages.product_page import PageObject
from .pages.base_page import BasePage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser, link)
    page.open()
    page.book_add_to_bucket()
    browser.implicitly_wait(1)
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(1)
    page.message_about_item_added_to_basket()
    page.message_about_price_of_the_basket()