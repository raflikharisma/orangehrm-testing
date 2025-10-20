import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

    def setUp(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_element_present(self):
        branding = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "orangehrm-login-branding"))
        )
        username = self.wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password = self.wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )

      
        self.assertTrue(branding.is_displayed())
        self.assertTrue(username.is_displayed())
        self.assertTrue(password.is_displayed())
        self.assertTrue(submit_btn.is_enabled())
        
    def test_valid_login(self):
        self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        self.wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
        self.assertIn("dashboard", self.driver.current_url.lower())

    def test_invalid_login(self):
        self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("testingInvalid123")
        self.wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("testingInvalid123")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        error_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")))
        self.assertIn("Invalid credentials", error_msg.text)
        
    def test_empty_login(self):
        self.wait.until.EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
