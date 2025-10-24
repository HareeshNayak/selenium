import pytest
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("setup")
class TestAddToCart:
    # ✅ 1. Add a phone to the cart
    def test_add_phone_to_cart(self):
        home = HomePage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)

        home.open_url("https://www.demoblaze.com/")

        try:
            home.open_category("Phones")
        except TimeoutException:
            self.driver.refresh()
            home.open_category("Phones")

        for attempt in range(3):
            try:
                product.select_product("Samsung galaxy s6")
                break
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
                self.driver.refresh()

        product.add_to_cart()
        cart.open_cart()
        cart.take_screenshot("cart_phone.png")

        items = self.driver.find_elements("xpath", "//td[contains(text(),'Samsung galaxy s6')]")
        assert len(items) > 0, "Phone not found in cart!"

    # ✅ 2. Add a laptop to the cart
    def test_add_laptop_to_cart(self):
        home = HomePage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)

        home.open_url("https://www.demoblaze.com/")
        home.open_category("Laptops")

        product.select_product("Sony vaio i5")
        product.add_to_cart()
        cart.open_cart()
        cart.take_screenshot("cart_laptop.png")

        items = self.driver.find_elements("xpath", "//td[contains(text(),'Sony vaio i5')]")
        assert len(items) > 0, "Laptop not found in cart!"

    # ✅ 3. Add a monitor to the cart
    def test_add_monitor_to_cart(self):
        home = HomePage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)

        home.open_url("https://www.demoblaze.com/")
        home.open_category("Monitors")

        product.select_product("Apple monitor 24")
        product.add_to_cart()
        cart.open_cart()
        cart.take_screenshot("cart_monitor.png")

        items = self.driver.find_elements("xpath", "//td[contains(text(),'Apple monitor 24')]")
        assert len(items) > 0, "Monitor not found in cart!"

    # ✅ 4. Add multiple products to cart
    def test_add_multiple_products(self):
        home = HomePage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)

        home.open_url("https://www.demoblaze.com/")

        # Add phone
        home.open_category("Phones")
        product.select_product("Samsung galaxy s6")
        product.add_to_cart()

        # Add laptop
        home.open_category("Laptops")
        product.select_product("Sony vaio i5")
        product.add_to_cart()

        cart.open_cart()
        cart.take_screenshot("cart_multiple.png")

        phones = self.driver.find_elements("xpath", "//td[contains(text(),'Samsung galaxy s6')]")
        laptops = self.driver.find_elements("xpath", "//td[contains(text(),'Sony vaio i5')]")

        assert len(phones) > 0 and len(laptops) > 0, "One or more products missing in cart!"

    # ✅ 5. Verify empty cart (no items)
    def test_empty_cart(self):
        home = HomePage(self.driver)
        cart = CartPage(self.driver)

        home.open_url("https://www.demoblaze.com/")
        cart.open_cart()
        cart.take_screenshot("cart_empty.png")

        items = self.driver.find_elements("xpath", "//td[contains(text(),'')]")
        assert len(items) == 0, "Cart is not empty when it should be!"
