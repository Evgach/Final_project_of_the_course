from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")    
    
    TITLE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    
    TITLE_ON_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
    
    PRICE_ON_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")
    
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>:nth-child(1)")
    
class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-items")
    
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")