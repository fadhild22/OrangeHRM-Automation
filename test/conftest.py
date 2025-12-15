import pytest
import os
from selenium import webdriver
from config import Config

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function")
def driver(request):
    print("\n[UI Setup]Opening Chrome Browser....")
    
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-infobars')
    options.add_argument('--ignore-certificate-errors')
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(Config.TIMEOUT)
    
    yield driver
    
    node = request.node
    if hasattr(node, "rep_call") and node.rep_call.failed:
        print("\n[Test Failed] Taking screenshot...")
        
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        file_name = f"{request.node.name}.png"
        file_path = os.path.join(screenshot_dir, file_name)
        
    try:
        driver.save_screenshot(file_path)
        print(f"[Screenshot Saved] {file_path}")
    except Exception as e:
        print(f"[Screenshot Failed] {e}")
    
    print("\n[UI Teardown] Closing browser...")
    driver.quit()