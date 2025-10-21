from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[text()='Add to cart']")
    PRODUCT_LINK = (By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]")

    def select_product(self):
        self.click(self.PRODUCT_LINK)
        time.sleep(2)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
