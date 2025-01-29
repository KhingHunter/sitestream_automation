import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

@pytest.mark.dependency()

def test_valid_login():
    driver = get_driver()
    driver.get("https://app.sitestreamtech.com/")  # Correct login URL

    print("Navigated to login page")

    login_page = LoginPage(driver)
    
    try:
        wait = WebDriverWait(driver, 20)  # Increase timeout to 20 seconds
        username_field = wait.until(EC.presence_of_element_located(login_page.username_field))
        print("Username field found")
        username_field.send_keys("hunter@redskytech.io")  # Replace with your actual username
    except TimeoutException:
        print("Failed to find the username field")
        driver.save_screenshot("screenshot_username_field.png")  # Capture screenshot for debugging
        driver.quit()
        assert False, "Timeout while waiting for the username field"

    login_page.enter_password("fat")  # Replace with your actual password
    print("Entered password")
    login_page.click_login()
    print("Clicked login button")

    # Wait for URL to contain "dashboard" or another expected element/condition
    try:
        wait.until(EC.url_contains("dashboard"))  # Or wait for a specific element
        print("Navigated to dashboard")
    except TimeoutException:
        print("Failed to navigate to the dashboard")
        driver.save_screenshot("screenshot_dashboard.png")  # Capture screenshot for debugging
        driver.quit()
        assert False, "Timeout while waiting for the dashboard"

    assert "dashboard" in driver.current_url
    print("Login successful")
    driver.quit()
