import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class TestNavigation:
    def test_navigation_categories(self):
        home = HomePage(self.driver)
        home.open_url("https://www.demoblaze.com/")
        home.open_category("Laptops")
        home.scroll_down()
        home.open_category("Monitors")
