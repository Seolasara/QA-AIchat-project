import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path


class HelpyChatPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def upload_image(self, filename: str):

        plus_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-haspopup='true'] svg[data-icon='plus']"))
        )
        self.driver.execute_script("arguments[0].closest('button').click();", plus_button)

        # 숨겨진 input[type=file] 직접 접근
        file_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#upload-button-input[type='file']"))
        )
        self.driver.execute_script("arguments[0].style.display = 'block';", file_input)

        # 파일 경로 설정
        project_root = Path(__file__).resolve().parents[2]
        file_path = project_root / "src" / "resources" / filename
        if not file_path.exists():
            raise FileNotFoundError(f"파일이 존재하지 않습니다: {file_path}")

        # 파일 업로드 (탐색창 없이)
        file_input.send_keys(str(file_path))

        # 업로드 완료 대기
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))