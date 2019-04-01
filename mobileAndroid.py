class mobileAndroidSettings(object):

    env="QA"
    desired_caps = {
        "platformName":"Android",
        "deviceName":"emulator-5554",
        "appPackage":"com.reviverauto.rplate",
        "appActivity":"com.reviverauto.rplate.SplashActivity",
        "noReset":"true"
    }
    serverAppium="http://127.0.0.1:4723/wd/hub"





