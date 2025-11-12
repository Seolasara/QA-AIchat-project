import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.config_reader import read_config


def test_scroll_to_top_and_click_latest(driver, login, send_test_message, timeout=150):
    """
    ✅ HelpyChat '오늘 주요 기사 요약해줘' 메시지 전송 후,
    1️⃣ 응답 완료 (텍스트 + 높이 안정화)
    2️⃣ 내부 스크롤 컨테이너(scrollTop=0)으로 이동
    3️⃣ 화살표 버튼 감지 및 클릭
    4️⃣ 최신 메시지 복귀 검증
    """

    config = read_config("helpychat")
    base_url = config["base_url"]
    driver.get(base_url)
    wait = WebDriverWait(driver, timeout)

    # 1️⃣ 메시지 전송
    send_test_message("오늘 주요 기사 요약해줘")
    print("💬 [STEP] 메시지 전송 완료")

    # 2️⃣ HelpyChat 응답 완료 감시 (텍스트 + 높이 안정화)
    print("⏳ [WAIT] HelpyChat 응답 전체 렌더링 대기 중...")

    start_time = time.time()
    last_length, last_height, stable_ticks = 0, 0, 0

    while time.time() - start_time < 120:
        text_length = len(driver.execute_script("return document.body.innerText;"))
        try:
            height = driver.execute_script("""
                const el = document.querySelector('div.relative.flex.flex-col.flex-grow.overflow-y-auto > div.flex.flex-col.flex-grow.overflow-y-auto');
                return el ? el.scrollHeight : 0;
            """)
        except Exception:
            height = 0

        if text_length == last_length and height == last_height:
            stable_ticks += 1
        else:
            stable_ticks = 0

        last_length, last_height = text_length, height

        # 5초 이상 변화 없으면 응답 완료로 판단
        if stable_ticks >= 5:
            print("🟩 [PASS] HelpyChat 응답 렌더링 완전히 종료됨 (자동 하단 스크롤 포함)")
            break
        time.sleep(1)
    else:
        raise AssertionError("❌ 응답이 제한 시간 내에 완료되지 않았습니다.")

    # 3️⃣ 실제 스크롤 가능한 내부 컨테이너 찾기
    print("⬆️ [STEP] 실제 응답 영역 기준으로 맨 위로 스크롤 중...")
    scroll_container = wait.until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            "div.relative.flex.flex-col.flex-grow.overflow-y-auto > div.flex.flex-col.flex-grow.overflow-y-auto"
        ))
    )

    # 4️⃣ scrollTop=0 명령 반복 — React 렌더링 후 덮어쓰기 방지
    success = False
    for i in range(15):
        driver.execute_script("arguments[0].scrollTop = 0;", scroll_container)
        time.sleep(0.5)
        scroll_top_now = driver.execute_script("return arguments[0].scrollTop;", scroll_container)
        if scroll_top_now == 0:
            print(f"🟢 [PASS] 채팅창 맨 위 도달 (iteration={i})")
            success = True
            break
    if not success:
        raise AssertionError("❌ 채팅창이 맨 위로 이동하지 않았습니다.")

    # 5️⃣ 화살표 버튼 감지
    print("👁️ [WAIT] ⬇️ 최신 메시지로 이동 버튼 렌더링 대기 중...")
    arrow_button = WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.absolute.bottom-4.left-0.right-0.flex.justify-center button")
        )
    )
    print("👁️ [PASS] ⬇️ 최신 메시지 버튼 감지됨")

    # 6️⃣ 버튼 클릭
    driver.execute_script("arguments[0].click();", arrow_button)
    print("⬇️ [PASS] 최신 메시지 보기 버튼 클릭 완료")

    # 7️⃣ 하단 도달 검증
    time.sleep(2)
    scroll_top = driver.execute_script("return arguments[0].scrollTop;", scroll_container)
    scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_container)
    client_height = driver.execute_script("return arguments[0].clientHeight;", scroll_container)
    at_bottom = abs(scroll_height - (scroll_top + client_height)) < 5

    if at_bottom:
        print("✅ [PASS] 최신 메시지로 자동 스크롤 이동 완료")
    else:
        raise AssertionError(
            f"⛔ 채팅창이 맨 아래로 이동하지 않음 "
            f"(scrollTop={scroll_top}, scrollHeight={scroll_height}, clientHeight={client_height})"
        )