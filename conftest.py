import json
import re
import time

import pytest
import requests
from pytest_bdd import given, parsers
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service_Chrome
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    """커맨드라인 옵션에 따라 분산 테스트 진행"""
    parser.addoption(
        "--browser",
        action="append",
        default=[],
        choices=["firefox", "chrome"],
        help="Your choice of browser to run tests.",
    )

    """ 커맨드라인 옵션에 따라 테스트 스킵 """
    parser.addoption("--skip", action="store_true", help="Skip testcase.")

    """ worknode or seleniumgrid 옵션에 따라 환경 구성 """
    parser.addoption(
        "--work",
        action="append",
        default=[],
        choices=["selenium", "worknode"],
        help="select testEnvironment",
    )

def pytest_runtest_setup(item):

    """'skip' 이라는 마커를 붙인 테스트를 수행하지 않도록 함"""
    if "skip" in item.keywords and not item.config.getoption("--skip"):
        pytest.skip("need --skip option to run")

def pytest_generate_tests(metafunc):
    """pytest_addoption의 plug-in을 'browser_inf'에 전달"""
    browsers = metafunc.config.getoption("browser")
    metafunc.parametrize("browser_inf", browsers)

    """ pytest_addoption의 plug-in을 'testwork'에 전달 """
    options = metafunc.config.getoption("work")
    metafunc.parametrize("testwork", options)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    out = yield

    # regex pattern
    browser_pattern = re.compile("[a-z]+")
    report = out.get_result()

    # browser inf 추출
    nodeid = str(report.nodeid).split("::")[1]
    testcaseinf = nodeid.split("[")[0]
    browser = browser_pattern.search(nodeid.split("[")[1]).group()

    # Setup 실패일 시 Slack으로 메시지 전송
    if report.when == "setup" and report.outcome == "failed":
        print("Test Automation System" + browser + " is Error Please check the system~")

    # TEST Passed일 시 Grafana 데이터 전송
    if report.when == "call" and report.outcome == "passed":
        print("browser :", browser)
        print("testcaseinf :", testcaseinf)

def web_setting(browser_inf):
    with open("webdriver_setting/" + browser_inf + "Config.json") as config_file:
        config = json.load(config_file)

        if browser_inf == "chrome":

            # Chrome WebDriver 인스턴스 초기화 작업
            options = webdriver.ChromeOptions()
            options.add_argument(config["userAgent"])
            options.add_argument(config["no-sandbox"])
            options.add_argument(config["shm-usage"])
            options.add_argument(config["notification"])
            options.add_argument('--remote-debugging-port=8443')

            return options

        else:
            assert False, "Please intput browser name"

@pytest.fixture(autouse=True)
def driver(browser_inf, testwork):

    """ pytest_generate_tests에서 받은 browser_inf를 통해서 WebdriverInstance 생성 """
    global driverInstance

    # chrome WebInstance (worknode)
    if browser_inf == "chrome":
        options = web_setting(browser_inf)

        if testwork == "worknode":
            driverInstance = webdriver.Chrome(
               service=Service_Chrome(executable_path="webdriver/chromedriver"),
                options=options
            )

        # chrome WebInstance (seleniumGrid)
        elif testwork == "selenium":
            driverInstance = webdriver.Remote(
                command_executor="http://localhost:4444/wd/hub",
                desired_capabilities=options.to_capabilities(),
            )

    # implicit_wait time : 10초 설정
    driverInstance.implicitly_wait(10)

    # WebDriver 인스턴스 설정
    yield driverInstance

    # WebDriver 인스턴스 종료
    time.sleep(1)
    driverInstance.quit()

def take_screenshot(id, timestamp):
    """step 에러일 시 스크린샷 작업 진행"""
    driverInstance.save_screenshot(
        "./screenshots/" + str(id) + "_" + timestamp + ".png"
    )

def pytest_bdd_step_error(
    request, feature, scenario, step, step_func, step_func_args, exception):
    """step Error일 시 name, step_function, exception의 정보 입력"""
    timestamp = datetime.now().strftime("%H-%M-%S")

    print("browser", str(step_func_args["driver"]).split(".")[2])
    print("step_name :", step.name)
    print("step_function :", step_func)
    print("exception :", exception)

    take_screenshot(step.name, timestamp)

# 공통 시나리오 정의 구간
@given(parsers.parse("swit 홈페이지로 접근한다."))
def navigate_to(driver):
    """swit 홈페이지 이동"""
    BASE_URL = "https://swit.io/"

    # response Code 확인
    if requests.get(BASE_URL).status_code == 200:
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            lambda x: x.execute_script("return document.readyState") == "complete"
        )

    else:
        assert False, "swit Page is not connected"