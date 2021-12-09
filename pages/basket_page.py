from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def there_are_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Product in basket"
        
    def there_is_text_about_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"