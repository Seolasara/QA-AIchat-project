import time
import platform
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from src.pages.login_page import LoginPage


def test_HIST035_chat_edit(driver,login,send_test_message) :

    # 테스트용 메세지 전송
    send_test_message("히스토리 제목 수정 테스트(답장하지마)")
    time.sleep(3)

    # 히스토리 중 첫번째 대화 세션 선택
    chat_frist = driver.find_element(By.CSS_SELECTOR, '[data-testid="virtuoso-item-list"] [data-index="0"]')
    chat_frist_title = chat_frist.text
    print(f"수정 전 첫 번째 대화 제목 : {chat_frist_title}")

    btn = chat_frist.find_element(By.CSS_SELECTOR, "button.MuiIconButton-root")
    ActionChains(driver).move_to_element(btn).perform()
    btn.click()
    time.sleep(3)

    # 드롭다운에서 이름 변경 버튼 클릭
    del_btn = driver.find_element(By.CSS_SELECTOR, "li[tabindex='0']")
    del_btn.click()

    # 대화 제목 변경 입력 
    title_input = driver.find_element(By.NAME,"name")
    title_input.click()

    # 운영체제에 맞는 input 내용 초기화
    if platform.system() == "Darwin":  # macOS
        title_input.send_keys(Keys.COMMAND + "a")
    else:  # Windows/Linux
        title_input.send_keys(Keys.CONTROL + "a")

    title_input.send_keys(Keys.BACKSPACE)  # 기존 값 삭제
    time.sleep(0.5)

    title_input.send_keys("히스토리 제목 수정 완료")
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()
    time.sleep(3)

    # 변경 후 제목
    chat_frist_after = driver.find_element(By.CSS_SELECTOR, '[data-testid="virtuoso-item-list"] [data-index="0"]')
    chat_frist_after_title = chat_frist_after.text
    print(f"수정 후 첫 번째 대화 제목 : {chat_frist_after_title}")

    assert "히스토리 제목 수정 완료" == chat_frist_after_title, "⛔ [FAIL] 제목 변경 실패"
    print("✅ [PASS] 제목 변경 성공")
