import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('code', ["0",
                                  "1",
                                  "2",
                                  "3",
                                  "4",
                                  "5",
                                  "6",
                                  pytest.param("7", marks=pytest.mark.xfail),
                                  "8",
                                  "9"])
def test_guest_can_add_product_to_basket(browser, code):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{code}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_the_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name_of_the_product()
    page.should_be_correct_price_of_the_product()
