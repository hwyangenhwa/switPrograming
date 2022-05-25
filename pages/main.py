import time

from selenium.webdriver.support.wait import WebDriverWait
from pages.base import BasePage

class Mainpage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def check_main(self) -> None:
        """ 메인페이지 항목 체크 """
        """ 타이틀, 상단 헤더아이콘, 메인 페이지 텍스트 """

        # 타이틀 제목
        assert (WebDriverWait(self.driver, 10).until(lambda x: x.execute_script("return document.title"))in "Swit")

        try:
            loginoutBtn = self.getElement("li.gnb__item.gnb__item--sign > a", "css")
            if loginoutBtn.text == "로그아웃":
                time.sleep(1)
                loginoutBtn.click()
        except:
            pass

    def check_mainHeaderMenu(self) -> None:
        """ mainHeaderMenu """

        # 상단 헤더 아이콘 (핵심가치, 리모트워크 ,기능 둘러보기, 요금 안내, 더보기)
        mainMenus = self.waitForElements("//ul[@class='gnb']//descendant::li/a[@class='gnb-button']", "xpath")
        for icon in mainMenus:
            assert icon.text in ['핵심 가치', '리모트워크', '기능 둘러보기', '요금 안내', '더 보기']

    def future_workOS(self):
        """ 미래형 WorkOS항목 선택 """

        # 미래형 WorkOS
        mainPageTxt = self.waitForElement("div > div.sec-osfor-contents-head.ng-tns-c154-1 > h2", "css")
        assert mainPageTxt.text in "미래형 Work OS"

        # Swit의 특징 요소 검증 (확장성, 호환성, 기능성)
        self.waitForElement("div > div.sec-osfor-contents-body.ng-tns-c154-1.sec-osfor-contents-body--kor > dl:nth-child(1) > dt > a", "css")
        self.clickElement(
            "div > div.sec-osfor-contents-body.ng-tns-c154-1.sec-osfor-contents-body--kor > dl:nth-child(1) > dt > a",
            "css")
        # 호환성
        self.waitForElement("div > div.sec-osfor-contents-body.ng-tns-c154-1.sec-osfor-contents-body--kor > dl:nth-child(2) > dt > a", "css")
        self.clickElement(
            "div > div.sec-osfor-contents-body.ng-tns-c154-1.sec-osfor-contents-body--kor > dl:nth-child(2) > dt > a",
            "css")
        # 기능성
        self.waitForElement("div > div.sec-osfor-contents-body.ng-tns-c154-1.sec-osfor-contents-body--kor > dl:nth-child(3) > dt > a", "css")
        self.clickElement("div > div.sec-osfor-contents-body.ng-tns-c154-1.sec-osfor-contents-body--kor > dl:nth-child(3) > dt > a", "css")

        # 이메일 입력칸 확인
        self.waitForElement("div > span > input", "css")
        # 이메일 보내기 Btn 확인
        self.waitForElement("div > input", "css")

    def check_employeeDanger(self):
        """ 직원 생산성의 위기"""

        nextInf = self.waitForElement("div > div.main-slider-wrap.main-slider-wrap--bg.ng-tns-c154-1", "css")
        self.driver.execute_script("arguments[0].scrollIntoView();", nextInf)

        # 직원 생산성의 위기 문구로 이동 및 문구 확인
        employee_prod = self.waitForElement("div.main-slider-wrap.main-slider-wrap--bg.ng-tns-c154-1 > div > div > h2", "css")
        assert employee_prod.text in '직원 생산성의 위기'

    def check_workosFormula(self):
        """ 기능의 결합으로 재정의된 workOS의 공식 """

        # 기능 결합 Work OS의 공식 문구로 이동 및 문구 확인
        work_os = self.waitForElement("div > div:nth-child(3) > div > div > h2", "css")
        self.driver.execute_script("arguments[0].scrollIntoView();", work_os)
        assert work_os.text in '기능의 결합으로 재정의된\n‘Work OS’의 공식'

    def check_organizationCulture(self):
        """ 사람 중심의 미래형 조직 문화 """

        # 사람중심의 미래형 조직문화 문구로 이동 및 문구 확인
        orgCulture = self.waitForElement("div.main-slider-wrap.main-slider-wrap--bg2.main-slider-wrap--short.ng-tns-c154-1 > div > div > h2", "css")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.execute_script("arguments[0].scrollIntoView();", orgCulture))
        assert orgCulture.text in '사람 중심 미래형\n조직 문화'

    def check_simply(self):
        """ 내일의 일하는 방식을 더 단순하게 """

        # 일하는 방식을 단순하게 문구로 이동 및 문구 확인
        simplyWork = self.waitForElement("div > div:nth-child(5) > div > div > h2", "css")
        self.driver.execute_script("arguments[0].scrollIntoView();", simplyWork)
        assert simplyWork.text in '내일의 일하는 방식을\n더 단순하게'

    def check_workSpace(self):
        """ 쾌적한 업무 공간 """

        # 쾌적한 업무공간 문구로 이동 및 문구 확인
        workSpace = self.waitForElement("div > div.sec-big.ng-tns-c154-1 > div > h3", "css")
        self.driver.execute_script("arguments[0].scrollIntoView();", workSpace)
        assert workSpace.text in '의미있는 일을 이루기 위한\n쾌적한 업무 공간'

    def check_experience(self):
        """ swit experience"""

        # swit 모의체험 문구로 이동 및 문구 확인
        swit_Experience = self.waitForElement("div > div.sec-simulator.ng-tns-c154-1 > span.sec-simulator__text.ng-tns-c154-1", "css")
        self.driver.execute_script("arguments[0].scrollIntoView();", swit_Experience)
        assert swit_Experience.text in '회원가입 없이\nSwit을 체험해보세요.'

        # swit 모의 체험 Btn
        self.waitForElement("div > div.sec-simulator.ng-tns-c154-1 > div > a", "css")

    def click_loginBtn(self) -> None:
        """ 로그인 하기 """
        time.sleep(3)

        # debugging 모드로 사용 시 세션 유지로 인해서 로그인 상태이면 로그아웃 Btn 선택
        try:
            loginoutBtn = self.getElement("li.gnb__item.gnb__item--sign > a", "css")
            if loginoutBtn.text == "로그아웃":
                time.sleep(1)
                loginoutBtn.click()

        except:
            pass

        self.clickElement("//a[@class='gnb-button ng-star-inserted']", "xpath")