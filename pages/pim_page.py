from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PIMPage (BasePage):
    ADD_BTN = (By.XPATH, "//button[text()=' Add ']")
    FIRST_NAME_FIELD = (By.NAME, "firstName")
    LAST_NAME_FIELD = (By.NAME, "lastName")
    SAVE_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".oxd-toast-content-text")
    
    SEARCH_NAME_FIELD = (By.XPATH, "//label[text()='Employee Name']/parent::div/parent::div//input")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    EDIT_ICON = (By.XPATH, "//div[@role='table']//button[contains(.,'bi-pencil-fil')]")
    DELETE_ICON = (By.XPATH, "//div[@role='table']//button[contains(.,'bi-trash')]")
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[contains(.,' Yes, Delete ')]")
    
    def click_add_employee(self):
        self.click(self.ADD_BTN)
    
    def fill_employee_data(self, first_name, last_name):
        self.set_text(self.FIRST_NAME_FIELD, first_name)   
        self.set_text(self.LAST_NAME_FIELD, last_name)
    
    def click_save(self):
        self.click(self.SAVE_BTN)
    
    def get_success_message(self):
        return self.get_text(self.SUCCESS_TOAST)
    
    def wait_for_save_completion(self):
        self.find(self.SUCCESS_TOAST)
        self.wait_until_invisible(self.SUCCESS_TOAST)
    
    def search_employee(self, full_name):
        self.set_text(self.SEARCH_NAME_FIELD, full_name)
        self.click(self.SEARCH_BTN)
    
    def click_edit_icon(self):
        self.click(self.EDIT_ICON)
    
    def click_delete_icon(self):
        self.click(self.DELETE_ICON)
    
    def confirm_delete(self):
        self.click(self.CONFIRM_DELETE_BTN)