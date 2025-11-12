import time
import platform
import os
from selenium.webdriver.common.by import By
from src.pages.login_page import LoginPage
from src.pages.agent_page import AgentPage
from src.pages.agent_enter_page import AgentEnterPage
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

def test_CSTM030_agent_delete(driver,login) :
    wait = WebDriverWait(driver, 10)

    # 내 에이전트 이동
    agent_page = AgentEnterPage(driver)
    agent_page.open()
    my_agent_btn = driver.find_element(By.LINK_TEXT, "내 에이전트")
    my_agent_btn.click()

    # 첫번째 에이전트 삭제
    first_agent = driver.find_elements(By.CSS_SELECTOR, 'button svg[data-testid="trashIcon"]')[0].click()
    delete_button = driver.find_element(By.XPATH, "//button[text()='삭제']").click()

    # 삭제 메세지
    wait.until(EC.text_to_be_present_in_element((By.ID, "notistack-snackbar"), "에이전트가 삭제되었습니다."))
    message = wait.until(EC.presence_of_element_located((By.ID, "notistack-snackbar"))).text.strip()
    assert "에이전트가 삭제되었습니다." in message, "⛔ [FAIL] 삭제 완료 메세지X"
    print("✅ [PASS] 에이전트 삭제 완료") 


    
def test_CSTM031_agent_delete_refresh(driver, new_agent):
    wait = WebDriverWait(driver, 10)

    # 삭제용 에이전트 생성
    new_agent.set_name("삭제 테스트용 에이전트") 
    time.sleep(3)
    new_agent.set_rules("삭제 테스트") 
    new_agent.set_start_message("식제 테스트 에이전트 입니다.")
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
    time.sleep(5)

    # 에이전트 삭제
    first_agent = driver.find_elements(By.CSS_SELECTOR, 'button svg[data-testid="trashIcon"]')[0].click()
    delete_button = driver.find_element(By.XPATH, "//button[text()='삭제']").click()
    wait.until(EC.text_to_be_present_in_element((By.ID, "notistack-snackbar"), "에이전트가 삭제되었습니다."))
    message = wait.until(EC.presence_of_element_located((By.ID, "notistack-snackbar"))).text.strip()
    assert "에이전트가 삭제되었습니다." in message, "⛔ [FAIL] 삭제 완료 메세지X"
    print("✅ [PASS] 에이전트 삭제 완료") 

    # 새로고침 후 삭제 재확인
    driver.refresh()
    time.sleep(3)
    agents = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='virtuoso-item-list']")
    agent_names = [a.text for a in agents]
    assert "삭제 테스트용 에이전트" not in agent_names, "⛔ [FAIL] 에이전트 삭제되지 않음"
    print("✅ [PASS] 에이전트 삭제 재확인 완료") 
