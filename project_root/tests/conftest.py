import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from src.pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from src.pages.agent_page import AgentPage
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidElementStateException


@pytest.fixture(scope="function")
def driver():
    """공통 WebDriver 설정"""
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")  # 알림창 차단
    chrome_options.add_argument("--disable-popup-blocking")  # 팝업 차단 해제
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # 💡 '여러 파일 다운로드' 자동 허용 설정
    prefs = {
        "profile.default_content_setting_values.automatic_downloads": 1,  # 여러 파일 다운로드 허용
        "profile.default_content_setting_values.popups": 0,
        "profile.default_content_setting_values.notifications": 2,  # 알림 비활성화
        "download.prompt_for_download": False,  # 다운로드 다이얼로그 안 띄움
    }
    chrome_options.add_experimental_option("prefs", prefs)
    try:
        driver = webdriver.Chrome(options=chrome_options)
        #driver.maximize_window()
        driver.implicitly_wait(5)
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def send_test_message(driver):
    """테스트용 메세지 보내는 fixture (메시지를 매개변수로 받아서 전송)"""
    def _create_chat(message):
        # 메시지 입력 및 전송
        message_box = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='메시지를 입력하세요...']")
        try:
            message_box.clear()
        except InvalidElementStateException:
            pass
        message_box.send_keys(message)
        driver.find_element(By.ID, "chat-submit").click()
        time.sleep(3)
    return _create_chat


@pytest.fixture
def login(driver):
    """HelpyChat 로그인 fixture"""
    login_page = LoginPage(driver)
    login_page.page_open()
    login_page.login()
    time.sleep(3)
    return login_page


@pytest.fixture
def new_agent(driver):
    """로그인 후 커스텀 에이전트 생성 페이지로 이동한 상태를 반환"""
    login_page = LoginPage(driver)
    login_page.page_open()
    login_page.login()

    agent_page = AgentPage(driver)
    agent_page.agent_create()
    return agent_page


@pytest.fixture
def click_plus(driver):
    """HelpyChat의 '+ 버튼' 클릭 """
    wait = WebDriverWait(driver, 15)

    def _click():
        # + 버튼 대기 및 클릭
        plus_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[aria-haspopup='true'] svg[data-icon='plus']")
            )
        )
        # svg 대신 부모 <button> 클릭
        driver.execute_script("arguments[0].closest('button').click();", plus_button)
        time.sleep(1)

    return _click


# 테스트 계정2
@pytest.fixture 
def login2(driver):
    """HelpyChat 계정2 로그인 fixture"""
    login_page = LoginPage(driver)
    login_page.page_open()
    login_page.login2()
    time.sleep(3)
    return driver


# 언어 설정 메뉴까지 진입
@pytest.fixture
def language(login2):
    driver = login2
    wait = WebDriverWait(driver, 10)
    
    # 아이콘 클릭 / 프로필 대기
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='PersonIcon']"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-elice-user-profile-content='true']")))
    time.sleep(1) # UI가 완전히 뜰 때까지 조금 더 대기(다른 요소에 의한 요소 가림 방지) 

    # 3. 언어설정 클릭
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-menu-id='locale_setting']"))).click()
    time.sleep(1) # UI가 완전히 뜰 때까지 조금 더 대기(다른 요소에 의한 요소 가림 방지)
    return driver
