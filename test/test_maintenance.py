import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.maintenance_page import MaintenancePage
from config import Config

class TestMaintenance:
    @pytest.fixture
    def login(self, driver):
        driver.maximize_window()
        login_page = LoginPage(driver)  
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        return driver
    
    def test_ohrm019_verify_admin_access_success(self, driver, login):
        maintenance_page = MaintenancePage(driver)
        maintenance_page.navigate_to_maintenance()
        print(f"\n[Test] Attempting access with VALID Password...")
        
        maintenance_page.verify_access(Config.ADMIN_PASS)
        is_granted = maintenance_page.is_access_granted()
        assert is_granted == True, "Failed to access Maintenance Mode with valid password!"
        print("[Test] Access Granted Successfully.")
    
    def test_ohrm020_verify_admin_access_invalid_pass(self, driver, login):
        maintenance_page = MaintenancePage(driver)
        maintenance_page.navigate_to_maintenance()
        wrong_pass = getattr(Config, 'INVALID_PASS', 'password_salah')
        print(f"\n[Test] Attempting access with INVALID Password: {wrong_pass}")
        maintenance_page.verify_access(wrong_pass)
        
        actual_error = maintenance_page.get_error_message()
        print(f"[Test] Error Message Received: {actual_error}")
        assert "Invalid credentials" in actual_error

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])