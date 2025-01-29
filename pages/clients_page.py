from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClientsPage:
    def __init__(self, driver):
        self.driver = driver
        self.create_client_button = (By.CSS_SELECTOR, "button.create-client")  # Replace with the correct selector
        self.client_name_field = (By.ID, "clientName")  # Replace with the correct selector
        self.save_button = (By.CSS_SELECTOR, "button.save-client")  # Replace with the correct selector

    def click_create_client(self):
        wait = WebDriverWait(self.driver, 10)
        create_button = wait.until(EC.element_to_be_clickable(self.create_client_button))
        create_button.click()

    def enter_client_name(self, client_name):
        wait = WebDriverWait(self.driver, 10)
        name_field = wait.until(EC.presence_of_element_located(self.client_name_field))
        name_field.send_keys(client_name)

    def click_save(self):
        wait = WebDriverWait(self.driver, 10)
        save_button = wait.until(EC.element_to_be_clickable(self.save_button))
        save_button.click()