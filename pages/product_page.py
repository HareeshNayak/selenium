from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[text()='Add to cart']")
    PRODUCT_LINK = (By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]")

    def select_product(self):
        # Wait until the product link is clickable and click it
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_LINK)).click()

        # Wait until the "Add to cart" button is visible on the new page
        self.wait.until(EC.visibility_of_element_located(self.ADD_TO_CART_BUTTON))

    def add_to_cart(self):
        # Wait until the add to cart button is clickable and click
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()

        # Wait for the alert and accept it
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

