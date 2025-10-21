import pytest
from selenium.webdriver.common.by import By
from helpers import get_driver, close_driver, wait_for_element, read_data_from_csv

# Read test data
test_data = read_data_from_csv("data/login_data.csv")


@pytest.mark.parametrize("data", test_data)
def test_login_data_driven(data):
    driver = get_driver()

    # Click on login
    wait_for_element(driver, By.ID, "login2").click()

    # Enter username and password
    wait_for_element(driver, By.ID, "loginusername").clear()
    wait_for_element(driver, By.ID, "loginusername").send_keys(data["username"])
    wait_for_element(driver, By.ID, "loginpassword").clear()
    wait_for_element(driver, By.ID, "loginpassword").send_keys(data["password"])

    # Click login button
    wait_for_element(driver, By.XPATH, "//button[text()='Log in']").click()

    # Wait to see if login succeeds (you can assert using visible element)
    driver.implicitly_wait(5)

    try:
        user = wait_for_element(driver, By.ID, "nameofuser", timeout=5)
        print(f"✅ Login successful for: {data['username']}")
    except Exception:
        print(f"❌ Login failed for: {data['username']}")

    # Close browser
    close_driver(driver)
