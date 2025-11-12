import pytest
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.config_reader import read_config


def test_CADV027_CADV028_deep_investigation_request(driver, login, click_plus, send_test_message):
    """심층 조사 기능 테스트 + 마크다운/한글파일 다운로드 검증"""

    config = read_config("helpychat")
    base_url = config["base_url"]
    driver.get(base_url)
    wait = WebDriverWait(driver, 15)
    
    click_plus()

    # 2️⃣ '심층 조사' 버튼 클릭
    deep_investigation_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.MuiButtonBase-root[role='button'] svg[data-icon='book-open-cover']"))
    )
    driver.execute_script("arguments[0].closest('div[role=\"button\"]').click();", deep_investigation_btn)
    print("✅ '심층 조사' 버튼 클릭 완료")

    # 3️⃣ 메시지 입력 및 전송 (공용 fixture)
    send_test_message("AI윤리문제에 대해 조사해줘")

    # 4️⃣ '시작' 버튼 클릭
    start_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='시작'] or contains(., '시작')]"))
    )
    driver.execute_script("arguments[0].click();", start_button)
    print("✅ '시작' 버튼 클릭 완료 — 심층조사 진행 중...")

    # 5️⃣ 조사 완료 대기 (최대 12분)
    try:
        WebDriverWait(driver, 720).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '조사 완료')]"))
        )
        print("✅ '조사 완료' 문구 감지됨 — 심층조사 성공적으로 종료")
    except:
        assert False, "❌ '조사 완료' 텍스트가 표시되지 않았습니다."

    # 📂 다운로드 디렉토리
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")

    def wait_for_download(extension: str, before_files: set, timeout=60):
        """지정 확장자의 파일이 새로 다운로드될 때까지 대기"""
        for _ in range(timeout):
            time.sleep(1)
            after_files = set(os.listdir(download_dir))
            new_files = after_files - before_files
            for f in new_files:
                if f.endswith(extension):
                    print(f"✅ {extension} 파일 다운로드 완료: {f}")
                    return True
        return False

    # 6️⃣ 마크다운 다운로드 버튼 클릭
    print("✅ 마크다운 다운로드 버튼 클릭 중...")
    markdown_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), '마크다운 다운로드')]]"))
    )

    before_files = set(os.listdir(download_dir))
    driver.execute_script("arguments[0].click();", markdown_button)
    print("✅ '마크다운 다운로드' 클릭 완료 — 파일 대기 중...")

    md_downloaded = wait_for_download(".md", before_files)
    assert md_downloaded, "❌ 마크다운 파일이 다운로드되지 않았습니다."

    # 7️⃣ 한글파일 다운로드 버튼 클릭
    print("✅ 한글파일 다운로드 버튼 클릭 중...")
    hwp_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), '한글파일 다운로드')]]"))
    )

    before_files = set(os.listdir(download_dir))
    driver.execute_script("arguments[0].click();", hwp_button)
    print("✅ '한글파일 다운로드' 클릭 완료 — 파일 대기 중...")

    hwp_downloaded = wait_for_download(".hwp", before_files)
    assert hwp_downloaded, "❌ 한글(.hwp) 파일이 다운로드되지 않았습니다."

    print("✅ 모든 파일 다운로드 검증 완료")