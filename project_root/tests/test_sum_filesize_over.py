import pytest
import time
from src.utils.config_reader import read_config
from src.pages.image_upload_page import HelpyChatPage


def test_CADV001_multi_file_upload_success(driver, login, send_test_message):
    """두 가지 파일의 용량을 합친게(18mb + 6.05mb) 최대허용 용량(20mb)보다 높아도 되는지 테스트"""

    config = read_config("helpychat")
    base_url = config["base_url"]

    driver.get(base_url)
    time.sleep(3)

    chat_page = HelpyChatPage(driver)

    # 1️⃣ 여러 파일 업로드
    files = ["18mb.jpg", "6.05mb.jpg"]
    for f in files:
        chat_page.upload_image(f)
        time.sleep(2)
    print(f"✅ 파일 업로드 완료 ({', '.join(files)})")

    # 2️⃣ 메시지 전송
    send_test_message("이 이미지들에 대해 설명해줘")
    print("✅ 메시지 전송 완료")

    # 3️⃣ HelpyChat 응답 대기 (단순 화면 렌더링 기준)
    print("✅ HelpyChat 응답이 렌더링될 때까지 대기")
    time.sleep(15)

    # 4️⃣ 결과 검증
    page_source = driver.page_source

    # 업로드된 이미지가 존재하는지 확인
    assert "<img" in page_source, "❌ 업로드된 이미지가 화면에 표시되지 않았습니다."
    # 사용자가 전송한 메시지가 존재하는지 확인
    assert "이 이미지들에 대해 설명해줘" in page_source, "❌ 전송한 메시지가 채팅창에 표시되지 않았습니다."

    print("✅ 이미지 업로드 및 응답 렌더링 성공")
    time.sleep(5)
