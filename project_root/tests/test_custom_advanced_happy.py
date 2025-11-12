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
    wait = WebDriverWait(new_agent.driver, 10)
    # 1. 필수값 이름/규칙 입력 선행
    new_agent.set_name("테스트") 
    time.sleep(3)
    new_agent.set_rules("테스트") 

    # 2. "+"버튼 클릭 
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='plusIcon']"))).click()
    
    # 3. 이미지 생성 버튼 누르고 대기
    new_agent.driver.find_element(By.XPATH, "//li[normalize-space(text())='이미지 생성기']").click()

    image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.MuiAvatar-img')))
    assert image.is_displayed(), "⛔ [FAIL] 이미지 생성 실패"
    print("✅ [PASS] 랜덤 이미지 생성 완료") 



# --- 에이전트 대용량 사진 업로드 --- 
def test_CSTM011_large_image(new_agent): 
    wait = WebDriverWait(new_agent.driver, 10)

    # 파일 경로 설정
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(project_root, "src", "resources", "20.5mb.jpg")

    # 1. "+"버튼/사진 업로드 버튼 클릭 
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='plusIcon']"))).click()
    new_agent.driver.find_element(By.XPATH, "//li[normalize-space(text())='사진 업로드']").click()

    # 2. 숨겨진 input 찾기 / 업로드
    file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))).send_keys(image_path)

    # 3. 이미지 업로드 확인
    image = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.MuiAvatar-img')))
    assert image.is_displayed(), "⛔ [FAIL] 이미지 업로드 실패"
    print("✅ [PASS] 20.5MB 이미지 업로드 성공") 
 



    # --- 모든 기능 설정한 에이전트 생성 --- 
def test_CSTM013_with_all_functions(new_agent):
    wait = WebDriverWait(new_agent.driver, 10)

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(project_root, "src", "resources", "20.5mb.jpg")

    # 1. 이미지 업로드
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='plusIcon']"))).click()
    image_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))).send_keys(image_path)
    assert os.path.exists(image_path), f"⛔ [FAIL] 파일 없음: {image_path}"

    image = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.MuiAvatar-img')))
    assert image.is_displayed(), "⛔ [FAIL] 이미지 업로드 실패"
    print("✅ [PASS] 이미지 업로드 성공") 

    # 2. 입력 필드 이름/한줄 소개/규칙/시작대화 입력 
    new_agent.set_name("테스트2")
    time.sleep(1)
    # new_agent.set_description("테스트2")
    new_agent.set_rules("테스트2")
    new_agent.set_start_message("테스트2")

    # 3. 파일 업로드(1번과 같은 파일)
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[2]"))).send_keys(image_path)
    assert os.path.exists(image_path), f"⛔ [FAIL] 파일 없음: {image_path}"

    file = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='20.5mb.jpg']")))
    assert file.is_displayed(), "⛔ [FAIL] 파일 업로드 실패"
    print("✅ [PASS] 파일 업로드 성공")

    # 4. 기능 전체 선택
    new_agent.checkbox_functions("search", "browsing", "image", "execution")

    checkboxes = [
        new_agent.search_function, 
        new_agent.browsing_function, 
        new_agent.image_function, 
        new_agent.execution_function,
        ]

    for box in checkboxes:
        assert new_agent.driver.find_element(*box).is_selected()
    print("✅ [PASS] 모든 기능 체크박스 선택 완료")
    
    # 5. 만들기/저장 클릭
    new_agent.click_create()
    new_agent.click_save()

    # 6. 에이전트 생성 메세지 확인
    text = wait.until(EC.presence_of_element_located((By.ID, "notistack-snackbar"))).text.strip()
    assert "에이전트가 생성 되었습니다." in text, "⛔ [FAIL] 생성 실패"
    print("✅ [PASS] 에이전트 생성 완료") 



# --- 다양한 확장자 업로드 테스트 ---
def test_CSTM015_upload_extensions(new_agent):
    wait = WebDriverWait(new_agent.driver, 10)

    # 파일 경로
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = [
        os.path.join(project_root, "src", "resources", "testfile2.pdf"),
        os.path.join(project_root, "src", "resources", "test.xlsx"),
        os.path.join(project_root, "src", "resources", "test.docx"),
        os.path.join(project_root, "src", "resources", "test.pptx"),
        os.path.join(project_root, "src", "resources", "18mb.jpg"),
        os.path.join(project_root, "src", "resources", "helpy chat.png"),
        os.path.join(project_root, "src", "resources", "test.html"),
        os.path.join(project_root, "src", "resources", "test.xml"),
    ]

    # 파일 input 찾기
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[2]")))

    # 한 번에 업로드
    file_input.send_keys("\n".join(files))

    # 확장자 검증
    for file_path in files:
        extension = os.path.splitext(file_path)[1] # 확장자 추출
        filename = os.path.basename(file_path) # 파일명 추출
        uploaded_file = wait.until(EC.visibility_of_element_located((By.XPATH, f"//p[text()='{filename}']")))

        assert uploaded_file.is_displayed(), f"⛔ [FAIL] {extension} 확장자 업로드 실패"
        print(f"✅ [PASS] {extension} 확장자 업로드 성공")

