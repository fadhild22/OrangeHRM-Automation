import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from config import Config

class TestPIM:
    def test_ohrm012_add_employee(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        pim_page = PIMPage(driver)
        
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.click_add_employee()
        unique_id = Config.get_random_id()
        
        print(f"\n[Data]Creating employee: {Config.EMP_FIRST_NAME} ID: {unique_id}")
        pim_page.fill_employee_data(Config.EMP_FIRST_NAME, Config.EMP_LAST_NAME, unique_id)
        
        pim_page.click_save()
        
        actual_msg = pim_page.get_success_message()
        assert "Success" in actual_msg, f"Employee creation failed! Message shown: {actual_msg}"
    
    def test_ohrm013_edit_employee(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        pim_page = PIMPage(driver)  
        
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        dashboard_page.navigate_to_menu("PIM")
        
        pim_page.click_add_employee()
        unique_id = Config.get_random_id()
        
        pim_page.fill_employee_data(Config.EMP_FIRST_NAME, Config.EMP_LAST_NAME, unique_id)
        pim_page.click_save()
        
        pim_page.wait_for_save_completion()
        
        dashboard_page.navigate_to_menu("PIM")
        full_name = f"{Config.EMP_FIRST_NAME} {Config.EMP_LAST_NAME}"
        pim_page.search_employee(full_name)
        
        pim_page.click_edit_icon(full_name)
        pim_page.fill_employee_data("Edited" + Config.EMP_FIRST_NAME, Config.EMP_LAST_NAME)
        pim_page.click_save()
        
        assert "Success" in pim_page.get_success_message()
    
    def test_ohrm014_delete_employee(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        pim_page = PIMPage(driver)  
        
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        dashboard_page.navigate_to_menu("PIM")
        
        pim_page.click_add_employee()
        unique_id = Config.get_random_id()
        name_to_delete = "ToBeDeleted"
        
        pim_page.fill_employee_data(name_to_delete, Config.EMP_LAST_NAME, unique_id)
        pim_page.click_save()
        pim_page.wait_for_save_completion()
        
        dashboard_page.navigate_to_menu("PIM")
        full_name = f"{name_to_delete} {Config.EMP_LAST_NAME}"
        pim_page.search_employee(emp_id=unique_id)
        pim_page.click_delete_icon(full_name)
        
        pim_page.confirm_delete()
        assert "Success" in pim_page.get_success_message()
    
if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])