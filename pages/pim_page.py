from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC        
from pages.base_page import BasePage
import time

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
            self.find(self.EMP_ID_FIELD).clear()
            self.set_text(self.EMP_ID_FIELD, emp_id)
    
    def click_save(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        except:
            pass
        time.sleep(1)
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
        self.click(self.SEARCH_BTN)
        try:
            self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        except:
            pass
        time.sleep(1)
    
    def click_edit_icon(self, employee_name):
        xpath_dynamic = f"//div[@role = 'row' and contains(., '{employee_name}')]//button[.//i[contains(@class, 'bi-pencil-fill')]]"
        self.click((By.XPATH, xpath_dynamic))

    def click_delete_icon(self, employee_name):
        xpath_dynamic = f"//div[@role='row' and contains(., '{employee_name}')]//button[.//i[contains(@class, 'bi-trash')]]"
        self.click((By.XPATH, xpath_dynamic))
    
    def confirm_delete(self):
        CONFIRM_BTN = (By.XPATH, "//button[contains(., ' Yes, Delete ')]") 
        self.click(CONFIRM_BTN)