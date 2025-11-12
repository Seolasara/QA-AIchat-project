import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.image_upload_page import HelpyChatPage
from src.utils.config_reader import read_config


def test_CADV011_hwp_upload_reject(driver, login):
    """20mb 이상 크기의 파일 업로드 시 'File is larger than 20 MB' 경고 문구가 표시되는지 확인"""

    # 설정 로드
    config = read_config("helpychat")
    base_url = config["base_url"]

    # 로그인 후 채팅 페이지 진입
    driver.get(base_url)
    time.sleep(3)

    chat_page = HelpyChatPage(driver)

    # 업로드 시도
    filename = "20.5mb.jpg"
    chat_page.upload_image(filename)

    # 경고 문구 대기 및 확인
    wait = WebDriverWait(driver, 10)

    try:
        alert_element = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'File is larger than 20 MB')]")
            )
        )
        assert alert_element.is_displayed(), "경고 문구가 표시되지 않았습니다."
        print(f"✅ 업로드 실패 경고 표시 확인: {filename}")

    except Exception:
        pytest.fail(f"❌ 업로드 실패 문구를 찾을 수 없습니다: {filename}")

    time.sleep(3)