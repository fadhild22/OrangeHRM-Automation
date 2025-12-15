from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import Config 

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def open_url(self, url):
        self.driver.get(url)
    
    def find(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def set_text(self, locator, text):
        element = self.find(locator)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(text)
    
    def get_text(self, locator):
        return self.find(locator).text

    def select_dropdown(self, dropdown_locator, option_text):
        self.click(dropdown_locator)
        option_xpath = (By.XPATH, f"//div[@role='listbox']//span[text()='{option_text}']")
        self.click(option_xpath)
    
    def is_displayed(self, locator):
        try:
            self.find(locator)
            return True
        except:
            return False
    
    def get_toast_msg(self):
        TOAST_LOCATOR = (By.CSS_SELECTOR, ".oxd-toast-content-text")
        return self.get_text(TOAST_LOCATOR)
    
    def wait_until_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))