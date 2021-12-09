from .pages.product_page import PageObject
from .pages.base_page import BasePage
import time
import pytest

@pytest.mark.skip
@pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=offer{offer}"
    page = PageObject(browser, link)
    page.open()
    page.book_add_to_basket()
    browser.implicitly_wait(1)
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(1)
    page.message_about_item_added_to_basket()
    page.message_about_price_of_the_basket()
    
@pytest.mark.skip  
@pytest.mark.parametrize('offer', [*range(0,7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, offer):
   link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=offer{offer}"

@pytest.mark.skip   
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = PageObject(browser, link)
    page.open()
    page.book_add_to_basket()
    #browser.implicitly_wait(1)
    page.should_not_be_success_message()
    
@pytest.mark.skip 
def test_guest_cant_see_success_message(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = PageObject(browser, link)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.skip     
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = PageObject(browser, link)
    page.open()
    page.book_add_to_basket()
    #browser.implicitly_wait(1)
    page.should_not_be_success_message_is_disappeared()

#@pytest.mark.skip    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    page.should_be_login_link()
    
#@pytest.mark.skip    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = PageObject(browser, link)
    page.open()
    browser.implicitly_wait(1)
    page.go_to_login_page()