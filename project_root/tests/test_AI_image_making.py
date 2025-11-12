import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.config_reader import read_config

def test_CADV090_image_generation(driver, login, click_plus, send_test_message):
    """HelpyChat 이미지 생성 테스트 (Azure Blob 이미지 감지 포함)"""

    config = read_config("helpychat")
    base_url = config["base_url"]
    driver.get(base_url)
    wait = WebDriverWait(driver, 30)

    click_plus()

    # 1️⃣ '이미지 생성' 버튼 클릭
    image_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@role='button']//span[contains(text(), '이미지 생성')]")))
    driver.execute_script("arguments[0].click();", image_button)
    print("✅ '이미지 생성' 버튼 클릭 완료")

    # 2️⃣ 기존 이미지 src 수집
    initial_srcs = {
        img.get_attribute("src")
        for img in driver.find_elements(By.TAG_NAME, "img")
        if img.get_attribute("src")
    }
    print(f"✅ 기존 이미지 {len(initial_srcs)}개 수집 완료")

    # 3️⃣ 메시지 전송
    send_test_message("귀여운 고양이 일러스트를 만들어줘")

    # 4️⃣ 새 이미지 감시 (최대 2분)
    print("✅ AI 이미지 렌더링 대기 중...")
    detected = False
    for sec in range(0, 120, 5):
        time.sleep(5)
        current_imgs = {
            i.get_attribute("src")
            for i in driver.find_elements(By.TAG_NAME, "img")
            if i.get_attribute("src")
        }

        # 새 이미지 감지 (Azure Blob 포함)
        new_imgs = [
            src for src in current_imgs
            if src not in initial_srcs and any(
                key in src for key in (
                    "blob:",
                    "data:image",
                    "elicebackendstorage.blob.core.windows.net"
                )
            )
        ]

        if new_imgs:
            print(f"✅ 새 이미지 감지됨 ({len(new_imgs)}개)\n→ {new_imgs[0][:100]}...")
            detected = True
            break
        else:
            print(f"⏳ {sec}초 경과 — 새 이미지 없음 ({len(current_imgs)}개 감지됨)")

    # 5️⃣ 결과 검증
    assert detected, "❌ HelpyChat 이미지가 렌더링되지 않음"
    print("✅ HelpyChat 이미지 생성 테스트 통과 — 실제 이미지 렌더링 확인됨")