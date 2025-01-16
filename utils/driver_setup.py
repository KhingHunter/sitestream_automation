from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver(browser_name="chrome"):
    if browser_name.lower() == "chrome":
        service = Service(r'C:\Users\thech\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')  # Replace with your chromedriver path
        driver = webdriver.Chrome(service=service)
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox() 
    else:
        raise ValueError("Unsupported browser")
    return driver
