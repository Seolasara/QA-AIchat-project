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
    # 필수값 이름/규칙 입력 선행
    new_agent.set_name("테스트") 
    new_agent.set_rules("테스트") 

    # "+"버튼 클릭 
    new_agent.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='plusIcon']"))).click()
    
    # 이미지 생성 버튼 누르고 대기
    new_agent.driver.find_element(By.XPATH, "//li[normalize-space(text())='이미지 생성기']").click()

    image = new_agent.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.MuiAvatar-img')))
    assert image.is_displayed(), "⛔ [FAIL] 이미지 생성 실패"
    print("✅ [PASS] 랜덤 이미지 생성 완료") 



# --- 에이전트 대용량 사진 업로드 --- 
def test_CSTM011_large_image(new_agent): 
    # 파일 경로 설정
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(project_root, "src", "resources", "20.5mb.jpg")

    # "+"버튼 클릭 
    new_agent.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='plusIcon']"))).click()

    # 숨겨진 input 찾기 / 업로드
    file_input = new_agent.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))).send_keys(image_path)

    # 이미지 업로드 확인
    image = new_agent.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.MuiAvatar-img')))
    assert image.is_displayed(), "⛔ [FAIL] 이미지 업로드 실패"
    print("✅ [PASS] 대용량 이미지 업로드 성공") 
 



# --- 모든 기능 설정한 에이전트 생성 --- 
def test_CSTM013_with_all_functions(new_agent):

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(project_root, "src", "resources", "20.5mb.jpg")

    # 이미지 업로드
    new_agent.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='plusIcon']"))).click()
    image_input = new_agent.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))).send_keys(image_path)
    assert os.path.exists(image_path), f"⛔ [FAIL] 파일 없음: {image_path}"

    image = new_agent.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.MuiAvatar-img')))
    assert image.is_displayed(), "⛔ [FAIL] 이미지 업로드 실패"
    print("✅ [PASS] 이미지 업로드 성공") 

    # 입력 필드 이름/한줄 소개/규칙/시작대화 입력 
    new_agent.set_name("테스트2")
    new_agent.set_description("테스트2")
    new_agent.set_rules("테스트2")
    new_agent.set_start_message("테스트2")

    # 파일 업로드(1번과 같은 파일)
    new_agent.upload_file("20.5mb.jpg")
    file = new_agent.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='20.5mb.jpg']")))
    assert file.is_displayed(), "⛔ [FAIL] 파일 업로드 실패"
    print("✅ [PASS] 파일 업로드 성공")

    # 기능 전체 선택
    new_agent.checkbox_functions("search", "browsing", "image", "execution")

    checkboxes = [
        "search_function", 
        "browsing_function", 
        "image_function", 
        "execution_function",
        ]

    for key in checkboxes:
        assert new_agent.driver.find_element(*new_agent.locators[key]).is_selected()
    print("✅ [PASS] 모든 기능 체크박스 선택 완료")
    
    # 만들기/저장 클릭
    new_agent.click_create()
    new_agent.click_save()

    # 에이전트 생성 메세지 확인
    text = new_agent.wait.until(EC.presence_of_element_located((By.ID, "notistack-snackbar"))).text.strip()
    assert "에이전트가 생성 되었습니다." in text, "⛔ [FAIL] 생성 실패"
    print("✅ [PASS] 에이전트 생성 완료") 



# --- 다양한 확장자 업로드 테스트 ---
def test_CSTM015_upload_extensions(new_agent):
    
    files = [
        "testfile2.pdf",
        "test.xlsx",
        "test.docx",
        "test.pptx",
        "18mb.jpg",
        "helpy chat.png",
        "test.html",
        "test.xml",
    ]
    
    # 경로 변환
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_paths = [os.path.join(project_root, "src", "resources", file) for file in files]
    
    # file_input 찾아서 한 번에 업로드
    file_input = new_agent.wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[2]")))
    file_input.send_keys("\n".join(full_paths))
    
    # 각 파일 업로드 확인
    for file in files:
        extension = os.path.splitext(file)[1]
        uploaded_file = new_agent.wait.until(EC.visibility_of_element_located((By.XPATH, f"//p[text()='{file}']")))
        assert uploaded_file.is_displayed(), f"⛔ [FAIL] {extension} 업로드 실패"
        print(f"✅ [PASS] {extension} 업로드 성공")
