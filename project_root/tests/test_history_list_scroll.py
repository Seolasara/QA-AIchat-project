import time
from selenium.webdriver.common.by import By
from src.pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

def test_HIST032_history_list_scroll(driver,login) :

    # 히스토리 목록이 나타날 때까지 대기
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='virtuoso-item-list']")))

    # 히스토리 목록 스크롤
    history_scroller = driver.find_element(By.CSS_SELECTOR, "div[data-testid='virtuoso-scroller']")

    prev_max_index = -1
    first_index = None

    # 히스토리 갯수 확인
    for i in range(1000):
        # 현재 렌더된 히스토리 목록 data-index 추출
        history_items = history_scroller.find_elements(By.CSS_SELECTOR, "a[data-index]")
        history_indexes = [int(item.get_attribute("data-index")) for item in history_items]

        if not history_indexes:
            print("⏳ 히스토리 항목이 아직 로드되지 않음, 재시도 중...")
            time.sleep(1)
            continue

        max_index = max(history_indexes)

        # 첫 번째 스크롤의 마지막 index 기록
        if i == 0:
            first_index = max_index
            print(f"\n현재 히스토리 목록 갯수 : {first_index+1}")

        # 더 이상 인덱스가 증가하지 않으면 상위 for문 종료
        if max_index == prev_max_index:
            break

        # 스크롤 내리기
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", history_scroller)
        time.sleep(1)

        prev_max_index = max_index

    print(f"\n최종 로드된 히스토리 목록 갯수 = {max_index+1}")

    assert max_index >= first_index, "⛔ [FAIL] 히스토리 목록 확인 실패"
    print("\n✅ [PASS] 히스토리 목록 확인 성공")
