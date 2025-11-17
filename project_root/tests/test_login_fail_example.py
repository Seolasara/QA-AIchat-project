import time
from src.pages.login_page import LoginPage

def test_login_fail_example(driver, login):
    # 로그인 후 URL 체크 – 일부러 틀린 값 넣어서 실패시키기
    assert "wrong-url.com" in driver.current_url, "URL이 예상과 다릅니다! (일부러 실패)"

    print("이 문장은 실행되지 않음")  # assert에서 이미 실패함
