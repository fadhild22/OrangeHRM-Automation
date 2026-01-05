import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from config import Config

class TestPIM:
    @pytest.fixture
    def login(self, driver):
        driver.maximize_window()
        login_page = LoginPage(driver)
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        return driver
    
    @pytest.fixture
    def created_employee(self, driver, login):
        pim_page = PIMPage(driver)
        dashboard_page = DashboardPage(driver)
        
        unique_id = Config.get_random_id()
        first_name = Config.EMP_FIRST_NAME
        last_name = f"{Config.EMP_LAST_NAME} {unique_id}"
        emp_id = unique_id
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.click_add_employee()
        pim_page.fill_employee_data(first_name, last_name, emp_id)
        pim_page.click_save()
        pim_page.wait_for_success_message()
        
        return {
            "first_name": first_name,
            "last_name": last_name,
            "emp_id": emp_id
        }
    
    @pytest.fixture
    def created_employee(self, driver, login):
        pim_page = PIMPage(driver)
        dashboard_page = DashboardPage(driver)
        
        unique_id = Config.get_random_id()
        first_name = Config.EMP_FIRST_NAME
        last_name = f"{Config.EMP_LAST_NAME} {unique_id}"
        emp_id = unique_id
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.click_add_employee()
        pim_page.fill_employee_data(first_name, last_name, emp_id)
        pim_page.click_save()
        pim_page.wait_for_save_completion()
        
        return {
            "first_name": first_name,
            "last_name": last_name,
            "emp_id": emp_id
        }
    
    def test_ohrm012_add_new_employee(self, driver, login):
        pim_page = PIMPage(driver)
        dashboard_page = DashboardPage(driver)
        unique_id = Config.get_random_id()
        print(f"\n[Test] Adding New Employee ID: {unique_id}")
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.click_add_employee()
        pim_page.fill_employee_data("Test", "User", unique_id)
        pim_page.click_save()
        success_message = pim_page.wait_for_save_completion()
        print(f"[DEBUG] Toast Message: '{success_message}'")
        assert "Success" in success_message
    
    def test_ohrm013_edit_employee(self, driver, created_employee):
        pim_page = PIMPage(driver)
        dashboard_page = DashboardPage(driver)
        target_id = created_employee['emp_id']
        new_first_name = "EditedName"
        print(f"\n[Test] Editing Employee ID: {target_id}")
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.search_employee(emp_id=target_id)
        pim_page.click_edit_icon(target_id)
        pim_page.wait_for_edit_page_load(created_employee['first_name'])
        pim_page.set_text(pim_page.FIRST_NAME_FIELD, new_first_name)
        pim_page.click_save()
        pim_page.wait_for_save_completion()
    
    def test_ohrm014_delete_employee(self, driver, created_employee):
        pim_page = PIMPage(driver)
        dashboard_page = DashboardPage(driver)
        target_id = created_employee['emp_id']
        print(f"\n[Test] Deleting Employee ID: {target_id}")
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.search_employee(emp_id=target_id)
        pim_page.click_delete_icon(target_id)
        pim_page.confirm_delete()
        pim_page.wait_for_save_completion()
    
if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])