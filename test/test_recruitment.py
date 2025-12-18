import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.admin_pages import AdminPage
from pages.recruitment_page import RecruitmentPage
from config import Config

class TestRecruitment:
    @pytest.fixture
    def setup_data(self, driver):
        pim_page = PIMPage(driver)
        admin_page = AdminPage(driver)
        dashboard_page = DashboardPage(driver)
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.click_add_employee()
        unique_id = Config.get_random_id()
        
        manager_first = "Manager"
        manager_last = f"Test{unique_id}"
        manager_full_name = f"{manager_first} {manager_last}"
        
        pim_page.fill_employee_data(manager_first, manager_last, unique_id)
        pim_page.click_save()
        pim_page.wait_for_save_completion()
        
        dashboard_page.navigate_to_menu("Admin")
        admin_page.navigate_to_job_titles()
        admin_page.click_add_user()
        
        job_title = f"QA Engineer {unique_id}"
        admin_page.fill_job_title(job_title)
        admin_page.click_save()
        admin_page.wait_for_save_completion()
        
        return {
            "manager_name": manager_full_name,
            "job_title": job_title,
            "unique_id": unique_id
        }
        