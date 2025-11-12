import time 
import os
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from src.pages.login_page import LoginPage 
from src.pages.agent_page import AgentPage 


def test_CSTM019_agent_preview(driver,new_agent): 

    # 전체 설정한 에이전트 생성
    wait = WebDriverWait(new_agent.driver, 10)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(project_root, "src", "resources", "20.5mb.jpg")
    # 1. 이미지 업로드
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='plusIcon']"))).click()
    image_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))).send_keys(image_path)
    assert os.path.exists(image_path), f"⛔ [FAIL] 파일 없음: {image_path}"
    image = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.MuiAvatar-img')))
    # 2. 입력 필드 이름/한줄 소개/규칙/시작대화 입력 
    new_agent.set_name("미리보기 테스트용 에이전트")
    time.sleep(1)
    new_agent.set_description("미리보기 테스트용 한줄소개")
    new_agent.set_rules("미리보기 테스트용 에이전트 입니다.")
    new_agent.set_start_message("안녕하세요 미리보기 테스트용 에이전트 입니다.")
    # 3. 파일 업로드(1번과 같은 파일)
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[2]"))).send_keys(image_path)
    file = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='20.5mb.jpg']")))
    # 4. 기능 전체 선택
    new_agent.checkbox_functions("search", "browsing", "image", "execution")
    # 5. 만들기/저장 클릭
    new_agent.click_create()
    new_agent.click_save()

    time.sleep(5)

    # 미리보기 
    pre_name = driver.find_element(By.CSS_SELECTOR, "div.css-o58jes h6.MuiTypography-h6").text
    pre_desc = driver.find_element(By.CSS_SELECTOR, "div.css-o58jes p.MuiTypography-body1").text
    pre_rule = driver.find_element(By.CSS_SELECTOR, "div.eawehs30 p.MuiTypography-body1").text

    assert (pre_name == "미리보기 테스트용 에이전트" and
        pre_desc == "미리보기 테스트용 한줄소개" and
        pre_rule == "안녕하세요 미리보기 테스트용 에이전트 입니다."), "⛔ [FAIL] 미리보기 확인 실패"
    print("✅ [PASS] 미리보기 성공")



