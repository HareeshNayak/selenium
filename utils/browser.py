from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--remote-debugging-port=9222")
    # Ensure Chrome does NOT try to reuse a local profile
    options.add_argument("--user-data-dir=/tmp/unique-chrome-profile")

    driver = webdriver.Chrome(options=options)
    return driver
