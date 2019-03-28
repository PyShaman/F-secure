from sys import platform


def environments(browser):
    if platform == 'linux' or platform == 'linux2' and browser == 'chrome':
        chrome_driver = "chromedriver"
        return chrome_driver
    if platform == 'linux' or platform == 'linux2' and browser == 'firefox':
        firefox_driver = "geckodriver"
        return firefox_driver
    if platform == 'linux' or platform == 'linux2' and browser == 'opera':
        opera_driver = "opera"
        return opera_driver
    if platform == 'win32' and browser == 'chrome':
        chrome_driver = "chromedriver.exe"
        return chrome_driver
    if platform == 'win32' and browser == 'firefox':
        firefox_driver = "geckodriver.exe"
        return firefox_driver
    if platform == 'win32' and browser == 'opera':
        opera_driver = "opera"
        return opera_driver
    else:
        print("Driver for " + platform + " not supported.")
