import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage

def test_HIST017_close_btn(driver,send_test_message,login) :

    # 히스토리 검색 버튼 클릭
    search_btn = driver.find_element(
        By.XPATH,
        "//div[@role='button' and .//span[text()='검색']]"
    )
    search_btn.click()
    time.sleep(5)

    # 검색창 닫기 버튼 클릭
    close_btn = driver.find_element(By.CLASS_NAME, "lucide-x")
    close_btn.click()
    time.sleep(2)

    # 검증
    search_input = driver.find_elements(By.CSS_SELECTOR, "input[placeholder='대화 검색...']")
    assert len(search_input) == 0, "⛔ [FAIL] 검색창 닫기 실패"
    print("✅ [PASS] 검색창 닫기 성공")
    


