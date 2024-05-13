from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "There is no 'add to basket' button"

    def add_to_the_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_correct_name_of_the_product(self):
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        name_of_product_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_BASKET).text
        assert name_of_product == name_of_product_in_basket, f"Name of product and name in basket are not the same"

    def should_be_correct_price_of_the_product(self):
        price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        price_of_product_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT_IN_BASKET).text
        assert price_of_product == price_of_product_in_basket, f"Price of product and price in basket are not the same"
