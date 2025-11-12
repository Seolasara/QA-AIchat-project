import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage

# CBAS037: 응답 싫어요
def test_CBAS037_ans_dislike(driver, login, send_test_message):
    
    send_test_message("응답 싫어요 테스트 입니다.")
    print("✅ [PASS] 질문 전송 완료")
    
    # AI 응답 대기 및 확인
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content"))
    )
    time.sleep(3)

    response_box = driver.find_element(By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content")
    response_text = response_box.get_attribute("innerText")

    response_div = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-step-type='assistant_message']"))
    )
    
    # 싫어요 버튼 확인
    dislike_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button:has(svg.lucide-thumbs-down)"))
    )
    
    # 싫어요 버튼 클릭
    dislike_button.click()
    print("✅ [PASS] 싫어요 버튼 클릭 완료")
    time.sleep(1)
    
    # 의견 추가 팝업 출력
    feedback_popup = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog'][data-state='open']"))
    )
    
    # 피드백 제출 버튼 클릭
    submit_button = feedback_popup.find_element(By.ID, "submit-feedback")
    submit_button.click()
    time.sleep(1)

    # 피드백 제출 후 토스트 메시지 대기
    toast_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            "section[aria-label='Notifications alt+T'] li[data-sonner-toast][data-type='success'] div[data-content]"
        ))
    )

    # 토스트 내용 확인
    message_text = toast_message.text
    print("✅ [PASS]", message_text)

    assert "피드백이 업데이트되었습니다" in message_text, "⛔ [FAIL] 토스트 메시지 내용 오류"

    # 싫어요 버튼 색상 빨간색 적용 확인
    if "text-red-600" in dislike_button.get_attribute("class"):
        print("✅ [PASS] 싫어요 성공 및 버튼 빨간색 적용")
    else:
        print("⛔ [FAIL] 싫어요 실패 또는 버튼 색상 적용 실패")

    # 싫어요 버튼 재클릭
    dislike_button.click()
    print("✅ [PASS] 싫어요 버튼 재클릭 완료")
    time.sleep(1)
    
    # 피드백 제출 후 토스트 메시지 대기
    toast_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            "section[aria-label='Notifications alt+T'] li[data-sonner-toast][data-type='success'] div[data-content]"
        ))
    )

    # 토스트 내용 확인
    message_text = toast_message.text
    print("✅ [PASS]", message_text)

    assert "피드백이 업데이트되었습니다" in message_text, "⛔ [FAIL] 토스트 메시지 내용 오류"

    # 싫어요 버튼 색상 검정색 적용 확인
    if "text-red-600" not in dislike_button.get_attribute("class"):
        print("✅ [PASS] 싫어요 취소 및 버튼 검정색 적용")
    else:
        print("⛔ [FAIL] 싫어요 취소 실패 또는 버튼 색상 적용 실패")
        