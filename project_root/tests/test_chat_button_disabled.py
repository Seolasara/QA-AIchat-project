import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage

# CBAS003: 입력창 공백 → 전송 버튼 비활성화 상태 확인
def test_CBAS003_button_disabled_when_empty(driver):
    login_page = LoginPage(driver)
    login_page.page_open()
    login_page.login()
    
    # 입력창 로드 확인
    input_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='메시지를 입력하세요...']"))
    )
    
    # 혹시 자동 입력되어 있을 수 있으니 공백으로 초기화
    input_box.clear()
    time.sleep(1)
    
    # 전송 버튼 요소 찾기
    send_button = driver.find_element(By.CSS_SELECTOR, "button#chat-submit")
    
    # 버튼의 disabled 속성 값 확인
    is_disabled = send_button.get_attribute("disabled")
    
    # 검증: disabled 속성이 존재해야 함
    assert is_disabled is not None, "❌ [FAIL] 입력창이 공백이지만 버튼이 활성화되어 있습니다."
    print("✅ [PASS] 입력창이 공백일 때 전송 버튼 클릭 불가(비활성화) 상태 확인 완료")
    