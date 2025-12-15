import pytest
from selenium import webdriver
from config import Config

@pytest.fixture(scope="function")
def driver():
    print("\n[UI Setup]Opening Chrome Browser....")
    
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-infobars')
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(Config.TIMEOUT)
    
    yield driver
    
    print("\n[UI Teardown] Closing browser...")
    driver.quit()