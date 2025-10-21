import pytest
from selenium.webdriver.common.by import By
from helpers import get_driver, close_driver, wait_for_element, read_data_from_excel

# Read test data from Excel
test_data = read_data_from_excel("data/test_data.xlsx", sheet_name="Sheet1")


@pytest.mark.parametrize("data", test_data)
def test_login_excel_data(data):
    driver = get_driver()

    # Click Login
    wait_for_element(driver, By.ID, "login2").click()

    # Enter username and password
    wait_for_element(driver, By.ID, "loginusername").clear()
    wait_for_element(driver, By.ID, "loginusername").send_keys(data["username"])
    wait_for_element(driver, By.ID, "loginpassword").clear()
    wait_for_element(driver, By.ID, "loginpassword").send_keys(data["password"])

    # Click login button
    wait_for_element(driver, By.XPATH, "//button[text()='Log in']").click()

    # Check login success or failure
    driver.implicitly_wait(5)
    try:
        user = wait_for_element(driver, By.ID, "nameofuser", timeout=5)
        print(f"✅ Login successful for: {data['username']}")
    except Exception:
        print(f"❌ Login failed for: {data['username']}")

    # Close browser
    close_driver(driver)
