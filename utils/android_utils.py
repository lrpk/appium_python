from appium.webdriver.common.mobileby import MobileBy


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '8.1',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': '2e37c6cd7d85',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }


#  required parameters
login_btn_locator = (MobileBy.XPATH, "//android.widget.TextView"
                                     "[@resource-id='com.ajaxsystems:id/text' and @text='Log In']")
email_field_locator = (MobileBy.XPATH, '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]')
pas_field_locator = (MobileBy.XPATH, '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]')
banner_locator = (MobileBy.ID, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/snackbar_text"]')
