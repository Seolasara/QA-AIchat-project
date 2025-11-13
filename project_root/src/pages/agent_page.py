import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AgentPage:
    def __init__(self,driver):
        self.driver = driver
        # 에이전트 생성/설정 버튼
        self.agent_menu = (By.CSS_SELECTOR, "a[href='/ai-helpy-chat/agent']")
        self.agent_button = (By.CSS_SELECTOR, "a[href='/ai-helpy-chat/agent/builder']")
        self.agent_settings = (By.CSS_SELECTOR, "button[value='form']")
        # 입력 필드
        self.name_field = (By.NAME, "name")
        self.description_field = (By.NAME, "description")
        self.rules_field = (By.NAME, "systemPrompt")
        self.start_message = (By.NAME, "conversationStarters.0.value")
        # 업로드 필드
        self.image_field = (By.CSS_SELECTOR, "svg[data-testid='plusIcon']")
        self.file_field = (By.CSS_SELECTOR, "label input[type='file']")
        # 기능 체크박스
        self.search_function = (By.CSS_SELECTOR, "input[value='web_search']")
        self.browsing_function = (By.CSS_SELECTOR, "input[value='web_browsing']")
        self.image_function = (By.CSS_SELECTOR, "input[value='image_generation']")
        self.execution_function = (By.CSS_SELECTOR, "input[value='code_execution']")
        # 만들기 버튼
        self.create_button = (By.XPATH, "//button[text()='만들기']")
        # 공개설정 저장버튼
        self.save_button = (By.CSS_SELECTOR, 'button[type="submit"]')


    # 에이전트 생성/설정 페이지
    def agent_create(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.agent_menu)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.agent_button)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.agent_settings)).click()

    # 필드 입력 메서드
    def set_name(self, name):
        el = self.driver.find_element(*self.name_field)
        el.clear()
        el.send_keys(name)

    def set_description(self, desc):
        description_el = self.driver.find_element(By.CSS_SELECTOR, "input[name='description']")
        description_el.clear()
        description_el.send_keys(desc)
        description_el.send_keys(Keys.TAB)


    def set_rules(self, rules):
        el = self.driver.find_element(*self.rules_field)
        el.clear()
        el.send_keys(rules)

    def set_start_message(self, msg):
        el = self.driver.find_element(*self.start_message)
        el.clear()
        el.send_keys(msg)

    # 기능 체크박스 클릭(단일)
    def checkbox_function(self, function):
        checkbox_map = {
            "search": self.search_function,
            "browsing": self.browsing_function,
            "image": self.image_function,
            "execution": self.execution_function
        }
        if function in checkbox_map:
            el = self.driver.find_element(*checkbox_map[function])
            if not el.is_selected():
                el.click()

    # 기능 체크박스 클릭(복수)
    def checkbox_functions(self, *functions):
        for function in functions:
            self.checkbox_function(function)

    # 만들기 버튼 활성화까지 대기
    def wait_for_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.create_button)
        )

    # 만들기 버튼 클릭
    def click_create(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.create_button)
        ).click()

    # 공개 설정 저장 버튼
    def click_save(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()

<<<<<<< HEAD
=======
    def upload_file(self, file_path):
        self.wait = WebDriverWait(self.driver, 10)
        project_root = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        file_path = os.path.join(project_root, "src", "resources", file_path)
        file_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[2]"))
        )
        file_input.send_keys(file_path)
>>>>>>> feature_account
