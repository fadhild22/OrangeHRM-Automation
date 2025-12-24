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
from pages.recruitment_page import RecruitmentPage
from config import Config

class TestRecruitment:
    @pytest.fixture
    def login_admin(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        return driver
    
    @pytest.fixture
    def hiring_manager(self, driver, login_admin):
        pim_page = PIMPage(driver)
        dashboard_page = DashboardPage(driver)
        unique_id = Config.get_random_id()
        
        manager_first = Config.EMP_FIRST_NAME
        manager_last = f"{Config.EMP_LAST_NAME} {unique_id}"
        
        dashboard_page.navigate_to_menu("PIM")
        pim_page.click_add_employee()
        pim_page.fill_employee_data(manager_first, manager_last, unique_id)
        pim_page.click_save()
        pim_page.wait_for_success_message()
        return {
            "name": f"{manager_first} {manager_last}",
            "id": unique_id
        }
    
    @pytest.fixture
    def job_title(self, driver, login_admin):
        admin_page = AdminPage(driver)
        dashboard_page = DashboardPage(driver)
        unique_id = Config.get_random_id()
        
        title_name = f"{Config.NEW_JOB_TITLE} {unique_id}"
        dashboard_page.navigate_to_menu("Admin")
        admin_page.navigate_to_job_titles()
        admin_page.click_add_user()
        admin_page.fill_job_title(title_name)
        admin_page.click_save()
        try:
            admin_page.wait_for_save_completion()
        except AttributeError:
            admin_page.wait_for_success_message()
        return{
            "name": title_name,
            "id": unique_id
        }

    
    @pytest.fixture
    def active_vacancy(self, driver, hiring_manager, job_title):
        recruitment_page = RecruitmentPage(driver)
        dashboard_page = DashboardPage(driver)
        
        vacancy_name = f"{Config.NAME_VACANCY} {hiring_manager['id']}"
        
        dashboard_page.navigate_to_menu("Recruitment")
        recruitment_page.navigate_to_vacancies()
        recruitment_page.click_add()
        recruitment_page.fill_vacancy_form(vacancy_name, job_title['name'], hiring_manager['name'])
        recruitment_page.click_save()
        recruitment_page.wait_for_success_message()
        return {
            "vacancy_name": vacancy_name,
            "job_data": job_title,
            "manager_data": hiring_manager
        }
    
    def test_ohrm017_add_new_vacancy(self, driver, hiring_manager, job_title):
        recruitment_page = RecruitmentPage(driver)
        dashboard_page = DashboardPage(driver)
        
        vacancy_name = f"{Config.NAME_VACANCY} {hiring_manager['id']}"
        
        dashboard_page.navigate_to_menu("Recruitment")
        recruitment_page.navigate_to_vacancies()
        recruitment_page.click_add()
        print(f"\n[Test] Creating Vacancy: {vacancy_name}")
        recruitment_page.fill_vacancy_form(vacancy_name, job_title['name'], hiring_manager['name'])
        recruitment_page.click_save()
        recruitment_page.wait_for_success_message()
        assert "addJobVacancy" in driver.current_url
    
    def test_ohrm015_and_016_add_new_candidate_and_shortlist(self, driver, active_vacancy):
        recruitment_page = RecruitmentPage(driver)
        data = active_vacancy
        
        recruitment_page.navigate_to_candidate()
        recruitment_page.click_add()
        
        cand_first = Config.CANDIDATE_FIRST_NAME
        cand_last = f"{Config.CANDIDATE_LAST_NAME} {data['manager_data']['id']}"
        cand_email = f"test{data['manager_data']['id']}@mail.com"
        print(f"\n[Test] Adding Candidate: {cand_first} {cand_last}")
        recruitment_page.fill_candidate_form(cand_first, cand_last, cand_email, data['vacancy_name'])
        recruitment_page.click_save()
        recruitment_page.wait_for_success_message()
        recruitment_page.shortlist_candidate()
    
    def test_ohrm018_delete_vacancy(self, driver, active_vacancy):
        recruitment_page = RecruitmentPage(driver)
        
        target_vacancy = active_vacancy['vacancy_name']
        print(f"\n[Test] Deleting Vacancy: {target_vacancy}")
        recruitment_page.delete_vacancy(target_vacancy)
    
if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])