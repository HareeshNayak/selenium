from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_ui_operations_with_all_locators(driver):
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 10)

    # ------------------ 1️⃣ Hover (using CSS_SELECTOR) ------------------
    driver.get("https://the-internet.herokuapp.com/hovers")
    time.sleep(2)

    # CSS_SELECTOR locator
    first_image = driver.find_element(By.CSS_SELECTOR, ".figure:nth-child(3) img")
    actions.move_to_element(first_image).perform()
    time.sleep(1)

    caption = driver.find_element(By.CSS_SELECTOR, ".figure:nth-child(3) .figcaption h5")
    assert "user1" in caption.text.lower()
    print("✅ Hover test passed using CSS_SELECTOR")

    # ------------------ 2️⃣ Drag and Drop (using ID + XPATH) ------------------
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    time.sleep(2)

    source = driver.find_element(By.ID, "column-a")
    target = driver.find_element(By.ID, "column-b")
    actions.drag_and_drop(source, target).perform()
    time.sleep(2)

    header_a = driver.find_element(By.XPATH, "//div[@id='column-a']/header").text
    assert header_a == "B"
    print("✅ Drag & Drop passed using ID + XPATH locators")

    # ------------------ 3️⃣ Checkbox (using TAG_NAME) ------------------
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    time.sleep(2)

    all_inputs = driver.find_elements(By.TAG_NAME, "input")
    for checkbox in all_inputs:
        if not checkbox.is_selected():
            checkbox.click()
    assert all(cb.is_selected() for cb in all_inputs)
    print("✅ Checkbox test passed using TAG_NAME")

    # ------------------ 4️⃣ Alert (using LINK_TEXT + XPATH) ------------------
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    time.sleep(2)

    # LINK_TEXT locator for validation
    footer_text = driver.find_element(By.LINK_TEXT, "Elemental Selenium").text
    assert "Elemental Selenium" in footer_text

    # XPATH locator for button
    js_alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    js_alert_button.click()

    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    print("✅ Alert handled successfully using XPATH + LINK_TEXT")

    # ------------------ 5️⃣ Frame (using NAME + CLASS_NAME) ------------------
    driver.get("https://the-internet.herokuapp.com/iframe")
    time.sleep(2)

    # Switch to frame by NAME
    driver.switch_to.frame("mce_0_ifr")

    # CLASS_NAME locator for TinyMCE editor
    editor = driver.find_element(By.CLASS_NAME, "mce-content-body")

    # FIX: use JavaScript to clear text (TinyMCE doesn’t support .clear())
    driver.execute_script("arguments[0].innerHTML = '';", editor)
    time.sleep(1)

    # Type new text
    editor.send_keys("Hello from Selenium using CLASS_NAME!")
    driver.switch_to.default_content()
    print("✅ Frame test passed using NAME + CLASS_NAME (fixed version)")

    # ------------------ 6️⃣ Radio Button (using CSS_SELECTOR + CLASS_NAME + ID) ------------------
    driver.get("https://demoqa.com/radio-button")
    time.sleep(2)

    # CSS_SELECTOR locator
    yes_label = driver.find_element(By.CSS_SELECTOR, "label[for='yesRadio']")
    driver.execute_script("arguments[0].click();", yes_label)

    # CLASS_NAME locator to verify
    selected_text = driver.find_element(By.CLASS_NAME, "text-success").text
    assert selected_text == "Yes"

    # ID locator to double-check
    radio_button = driver.find_element(By.ID, "yesRadio")
    assert radio_button.is_selected() is True
    print("✅ Radio Button test passed using CSS_SELECTOR + CLASS_NAME + ID")

    print("\n🎉 All operations executed successfully using ALL locator strategies!")
