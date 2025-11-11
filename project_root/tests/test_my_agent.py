import time
from selenium.webdriver.common.by import By
from src.pages.login_page import LoginPage
from src.pages.agent_enter_page import AgentEnterPage
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

def test_CSTM021_my_agent(driver, login):

    # 에이전트 페이지 접속
    agent_page = AgentEnterPage(driver)
    agent_page.open()

    # 내 에이전트 이동
    my_agent_btn = driver.find_element(By.LINK_TEXT, "내 에이전트")
    my_agent_btn.click()
    time.sleep(3)

    # 내 에이전트 목록 스크롤 영역
    scrollers = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='virtuoso-scroller']")
    my_agent_scroller = scrollers[1]

    prev_max_index = -1
    first_agent_name = None
    last_agent_name = None

    for i in range(10):
        agent_items = my_agent_scroller.find_elements(By.CSS_SELECTOR, "div[data-index]")
        agent_indexes = [int(item.get_attribute("data-index")) for item in agent_items]
        max_index = max(agent_indexes)

        # 현재 로드된 에이전트 이름 목록
        agent_names = [
            item.find_element(By.CSS_SELECTOR, "p.MuiTypography-body1.MuiTypography-noWrap").text
            for item in agent_items
        ]

        # 첫 번째 루프에서 첫 번째 에이전트 이름 저장
        if i == 0 and agent_names:
            first_agent_name = agent_names[0]

        # 매번 마지막 항목 이름 갱신
        if agent_names:
            last_agent_name = agent_names[-1]

        # 더 이상 새로 로드된 게 없으면 종료
        if max_index == prev_max_index:
            break

        # 스크롤 내리기
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", my_agent_scroller)
        time.sleep(1)

        # 전 루프의 인덱스 값을 prev로 저장해 비교
        prev_max_index = max_index

    print(f"\n🟢 첫 번째 에이전트 이름: {first_agent_name}")
    print(f"🔵 마지막 에이전트 이름: {last_agent_name}")

    assert last_agent_name is not None, "⛔ [FAIL] 에이전트 이름 확인 실패"
    print("✅ [PASS] 에이전트 이름 확인 성공")