import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.admin_pages import AdminPage
from config import Config

class TestAdmin:
    
    def test_ohrm0006_add_new_admin_user(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        pim_page = PIMPage(driver)
        admin_page = AdminPage(driver)
        
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.click_add_employee()
        
        unique_id = Config.get_random_id()
        first_name = Config.EMP_FIRST_NAME
        last_name = f"{Config.EMP_LAST_NAME}{unique_id}"
        full_employee_name = f"{first_name} {last_name}"
        
        pim_page.fill_employee_data(first_name, last_name, unique_id)
        pim_page.click_save()
        pim_page.wait_for_save_completion()
        
        dashboard_page.navigate_to_menu("Admin")
        admin_page.click_add_user()
        
        new_username = f"admin_{unique_id}"
        print(f"\n[Data] Creating Admin User: {new_username} linked to {full_employee_name}")
        
        admin_page.fill_user_data(
            emp_name = full_employee_name,
            username = new_username,
            password = "Password123!",
            role = "Admin",
            status = "Enabled"
        )
        
        admin_page.click_save()
        assert "Success" in admin_page.get_success_message()
    
    def test_ohrm007_search_user_by_username(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        pim_page = PIMPage(driver)
        admin_page = AdminPage(driver)
        
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.click_add_employee()
        unique_id = Config.get_random_id()
        
        full_employee_name = f"{Config.EMP_FIRST_NAME} {Config.EMP_LAST_NAME}{unique_id}"
        pim_page.fill_employee_data(Config.EMP_FIRST_NAME, f"{Config.EMP_LAST_NAME}{unique_id}", unique_id)
        pim_page.click_save()
        pim_page.wait_for_save_completion()
        
        dashboard_page.navigate_to_menu("Admin")
        admin_page.click_add_user()
        target_username = f"search_{unique_id}"
        admin_page.fill_user_data(full_employee_name, target_username, "Password123!")
        admin_page.click_save()
        admin_page.wait_for_save_completion()
        
        try:
            admin_page.wait_for_save_completion()
        except:
            pass
        print(f"\n[Data] Searching User: {target_username}")
        admin_page.search_user(target_username)
    
    def test_ohrm008_add_username_exist(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        pim_page = PIMPage(driver)
        admin_page = AdminPage(driver)
        
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.click_add_employee()
        
        unique_id = Config.get_random_id()
        first_name = Config.EMP_FIRST_NAME
        last_name = f"{Config.EMP_LAST_NAME}{unique_id}"
        full_employee_name = f"{first_name} {last_name}"
        
        pim_page.fill_employee_data(first_name, last_name, unique_id)
        pim_page.click_save()
        pim_page.wait_for_save_completion()
        
        dashboard_page.navigate_to_menu("Admin")
        admin_page.click_add_user()
        target_username = Config.NEW_ADMIN_USER
        
        print(f"\n[Setup] Creating Initial User: {target_username}")
        admin_page.fill_user_data(full_employee_name, target_username, "Password123!")
        admin_page.click_save()
        admin_page.wait_for_save_completion()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(admin_page.SEARCH_BTN)
        )
        admin_page.click_add_user()
        print(f"[Negative Test] Input Duplicate Username from Config: {target_username}")
        admin_page.fill_user_data(full_employee_name, target_username, "Password123!")
        admin_page.verify_error_message_contains("Already exist")
        
        error_msg = admin_page.get_input_error_message()
        print(f"Error Message Found: {error_msg}")
        assert "Already exists" in error_msg
    
    def test_ohrm009_edit_user_details(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        pim_page = PIMPage(driver)
        admin_page = AdminPage(driver)
        
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.click_add_employee()
        unique_id = Config.get_random_id()
        full_employee_name = f"{Config.EMP_FIRST_NAME} {Config.EMP_LAST_NAME}{unique_id}"
        pim_page.fill_employee_data(Config.EMP_FIRST_NAME, f"{Config.EMP_LAST_NAME}{unique_id}", unique_id)
        pim_page.click_save()
        pim_page.wait_for_save_completion()
        
        dashboard_page.navigate_to_menu("Admin")
        admin_page.click_add_user()
        username_to_edit = f"edit_user_{unique_id}"
        admin_page.fill_user_data(full_employee_name, username_to_edit, "Password123!")
        admin_page.click_save()
        admin_page.wait_for_save_completion()
        
        print(f"\n[Data] Editing User: {username_to_edit}")
        admin_page.search_user(username_to_edit)
        admin_page.click_edit_user(username_to_edit)
        admin_page.select_user_role("ESS")
        admin_page.click_save()
        assert "Success" in admin_page.get_success_message()
    
    def test_ohrm010_add_new_job_title(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        admin_page = AdminPage(driver)
        
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        
        dashboard_page.navigate_to_menu("Admin")
        admin_page.navigate_to_job_titles()
        admin_page.click_add_user()
        
        unique_id = Config.get_random_id()
        new_job_title = f"{Config.NEW_JOB_TITLE} {Config.get_random_id()}"
        print(f"\n[Data] Creating Job Title: {new_job_title}")
        admin_page.fill_job_title(new_job_title)
        admin_page.click_save()
        assert "Success" in admin_page.get_success_message()
    
    def test_ohrm011_delete_job_title(self, driver):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        admin_page = AdminPage(driver)
        
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        
        dashboard_page.navigate_to_menu("Admin")
        admin_page.navigate_to_job_titles()
        admin_page.click_add_user()
        
        unique_id = Config.get_random_id()
        job_to_delete = f"Job To Delete {unique_id}"
        
        admin_page.fill_job_title(job_to_delete)
        admin_page.click_save()
        admin_page.wait_for_save_completion()
        
        print(f"\n[Data] Deleting Job Title: {job_to_delete}")
        admin_page.click_delete_icon_generic(job_to_delete)
        admin_page.confirm_delete()
        assert "Success" in admin_page.get_success_message()

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])