import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login_logout(self):
        home = HomePage(self.driver)
        login = LoginPage(self.driver)

        home.open_url("https://www.demoblaze.com/")
        home.click_login()
        login.login("hareesh", "hareesh")  # Replace with valid credentials
        home.logout()
