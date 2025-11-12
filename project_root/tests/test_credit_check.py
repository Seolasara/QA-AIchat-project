import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage

def test_BILL001_credit_check(login):
    driver = login.driver
    wait = WebDriverWait(driver,10)

    # 1. 로그인
    # 2. 크레딧 UI 대기
    credit_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='https://qaproject.elice.io/admin/org/billing/payments/credit']"))
    )
    time.sleep(2)

    # 3. 텍스트 추출
    credit_text = credit_element.text.strip()
    print(f"추출 결과: {credit_text}")

    assert ("크레딧" in credit_text) or ("₩" in credit_text), "⛔ [FAIL] 크레딧 표시X"
    print("✅ [PASS] 잔여 크레딧 표시 확인")

    