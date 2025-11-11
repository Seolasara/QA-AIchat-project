import time
import platform
from selenium.webdriver.common.by import By
from src.pages.login_page import LoginPage
from src.pages.agent_page import AgentPage
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

def test_CSTM024_my_agent_edit(driver, new_agent):

    # 수정용 에이전트 생성
    new_agent.set_name("수정 테스트용 에이전트") 
    time.sleep(3)
    new_agent.set_rules("수정 테스트") 
    new_agent.click_create()
    new_agent.click_save()
    time.sleep(3)

    # 뒤로가기
    back_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="뒤로가기"]')
    back_btn.click()

    # 내 에이전트 이동
    my_agent_btn = driver.find_element(By.LINK_TEXT, "내 에이전트")
    my_agent_btn.click()
    time.sleep(5)

    # 에이전트 선택
    first_agent = driver.find_elements(By.CSS_SELECTOR, 'button svg[data-testid="penIcon"]')[0]
    first_agent.click()
    time.sleep(5)
    
    # 에이전트 수정
    new_agent = AgentPage(driver)

    # 기존 이름 지우고 수정
    name = driver.find_element(*new_agent.name_field)
    name.click()
    if platform.system() == "Darwin":
        name.send_keys(Keys.COMMAND + "a")
    else:  
        name.send_keys(Keys.CONTROL + "a")
    name.send_keys(Keys.BACKSPACE) 
    time.sleep(0.5)
    new_agent.set_name("수정 완료 된 에이전트")

    # 기존 규칙 지우고 수정
    rules = driver.find_element(*new_agent.rules_field)
    rules.click()
    if platform.system() == "Darwin":
        rules.send_keys(Keys.COMMAND + "a")
    else:  # Windows/Linux
        rules.send_keys(Keys.CONTROL + "a")
    rules.send_keys(Keys.BACKSPACE)
    time.sleep(0.5)
    new_agent.set_rules("수정 완료 된 테스트 에이전트 입니다.")

    # 시작 대화
    new_agent.set_start_message("수정 완료 된 테스트 에이전트 입니다.")

    # 기능 체크
    new_agent.checkbox_functions("search", "browsing")
    time.sleep(3)
    update_btn = driver.find_element(By.XPATH, "//button[text()='업데이트']").click()
    new_agent.click_save()
    time.sleep(5)

    back_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="뒤로가기"]')
    back_btn.click()
    time.sleep(3)

    # 수정 된 에이전트
    first_agent = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/ai-helpy-chat/agent/"]')[1]

    assert "수정 완료 된 에이전트" in first_agent.text, "⛔ [FAIL] 에이전트 수정 실패"
    print("✅ [PASS] 에이전트 수정 성공")



