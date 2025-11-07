import pytest
from selenium import webdriver
import logging
import os
from datetime import datetime

@pytest.fixture(scope="function")
def driver():
    """공통 WebDriver 설정"""
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
<<<<<<< HEAD
    driver.quit()

@pytest.fixture(scope="session", autouse=True)
def setup_logger():
    """전역 로거 설정 (pytest 실행 시 자동 적용)"""
    # 루트 로거 가져오기
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # INFO 이상만 출력

    # 기존 핸들러 제거 (Selenium 등의 DEBUG 로그 차단)
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # 새 콘솔 핸들러 추가
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # INFO 이상만 출력
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logging.info("=== ✅ 전역 로거 설정 완료 ===")
    yield
    logging.info("=== 🧾 테스트 세션 종료 ===")
=======
    driver.quit()
>>>>>>> feature_chat_advanced
