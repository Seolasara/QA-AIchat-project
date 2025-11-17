import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_CBAS001_chat_basic_fail_example(driver, login, send_test_message):
    
    # 질문 전송
    send_test_message("오늘 서울 날씨 어때?")
    print("질문 전송!")

    # 응답 대기
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content")
        )
    )

    response_box = driver.find_element(
        By.CSS_SELECTOR,
        "div[data-step-type='assistant_message'] .message-content"
    )
    response_text = response_box.get_attribute("innerText")
    
    print("응답 내용:", response_text)

    # 여기서 **일부러 실패** 만들기
    assert "이 문자열은 절대 포함되지 않음" in response_text, \
        "❌ 실패 유도: response_text 안에 특정 문자열이 없습니다!"