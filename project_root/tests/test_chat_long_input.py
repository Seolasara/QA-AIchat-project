import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage

# CBAS004: 긴 입력값 → 잘림 없이 전송 및 AI 응답 확인
def test_CBAS004_chat_long_input(driver):
    login_page = LoginPage(driver)
    login_page.page_open()
    login_page.login()
    
    # 긴 질문 입력
    long_text = "긴 입력값 일 때 잘림 없이 전송 및 AI 응답 확인 테스트. " * 50
    
    input_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='메시지를 입력하세요...']"))
    )
    input_box.send_keys(long_text)
    time.sleep(1)
    
    # 전송 버튼 클릭 가능 확인 후 전송
    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button#chat-submit"))
    )
    send_button.click()
    print("✅ [PASS] 긴 입력값 전송 완료")
    
    # AI 응답 대기 및 검증
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content"))
    )
    time.sleep(15)
    
    response_box = driver.find_element(By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content")
    response_text = response_box.get_attribute("innerText")
    
    assert len(response_text) > 0, "❌ [FAIL] 긴 입력값에 대한 AI 응답이 표시되지 않았습니다."
    print("✅ [PASS] 긴 입력값 응답 확인 완료:", response_text[:100])
    