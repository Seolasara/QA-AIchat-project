import pytest
import time
from src.pages.login_page import LoginPage
from src.pages.image_upload_page import HelpyChatPage
from src.utils.config_reader import read_config


def test_CADV001_image_upload_success(driver, login, send_test_message):
    # 이미지 업로드 및 메시지 전송 성공 테스트

    from src.pages.image_upload_page import HelpyChatPage
    from src.utils.config_reader import read_config 

    config = read_config("helpychat")
    base_url = config["base_url"]

    driver.get(base_url)
    time.sleep(3)

    chat_page = HelpyChatPage(driver)

    chat_page.upload_image("dogimage.jpg")
    send_test_message("이 이미지에 대해 설명해줘")

    assert "<img" in driver.page_source
    assert "이 이미지에 대해 설명해줘" in driver.page_source

    time.sleep(10)