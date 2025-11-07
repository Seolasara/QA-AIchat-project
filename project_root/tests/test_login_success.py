import time
from src.pages.login_page import LoginPage

def test_helpychat_login(driver):
    login_page = LoginPage(driver)
    login_page.page_open()
    login_page.login()
    time.sleep(5)
    assert "qaproject.elice.io" in driver.current_url
    print("✅ HelpyChat 로그인 성공!")
