import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.config_reader import read_config
from src.pages.login_page import LoginPage


def test_CADV089_quiz_subjective_single_answer(driver, login, click_plus, send_test_message):
    """HelpyChat 퀴즈 생성 (주관식 1정답 검증)"""

    config = read_config("helpychat")
    base_url = config["base_url"]
    driver.get(base_url)
    wait = WebDriverWait(driver, 40)

    click_plus()

    quiz_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button']//span[contains(text(), '퀴즈 생성')]")))
    driver.execute_script("arguments[0].click();", quiz_button)

    # 메시지 전송 (주관식)
    send_test_message("우리나라 동물에 관한 퀴즈 주관식으로 만들어줘")

    print("✅ 퀴즈 생성 중... (최대 5분 대기)")
    try:
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'완료')]"))
        )
        print("✅ '완료' 문구 감지됨")
    except Exception as e:
        print("❌ '완료' 문구를 찾지 못했습니다:", e)
        assert False, "'퀴즈 생성 완료' 문구가 표시되지 않았습니다."

    time.sleep(8)

    # 유형 확인: text 여부
    try:
        quiz_type = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='text-sm truncate' and text()='text']"))
        )
        print(f"✅ 퀴즈 유형 확인됨 : {quiz_type.text}")
    except Exception as e:
        print("❌ 퀴즈 유형 'text' 감지 실패:", e)
        assert False, "퀴즈 유형이 'text'로 표시되지 않았습니다."

    # 정답 아이콘 감지 (lucide-circle-check-big)
    correct_icons = driver.find_elements(
        By.CSS_SELECTOR, "svg.lucide.lucide-circle-check-big.text-green-600"
    )

    count = len(correct_icons)
    print(f"✅ 감지된 정답 아이콘 개수: {count}")

    # 검증 — 정답은 정확히 1개여야 함
    assert count == 1, f"❌ 정답 아이콘 개수가 1개가 아닙니다 (현재 {count}개)"
    print("✅ 주관식 퀴즈 검증 성공")
