from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_LINK = (By.ID, "cartur")
    DELETE_BUTTON = (By.XPATH, "//a[text()='Delete']")

    def open_cart(self):
        self.click(self.CART_LINK)

    def delete_item(self):
        self.click(self.DELETE_BUTTON)
