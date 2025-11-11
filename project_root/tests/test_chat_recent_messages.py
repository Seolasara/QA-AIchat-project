import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_assistant_to_finish(driver, selector, timeout=30, stable_time=2):
    """AI 응답이 끝날 때까지 scrollHeight 변동 없을 때까지 대기"""
    scroll_container = driver.find_element(
        By.CSS_SELECTOR, "div.relative.flex.flex-col.flex-grow.overflow-y-auto"
    )
    end_time = time.time() + timeout
    last_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_container)
    stable_start = None

    while time.time() < end_time:
        time.sleep(0.5)
        new_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_container)
        # 높이가 변하면 다시 카운트 리셋
        if new_height != last_height:
            stable_start = None
            last_height = new_height
        else:
            # 일정 시간 동안 높이 변화 없으면 응답 완료로 판단
            if stable_start is None:
                stable_start = time.time()
            elif time.time() - stable_start >= stable_time:
                print("✅ [PASS] AI 응답 완료 (scrollHeight 안정)")
                return
    raise TimeoutError("AI 응답이 끝나지 않았습니다.")


def test_CBAS074_chat_basic(driver, login, send_test_message):
    assistant_selector = "div[data-step-type='assistant_message'] .message-content"
    before_count = len(driver.find_elements(By.CSS_SELECTOR, assistant_selector))

    # 메시지 전송
    send_test_message("오늘 주요 기사 내용 요약해줘")

    # 응답 시작될 때까지 대기
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, assistant_selector))
    )
    print("✅ [PASS] AI 응답 시작 확인")

    # ✅ 응답이 끝날 때까지 scrollHeight 안정될 때까지 기다림
    wait_for_assistant_to_finish(driver, assistant_selector)

    # 스크롤 컨테이너 찾아 상단으로 이동
    scroll_container = driver.find_element(
        By.CSS_SELECTOR, "div.relative.flex.flex-col.flex-grow.overflow-y-auto"
    )
    driver.execute_script("arguments[0].scrollTop = 0;", scroll_container)
    scroll_top = driver.execute_script("return arguments[0].scrollTop;", scroll_container)
    print(f"⬆️ [PASS] 스크롤 상단 이동 완료 (scrollTop={scroll_top})")

    # 확인용
    time.sleep(5)
    
    # send_test_message("오늘 주요 기사 내용 요약해줘")
    
    # # 마지막 응답 대기
    # WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content"))
    # )
    # print("✅ [PASS] 마지막 응답 확인 완료")
    # time.sleep(10)
    
    # # 스크롤바 생성
    
    
    # # 최근 메시지 보기 버튼 확인 및 클릭
    # arrow_down_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "button.inline-flex.items-center.justify-center.gap-2.h-9.w-9.rounded-full"))
    # )
    # WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable(arrow_down_button)
    # )
    # arrow_down_button.click()
    # print("✅ [PASS] 최근 메시지 보기 버튼 클릭 완료")
    # time.sleep(1)
    
    # # 마지막 메시지로 자동 스크롤 이동 확인
    # last_message = driver.find_element(By.CSS_SELECTOR, "div[data-step-type='assistant_message']:last-child")
    # is_visible = driver.execute_script(
    #     "var rect = arguments[0].getBoundingClientRect(); return (rect.top >= 0 && rect.bottom <= window.innerHeight);",
    #     last_message
    # )

    # assert is_visible, "⛔ [FAIL] 최근 메시지로 자동 스크롤 이동 실패"
    # print("✅ [PASS] 최근 메시지 보기 확인 완료")
    