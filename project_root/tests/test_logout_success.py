import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage


# 로그아웃 테스트
def test_ACCT009_logout_success(driver,login):
    wait = WebDriverWait(driver, 10)

    # 로그인
    assert "qaproject.elice.io" in driver.current_url, "[FAIL] 로그인 실패"
    print("✅ [PASS] 로그인 성공")


    # 로그아웃 시도 / 프로필 클릭
    profile = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='PersonIcon']"))
    )
    profile.click()

    # 프로필이 뜰 때까지 대기
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-elice-user-profile-content='true']"))
    )

    # UI가 완전히 뜰 때까지 조금 더 대기(다른 요소에 의한 요소 가림 방지) 
    time.sleep(1)

    # 로그아웃 버튼 클릭
    logout_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='로그아웃']"))
    )
    logout_button.click()
    
    time.sleep(5)

    assert "accounts" in driver.current_url.lower(), "[FAIL] 로그아웃 실패"
    print("✅ [PASS] 로그아웃 성공")


