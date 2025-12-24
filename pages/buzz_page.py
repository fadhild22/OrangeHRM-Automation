from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class BuzzPage(BasePage):
    BUZZ_MENU = (By.XPATH, "//a[contains(@href, 'viewBuzzModule')]")
    
    POST_INPUT = (By.XPATH, "//textarea[contains(@class, 'oxd-buzz-post-input')]")
    POST_BTN = (By.XPATH, "//button[contains(., ' Post ')]")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".oxd-toast-content-text")
    
    FEED_CONTENT = (By.CLASS_NAME, "orangehrm-buzz-newsfeed")
    LATEST_POST_CONTAINER = (By.XPATH, "(//div[@class='oxd-grid-item oxd-grid-item--gutters'])[1]")
    LATEST_POST_TEXT = (By.XPATH, "(//div[@class='oxd-grid-item oxd-grid-item--gutters'])[1]//p[contains(@class, 'oxd-text--body-medium')]")
    
    LATEST_HEART_ICON = (By.XPATH, "(//div[@class='oxd-grid-item oxd-grid-item--gutters'])[1]//i[contains(@class, 'bi-heart')]")
    LATEST_KEBAB_MENU = (By.XPATH, "(//div[@class='oxd-grid-item oxd-grid-item--gutters'])[1]//button[.//i[contains(@class, 'bi-three-dots')]]")
    
    DELETE_OPTION = (By.XPATH, "//li[contains(., 'Delete Post')]")
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[contains(., ' Yes, Delete ')]")
    
    def navigate_to_buzz(self):
        self.click(self.BUZZ_MENU)
        self.wait.until(EC.visibility_of_element_located(self.POST_INPUT))
    
    def create_post(self, text):
        self.set_text(self.POST_INPUT, text)
        self.click(self.POST_BTN)
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TOAST))
            self.wait_until_invisible(self.SUCCESS_TOAST)
        except:
            pass
        self.wait.until(EC.text_to_be_present_in_element(self.FEED_CONTENT, text))
    
    def like_lates_post(self):
        self.wait.until(EC.element_to_be_clickable(self.LATEST_HEART_ICON))
        self.click(self.LATEST_HEART_ICON)
    
    def delete_latest_post(self):
        self.wait.until(EC.element_to_be_clickable(self.LATEST_KEBAB_MENU))
        self.click(self.LATEST_KEBAB_MENU)
        
        self.wait.until(EC.visibility_of_element_located(self.DELETE_OPTION))
        self.click(self.DELETE_OPTION)
        
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN))
        self.click(self.CONFIRM_DELETE_BTN)
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TOAST))