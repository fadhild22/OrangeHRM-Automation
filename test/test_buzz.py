import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.buzz_page import BuzzPage
from config import Config

class TestBuzz:
    @pytest.fixture
    def login(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(Config.BASE_URL_UI)
        login_page.login(Config.ADMIN_USER, Config.ADMIN_PASS)
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    
    def test_ohrm019_create_like_delete_buzz_post(self, driver, login):
        buzz_page = BuzzPage(driver)
        dashboard_page = DashboardPage(driver)
        
        unique_id = Config.get_random_id()
        base_text = getattr(Config, 'BUZZ_POST_TEXT', 'Test Status Update')
        post_content = f"{base_text} {unique_id}"
        
        dashboard_page.navigate_to_menu()
        buzz_page.navigate_to_buzz()
        print(f"\n[Test] Creating Post: {post_content}")
        buzz_page.create_post(post_content)
        print("[Test] Liking the latest post...")
        buzz_page.like_lates_post()
        print("[Test] Deleting the latest post...")
        buzz_page.delete_latest_post()

if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])