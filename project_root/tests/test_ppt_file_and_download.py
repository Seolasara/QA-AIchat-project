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


    send_test_message("겨울에 주로 먹는 음식에 대한 ppt 3페이지 정도로 만들어줘")
    time.sleep(3) 

    create_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(normalize-space(.), '생성')]"))
    )
    driver.execute_script("arguments[0].click();", create_button)
    print("✅ PPT 생성 시작")
    

    print("⚙️ PPT 생성 중... 최대 10분까지 대기합니다.")
    max_wait = 600  # 10분
    poll_interval = 10  # 10초마다 확인

    elapsed = 0
    complete_keywords = ["완료", "완성", "성공", "Presentation"]

    complete_msg = None
    while elapsed < max_wait:
        page_text = driver.page_source
        if any(keyword in page_text for keyword in complete_keywords):
            print(f"✅ PPT 생성 완료 감지됨 ({elapsed}초 경과)")
            break
        time.sleep(poll_interval)
        elapsed += poll_interval
        print(f"⏳ {elapsed}초 경과... 아직 생성 중")

    if elapsed >= max_wait:
        raise TimeoutError("❌ 10분이 지나도 PPT 생성 완료 문구를 찾지 못했습니다.")
    
   # 5️⃣ PPT 생성 완료 문구 대기 및 검증 (문구 유연하게 대기)
    complete_msg = WebDriverWait(driver, 500).until(
        EC.presence_of_element_located((
            By.XPATH,
            "//*[contains(text(),'완료') or contains(text(),'완성') or contains(text(),'성공') or contains(text(),'Presentation')]"
        ))
    )
    
    # 'PPTX 다운로드' 버튼 클릭
    try:
        download_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((
            By.XPATH,
            "//button[contains(normalize-space(.), '다운로드') or contains(., 'PPTX')]"
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