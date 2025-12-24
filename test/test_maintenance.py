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
        login_page = LoginPage(driver)  
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        return driver
    
    def test_ohrm020_verify_admin_access_success(self, driver, login):
        maintenance_page = MaintenancePage(driver)
        dashboard_page = DashboardPage(driver)
        
        print("\n[Test] Navigating to Maintenance Mode (Valid Password)")
        dashboard_page.navigate_to_menu("Maintenance")
        maintenance_page.navigate_to_maintenance()
        maintenance_page.verify_access(Config.ADMIN_PASS)
        is_granted = maintenance_page.is_access_granted()
        assert is_granted == True, "Gagal masuk maintenance mode dengan password yang benar!"
    
    def test_ohrm021_verify_admin_access_invalid_pass(self, driver, login):
        maintenance_page = MaintenancePage(driver)
        dashboard_page = DashboardPage(driver)  
        
        print("\n[Test] Navigating to Maintenance Mode (Invalid Password)")
        dashboard_page.navigate_to_menu("Maintenance")
        maintenance_page.navigate_to_maintenance()
        maintenance_page.verify_access("WrongPass123!")
        
        error_msg = maintenance_page.get_error_message()
        print(f"[Test] Error Message Received: {error_msg}")
        assert "Invalid credentials" in error_msg

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])