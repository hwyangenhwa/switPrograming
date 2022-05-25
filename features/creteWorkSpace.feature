Feature: Checkboxes Page

  Background: swit 페이지 접근
    Given swit 홈페이지로 접근한다.

  @pytest.mark.order(order=6)
    @wrongcreateworkspace
    Scenario Outline: swit 잘못된 제목 및 URL 입력 시 워크스페이스 미 생성 유무 확인
      When 로그인 페이지 접근
      And Free/Standard 선택
      And 아이디:<id>, 패스워드:<pw> 입력
      Then 로그인 하기:<login>
      Then 워크스페이스 제목:<sub> 및 URL:<url> 입력
      Then 워크스페이스 미 생성 확인

      Examples:
      | id                | pw        | login  | sub  | url  |
      | junkune@gmail.com | sky!20638 | normal | test | a    |
      | junkune@gmail.com | sky!20638 | normal | test | test |

  @pytest.mark.order(order=7)
    @createworkspace
  Scenario Outline: swit 정상적인 워크스페이스 생성
    When 로그인 페이지 접근
    And Free/Standard 선택
    And 아이디:<id>, 패스워드:<pw> 입력
    Then 로그인 하기:<login>
    Then 워크스페이스 제목:<sub> 및 URL:<url> 입력
    Then 워크스페이스 생성 확인:<sub>

    Examples:
      | id                | pw        | login  | sub      | url      |
      | junkune@gmail.com | sky!20638 | normal | testyang | testyang |