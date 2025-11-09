import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage


# 재로그인 테스트
def test_ACCT008_relogin_success(driver,login):
    wait = WebDriverWait(driver, 10)

    # 로그인
    assert "qaproject.elice.io" in driver.current_url, "[FAIL] 로그인 실패"
    print("✅ [PASS] 로그인 성공")


    # 로그아웃 시도
    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='PersonIcon']"))
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-elice-user-profile-content='true']"))
    )
     
    time.sleep(1) # UI가 완전히 뜰 때까지 조금 더 대기(다른 요소에 의한 요소 가림 방지)

    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='로그아웃']"))
    ).click()


    # 로그아웃 후 비밀번호 입력칸이 보일 때까지 대기
    wait.until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )
    assert "accounts" in driver.current_url.lower(), "[FAIL] 로그아웃 실패"
    print("✅ [PASS] 로그아웃 성공")


    # 이메일 연동된 상태에서 비밀번호만 입력하여 재로그인
    relogin_page = LoginPage(driver)
    relogin_page.enter_password(relogin_page.config["login_pw"])
    relogin_page.click_login_button()

    time.sleep(5)
    assert "qaproject.elice.io" in driver.current_url, "[FAIL] 재로그인 실패"
    print("✅ [PASS] 재로그인 성공")
