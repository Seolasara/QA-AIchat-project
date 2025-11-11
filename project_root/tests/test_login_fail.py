import time
from src.pages.login_page import LoginPage


# --- 잘못된 이메일 케이스 3개 ---

def test_ACCT003_invalid_email_domain(driver):
    login_page = LoginPage(driver)
    login_page.page_open()

    # 잘못된 이메일 입력(도메인X)
    wrong_email = "team2"

    login_page.enter_email(wrong_email)
    login_page.enter_password(login_page.config["login_pw"])
    login_page.click_login_button()

    time.sleep(1)

    current_url = driver.current_url
    assert "accounts" in current_url.lower(), "[FAIL] 예상대로 로그인 페이지 유지X"
    print("❎ [XFAIL] 로그인 실패 - 이메일 도메인 불일치")


def test_ACCT004_invalid_email(driver):
    login_page = LoginPage(driver)
    login_page.page_open()

    # 잘못된 이메일 입력
    wrong_email = "team1@elice.com"

    login_page.enter_email(wrong_email)
    login_page.enter_password(login_page.config["login_pw"])
    login_page.click_login_button()

    time.sleep(1)

    current_url = driver.current_url
    assert "accounts" in current_url.lower(), "[FAIL] 예상대로 로그인 페이지 유지X"
    print("❎ [XFAIL] 로그인 실패 - 이메일 혹은 비밀번호 불일치")


def test_ACCT005_extreme_email_input(driver):
    login_page = LoginPage(driver)
    login_page.page_open()

    # 이메일 필드에 극단적 입력
    extreme_email = "team2@elice.com" + "asdf" * 10

    login_page.enter_email(extreme_email)
    login_page.enter_password(login_page.config["login_pw"])
    login_page.click_login_button()

    time.sleep(1)

    current_url = driver.current_url
    assert "accounts" in current_url.lower(), "[FAIL] 예상대로 로그인 페이지 유지X"
    print("❎ [XFAIL] 로그인 실패 - 이메일 혹은 비밀번호 불일치")


# --- 잘못된 비밀번호 케이스 2개 ---

def test_ACCT006_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.page_open()

    # 잘못된 비밀번호 입력
    wrong_password = "team2elice!"

    login_page.enter_email(login_page.config["login_id"])
    login_page.enter_password(wrong_password)
    login_page.click_login_button()

    time.sleep(1)

    current_url = driver.current_url
    assert "accounts" in current_url.lower(), "[FAIL] 예상대로 로그인 페이지 유지X"
    print("❎ [XFAIL] 로그인 실패 - 이메일 혹은 비밀번호 불일치")



def test_ACCT007_extreme_password_input(driver):
    login_page = LoginPage(driver)
    login_page.page_open()

    # 잘못된 비밀번호 입력
    extreme_password = "team2elice!@" + "@" * 30

    login_page.enter_email(login_page.config["login_id"])
    login_page.enter_password(extreme_password)
    login_page.click_login_button()

    time.sleep(1)

    current_url = driver.current_url
    assert "accounts" in current_url.lower(), "[FAIL] 예상대로 로그인 페이지 유지X"
    print("❎ [XFAIL] 로그인 실패 - 이메일 혹은 비밀번호 불일치")