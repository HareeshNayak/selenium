import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("setup")
class TestAddToCart:
    def test_add_to_cart(self):
        home = HomePage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)

        home.open_url("https://www.demoblaze.com/")
        home.open_category("Phones")
        product.select_product()
        product.add_to_cart()
        cart.open_cart()
        cart.take_screenshot("cart.png")
