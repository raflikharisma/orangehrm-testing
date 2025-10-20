from selenium.webdriver.common.by import By
from utils.config import BASE_URL, DEFAULT_TIMEOUT
from .base_page import BasePage

class LoginPage(BasePage):
    URL = BASE_URL
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT = (By.XPATH, "//button[@type='submit]")
    DASHBOARD = (By.XPATH, "//h6[text()='Dashboard]")
    ERROR_TXT =(By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
    REQUIRED = (By.XPATH, "//span[text()='Required']")
    
    def __init__(self, driver):
        super().__init__(driver, DEFAULT_TIMEOUT)
        
    def open(self):
        self.driver.get(self.URL)
        return self
    
    def login_as(self, username, password):
        self.wait_visible(self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.wait_clickable(self.SUBMIT).click()
        
        
    


    