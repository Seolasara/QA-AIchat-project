import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_helpychat_login(driver):
    """HelpyChat 로그인 자동화 테스트"""
    # 1️⃣ 로그인 페이지 접속
    driver.get(
        "https://qaproject.elice.io/ai-helpy-chat"
    )

    # 2️⃣ 이메일 입력
    id_field = driver.find_element(By.ID, ":r0:")
    id_field.send_keys("team2@elice.com")

    # 3️⃣ 비밀번호 필드 선택
    pw_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="password" and @type="password"]'))
    )

    # 4️⃣ JavaScript로 React MUI 필드에 값 입력
    password = "team2elice!@"
    driver.execute_script("""
    const input = arguments[0];
    const value = arguments[1];
    input.focus();
    const lastValue = input.value;
    input.value = value;
    const tracker = input._valueTracker;
    if (tracker) tracker.setValue(lastValue);
    input.dispatchEvent(new InputEvent('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
    """, pw_field, password)
   

    # 5️⃣ 로그인 버튼 클릭
    login_button = driver.find_element(By.ID, ":r3:")
    login_button.click()

    # 6️⃣ 페이지 이동 대기
    time.sleep(10)

    # 7️⃣ 로그인 성공 검증
    assert "qatrack.elice.io" in driver.current_url
    print("✅ HelpyChat 로그인 자동화 테스트 성공!")