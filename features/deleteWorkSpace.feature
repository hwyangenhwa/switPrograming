Feature: Checkboxes Page

  Background: swit 페이지 접근
    Given swit 홈페이지로 접근한다.

@pytest.mark.order(order=8)
    @deleteworkspace
  Scenario Outline: swit 워크스페이스 삭제
    When 로그인 페이지 접근
    And Free/Standard 선택
    And 아이디:<id>, 패스워드:<pw> 입력
    Then 로그인 하기:<login>
    Then 워크스페이스 삭제하기:<pw>

    Examples:
      | id                | pw        | login  |
      | - | - | normal |
