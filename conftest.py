import pytest
from utils.driver_setup import get_driver

@pytest.fixture(scope="session")  # Or "function" scope if needed
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
