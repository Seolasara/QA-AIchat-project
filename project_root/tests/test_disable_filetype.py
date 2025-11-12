import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.image_upload_page import HelpyChatPage
from src.utils.config_reader import read_config


def test_CADV011_file_upload_reject(driver, login):
    """업로드 제한 파일(ZIP, HWP, Json, md, log, bin)-6개 업로드 테스트"""

    config = read_config("helpychat")
    base_url = config["base_url"]

    driver.get(base_url)
    time.sleep(3)

    chat_page = HelpyChatPage(driver)
    wait = WebDriverWait(driver, 10)

    # 1️⃣ 테스트할 파일 목록
    test_files = ["Desktop.zip", "testfile.hwp","test_data.json","test_doc.md","test_log.log","sample.bin"]

    for filename in test_files:
        print(f"✅ {filename} 업로드 중")

        # 파일 업로드 시도
        chat_page.upload_image(filename)

        # 2️⃣ 경고 문구 감지
        try:
            alert_element = wait.until(
                EC.visibility_of_element_located((
                    By.XPATH,
                    "//*[contains(text(), 'File type') or contains(text(), 'not allowed') or contains(text(), '허용되지')]"
                ))
            )
            assert alert_element.is_displayed(), f"❌ {filename} 업로드 시 경고 문구가 표시되지 않았습니다."
            print(f"✅ 업로드 실패 경고 표시 확인됨: {filename}")

        except Exception:
            pytest.fail(f"❌ [FAIL] 업로드 실패 문구를 찾을 수 없습니다: {filename}")

        time.sleep(2)

    print("✅ 업로드 제한 파일 검증 완료")