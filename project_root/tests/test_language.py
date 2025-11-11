import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 테스트 계정2 로그인
@pytest.fixture 
def test_account2(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://qaproject.elice.io/ai-helpy-chat")
    driver.find_element(By.NAME, "loginId").send_keys("team2a@elice.com")
    driver.find_element(By.NAME, "password").send_keys("team2elice!@")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    return driver

# 언어 설정 메뉴까지 진입
@pytest.fixture
def language(test_account2):
    driver = test_account2
    wait = WebDriverWait(driver, 10)
    
    # 1. 프로필 아이콘 클릭
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='PersonIcon']"))).click()

    # 2. 프로필이 뜰 때까지 대기
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-elice-user-profile-content='true']")))

    time.sleep(1) # UI가 완전히 뜰 때까지 조금 더 대기(다른 요소에 의한 요소 가림 방지) 

    # 3. 언어설정 클릭
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-menu-id='locale_setting']"))).click()
 
    time.sleep(1) # UI가 완전히 뜰 때까지 조금 더 대기(다른 요소에 의한 요소 가림 방지)
    return driver


# --- 영어로 변경 ---
def test_ACCT010_change_english(language):
    driver = language
    wait = WebDriverWait(driver, 10)

    # 프로필 언어설정에서 "American English"(영어) 클릭
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='American English']"))
    ).click()

    message_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='Enter your message...']"))
    )

    actual_text = message_box.get_attribute("placeholder")
    expected_text = "Enter your message..."

    assert actual_text == expected_text, "[FAIL] 영어 변경 실패"
    print("✅ [PASS] 영어 번경 성공")


# --- 일본어로 변경 ---
def test_ACCT011_change_japanese(language):
    driver = language
    wait = WebDriverWait(driver, 10)

    # 프로필 언어설정에서 "日本語 (日本)"(일본어) 클릭
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='日本語 (日本)']"))
    ).click()

    message_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='メッセージを入力してください...']"))
    )

    actual_text = message_box.get_attribute("placeholder")
    expected_text = "メッセージを入力してください..."

    assert actual_text == expected_text, "[FAIL] 일본어 변경 실패"
    print("✅ [PASS] 일본어 번경 성공")


# --- 태국어로 변경 ---
def test_ACCT012_change_thai(language):
    driver = language
    wait = WebDriverWait(driver, 10)

    # 프로필 언어설정에서 "ไทย (ไทย)"(태국어) 클릭
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='ไทย (ไทย)']"))
    ).click()

    message_box = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='ป้อนข้อความของคุณ...']"))
    )

    actual_text = message_box.get_attribute("placeholder")
    expected_text = "ป้อนข้อความของคุณ..."

    assert actual_text == expected_text, "[FAIL] 태국어 변경 실패"
    print("✅ [PASS] 태국어 번경 성공")



# --- 영어로 변경 후 재로그인시 유지 확인 ---
def test_ACCT013_change_english_relogin(language):
    driver = language
    wait = WebDriverWait(driver, 10)

    # 1. 언어 초기화
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='한국어(대한민국)']"))).click()
    time.sleep(3) # UI 안정화

    driver.find_element(By.CSS_SELECTOR, "svg[data-testid='PersonIcon']").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-elice-user-profile-content='true']")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-menu-id='locale_setting']"))).click()

    # 2. 영어 선택
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='American English']"))).click()
    message_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='Enter your message...']")))

    assert message_box.get_attribute("placeholder") == "Enter your message...", "[FAIL] 영어 변경 실패"
    print("✅ [PASS] 영어 번경 성공")

    # 3. 로그아웃
    driver.find_element(By.CSS_SELECTOR, "svg[data-testid='PersonIcon']").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-elice-user-profile-content='true']")))
    time.sleep(1) # UI가 완전히 뜰 때까지 조금 더 대기(다른 요소에 의한 요소 가림 방지)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Logout']"))).click()
    wait.until(EC.url_contains("accounts.elice.io"))

    assert "accounts" in driver.current_url, "[FAIL] 로그아웃 실패"
    print("✅ [PASS] 로그아웃 성공")

    # 4. 재로그인
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("team2elice!@")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    wait.until(EC.url_contains("qaproject.elice.io"))

    assert "qaproject.elice.io" in driver.current_url, "[FAIL] 재로그인 실패"
    print("✅ [PASS] 재로그인 성공")

    # 5. 언어 설정 유지 확인
    message_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='Enter your message...']")))

    assert message_box.get_attribute("placeholder") == "Enter your message...", "[FAIL] 영어 유지 실패"
    print("✅ [PASS] 영어 유지 성공")
