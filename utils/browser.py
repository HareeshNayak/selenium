from selenium import webdriver

def get_driver(browser_name="chrome"):
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Browser not supported")
    return driver
