import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage


def test_HIST001_newchat_create(driver,send_test_message,login) :
    
    # 새 채팅 세션을 만들기 위한 기존 세션 생성
    time.sleep(2)
    send_test_message("새 채팅을 테스트하기 위한 테스트 채팅 메일입니다(답장하지마)")

    # 새 채팅 세션 생성
    newchat_btn = driver.find_element(By.CSS_SELECTOR, "div[role='button'].MuiListItemButton-root")    #버튼 중 첫번째 요소를 가져옴
    newchat_btn.click()
    time.sleep(5)


    assert "qaproject.elice.io" in driver.current_url, f"⛔ [FAIL] 새 채팅 생성 실패 - 현재 URL = {driver.current_url}"
    print("✅ [PASS] 새 채팅 생성 성공")
    time.sleep(5)

    

