from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage): 
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password") 
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    
    ERROR_ALERT = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    REQUIRED_MSG = (By.XPATH, "//span[contains(@class, 'oxd-input-field-error-message')]")
    
    FORGOT_PASS_LINK = (By.CSS_SELECTOR, ".orangehrm-login-forgot-header")
    RESET_PAGE_TITLE = (By.XPATH, "//h6[text()='Reset Password']")
    
    def login(self, username, password):
        if username:
            self.set_text(self.USERNAME_FIELD, username)
        
        if password:
            self.set_text(self.PASSWORD_FIELD, password)
        
        self.click(self.LOGIN_BTN)
    
    def get_error_message(self):
        return self.get_text(self.ERROR_ALERT)
    
    def get_required_message(self):
        return self.get_text(self.REQUIRED_MSG)
    
    def click_forgot_password(self):
        self.click(self.FORGOT_PASS_LINK)
    
    def get_reset_title(self):
        return self.get_text(self.RESET_PAGE_TITLE)