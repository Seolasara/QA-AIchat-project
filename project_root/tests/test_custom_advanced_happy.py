import os
import time 
import pytest 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from src.pages.login_page import LoginPage 
from src.pages.agent_page import AgentPage 


# --- 에이전트 랜덤 이미지 생성 기능 테스트 --- 
def test_CSTM010_create_image(new_agent): 
    # 1.로그인 
    # 2. AgentPage 객체 생성 / 에이전트 생성 페이지 이동 

    # 3. 필수값 이름/규칙 입력 선행
    new_agent.set_name("테스트") 
    time.sleep(3)
    new_agent.set_rules("테스트") 

    # 4. "+"버튼 누르기 
    WebDriverWait(new_agent.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='plusIcon']"))
    ).click()
    
    # 5. 이미지 생성 버튼 누르고 대기
    new_agent.driver.find_element(By.XPATH, "//li[normalize-space(text())='이미지 생성기']").click()
    
    image = WebDriverWait(new_agent.driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'img.MuiAvatar-img'))
    )

    # 6. 랜덤 이미지 생성 확인
    assert image.is_displayed(), "[FAIL] 이미지 생성 실패"
    print("✅ [PASS] 랜덤 이미지 생성 완료") 


# --- 에이전트 대용량 사진 업로드 (필수값 입력 불필요) --- 
def test_CSTM011_large_image(new_agent): 

    # 1. "+"버튼 누르기 
    WebDriverWait(new_agent.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='plusIcon']"))
    ).click()
    
    # 2. 사진 업로드 버튼 클릭
    new_agent.driver.find_element(By.XPATH, "//li[normalize-space(text())='사진 업로드']").click()

    # 3. 숨겨진 <input type='file'> 필드 찾기
    file_input = WebDriverWait(new_agent.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
    )
    
    # 4. 파일 경로 설정 / 전송
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(project_root, "src", "resources", "for_custom.jpg")
    assert os.path.exists(image_path), f"[FAIL] 파일 없음: {image_path}"

    file_input.send_keys(image_path)

    # 5. 이미지 업로드 확인
    image = WebDriverWait(new_agent.driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'img.MuiAvatar-img'))
    )

    assert image.is_displayed(), "[FAIL] 이미지 업로드 실패"
    print("✅ [PASS] 11.4MB 이미지 업로드 성공") 
    
    time.sleep(3)


    # --- 모든 기능 설정한 에이전트 생성 --- 
def test_CSTM013_with_all_functions(new_agent):

    # 1. 이미지 업로드
    WebDriverWait(new_agent.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='plusIcon']"))).click()
    file_input = WebDriverWait(new_agent.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(project_root, "src", "resources", "20.5mb.jpg")
    assert os.path.exists(image_path), f"[FAIL] 파일 없음: {image_path}"

    file_input.send_keys(image_path)
    image = WebDriverWait(new_agent.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.MuiAvatar-img')))

    assert image.is_displayed(), "[FAIL] 이미지 업로드 실패"
    print("✅ [PASS] 이미지 업로드 성공") 
    time.sleep(3)

    # 2. 입력 필드 이름/한줄 소개/규칙/시작대화 입력 
    new_agent.set_name("테스트2")
    time.sleep(3)
    new_agent.set_description("테스트2")
    time.sleep(3)
    new_agent.set_rules("테스트2")
    time.sleep(3)
    new_agent.set_start_message("테스트2")

    # 3. 파일 업로드(1번과 같은 파일)
    # WebDriverWait(new_agent.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[text()='파일 업로드']")))
    # file_input = WebDriverWait(new_agent.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
    # project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # image_path = os.path.join(project_root, "src", "resources", "20.5mb.jpg")
    # assert os.path.exists(image_path), f"[FAIL] 파일 없음: {image_path}"

    # file_input.send_keys(image_path)
    # image = WebDriverWait(new_agent.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='20.5mb.jpg']")))

    # assert image_label.is_displayed(), "[FAIL] 파일 업로드 실패"
    # print("✅ [PASS] 파일 업로드 성공")

    # 4. 기능 전체 선택
    new_agent.checkbox_functions("search", "browsing", "image", "execution")
    
    # 5. 만들기/저장 클릭
    new_agent.click_create()
    new_agent.click_save()

    # 6. 에이전트 생성 메세지 확인
    text = WebDriverWait(new_agent.driver, 10).until(
        EC.presence_of_element_located((By.ID, "notistack-snackbar"))
    ).text.strip()

    assert "에이전트가 생성 되었습니다." in text, "[FAIL] 생성 실패"
    print("✅ [PASS] 에이전트 생성 완료") 

