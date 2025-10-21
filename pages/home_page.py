from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    LOGIN_LINK = (By.ID, "login2")
    LOGOUT_LINK = (By.ID, "logout2")
    CATEGORY_PHONE = (By.LINK_TEXT, "Phones")
    CATEGORY_LAPTOPS = (By.LINK_TEXT, "Laptops")
    CATEGORY_MONITORS = (By.LINK_TEXT, "Monitors")

    def click_login(self):
        self.click(self.LOGIN_LINK)

    def logout(self):
        self.click(self.LOGOUT_LINK)

    def open_category(self, category_name):
        if category_name.lower() == "phones":
            self.click(self.CATEGORY_PHONE)
        elif category_name.lower() == "laptops":
            self.click(self.CATEGORY_LAPTOPS)
        elif category_name.lower() == "monitors":
            self.click(self.CATEGORY_MONITORS)
