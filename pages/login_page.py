from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "email")
        self.password_field = (By.CSS_SELECTOR, "inputtype='password']")  
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")  

    def enter_username(self, username):
        wait = WebDriverWait(self.driver, 10)
        username_field = wait.until(EC.presence_of_element_located(self.username_field))
        username_field.send_keys(username)

    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        password_field = wait.until(EC.presence_of_element_located(self.password_field))
        password_field.send_keys(password)

    def click_login(self):
        wait = WebDriverWait(self.driver, 10)
        login_button = wait.until(EC.element_to_be_clickable(self.login_button))
        login_button.click()
