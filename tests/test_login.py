from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login():
    driver = get_driver()
    driver.get("https://app.sitestreamtech.com/")  # Replace with your login URL

    login_page = LoginPage(driver)
    login_page.enter_username("your_username")  # Replace with your actual username
    login_page.enter_password("your_password")  # Replace with your actual password
    login_page.click_login()

    # Wait for URL to contain "dashboard" or another expected element/condition
    wait = WebDriverWait(driver, 10)  
    wait.until(EC.url_contains("dashboard"))  # Or wait for a specific element

    assert "dashboard" in driver.current_url
    # ... rest of your test ...
