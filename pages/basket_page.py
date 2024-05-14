from stepik_auto_tests_course_final_project.pages.base_page import BasePage
from stepik_auto_tests_course_final_project.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "There is no 'basket' in url"

    def should_be_text_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "The basket isn't empty"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "There are products in the basket"
