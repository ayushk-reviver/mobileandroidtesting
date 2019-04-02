import pytest
import time

from pyrobot import Robot,Keys
from locators import CDPLocators
from page import LoginPage
from appium.webdriver.common.touch_action import TouchAction
from login_TestData import logintestdata as testdata
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestLogin(object):

    locators_login = CDPLocators()
    pageFn = LoginPage()


    @pytest.mark.mobile1
    def test_app_launch(self):
        driver = self.pageFn.launchapp()
        actions = TouchAction(driver)
        robot = Robot()

        #wait = WebDriverWait(driver, 10)
        elem=WebDriverWait(driver,30).until(
            ec.visibility_of_element_located((By.XPATH,self.locators_login.LOC_ENVIRONMENT_QA)))
        elem.click()
        time.sleep(5)
        actions.tap(None,200,1670,1).perform()
        WebDriverWait(driver, 30).until(
            ec.visibility_of_element_located((By.XPATH, self.locators_login.LOC_SIGNIN_BUTTON)))

        driver.find_element_by_xpath(self.locators_login.LOC_EMAIL_TEXTBOX).send_keys(testdata.username)
        robot.press_and_release(Keys.enter)
        driver.find_element_by_xpath(self.locators_login.LOC_PASSWORD_TEXTBOX).send_keys(testdata.password)
        driver.find_element_by_xpath(self.locators_login.LOC_SIGNIN_BUTTON).click()
        time.sleep(10)


        actions.tap(None,30,150,1).perform()
        time.sleep(2)
        actions.tap(None,1000,1050,1).perform()


        asselem = driver.find_element_by_xpath(self.locators_login.LOC_HOMEPAGE_TOOLBAR).is_displayed()

        assert asselem==True

        # time.sleep(5)
        driver.quit()