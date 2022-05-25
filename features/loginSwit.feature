
Feature: Checkboxes Page

  Background: swit 페이지 접근
    Given swit 홈페이지로 접근한다.

  @pytest.mark.order(order=1)
    @main
    Scenario: swit 페이지 관련해서 동작 유무를 확인
      When 메인 페이지 확인

  @pytest.mark.order(order=2)
    @login @adnormallogin
    Scenario Outline: swit 로그인 관련해서 비 정상동작 유무를 확인
      When 로그인 페이지 접근
      And Free/Standard 선택
      And 아이디:<id>, 패스워드:<pw> 입력
      Then 로그인 하기:<login>

    Examples:
      | id              | pw         | login |
      | jukune          | None       | ad    |
      | None            | sky!20638  | ad    |
      | None            | None       | ad    |
      | junkune@        | sky!20368  | ad    |
      | junku@gmail.com | sky!!20368 | ad    |

  @pytest.mark.order(order=3)
    @login @normallogin
    Scenario Outline: swit 로그인 관련해서 정상동작 유무를 확인
      When 로그인 페이지 접근
      And Free/Standard 선택
      And 아이디:<id>, 패스워드:<pw> 입력
      Then 로그인 하기:<login>

      Examples:
      | id                | pw        | login  |
      | junkune@gmail.com | sky!20638 | normal |