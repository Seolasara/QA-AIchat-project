import configparser
import os

def read_config(section="helpychat"):
    config = configparser.ConfigParser() #파일을 딕셔너리처럼 만들어줌
    base_path = os.path.dirname(os.path.dirname(__file__)) #경로 올바르게 찾아주는 코드
    config_path = os.path.join(base_path, "config", "config.ini")

    config.read(config_path, encoding="utf-8")
    if section not in config: #명시적 에러
        raise KeyError(f"Section '{section}' not found in config.ini")

    return dict(config[section]) #딕셔너리 형태로 반환