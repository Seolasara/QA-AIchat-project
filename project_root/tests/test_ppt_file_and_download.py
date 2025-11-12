import pytest
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.config_reader import read_config
from src.pages.login_page import LoginPage


def test_CADV078_ppt_create_and_download(driver, login, click_plus, send_test_message):
    """HelpyChat PPT 생성 후 PPTX 파일 다운로드 테스트"""

    config = read_config("helpychat")
    base_url = config["base_url"]
    driver.get(base_url)
    wait = WebDriverWait(driver, 30)

    click_plus()

    ppt_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='button']//span[contains(text(), 'PPT 생성')]"))
    )
    driver.execute_script("arguments[0].click();", ppt_button)


    send_test_message("겨울에 주로 먹는 음식에 대한 ppt 만들어줘")
    time.sleep(3) #생성버튼 로딩대기

    create_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(normalize-space(.), '생성')]"))
    )
    driver.execute_script("arguments[0].click();", create_button)
    print("✅ PPT 생성 시작")

    # 5PPT 생성 완료 문구 대기 및 검증
    complete_msg = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'프레젠테이션 생성이 완료되었습니다')]"))
    )
    assert "프레젠테이션 생성이 완료되었습니다" in complete_msg.text
    print("✅ 프레젠테이션 생성 완료 문구 감지")

    # 다운로드 전 폴더 상태 저장
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    before_files = set(os.listdir(download_dir))

    # 'PPTX 다운로드' 버튼 클릭
    try:
        download_button = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(@class,'MuiButton-root') and contains(normalize-space(.), 'PPTX 다운로드')]"
            ))
        )
        driver.execute_script("arguments[0].click();", download_button)
        print("✅ 파일 다운로드 시작")
    except Exception as e:
        print("❌ 'PPTX 다운로드' 버튼을 찾지 못했습니다:", e)
        assert False, "'PPTX 다운로드' 버튼 클릭 실패"

    # 8️⃣ 다운로드 파일 검증 (최대 60초 대기)
    file_downloaded = False
    for _ in range(60):
        time.sleep(1)
        after_files = set(os.listdir(download_dir))
        new_files = after_files - before_files
        if any(f.lower().endswith(".pptx") for f in new_files):
            pptx_file = [f for f in new_files if f.lower().endswith(".pptx")][0]
            print(f"✅ PPTX 파일 다운로드 완료: {pptx_file}")
            file_downloaded = True
            break

    assert file_downloaded, "❌ PPTX 파일이 다운로드되지 않았습니다."
    print("✅ PPT 생성 및 PPTX 파일 다운로드 검증 완료")