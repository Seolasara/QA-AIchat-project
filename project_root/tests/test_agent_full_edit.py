import time
import platform
import os
from selenium.webdriver.common.by import By
from src.pages.login_page import LoginPage
from src.pages.agent_page import AgentPage
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

def test_CSTM024_my_agent_edit(driver, new_agent):

    # 수정용 에이전트 생성
    new_agent.set_name("수정 테스트용 에이전트") 
    new_agent.set_description("한줄 소개 테스트")
    # time.sleep(0.5)
    new_agent.set_rules("수정 테스트") 
    new_agent.set_start_message("수정 테스트 에이전트 입니다.")
    wait = WebDriverWait(new_agent.driver, 10) 
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    file_path = os.path.join(project_root, "src", "resources", "testfile2.pdf") 
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[2]"))) 
    file_input.send_keys(file_path)
    new_agent.checkbox_functions("search", "browsing", "image", "execution")
    new_agent.click_create()
    new_agent.click_save()
    time.sleep(3)

    # 뒤로가기
    back_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="뒤로가기"]')
    back_btn.click()

    # 내 에이전트 이동
    my_agent_btn = driver.find_element(By.LINK_TEXT, "내 에이전트")
    my_agent_btn.click()
    time.sleep(3)

    # 에이전트 선택
    first_agent = driver.find_elements(By.CSS_SELECTOR, 'button svg[data-testid="penIcon"]')[0]
    first_agent.click()
    time.sleep(3)
    
# 에이전트 수정
    new_agent = AgentPage(driver)

    # 기존 이름 지우고 수정
    name = driver.find_element(*new_agent.name_field)
    name.click()
    current_value = name.get_attribute("value")
    for _ in range(len(current_value)):
        name.send_keys(Keys.BACKSPACE)
    time.sleep(0.2)
    new_agent.set_name("수정 완료 된 에이전트")

    # 기존 한줄소개 지우고 수정
    desc = driver.find_element(By.CSS_SELECTOR, "input[name='description']")
    desc.click()
    current_value = desc.get_attribute("value")
    for _ in range(len(current_value)):
        desc.send_keys(Keys.BACKSPACE)
    time.sleep(0.2)
    new_agent.set_description("수정 완료 된 한줄소개")

    # 기존 규칙 지우고 수정
    rules = driver.find_element(*new_agent.rules_field)
    rules.click()
    current_value = rules.get_attribute("value")
    for _ in range(len(current_value)):
        rules.send_keys(Keys.BACKSPACE)
    time.sleep(0.2)
    new_agent.set_rules("수정 완료 된 테스트 에이전트 입니다.")
    time.sleep(0.5)

    # 시작 대화
    close_buttons = driver.find_elements(By.CSS_SELECTOR, '[data-testid="xmarkIcon"]')
    close_buttons[0].click()
    new_agent.set_start_message("수정 완료 된 테스트 에이전트 입니다.")

    # 파일 삭제
    del_btn = driver.find_element(By.CSS_SELECTOR,'[aria-label="삭제"]')
    del_btn.click()
    time.sleep(2)

    # 기능 체크 해제
    search = driver.find_element(*new_agent.search_function).click()
    browsing = driver.find_element(*new_agent.browsing_function).click()
    time.sleep(3)

    update_btn = driver.find_element(By.XPATH, "//button[text()='업데이트']").click()
    new_agent.click_save()
    time.sleep(8)

    back_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="뒤로가기"]')
    back_btn.click()
    time.sleep(3)

    # 수정 된 에이전트
    first_agent = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/ai-helpy-chat/agent/"]')[1]

    assert "수정 완료 된 에이전트" in first_agent.text, "⛔ [FAIL] 에이전트 수정 실패"
    print("✅ [PASS] 에이전트 수정 성공")



