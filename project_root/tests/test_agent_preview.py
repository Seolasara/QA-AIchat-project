import time 
import pytest 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from src.pages.login_page import LoginPage 
from src.pages.agent_page import AgentPage 


def test_CSTM019_agent_preview(new_agent): 
    # 1.로그인 
    # 2. AgentPage 객체 생성 / 에이전트 생성 페이지 이동 

    # 3. 필수값 이름/규칙 입력 
    new_agent.set_name("테스트") 
    time.sleep(3)
    new_agent.set_rules("테스트") 
    
    # 4. 만들기 클릭
    new_agent.click_create()

    # 5. 공개 설정 후 저장 클릭
    new_agent.click_save()

    # 6. 에이전트 생성 메세지 확인
    text = WebDriverWait(new_agent.driver, 10).until(
        EC.presence_of_element_located((By.ID, "notistack-snackbar"))
    ).text.strip()

    assert "에이전트가 생성 되었습니다." in text, "[FAIL] 생성 실패"
    print("✅ [PASS] 에이전트 생성 완료")