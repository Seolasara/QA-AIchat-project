import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.config_reader import read_config

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.config = read_config("helpychat")
        
        self.email_input = (By.NAME, "loginId")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[text()='Login']")

    def page_open(self):
        self.driver.get( self.config["base_url"])

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login(self):
        self.enter_email(self.config["login_id"])
        self.enter_password(self.config["login_pw"])
        self.click_login_button()

    def login2(self):
        self.enter_email("team2a@elice.com")
        self.enter_password("team2elice!@")
        self.click_login_button()