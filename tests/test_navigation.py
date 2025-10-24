import pytest
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestNavigation:

    # ✅ 1. Verify navigation to Laptops category
    def test_navigate_to_laptops(self):
        home = HomePage(self.driver)
        home.open_url("https://www.demoblaze.com/")
        home.open_category("Laptops")
        home.take_screenshot("navigate_laptops.png")

        # Verify URL or page title (basic validation)
        assert "Laptops" in self.driver.page_source, "Laptops category not loaded properly!"

    # ✅ 2. Verify navigation to Monitors category
    def test_navigate_to_monitors(self):
        home = HomePage(self.driver)
        home.open_url("https://www.demoblaze.com/")
        home.open_category("Monitors")
        home.take_screenshot("navigate_monitors.png")

        assert "Monitors" in self.driver.page_source, "Monitors category not loaded properly!"

    # ✅ 3. Verify navigation to Phones category
    def test_navigate_to_phones(self):
        home = HomePage(self.driver)
        home.open_url("https://www.demoblaze.com/")
        home.open_category("Phones")
        home.take_screenshot("navigate_phones.png")

        assert "Phones" in self.driver.page_source, "Phones category not loaded properly!"

    # ✅ 4. Verify scroll and navigation between categories
    def test_scroll_and_switch_categories(self):
        home = HomePage(self.driver)
        home.open_url("https://www.demoblaze.com/")

        home.open_category("Laptops")
        home.scroll_down()
        home.open_category("Monitors")
        home.scroll_down()
        home.take_screenshot("scroll_and_switch.png")

        assert "Monitors" in self.driver.page_source, "Category switch failed after scroll!"

    # ✅ 5. Verify Home button navigates back to main page
    def test_home_button_navigation(self):
        home = HomePage(self.driver)
        home.open_url("https://www.demoblaze.com/")

        home.open_category("Laptops")
        home.click_home_button()
        home.take_screenshot("home_button_navigation.png")

        # Verify we returned to the main/home view
        assert "Welcome to the store" in self.driver.page_source, "Home button did not navigate back properly!"
