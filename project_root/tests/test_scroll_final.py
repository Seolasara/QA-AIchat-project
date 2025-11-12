import time
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SCREENSHOT_DIR = os.path.expanduser("~/Desktop/team2_project/scroll_debug_screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def test_scroll_first_message_to_top_with_offset(driver, login, send_test_message):
    # 메시지 전송
    send_test_message("오늘 주요 기사 내용 요약해줘")

    # AI 응답 렌더링 대기
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content"))
    )
    time.sleep(0.5)

    # 스크롤 컨테이너 선택 (응답 화면)
    containers = driver.find_elements(By.CSS_SELECTOR, "div.relative.flex.flex-col.flex-grow.overflow-y-auto")
    scroll_container = None
    for c in reversed(containers):
        sh = driver.execute_script("return arguments[0].scrollHeight;", c)
        ch = driver.execute_script("return arguments[0].clientHeight;", c)
        if sh > ch:
            scroll_container = c
            break
    if scroll_container is None:
        scroll_container = containers[-1]

    # 첫 메시지 선택
    first_msg = driver.find_element(By.CSS_SELECTOR, "div[data-step-type='user_message']:first-child")

    # padding-top 확인
    padding_top = driver.execute_script(
        "return parseInt(window.getComputedStyle(arguments[0]).paddingTop || '0');", scroll_container
    ) or 0

    # 반복 강제 스크롤: 렌더링 변동 대응
    for _ in range(8):
        offset = driver.execute_script("return arguments[0].offsetTop;", first_msg)
        desired = max(offset - padding_top, 0)
        driver.execute_script("""
            const cont = arguments[0];
            const pos = arguments[1];
            cont.scrollTop = pos;
            if (typeof cont.scrollTo === 'function') { cont.scrollTo({top: pos, behavior:'auto'}); }
        """, scroll_container, desired)
        time.sleep(0.3)

    # 최종 scrollTop 및 메시지 위치 확인
    scroll_top = driver.execute_script("return arguments[0].scrollTop;", scroll_container)
    msg_diff = driver.execute_script("""
        const cont = arguments[0];
        const msg = arguments[1];
        return Math.abs(msg.getBoundingClientRect().top - cont.getBoundingClientRect().top);
    """, scroll_container, first_msg)

    # 스크린샷 저장
    ts = int(time.time())
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"scroll_debug_{ts}.png")
    driver.save_screenshot(screenshot_path)
    print(f"📸 스크린샷 저장: {screenshot_path}")
    print(f"⬆️ 스크롤 상단 이동 시도")
    print(f"현재 scrollTop 값: {scroll_top}")
    print(f"첫 메시지 화면 상단과 컨테이너 top 차이: {msg_diff}px")

    # 검증
    assert msg_diff <= 24, "❌ 첫 메시지가 화면 상단에 위치하지 않음"