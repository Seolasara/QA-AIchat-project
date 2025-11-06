import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_helpychat_login_fixed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(
        "https://accounts.elice.io/accounts/signin/me?continue_to=https%3A%2F%2Fqatrack.elice.io%2Fai-helpy-chat&lang=en-US&org=qatrack"
    )

    # 1️⃣ 아이디 입력
    id_field = driver.find_element(By.XPATH, '//input[@type="email" or @id=":r0:"]')
    id_field.click()
    id_field.send_keys("wivepam991@fandoe.com")

    # 2️⃣ 비밀번호 필드 찾기 (정확한 XPath)
    pw_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="password" and @type="password"]'))
)

    # 3️⃣ JavaScript로 값과 이벤트 강제 주입 (React MUI 완전 대응)
    password = "password123!"
    driver.execute_script("""
    const input = arguments[0];
    const value = arguments[1];

    // Focus 먼저
    input.focus();

    // 실제 값 대입
    const lastValue = input.value;
    input.value = value;

    // React 내부 value tracker 갱신
    const tracker = input._valueTracker;
    if (tracker) {
        tracker.setValue(lastValue);
    }

    // React 가 인식하도록 input / change 이벤트 발생
    const event = new InputEvent('input', { bubbles: true });
    input.dispatchEvent(event);
    input.dispatchEvent(new Event('change', { bubbles: true }));
    """, pw_field, password)

    time.sleep(1)

    # 4️⃣ 로그인 버튼 클릭 (정확한 XPath)
    login_btn = driver.find_element(By.XPATH, '//button[@type="submit" or @id=":r3:"]')
    login_btn.click()

    # 5️⃣ 페이지 이동 대기
    time.sleep(10)

    # 6️⃣ 로그인 성공 여부 검증
    assert "qatrack.elice.io" in driver.current_url
    print("✅ HelpyChat 로그인 자동화 테스트 성공!")

    driver.quit()
