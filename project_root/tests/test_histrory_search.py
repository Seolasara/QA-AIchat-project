import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage


def test_HIST003_history_search(driver,send_test_message,login) :
    # login_page = LoginPage(driver)
    # login_page.page_open()
    # login_page.login()
    # time.sleep(5)

    # 새 채팅 세션을 만들기 위한 기존 세션 생성
    send_test_message("테스트 키워드 : 엘리스")

    # 히스토리 검색 버튼 클릭
    search_btn = driver.find_element(
        By.XPATH,
        "//div[@role='button' and .//span[text()='검색']]"
    )
    search_btn.click()
    time.sleep(5)

    # 검색어 입력 
    search_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='대화 검색...']")
    search_input.clear()
    search_input.send_keys("엘리스")
    time.sleep(5)

    # 검색 목록 검증
    search_result = driver.find_element(By.CSS_SELECTOR, "div[data-value*='엘리스']")
    assert "엘리스" in search_result.text  ,"⛔ [FAIL] 히스토리 검색 실패 "
    print("✅ [PASS] 히스토리 검색 성공")
















    
