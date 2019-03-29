from sys import platform


def os_platforms(browser):
    """
    Function checks the platform that framework is running (linux or windows)
    and returns specific driver for chrome and firefox
    """
    if platform == 'linux' or platform == 'linux2' and browser == 'chrome':
        chrome_driver = "chromedriver"
        return chrome_driver
    if platform == 'linux' or platform == 'linux2' and browser == 'firefox':
        firefox_driver = "geckodriver"
        return firefox_driver
    if platform == 'win32' and browser == 'chrome':
        chrome_driver = "chromedriver.exe"
        return chrome_driver
    if platform == 'win32' and browser == 'firefox':
        firefox_driver = "geckodriver.exe"
        return firefox_driver
    else:
        print("Driver for " + platform + " not supported.")
