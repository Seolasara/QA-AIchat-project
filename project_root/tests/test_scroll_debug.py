import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import LoginPage

def test_find_real_scroll_container_stable(driver, login, send_test_message):
    send_test_message("오늘 주요 기사 내용 요약해줘")

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[data-step-type='assistant_message'] .message-content")
        )
    )
    print("✅ [PASS] AI 응답 렌더링 완료")
    time.sleep(2)

    # 최대 div 개수 제한 (너무 많으면 너무 오래 걸림)
    max_divs = 200  

    for i in range(max_divs):
        try:
            # 매번 새로 div 요소를 찾아서 stale 방지
            div = driver.find_elements(By.TAG_NAME, "div")[i]

            scroll_height = driver.execute_script("return arguments[0].scrollHeight;", div)
            client_height = driver.execute_script("return arguments[0].clientHeight;", div)
            scroll_top = driver.execute_script("return arguments[0].scrollTop;", div)

            # 스크롤 가능한 div만 탐색
            if scroll_height > client_height:
                print(f"\n[{i}] ✅ scrollable div 발견!")
                print(f"   scrollHeight={scroll_height}, clientHeight={client_height}, scrollTop={scroll_top}")

                # 스크롤 이동 테스트
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", div)
                time.sleep(0.5)
                new_top = driver.execute_script("return arguments[0].scrollTop;", div)
                print(f"   ⬇️ 하단 이동 후 scrollTop={new_top}")

                driver.execute_script("arguments[0].scrollTop = 0;", div)
                time.sleep(0.5)
                new_top2 = driver.execute_script("return arguments[0].scrollTop;", div)
                print(f"   ⬆️ 상단 이동 후 scrollTop={new_top2}")

        except IndexError:
            break  # div 개수 다 탐색했으면 종료
        except Exception as e:
            print(f"[{i}] ⚠️ 예외 발생: {type(e).__name__} — {e}")
            continue

    print("\n✅ 디버그 완료 — scrollTop이 실제 변하는 div를 찾아봐!")