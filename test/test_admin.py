import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.admin_page import AdminPage
from config import Config

class TestAdmin:
    @pytest.fixture
    def login(self, driver):
        driver.maximize_window()
        login_page = LoginPage(driver) 
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        WebDriverWait(driver, 15).until(EC.url_contains("dashboard"))
        return driver
    
    @pytest.fixture
    def setup_employee(self, driver, login):
        pim_page = PIMPage(driver)
        dashboard_page = DashboardPage(driver)
        
        first_name = Config.EMP_FIRST_NAME
        last_name = f"{Config.EMP_LAST_NAME} {Config.get_random_id()}"
        emp_id = Config.get_random_id()
        print(f"\n[Fixture] Creating PIM Employee: {first_name} {last_name}")
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.click_add_employee()
        pim_page.fill_employee_data(first_name, last_name, emp_id)
        pim_page.click_save()
        pim_page.wait_for_save_completion()
        return first_name
    
    @pytest.fixture
    def created_admin_user(self, driver, login):
        admin_page = AdminPage(driver)
        unique_id = Config.get_random_id()
        username = f"Adm{unique_id}"
        emp_name = getattr(Config, 'EMP_FIRST_NAME', "Riski")
        admin_page.navigate_to_admin()
        admin_page.click_add_user()
        
        admin_page.fill_user_data(emp_name, username, "Password123!", "Admin", "Enabled")
        admin_page.click_save()
        admin_page.wait_for_save_completion()
        return {
            "username": username,
            "emp_name": emp_name
        }
    
    @pytest.fixture
    def created_job_title(self, driver, login):
        admin_page = AdminPage(driver)
        unique_id = Config.get_random_id()
        job_title = f"{Config.NEW_JOB_TITLE} {unique_id}"
        
        admin_page.navigate_to_admin()
        admin_page.navigate_to_job_titles()
        admin_page.click_add_user()
        admin_page.fill_job_title(job_title)
        admin_page.click_save()
        admin_page.wait_for_save_completion()
        return job_title
    
    def test_ohrm006_add_new_admin_user(self, driver, setup_employee):
        admin_page = AdminPage(driver)
        username = f"New{Config.NEW_ADMIN_USER}{Config.get_random_id()}"
        emp_name = setup_employee
        print(f"\n[Test] Adding Admin User: {username} linked to {emp_name}")
        
        admin_page.navigate_to_admin()
        admin_page.click_add_user()
        admin_page.fill_user_data(emp_name, username, "Password123!", "Admin", "Enabled")
        admin_page.click_save()
        
        success_msg = admin_page.wait_for_save_completion()
        if success_msg:
            assert "Success" in success_msg
        admin_page.search_user(username)
    
    def test_ohrm007_search_by_username(self, driver, created_admin_user):
        admin_page = AdminPage(driver)
        target_user = created_admin_user['username']
        print(f"\n[Test] Searching: {target_user}")
        admin_page.navigate_to_admin()
        admin_page.search_user(target_user)
    
    def test_ohrm008_add_user_username_exist(self, driver, created_admin_user):
        admin_page = AdminPage(driver)
        existing_user = created_admin_user['username']
        emp_name = created_admin_user['emp_name']
        
        print(f"\n[Test] Negative Test Duplicate: {existing_user}")
        admin_page.navigate_to_admin()
        admin_page.click_add_user()
        admin_page.fill_user_data(emp_name, existing_user, "Password123!", "ESS", "Enabled")
        admin_page.click_save()
        msg = admin_page.get_input_error_message()
        assert "Already exists" in msg
    
    def test_ohrm009_edit_user_details(self, driver, created_admin_user):
        admin_page = AdminPage(driver)
        old_user = created_admin_user['username']
        new_user = f"Edit{Config.get_random_id()}"
        
        print(f"\n[Test] Edit User: {old_user} -> {new_user}")
        admin_page.navigate_to_admin()
        admin_page.search_user(old_user)
        admin_page.click_edit_user(old_user)
        
        admin_page.click(admin_page.USERNAME_FIELD)
        admin_page.find(admin_page.USERNAME_FIELD).send_keys("\ue003" * 30)
        admin_page.set_text(admin_page.USERNAME_FIELD, new_user)
        admin_page.click_save()
        admin_page.wait_for_save_completion()
        admin_page.navigate_to_admin()
        
        print(f"[Test] Searching New User: {new_user}")
        admin_page.search_user(new_user)
        assert admin_page.verify_user_in_list(new_user) == True
    
    def test_ohrm010_add_new_job(self, driver, login):
        admin_page = AdminPage(driver)
        job_title = f"{Config.NEW_JOB_TITLE} {Config.get_random_id()}"
        
        print(f"\n[Test] Add Job: {job_title}")
        admin_page.navigate_to_admin()
        admin_page.navigate_to_job_titles()
        admin_page.click_add_user()
        admin_page.fill_job_title(job_title)
        admin_page.click_save()
        admin_page.wait_for_save_completion()
    
    def test_ohrm011_delete_job(self, driver, created_job_title):
        admin_page = AdminPage(driver)
        target_job = created_job_title
        
        print(f"\n[Test] Delete Job: {target_job}")
        admin_page.navigate_to_admin()
        admin_page.navigate_to_job_titles()
        admin_page.click_delete_icon_generic(target_job)
        admin_page.confirm_delete()
        admin_page.wait_for_save_completion()

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])