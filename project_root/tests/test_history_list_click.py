import time
from selenium.webdriver.common.by import By
from src.pages.login_page import LoginPage


def test_HIST028_agent_btn(driver,login,send_test_message) :

    # 테스트용 메세지 전송
    send_test_message("히스토리 목록 클릭 테스트 메세지(답장하지마)")
    time.sleep(3)

    # 메인페이지 이동
    driver.get("https://qaproject.elice.io/ai-helpy-chat")

    # 히스토리 중 가장 최신대화 클릭
    list = driver.find_elements(By.CSS_SELECTOR, '[data-testid="virtuoso-item-list"] [data-index="0"]')
    history_frist = list[0]
    history_frist.click()
    time.sleep(3)

    # 대화 내역 확인
    chat_container = driver.find_element(By.CSS_SELECTOR, '.flex.flex-col.flex-grow.overflow-y-auto')
    user_msg = chat_container.find_elements(By.CSS_SELECTOR, "div[data-step-type='user_message'] .prose")
    ai_msg = chat_container.find_elements(By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .prose")

    assert len(user_msg) > 0 and len(ai_msg) > 0, "⛔ [FAIL] 사용자 또는 헬피 메시지 확인 실패"
    print("✅ [PASS] 사용자 및 헬피 메시지 정상 확인")


