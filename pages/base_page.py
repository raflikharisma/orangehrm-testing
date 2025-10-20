from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait =  WebDriverWait(driver, timeout)
        
    
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    