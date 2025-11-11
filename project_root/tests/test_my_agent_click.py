import time
from selenium.webdriver.common.by import By
from src.pages.login_page import LoginPage
from src.pages.agent_enter_page import AgentEnterPage
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

def test_CSTM022_my_agent_click(driver, login):

    # 에이전트 페이지 접속
    agent_page = AgentEnterPage(driver)
    agent_page.open()

    # 내 에이전트 이동
    my_agent_btn = driver.find_element(By.LINK_TEXT, "내 에이전트")
    my_agent_btn.click()
    time.sleep(5)

    first_agent = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/ai-helpy-chat/agent/"]')[1]
    first_agent.click()
    time.sleep(5)
    
    assert "builder#form" in driver.current_url, "⛔ [FAIL] 내 에이전트 기본정보 확인 실패"
    print("✅ [PASS] 내 에이전트 기본정보 확인 성공")

