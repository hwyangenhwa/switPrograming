from pages.base import BasePage

class Createpage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def create_Workspace(self):
        """ 워크스페이스 생성 """

        # workspace 페이지 노출 확인
        self.getElement("swit-home > swit-workspace-tile", "css")

        # workspace create 선택
        self.clickElement("swit-workspace-tile > ul > li > a", "css")
        # workspace name
        self.getElement("#workspaceName", "css")
        # workspace url
        self.getElement("#workspaceUrl", "css")

    def input_Workspace(self, sub):
        """ 워크스페이스 제목 입력 """
        if sub == 'None':
            pass
        else:
            self.sendText(sub, "#workspaceName", "css")

    def input_url(self, url):
        """ 워크스페이스 URL 입력 """
        if url == 'None':
            pass
        else:
            self.sendText(url, "#workspaceUrl", "css")

    def check_Workspace(self):
        """ 워크스페이스 URL 입력 시 경고 메시지 확인 """
        errorMsg = self.getElement("div.error-text.ng-star-inserted", "css")

        assert errorMsg.text in '이미 사용 중 이름입니다.' or '영문자, 숫자, 하이픈(-)을 포함하여 4~20자 사이여야 하며, 하이픈(-)은 맨 앞이나 맨 뒤에 올 수 없습니다.' or\
               '워크스페이스 이름과 URL 주소는 언제든지 워크스페이스 설정 페이지에서 변경할 수 있습니다.'

        # 생성버튼 선택
        createBtn = self.getElement("form > div > button", "css")

        if createBtn.is_enabled() == False:
            pass

    def complete_Workspace(self):
        """ 생성완료 버튼 선택 """
        while True:
            try:
                if self.getElement("button.button.button--important.button--large", "css").is_enabled() == True:
                    self.clickElement("button.button.button--important.button--large", "css")
                    break
                else:
                    pass
            except:
                assert False, "Element is not chagned"

    def after_invite(self):
        """ 인원 초대하기 """
        # 나중에하기 선택
        self.clickElement("div.link-skip-wrap.ng-star-inserted > a", "css")

    def after_dataPperistalsis(self):
        """ 데이터 연동하기 """
        # 나중에하기 선택
        self.clickElement("swit-workspace-import-form > div > a", "css")

    def check_completeWorkspace(self, sub):
        """ 워크스페이스 생성 후 타이틀 확인 """
        # 타이틀 확인
        tilte = self.getElement("div.workspace-title > div > span.selected-title.selected-title--limit > span", "css")
        assert tilte.text == sub

    def select_setting(self):
        """ 환경설정 Btn 선택 """
        try:
            self.getElements("swit-workspace-tile > div > ul > li", "css")
            self.clickElement("a.workspace-card-btn.ng-star-inserted", "css")
            self.clickElement("li:nth-child(11) > a", "css")
        except:
            assert False, "Plz your workSpace"

    def click_delteOption(self, pw):
        """ 환경설정 Btn 선택 """
        self.clickElement("ul > li > button", "css")
        self.clickElement("#checkTest", "css")
        self.sendText(pw, "#password", "css")
        self.clickElement("button.button.button--unimportant", "css")

    def check_delteWorkspace(self):
        """ 워크스페이스 삭제 확인 """
        workspace = self.getElements("swit-workspace-tile > ul > li")
        if len(workspace) == 1:
            pass
        else:
            assert False, "Workspace is not delete"