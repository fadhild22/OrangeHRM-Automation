import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    print("\n[UI Setup]Opening Chrome browser...")
    service_obj = Service(ChromeDriverManager().install())
    
    options = webdriver.ChromeOptions()
    options.add.argument("--start-maximized")
    
    driver = webdriver.Chrome(service=service_obj, options=options)
    driver.implicitly_wait(5)
    
    yield driver
    
    print("\n[UI Teardown]Closing Chrome browser...")
    driver.quit()
    