from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class PageObject(BasePage):
    def book_add_to_bucket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        
    def message_about_item_added_to_basket(self):
        title_in_mes = self.browser.find_element(*ProductPageLocators.TITLE_IN_MESSAGE).text
        title_in_pag = self.browser.find_element(*ProductPageLocators.TITLE_ON_PAGE).text
        assert title_in_mes == title_in_pag, "The name of the item DOES NOT match the name of the item in the cart" 
        
    def message_about_price_of_the_basket(self):
        price_in_mes = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        price_on_pag = self.browser.find_element(*ProductPageLocators.PRICE_ON_PAGE).text
        assert price_in_mes == price_on_pag, "The cost of the basket DOES NOT match the price of the item"