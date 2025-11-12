import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from src.pages.login_page import LoginPage


def test_HIST034_chat_delete(driver,login,send_test_message) :
    time.sleep(5)
    
    # 테스트용 메세지 전송
    send_test_message("히스토리 목록 삭제 테스트(답장하지마)")
    time.sleep(3)

    # 히스토리 중 첫번째 대화 세션 선택
    chat_frist = driver.find_element(By.CSS_SELECTOR, '[data-testid="virtuoso-item-list"] [data-index="0"]')
    chat_frist_title = chat_frist.text
    print(f"삭제 전 첫 번째 대화 제목 : {chat_frist_title}")

    btn = chat_frist.find_element(By.CSS_SELECTOR, "button.MuiIconButton-root")
    ActionChains(driver).move_to_element(btn).perform()
    btn.click()
    time.sleep(3)

    # 드롭다운에서 삭제 버튼 클릭
    del_btn = driver.find_element(By.CSS_SELECTOR, "li[tabindex='-1']")
    del_btn.click()
    time.sleep(3)

    # 팝업 창에서 삭제 버튼 클릭
    del_btn2 = driver.find_element(By.CSS_SELECTOR, "button.MuiButton-containedError")
    del_btn2.click()
    time.sleep(5)

    # 삭제 후 히스토리 중 첫번째 대화 세션 선택
    chat_frist_after = driver.find_element(By.CSS_SELECTOR, '[data-testid="virtuoso-item-list"] [data-index="0"]')
    chat_frist_after_title = chat_frist_after.text
    print(f"삭제 후 첫 번째 대화 제목 : {chat_frist_after_title}")

    assert chat_frist_title != chat_frist_after_title, "⛔ [FAIL] 대화 삭제 실패"
    print("✅ [PASS] 대화 삭제 성공")






