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
    driver.quit()