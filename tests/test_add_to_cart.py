import pytest
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("setup")
class TestAddToCart:
    def test_add_to_cart(self):
        home = HomePage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)

        # Step 1: Open the website
        home.open_url("https://www.demoblaze.com/")

        # Step 2: Open the "Phones" category with a small wait
        try:
            home.open_category("Phones")
        except TimeoutException:
            self.driver.refresh()
            home.open_category("Phones")

        # Step 3: Select product with retry mechanism for stale elements
        for attempt in range(3):
            try:
                product.select_product()
                break
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
                self.driver.refresh()

        # Step 4: Add to cart and accept alert
        product.add_to_cart()

        # Step 5: Open cart page and verify item
        cart.open_cart()
        self.driver.implicitly_wait(5)

        # Step 6: Take a screenshot for report
        cart.take_screenshot("cart_page.png")

        # Step 7: Assertion to verify product added
        items = self.driver.find_elements("xpath", "//td[contains(text(),'Samsung galaxy s6')]")
        assert len(items) > 0, "Product not found in cart!"


