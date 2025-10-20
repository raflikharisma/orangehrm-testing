import unittest
from utils.driver import create_driver
from pages.login_page import LoginPage
from utils.config import VALID_USER

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = create_driver("edge")
        
    def setUp(self):
        self.driver.delete_all_cookies()
        self.login = LoginPage(self.driver).open()
        
    def test_elements_present(self):
        self.assertTrue(self.login.wait_visible(LoginPage.USERNAME_INPUT).is_displayed())
        self.assertTrue(self.login.wait_visible(LoginPage.PASSWORD_INPUT).is_displayed())
        self.assertTrue(self.login.wait_visible(LoginPage.SUBMIT).is_enabled())
        
    def test_valid_login(self):
        self.login.login_as(VALID_USER["username"], VALID_USER["password"])
        self.assertTrue(self.login.wait_visible(LoginPage.DASHBOARD).is_displayed())
        self.assertIn("dashboard",self.driver.current_url.lower())
        
    def test_empty_login(self):
        self.login.wait_clickable(LoginPage.SUBMIT).click()
        self.assertTrue(self.login.wait_visible(LoginPage.REQUIRED).is_displayed())
        

if __name__ == "__main__":
    unittest.main()
        