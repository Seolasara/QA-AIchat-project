import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage


def test_HIST003_history_search(driver) :
    login_page = LoginPage(driver)
    login_page.page_open()
    login_page.login()
    time.sleep(5)

    # 새 채팅 세션을 만들기 위한 기존 세션 생성
    message_box = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Enter your message...']").send_keys(
        "테스트 검색어 : 엘리스")
    message_box_btn = driver.find_element(By.ID,"chat-submit").click()
    time.sleep(5)

    
