import pytest
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.config_reader import read_config


def test_CADV078_ppt_create_and_download(driver, login, click_plus, send_test_message):
    """HelpyChat PPT 생성 후 PPTX 파일 다운로드 테스트 (MUI 버튼 대응 완성형)"""

    # ✅ 환경 설정
    config = read_config("helpychat")
    base_url = config["base_url"]
    driver.get(base_url)
    wait = WebDriverWait(driver, 30)

    # ✅ + 버튼 클릭 → PPT 생성 진입
    click_plus()
    ppt_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='button']//span[contains(text(), 'PPT 생성')]"))
    )
    driver.execute_script("arguments[0].click();", ppt_button)
    print("✅ 'PPT 생성' 버튼 클릭 완료")

    # ✅ HelpyChat 메시지 전송
    send_test_message("우리나라 동물에 대한 ppt 3페이지로 만들어줘")
    time.sleep(3)

    # ✅ '생성' 버튼 클릭
    create_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(normalize-space(.), '생성')]"))
    )
    driver.execute_script("arguments[0].click();", create_button)
    print("✅ PPT 생성 시작")
    

    # ✅ 다운로드 폴더 상태 저장
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    before_files = set(os.listdir(download_dir))

    # ✅ "프레젠테이션 생성 완료" 문구 대기
    print("⚙️ PPT 생성 중... 최대 15분까지 대기합니다.")
    complete_msg = WebDriverWait(driver, 900).until(
        EC.presence_of_element_located((
            By.XPATH,
            "//*[contains(text(),'프레젠테이션 생성이 완료되었습니다') or contains(text(),'Presentation completed')]"
        ))
    )
    print("✅ 프레젠테이션 생성 완료 문구 감지됨!")

    # 잠시 대기 (HelpyChat이 버튼을 렌더링할 시간)
    time.sleep(5)

    # ✅ MUI 기반 "PPTX 다운로드" 버튼 대기 및 클릭
    print("🔍 'PPTX 다운로드' 버튼 탐색 중")
    try:
        download_button = WebDriverWait(driver, 300).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(@class,'MuiButton-root') and contains(normalize-space(.), 'PPTX 다운로드')]"
            ))
        )
        # 스크롤 후 클릭
        driver.execute_script("arguments[0].scrollIntoView(true);", download_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", download_button)
        print("✅ 'PPTX 다운로드' 버튼 클릭 완료")

    except Exception as e:
        print("❌ 다운로드 버튼 클릭 실패:", e)
        assert False, "'PPTX 다운로드' 버튼 클릭 실패"

    # ✅ 파일 다운로드 완료 검증
    print("📥 파일 다운로드 대기")
    file_downloaded = False
    for _ in range(180):  # 최대 3분 대기
        time.sleep(1)
        after_files = set(os.listdir(download_dir))
        new_files = after_files - before_files
        if any(f.lower().endswith(".pptx") for f in new_files):
            pptx_file = [f for f in new_files if f.lower().endswith(".pptx")][0]
            print(f"✅ PPTX 파일 다운로드 완료: {pptx_file}")
            file_downloaded = True
            break

    assert file_downloaded, "❌ PPTX 파일이 다운로드되지 않았습니다."
    print("✅ HelpyChat PPT 생성 및 다운로드 테스트 성공")
    
