import time, logging

from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
    ElementNotSelectableException,
)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # element의 존재유무 확인
    def waitForElement(self, locatorValue, locatorType) -> "web Element":

        # PageLoad, locatorTyper, elemet variable
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(
            self.driver,
            15,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotSelectableException,
                ElementNotVisibleException,
            ],
        )

        try:
            if locatorType == "id":
                # element = wait.until(lambda x: x.find_element_by_id(locatorValue))
                element = wait.until(
                    EC.presence_of_element_located((By.ID, locatorValue))
                )
                self._highlight(element)
                return element

            elif locatorType == "class":
                # element = wait.until(lambda x: x.find_element_by_class_name(locatorValue))
                element = wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, locatorValue))
                )
                self._highlight(element)
                return element

            elif locatorType == "xpath":
                # element = wait.until(lambda x: x.find_element_by_xpath(locatorValue))
                element = wait.until(
                    EC.presence_of_element_located((By.XPATH, locatorValue))
                )
                self._highlight(element)
                return element

            elif locatorType == "css":
                # element = wait.until(lambda x: x.find_element_by_css_selector(locatorValue))
                element = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, locatorValue))
                )
                self._highlight(element)
                return element

        except Exception as ex:
            print(ex)
            assert False, locatorType + " is not found : " + locatorValue

    # element의 복수 존재유무 확인
    def waitForElements(self, locatorValue, locatorType) -> "web Elements":

        # PageLoad, locatorTyper, elemet variable
        locatorType = locatorType.lower()
        wait = WebDriverWait(
            self.driver,
            15,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotSelectableException,
                ElementNotVisibleException,
            ],
        )

        try:
            if locatorType == "id":
                elements = wait.until(
                    lambda x: x.find_elements(by=By.ID, value=locatorValue)
                )
                # self._highlight(elements)
                return elements

            elif locatorType == "class":
                elements = wait.until(
                    lambda x: x.find_elements(by=By.CLASS_NAME, value=locatorValue)
                )
                # self._highlight(elements)
                return elements

            elif locatorType == "xpath":
                elements = wait.until(
                    lambda x: x.find_elements(by=By.XPATH, value=locatorValue)
                )
                # self._highlight(elements)
                return elements

            elif locatorType == "css":
                elements = wait.until(
                    lambda x: x.find_elements(by=By.CSS_SELECTOR, value=locatorValue)
                )
                # self._highlight(elements)
                return elements

        except Exception:
            assert False, locatorType + " is not found : " + locatorValue

    # element의 단수의 요소 선택
    def getElement(self, locatorValue, locatorType="id") -> "web Element":
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
        except:
            element = None

        return element

    # element의 복수의 요소 선택
    def getElements(self, locatorValue, locatorType="id") -> "web Elements":
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElements(locatorValue, locatorType)
        except:
            print("Elements is not None")

        return element

    # element의 요소에 Click
    def clickElement(self, locatorValue, locatorType="id") -> None:
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()

        except Exception as ex:
            assert False, ex

    # element의 요소에 Text 입력
    def sendText(self, text, locatorValue, locatorType="id") -> None:
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
        except:
            logging.warning("Send Text Error")

    # element의 select 요소 선택
    def select(self, selectByValue, selectBy, locatorValue, locatorType="id") -> None:
        element = self.waitForElement(locatorValue, locatorType)
        select = Select(element)

        try:
            if selectBy == "value":
                select.select_by_value(selectByValue)
            elif selectBy == "index":
                select.select_by_index(selectByValue)
            elif selectBy == "text":
                select.select_by_visible_text(selectByValue)
        except:
            assert False, "Select element Error"

    # element의 선택된 요소에 노출/ 미노출
    def isDisplayed(self, locatorValue, locatorType="id") -> "True False":
        element = None
        locatorType = locatorType.lower()
        element = self.waitForElement(locatorValue, locatorType)
        time.sleep(3)

        if element.is_displayed() == True:
            return True
        else:
            return False

        # element의 select 요소 선택

    # alert 창 여부 확인
    def checkalert(self) -> "alert element":
        try:
            alert = self.driver.switch_to.alert
            return alert

        except Exception as ex:
            print(ex)

    # element의 선택된 요소에 대해서 highlight
    def _highlight(self, element):
        # element 선택
        driver = element._parent
        original_style = element.get_attribute("style")

        # highlight style 적용 (background : White, boarderline : Red)
        def apply_style(s):
            driver.execute_script(
                "arguments[0].setAttribute('style', arguments[1]);", element, s
            )

        apply_style("border: 2px solid red;")
        time.sleep(0.5)
        apply_style(original_style)
