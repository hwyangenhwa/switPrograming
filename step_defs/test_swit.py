from pytest_bdd import scenarios, when, then, parsers

from pages.main import Mainpage
from pages.login import Loginpage
from pages.create import Createpage

scenarios("../features")

@when(parsers.parse("메인 페이지 확인"))
def click_checkbox(driver):
    Mainpage(driver).check_main()
    Mainpage(driver).check_mainHeaderMenu()
    Mainpage(driver).future_workOS()
    Mainpage(driver).check_employeeDanger()
    Mainpage(driver).check_workosFormula()
    Mainpage(driver).check_simply()
    Mainpage(driver).check_workSpace()
    Mainpage(driver).check_experience()

@when(parsers.parse("로그인 페이지 접근"))
def check_login(driver):
    Mainpage(driver).click_loginBtn()

@when(parsers.parse("Free/Standard 선택"))
def check_free_standard(driver):
    Loginpage(driver).select_FreeStandard()

@when(parsers.parse("아이디:{id}, 패스워드:{pw} 입력"))
def input_id_pw(driver, id, pw):
    Loginpage(driver).input_IDPW(id, pw)

@then(parsers.parse("로그인 하기:{login}"))
def click_idpw(driver, login):
    Loginpage(driver).click_Login(login)

@then(parsers.parse("워크스페이스 제목:{sub} 및 URL:{url} 입력"))
def input_titleUrl(driver, sub, url):
    Createpage(driver).create_Workspace()
    Createpage(driver).input_Workspace(sub)
    Createpage(driver).input_url(url)

@then(parsers.parse("워크스페이스 미 생성 확인"))
def check_createWorkspace(driver):
    Createpage(driver).check_Workspace()

@then(parsers.parse("워크스페이스 생성 확인:{sub}"))
def check_completeWorkspace(driver, sub):
    Createpage(driver).complete_Workspace()
    Createpage(driver).after_invite()
    Createpage(driver).after_dataPperistalsis()
    Createpage(driver).check_completeWorkspace(sub)

@then(parsers.parse("워크스페이스 삭제하기:{pw}"))
def delete_workspace(driver, pw):
    Createpage(driver).select_setting()
    Createpage(driver).click_delteOption(pw)