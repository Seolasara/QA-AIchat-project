import time
from src.pages.login_page import LoginPage


def test_ACCT005_extreme_email_input(driver):
    login_page = LoginPage(driver)
    login_page.page_open()

    # 이메일 필드에 극단적 입력
    extreme_email = "team2@elice.com" + "asdf" * 10

    login_page.enter_email(extreme_email)
    login_page.enter_password(login_page.config["login_pw"])
    login_page.click_login_button()

    time.sleep(5)

    current_url = driver.current_url
    assert "accounts" in current_url.lower(), "[FAIL] 예상대로 로그인 페이지 유지X"
    print("⛔ [FAIL] 로그인 실패 - 이메일 혹은 비밀번호 불일치")