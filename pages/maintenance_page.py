from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class MaintenancePage(BasePage):
    MAINTENANCE_MENU = (By.XPATH, "//a[contains(@href, 'viewMaintenanceModule')]")
    
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MSG = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")
    
    PURGE_TITLE = (By.XPATH, "//h6[contains(text(), 'Purge Employee Records')]")

    def navigate_to_maintenance(self):
        self.click(self.MAINTENANCE_MENU)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
    
    def verify_access(self, password):
        self.set_text(self.PASSWORD_INPUT, password)
        self.click(self.CONFIRM_BTN)
    
    def is_access_granted(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.PURGE_TITLE))
            return True
        except:
            return False
    
    def get_error_message(self):
        self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG))
        return self.get_text(self.ERROR_MSG)