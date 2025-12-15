from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    HEADER_TITLE = (By.XPATH, "//h6[contains(@class, 'oxd-topbar-header-breadcrumb-module')]")
    
    USER_DROPDOWN = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")
    
    def get_header_title(self):
        return self.get_text(self.HEADER_TITLE)
    
    def logout(self):
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_LINK)

    def navigate_to_menu(self, menu_name):
        MENU_LOCATOR = (By.LINK_TEXT, menu_name)
        self.click(MENU_LOCATOR)