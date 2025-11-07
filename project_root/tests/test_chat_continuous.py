import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage

# CBAS002: 연속 질문 → 응답 확인
def test_CBAS002_chat_continuous(driver):
    login_page = LoginPage(driver)
    login_page.page_open()
    login_page.login()
    
    # 첫 번째 질문
    first_question = "오늘 서울 날씨 어때?"
    
    input_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='메시지를 입력하세요...']"))
    )
    input_box.send_keys(first_question)
    time.sleep(1)  # React의 입력 감지 대기
    
    # 버튼 활성화될 때까지 기다리기
    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button#chat-submit"))
    )

    # 전송
    send_button.click()
    print(f"✅ [PASS] 첫 번째 질문 전송 완료: {first_question}")
    
    # 첫 번째 질문 AI 응답 대기 및 확인
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content"))
    )
    time.sleep(20)
    
    # 첫 번째 응답 텍스트 확인
    responses = driver.find_elements(By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content")
    first_response = responses[-1].get_attribute("innerText")
    
    assert len(first_response) > 0, "❌ [FAIL] 첫 번째 AI 응답이 표시되지 않았습니다."
    print("✅ [PASS] 첫 번째 응답 확인 완료:", first_response[:100])
    
    # 두 번째 질문 (연속 질문)
    second_question = "그럼 내일은?"
    input_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='메시지를 입력하세요...']"))
    )
    input_box.clear()  # 이전 입력 초기화
    input_box.send_keys(second_question)
    time.sleep(1)

    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button#chat-submit"))
    )
    send_button.click()
    print(f"✅ [PASS] 두 번째 질문 전송 완료: {second_question}")

    # 두 번째 응답 대기
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content"))
    )
    time.sleep(20)

    # 두 번째 응답 텍스트 확인
    responses = driver.find_elements(By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content")
    second_response = responses[-1].get_attribute("innerText")

    assert len(second_response) > 0, "❌ [FAIL] 두 번째 AI 응답이 표시되지 않았습니다."
    print("✅ [PASS] 두 번째 응답 확인 완료:", second_response[:100])
    