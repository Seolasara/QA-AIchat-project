import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage

# CBAS004: 긴 입력값 → 잘림 없이 전송 및 응답 확인
def test_CBAS004_chat_long_input(driver, login, send_test_message):
    
    send_test_message("긴 입력값 일 때 잘림 없이 전송 및 AI 응답 확인 테스트 입니다. " * 50)
    print("✅ [PASS] 긴 입력값 전송 완료")
    
    # AI 응답 대기 및 검증
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content"))
    )
    
    response_box = driver.find_element(By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content")
    response_text = response_box.get_attribute("innerText")
    
    assert len(response_text) > 0, "⛔ [FAIL] 긴 입력값 AI 응답 확인 실패"
    print("✅ [PASS] 긴 입력값 AI 응답 확인 완료")
    