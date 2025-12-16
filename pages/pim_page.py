from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException        
from pages.base_page import BasePage

class PIMPage (BasePage):
    ADD_BTN = (By.XPATH, "//button[text()=' Add ']")
    FIRST_NAME_FIELD = (By.NAME, "firstName")
    LAST_NAME_FIELD = (By.NAME, "lastName")
    SAVE_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    EMP_ID_FIELD = (By.XPATH, "//label[text()='Employee Id']/parent::div/parent::div//input")
    
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".oxd-toast-content-text")
    LOADER = (By.CLASS_NAME, "oxd-form-loader")
    
    SEARCH_NAME_FIELD = (By.XPATH, "//label[text()='Employee Name']/parent::div/parent::div//input")
    SEARCH_ID_FIELD = (By.XPATH, "//label[text()='Employee Id']/parent::div/parent::div//input")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    
    def click_add_employee(self):
        self.click(self.ADD_BTN)
    
    def fill_employee_data(self, first_name, last_name, emp_id=None):
        self.set_text(self.FIRST_NAME_FIELD, first_name)   
        self.set_text(self.LAST_NAME_FIELD, last_name)
        if emp_id:
            self.find(self.EMP_ID_FIELD).send_keys("\ue003"*10)
            self.set_text(self.EMP_ID_FIELD, emp_id)
    
    def click_save(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        except:
            pass
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BTN))
        self.click(self.SAVE_BTN)
    
    def get_success_message(self):
        return self.get_text(self.SUCCESS_TOAST)
    
    def wait_for_save_completion(self):
        self.find(self.SUCCESS_TOAST)
        self.wait_until_invisible(self.SUCCESS_TOAST)
    
    def search_employee(self, name=None, emp_id=None):
        if name:
            self.set_text(self.SEARCH_NAME_FIELD, name)
        
        if emp_id:
            self.set_text(self.SEARCH_ID_FIELD, emp_id)
        short_wait = WebDriverWait(self.driver, 3)
        
        for attempt in range(3):
            self.click(self.SEARCH_BTN)
            try:
                self.wait.until(EC.invisibility_of_element_located(self.LOADER))
            except:
                pass
        
        if emp_id:
            xpath_record = f"//div[@role='row' and contains(., '{emp_id}')]"
            try:
                short_wait.until(EC.visibility_of_element_located((By.XPATH, xpath_record)))
                return
            except TimeoutException:
                pass
        
        if emp_id:
            xpath_record = f"//div[@role='row' and contains(., '{emp_id}')]"
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_record)))
    
    def click_edit_icon(self, value):
        row_xpath = f"//div[@role = 'row' and contains(., '{value}')]"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, row_xpath)))
        btn_xpath = f"{row_xpath}//button[.//i[contains(@class, 'bi-pencil-fill')]]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, btn_xpath)))
        self.click((By.XPATH, btn_xpath))
    
    def wait_for_edit_page_load(self, expected_firstname):
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, expected_firstname))
        
    def click_delete_icon(self, value):
        row_xpath = f"//div[@role='row' and contains(., '{value}')]"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, row_xpath)))
        btn_xpath = f"{row_xpath}//button[.//i[contains(@class, 'bi-trash')]]"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, btn_xpath)))
        self.click((By.XPATH, btn_xpath))
    
    def confirm_delete(self):
        CONFIRM_BTN = (By.XPATH, "//button[contains(., ' Yes, Delete ')]")
        self.wait.until(EC.element_to_be_clickable(CONFIRM_BTN))
        self.click(CONFIRM_BTN)