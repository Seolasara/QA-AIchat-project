import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage

# CBAS001: 단일 질문 → 응답 확인
def test_CBAS001_chat_basic(driver):
    login_page = LoginPage(driver)
    login_page.page_open()
    login_page.login()
        
    # 질문(자연어) 입력
    input_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='메시지를 입력하세요...']"))
    )
    input_box.send_keys("오늘 서울 날씨 어때?")
    time.sleep(1)  # React의 입력 감지 대기

    # 버튼 활성화될 때까지 기다리기
    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button#chat-submit"))
    )

    # 전송
    send_button.click()
    print("✅ [PASS] 질문 전송 완료")
    
    # AI 응답 대기 및 확인
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content"))
    )
    time.sleep(20)

    response_box = driver.find_element(By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content")
    response_text = response_box.get_attribute("innerText")

    assert len(response_text) > 0, "❌ [FAIL] AI 응답이 표시되지 않았습니다."
    print("✅ [PASS] AI 응답 확인 완료:", response_text[:100])
