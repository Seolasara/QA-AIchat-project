import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scroll_to_top_and_click_latest(driver, timeout=30):
    """
    HelpyChat 실제 스크롤 가능한 컨테이너 기준으로 맨 위까지 강제 스크롤
    """
    wait = WebDriverWait(driver, timeout)

    # ✅ 올바른 스크롤 컨테이너
    scroll_container = driver.find_element(
        By.CSS_SELECTOR, "div.flex.flex-col.flex-grow.overflow-y-auto"
    )

    # 1️⃣ 최상단 시도
    driver.execute_script("arguments[0].scrollTop = 0;", scroll_container)
    time.sleep(0.5)

    # 2️⃣ 혹시 안 올라갔으면 반복 스크롤
    prev_top = None
    for i in range(50):
        driver.execute_script("arguments[0].scrollBy(0, -800);", scroll_container)
        time.sleep(0.1)
        scroll_top = driver.execute_script("return arguments[0].scrollTop;", scroll_container)
        if prev_top == scroll_top or scroll_top == 0:
            print(f"🟩 [PASS] 최상단 도달 (iteration={i}) scrollTop={scroll_top}")
            break
        prev_top = scroll_top
    else:
        driver.save_screenshot("scroll_not_reached_top.png")
        raise AssertionError("❌ 스크롤이 최상단에 도달하지 않았습니다. (스크린샷 저장됨)")

    # 3️⃣ 화살표 버튼 찾기
    selectors = [
        "button svg.lucide-arrow-down",
        "button svg.lucide.lucide-arrow-down",
        "button[data-testid='scroll-down']",
        "button[aria-label*='스크롤']",
    ]

    arrow_button = None
    for selector in selectors:
        try:
            arrow_svg = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
            arrow_button = arrow_svg.find_element(By.XPATH, "./ancestor::button[1]")
            print(f"👁️ [PASS] 화살표 버튼 감지됨 (selector: {selector})")
            break
        except:
            continue

    if not arrow_button:
        driver.save_screenshot("no_arrow_button.png")
        raise AssertionError("❌ 화살표 버튼이 렌더링되지 않았습니다. (스크린샷 저장됨)")

    # 4️⃣ 클릭
    driver.execute_script("arguments[0].click();", arrow_button)
    print("⬇️ [PASS] 최신 메시지 보기 버튼 클릭 완료")

    # 5️⃣ 하단 도달 검증
    time.sleep(1)
    scroll_top = driver.execute_script("return arguments[0].scrollTop;", scroll_container)
    scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_container)
    client_height = driver.execute_script("return arguments[0].clientHeight;", scroll_container)
    at_bottom = abs(scroll_height - (scroll_top + client_height)) < 5

    if at_bottom:
        print("✅ [PASS] 최신 메시지로 자동 스크롤 이동 완료")
    else:
        raise AssertionError(
            f"⛔ 스크롤이 맨 아래로 이동하지 않음 "
            f"(scrollTop={scroll_top}, scrollHeight={scroll_height}, clientHeight={client_height})"
        )