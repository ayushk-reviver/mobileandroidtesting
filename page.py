import appsettings as appsettings
from appium import webdriver
from mobileAndroid import mobileAndroidSettings

class LoginPage(object):
    appsettings = mobileAndroidSettings()


    def launchapp(self):
        driver=webdriver.Remote(self.appsettings.serverAppium,self.appsettings.desired_caps)
        return driver
