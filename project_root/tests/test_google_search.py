import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.config_reader import read_config


def test_CADV032_google_search_request(driver, login, click_plus, send_test_message):
    """HelpyChat 구글 검색 기능 테스트 (assistant_message 기준 버전)"""

    config = read_config("helpychat")
    base_url = config["base_url"]
    driver.get(base_url)
    wait = WebDriverWait(driver, 15)

    # + 버튼 클릭
    click_plus()

    # '구글 검색' 버튼 클릭
    google_search_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[@role='button']//span[contains(text(), '구글 검색')]"
        ))
    )
    driver.execute_script("arguments[0].click();", google_search_btn)
    print("✅ '구글 검색' 버튼 클릭 완료")

    # 사용자 메시지 전송
    send_test_message("현재 대전 온도 알려줘")

    # ✅ Helpy 응답 대기 (assistant_message 기준)
    response_box = WebDriverWait(driver, 90).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content"))
    )
    time.sleep(3)

    # ✅ 텍스트 추출 및 검증
    response_text = response_box.get_attribute("innerText")
    print(f"✅ Helpy 응답 감지됨:\n{response_text}")

    keywords = ["Daejeon", "대전", "온도", "℃", "°C", "temperature"]
    matched = [kw for kw in keywords if kw.lower() in response_text.lower()]

    assert len(matched) >= 2, f"❌ Helpy 응답 내 키워드 부족: {matched}"
    print(f"✅ HelpyChat 구글 검색 테스트 통과(감지된 키워드: {matched})")

    time.sleep(2)