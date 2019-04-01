import pytest
import time

from locators import CDPLocators
from page import LoginPage
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




        #wait = WebDriverWait(driver, 10)
        elem=WebDriverWait(driver,5).until(
            ec.visibility_of_element_located((By.XPATH,self.locators_login.LOC_ENVIRONMENT_QA)))
        elem.click()

        #driver.implicitly_wait(10)
        elem2=WebDriverWait(driver,30).until(ec.visibility_of_element_located((By.ID,"com.reviverauto.rplate:id/txtSignIn")))
        elem2.click()
        driver.find_element_by_id("com.reviverauto.rplate:id/txtSignIn").click()
        #driver.find_element_by_xpath(self.locators_login.LOC_SIGNIN).click()
        # elem2 = WebDriverWait(driver, 5).until(
        #     ec.visibility_of_element_located((By.XPATH,)))
        # elem2.click
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, self.locators_login.LOC_SIGNIN_BUTTON)))

        driver.find_element_by_xpath(self.locators_login.LOC_EMAIL_TEXTBOX).send_keys(testdata.username)
        driver.find_element_by_xpath(self.locators_login.LOC_PASSWORD_TEXTBOX).click().send_keys(testdata.password)
        driver.find_element_by_xpath(self.locators_login.LOC_EMAIL_TEXTBOX).click()

        asselem=driver.find_element_by_xpath(self.locators_login.LOC_HOMEPAGE_TOOLBAR)

        if(asselem.is_displayed()):
            print("HOMEPAGE IS DISPLAYED")
        else:
            print("TESTING FAILED")

        time.sleep(5)

        driver.quit()