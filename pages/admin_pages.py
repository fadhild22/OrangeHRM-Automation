from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AdminPage(BasePage):
    ADMIN_MENU = (By.XPATH, "//a[contains(@href, '/admin/viewAdminModule')]")
    ADD_BTN = (By.XPATH, "//button[text()=' Add ']")
    SAVE_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".oxd-toast-content-text")
    LOADER = (By.CLASS_NAME, "oxd-form-loader")
    
    USER_ROLE_DROPDOWN = (By.XPATH, "//label[text()='User Role']/parent::div/parent::div//div[contains(@class,'oxd-select-text')]")
    STATUS_DROPDOWN = (By.XPATH, "//label[text()='Status']/parent::div/parent::div//div[contains(@class,'oxd-select-text')]")
    
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//label[text()='Employee Name']/parent::div/parent::div//input")
    AUTOCOMPLETION_OPTION = (By.XPATH, "//div[@role='listbox']//span")
    USERNAME_FIELD = (By.XPATH, "//label[text()='Username']/parent::div/parent::div//input")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Password']/parent::div/parent::div//input")
    CONFIRM_PASS_FIELD = (By.XPATH, "//label[text()='Confirm Password']/parent::div/parent::div//input")
    
    SEARCH_USERNAME_FIELD = (By.XPATH, "//label[text()='Username']/parent::div/parent::div//input")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    
    FIELD_ERROR_MSG = (By.XPATH, "//span[contains(@class, 'oxd-input-field-error-message')]")
    JOB_MENU_DROPDOWN = (By.XPATH, "//span[contains(., 'Job')]")
    JOB_TITLES_ITEM = (By.XPATH, "//a[contains(., 'Job Titles')]")
    JOB_TITLE_FIELD = (By.XPATH, "//label[text()='Job Title']/parent::div/parent::div//input")
    
    def navigate_to_admin(self):
        self.click(self.ADMIN_MENU)
        self.wait.until(EC.url_contains("admin"))
    
    def click_add_user(self):
        self.click(self.ADD_BTN)
    
    def select_user_role(self, role_name="Admin"):
        self.click(self.USER_ROLE_DROPDOWN)
        option_xpath = f"//div[@role='listbox']//span[text()='{role_name}']"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, option_xpath)))
        self.click((By.XPATH, option_xpath))
    
    def select_status(self, status_name="Enabled"):
        self.click(self.STATUS_DROPDOWN)
        option_xpath = f"//div[@role='listbox']//span[text()='{status_name}']"
        self.wait.untill(EC.visibility_of_element_located((By.XPATH, option_xpath)))
        self.click((By.XPATH, option_xpath))
    
    def select_employee_name(self, emp_name):
        self.set_text(self.EMPLOYEE_NAME_INPUT, emp_name)
        self.wait.until(EC.visibility_of_element_located(self.AUTOCOMPLETION_OPTION))
        self.click(self.AUTOCOMPLETION_OPTION)
    
    def fill_user_data(self, emp_name, username, password, role="Admin", status="Enabled"):
        self.select_user_role(role)
        self.select_employee_name(emp_name)
        self.select_status(status)
        self.set_text(self.USERNAME_FIELD, username)
        self.set_text(self.PASSWORD_FIELD, password)
        self.set_text(self.CONFIRM_PASS_FIELD, password)
    
    def click_save(self):
        try:
            self.wait.untill(EC.invisibility_of_element_located(self.LOADER))
        except:
            pass
        self.wait.until(EC.invisibility_of_element_located(self.SAVE_BTN))
        self.click(self.SAVE_BTN)
    
    def get_success_message(self):
        return self.get_text(self.SUCCESS_TOAST)
    
    def search_user(self, username):
        self.set_text(self.SEARCH_USERNAME_FIELD, username)
        self.click(self.SEARCH_BTN)
        xpath_record = f"//div[@role='row' and contains(., '{username}')]"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_record)))
    
    def get_input_error_message(self):
        self.wait.until(EC.visibility_of_element_located(self.FIELD_ERROR_MSG))
        return self.get_text(self.FIELD_ERROR_MSG)
    
    def navigate_to_job_titles(self):
        self.click(self.JOB_MENU_DROPDOWN)
        self.wait.until(EC.visibility_of_element_located(self.JOB_TITLES_ITEM))
        self.click(self.JOB_TITLES_ITEM)
    
    def fill_job_title(self, title):
        self.set_text(self.JOB_TITLE_FIELD, title)
    
    def click_edit_user(self, username):
        row_xpath = f"//div[@role='row' and contains(., '{username}')]"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, row_xpath)))
        
        btn_xpath = f"{row_xpath}//button[.//i[contains(@class, 'bi-pencil-fill')]]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, btn_xpath)))
        self.click((By.XPATH, btn_xpath))
    
    def click_delete_icon_generic(self, item_name):
        row_xpath = f"//div[@role='row' and contains(., '{item_name}')]"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, row_xpath)))
        
        btn_xpath = f"{row_xpath}//button[.//i[contains@class, 'bi-trash']]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, btn_xpath)))
        self.click((By.XPATH, btn_xpath))