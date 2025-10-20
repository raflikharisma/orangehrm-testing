import unittest
from utils.driver import create_driver
from pages.login_page import LoginPage
from utils.config import VALID_USER, INVALID_PASSWORD

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = create_driver()
        
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
        
    def test_invalid_login_wrong_username(self):
        """TC-LOGIN-004: Username salah, password benar"""
        self.login.login_as("wronguser", "admin123")
        error = self.login.wait_visible(LoginPage.ERROR_TEXT)
        self.assertIn("Invalid credentials", error.text)

    def test_invalid_login_wrong_password(self):
        """TC-LOGIN-005: Username benar, password salah"""
        self.login.login_as("Admin", "wrongpass")
        error = self.login.wait_visible(LoginPage.ERROR_TEXT)
        self.assertIn("Invalid credentials", error.text)

    def test_invalid_login_wrong_both(self):
        """TC-LOGIN-006: Username dan password salah"""
        self.login.login_as("fakeuser", "fakepass")
        error = self.login.wait_visible(LoginPage.ERROR_TEXT)
        self.assertIn("Invalid credentials", error.text)

    def test_invalid_login_empty_username(self):
        """TC-LOGIN-007: Username kosong"""
        self.login.login_as("", "admin123")
        required = self.login.wait_visible(LoginPage.REQUIRED)
        self.assertTrue(required.is_displayed())

    def test_invalid_login_empty_password(self):
        """TC-LOGIN-008: Password kosong"""
        self.login.login_as("Admin", "")
        required = self.login.wait_visible(LoginPage.REQUIRED)
        self.assertTrue(required.is_displayed())


if __name__ == "__main__":
    unittest.main()
        