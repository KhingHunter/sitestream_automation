import pytest
import random
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.units_page import UnitsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_create_unit():
    driver = get_driver()
    driver.get("https://app.sitestreamtech.com/")  # Correct login URL

    login_page = LoginPage(driver)
    login_page.enter_username("josh@redskytech.io")  # Replace with your actual username
    login_page.enter_password("fat")  # Replace with your actual password
    login_page.click_login()

    # Wait for URL to contain "dashboard" or another expected element/condition
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("dashboard"))  # Or wait for a specific element

    assert "dashboard" in driver.current_url

    # Navigate to the Units page through the dashboard
    dashboard_units_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/units/list']")))  # Replace with the correct selector
    dashboard_units_link.click()

    units_page = UnitsPage(driver)
    units_page.click_create_unit()
    unit_name = f"Test Unit {random.randint(1000, 9999)}"
    units_page.enter_unit_name(unit_name)
    units_page.click_save()

    # Add assertions to verify unit creation
    # Example: Wait for a success message or check if the new unit appears in a list
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.ID, "success_message"), "Unit created successfully!"))
    driver.quit()

def test_create_unit_with_long_name():
    driver = get_driver()
    driver.get("https://app.sitestreamtech.com/")  # Correct login URL

    login_page = LoginPage(driver)
    login_page.enter_username("josh@redskytech.io")  # Replace with your actual username
    login_page.enter_password("fat")  # Replace with your actual password
    login_page.click_login()

    # Wait for URL to contain "dashboard" or another expected element/condition
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("dashboard"))  # Or wait for a specific element

    assert "dashboard" in driver.current_url

    # Navigate to the Units page through the dashboard
    dashboard_units_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/units/list']")))  # Replace with the correct selector
    dashboard_units_link.click()

    units_page = UnitsPage(driver)
    units_page.click_create_unit()

    unit_name = "Test Unit " + "A" * 255  # Long unit name

    units_page.enter_unit_name(unit_name)
    units_page.click_save()

    # Add assertions to verify unit creation
    # Example: Wait for a success message or check if the new unit appears in a list
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.ID, "success_message"), "Unit created successfully!"))
    driver.quit()