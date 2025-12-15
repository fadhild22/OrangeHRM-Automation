import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config import Config

class TestLogin:
    def test_ohrm001_login_valid(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        login_page.open_url(Config.BASE_URL_UI)
        
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        
        assert dashboard_page.get_header_title() == "Dashboard", "Login failed with valid credentials"
    
    def test_ohrm002_login_invalid(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(Config.BASE_URL_UI)
        
        login_page.login(Config.ADMIN_USER, Config.INVALID_PASS)
        
        assert login_page.get_error_message() == "Invalid credentials", "Error message not displayed for invalid login"
    
    def test_ohrm003_login_empty(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(Config.BASE_URL_UI)
        
        login_page.login(Config.EMPTY_USER, Config.ADMIN_PASS)
        
        assert login_page.get_required_message() == "Required", "Error message not displayed for empty username"
    
    def test_ohrm004_logout(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        login_page.open_url(Config.BASE_URL_UI)
        
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        dashboard_page.logout()
        
        assert login_page.is_displayed(LoginPage.LOGIN_BTN), "Logout failed, login button not displayed"
    
    def test_ohrm005_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(Config.BASE_URL_UI)
        
        login_page.click_forgot_password()
        
        actual_title = login_page.get_reset_title()
        assert actual_title == "Reset Password", f"Salah halaman! Munculnya: {actual_title}"
    
    if __name__ == "__main__":
        pytest.main(["-v", "-s", __file__])