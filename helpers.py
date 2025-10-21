import os
import time
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(browser_name="chrome", headless=False):
    """Initialize the browser driver."""
    if browser_name.lower() == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")  # Important for CI
        options.add_argument("--disable-dev-shm-usage")  # For CI environments
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")

        # Use a temporary user data directory
        tmp_user_data_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={tmp_user_data_dir}")

        if headless:
            options.add_argument("--headless=new")  # use new headless mode
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    elif browser_name.lower() == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        from webdriver_manager.firefox import GeckoDriverManager

        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        raise Exception("Unsupported browser! Use 'chrome' or 'firefox'.")

    driver.get("https://www.demoblaze.com/")
    driver.implicitly_wait(10)
    return driver




# -------------------- WAIT UTILITIES --------------------
def wait_for_element(driver, by, locator, timeout=10):
    """Wait for element to be visible and return it."""
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))


# -------------------- SCREENSHOT --------------------
def take_screenshot(driver, name="screenshot"):
    """Takes a screenshot with timestamp."""
    folder = "reports/screenshots"
    os.makedirs(folder, exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    path = os.path.join(folder, f"{name}_{timestamp}.png")
    driver.save_screenshot(path)
    return path


# -------------------- DATA READING --------------------
def read_data_from_csv(file_path):
    """Reads test data from a CSV file."""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


def read_data_from_excel(file_path, sheet_name="Sheet1"):
    """Reads test data from an Excel file using pandas."""
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df.to_dict(orient="records")


# -------------------- CLEANUP --------------------
def close_driver(driver):
    """Close the browser safely."""
    if driver:
        driver.quit()
