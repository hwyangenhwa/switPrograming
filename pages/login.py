import time
import requests
from pages.base import BasePage

class Loginpage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def select_FreeStandard(self):
        """ free/standard 선택"""
        select_URL = self.driver.current_url

        # URL 상태값 확인
        if requests.get(select_URL).status_code == 200:
            # free/standard 선택
            self.clickElement("button.sign-button.free-standard.button.button--simple.button--large", "css")
        else:
            assert False, select_URL + "is connection Error"

    def input_IDPW(self, id, pw):
        """ 아이디/ 패스워드 입력 """

        login_URL = self.driver.current_url
        if requests.get(login_URL).status_code == 200:
            # id 입력 및 미입력 여부 체크
            if id == 'None':
                pass
            else:
                self.sendText(id, "#id", "css")

            # pw 입력 및 미입력 여부 체크
            if pw == 'None':
                pass
            else:
                self.sendText(pw, "#password", "css")

        else:
            assert False, login_URL + "is connection Error"

    def click_Login(self, login):
        """ 로그인 시도 하기 """
        """ login type : ad 잘못된 로그인 시도 타입 """
        """ login type : normal 정상 로그인 시도 타입"""

        if login == 'ad':
            try:
                loginBtn = self.getElement("div.form-buttons > button", "css")

                if loginBtn.is_enabled() == False:
                    pass

                else:
                    loginBtn.click()
                    loginErrorMsg = self.getElement("div.error-text.ng-star-inserted", "css")
                    assert loginErrorMsg.text in '이메일 주소 또는 비밀번호를 확인해주세요.'

            except Exception as ex:
                print(ex)

        elif login == 'normal':
            time.sleep(3)
            self.clickElement("div.form-buttons > button", "css")
            self.getElement("swit-workspace-tile > ul > li > a", "css")