from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class RecruitmentPage(BasePage):
    RECRUITMENT_MENU = (By.XPATH, "//a[contains(@href, 'viewRecruitmentModule')]")
    VACANCIES_TAB = (By.XPATH, "//a[contains(text(), 'Vacancies')]")
    CANDIDATES_TAB = (By.XPATH, "//a[contains(text(), 'Candidates')]")
    
    ADD_BTN = (By.XPATH, "//button[contains(., ' Add ')]")
    SAVE_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".oxd-toast-content-text")
    LOADER = (By.CLASS_NAME, "oxd-form-loader")
    
    VACANCY_NAME_INPUT = (By.XPATH, "//label[text()='Vacancy Name']/parent::div/parent::div//input")
    JOB_TITLE_DROPDOWN = (By.XPATH, "//label[text()='Job Title']/parent::div/parent::div//div[contains(@class,'oxd-select-text')]")
    HIRING_MANAGER_INPUT = (By.XPATH, "//label[text()='Hiring Manager']/parent::div/parent::div//input")
    AUTOCOMPLETE_OPTION = (By.XPATH, "//div[@role='listbox']//span")
    
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/parent::div/parent::div//input")
    VACANCY_DROPDOWN = (By.XPATH, "//label[text()='Vacancy']/parent::div/parent::div//div[contains(@class,'oxd-select-text')]")
    
    SHORTLIST_BTN = (By.XPATH, "//button[contains(., 'Shortlist')]")
    WORKFLOW_SAVE_BTN = (By.XPATH, "//button[contains(., 'Save')]")
    STATUS_LABEL = (By.XPATH, "//p[contains(@class, 'oxd-text--subtitle-2')]")
    
    VACANCY_LIST_DROPDOWN = (By.XPATH, "//label[text()='Vacancy']/parent::div/parent::div//div[contains(@class,'oxd-select-text')]")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    DELETE_ICON = (By.XPATH, "//button[.//i[contains(@class, 'bi-trash')]]")
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[contains(., ' Yes, Delete ')]")
    
    def navigate_to_recruitment(self):
        self.click(self.RECRUITMENT_MENU)
        self.wait.until(EC.url_contains("recruitment"))
    
    def navigate_to_vacancies(self):
        self.click(self.VACANCIES_TAB)
        self.wait.until(EC.visibility_of_element_located(self.ADD_BTN))
    
    def navigate_to_candidate(self):
        self.click(self.CANDIDATES_TAB)
        self.wait.until(EC.visibility_of_element_located(self.ADD_BTN))
    
    def click_add(self):
        self.click(self.ADD_BTN)
    
    def select_dropdown_option(self, dropdown_locator, option_text):
        self.click(dropdown_locator)
        option_xpath = f"//div[@role='listbox']//span[contains(text(), '{option_text}')]"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, option_xpath)))
        self.click((By.XPATH, option_xpath))
    
    def fill_hiring_manager(self, manager_name):
        self.find(self.HIRING_MANAGER_INPUT).send_keys(Keys.CONTROL + "a")
        self.find(self.HIRING_MANAGER_INPUT).send_keys(Keys.BACK_SPACE)
        self.set_text(self.HIRING_MANAGER_INPUT, manager_name)
        try:
            self.wait.until(EC.visibility_of_element_located(self.AUTOCOMPLETE_OPTION))
            self.click(self.AUTOCOMPLETE_OPTION)
        except TimeoutException:
            print(f"Manager '{manager_name}' autocomplete missed. Retrying...")
            self.find(self.HIRING_MANAGER_INPUT).send_keys(Keys.BACK_SPACE)
            self.wait.until(EC.visibility_of_element_located(self.AUTOCOMPLETE_OPTION))
            self.click(self.AUTOCOMPLETE_OPTION)
    
    def fill_vacancy_form(self, name, job_title, manager):
        self.set_text(self.VACANCY_NAME_INPUT, name)
        self.select_dropdown_option(self.JOB_TITLE_DROPDOWN, job_title)
        self.fill_hiring_manager(manager)
    
    def fill_cadidate_form(self, first_name, last_name, email, vacancy_name):
        self.set_text(self.FIRST_NAME_INPUT, first_name)
        self.set_text(self.LAST_NAME_INPUT, last_name)
        self.set_text(self.EMAIL_INPUT, email)
        self.select_dropdown_option(self.VACANCY_DROPDOWN, vacancy_name)
    
    def click_save(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        except: pass
        self.click(self.SAVE_BTN)
    
    def wait_for_success_message(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TOAST))
            self.wait_until_invisible(self.SUCCESS_TOAST)
        except:
            print("Toast missed or too fast. Proceeding.")
    
    def shortlist_candidate(self):
        self.wait.until(EC.visibility_of_element_located(self.SHORTLIST_BTN))
        self.click(self.SHORTLIST_BTN)
        self.wait.until(EC.visibility_of_element_located(self.WORKFLOW_SAVE_BTN))
        self.click(self.WORKFLOW_SAVE_BTN)
        self.wait.until(EC.text_to_be_present_in_element(self.STATUS_LABEL, "Shortlisted"))
    
    def delete_vacancy(self, vacancy_name):
        self.navigate_to_vacancies()
        self.select_dropdown_option(self.VACANCY_LIST_DROPDOWN, vacancy_name)
        self.click(self.SEARCH_BTN)
        
        try:
            self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        except: pass
        
        self.wait.until(EC.element_to_be_clickable(self.DELETE_ICON))
        self.click(self.DELETE_ICON)
        
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN))
        self.click(self.CONFIRM_DELETE_BTN)
        self.wait_for_success_message()