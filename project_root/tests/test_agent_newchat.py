import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage
from src.pages.agent_enter_page import AgentEnterPage

def test_HIST025_agent_newchat(driver,login) :

    # 에이전트 페이지 접속
    agent_page = AgentEnterPage(driver)
    agent_page.open()

    # 에이전트 리스트 중 첫번째 에이전트 선택
    list = driver.find_elements(By.CSS_SELECTOR, '[data-testid="virtuoso-item-list"] [data-index="0"]')
    frist_agent = list[1]
    frist_agent.click()
    time.sleep(3)
    
    # 테스트 메세지 전송
    msg_input = driver.find_element(By.NAME,"input").send_keys("무슨 에이전트인지 한줄로 소개해줘")
    msg_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="보내기"]').click()
    time.sleep(3)

    # 답변 확인
    chat_container = driver.find_element(By.CSS_SELECTOR, '.css-ovflmb')
    time.sleep(3)
    agent_responses = chat_container.find_elements(By.CSS_SELECTOR, 'div.aichatkit-md p')
    print(agent_responses[0].text)

    assert len(agent_responses) > 0, "⛔ [FAIL] 에이전트 새 채팅 생성 실패"
    print("✅ [PASS] 에이전트 새 채팅 생성 성공")


