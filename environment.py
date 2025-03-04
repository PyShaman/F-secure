import logging
import os
import shutil
import time

from sys import platform
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from lib.drivers.os_platforms import os_platforms


def before_all(context):
    # Create logger
    context.logger = logging.getLogger('seleniumframework_tests')
    handler = logging.FileHandler('./seleniumframework_tests.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    context.logger.addHandler(handler)
    context.logger.setLevel(logging.DEBUG)


def before_scenario(context, scenario):
    print("User data:", context.config.userdata)
    if 'browser' in context.config.userdata.keys():
        if context.config.userdata['browser'] is None:
            browser = 'chrome'
        else:
            browser = context.config.userdata['browser']
    else:
        browser = 'chrome'
    if browser == 'chrome':
        context.browser = webdriver.Chrome(executable_path=(os.getcwd() + '/' + os_platforms(browser)))
    elif browser == 'firefox':
        if platform == 'linux' or platform == 'linux2':
            binary = FirefoxBinary("/usr/bin/firefox")
        if platform == 'win32':
            binary = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
        # this does not work, I am not sure why... for further investigation
        context.browser = webdriver.Firefox(firefox_binary=binary)
        # context.browser = webdriver.Firefox(executable_path=(os.getcwd() + '/' + os_platforms(browser) + '-headless'))
    else:
        print("Browser you entered:", browser, "is invalid value")

    context.browser.maximize_window()


def after_scenario(context, scenario):
    print("scenario status" + str(scenario.status))
    if str(scenario.status) == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")
    context.browser.quit()


def after_all(context):
    print("User data:", context.config.userdata)
    # behave -D ARCHIVE=Yes
    if 'ARCHIVE' in context.config.userdata.keys():
        if os.path.exists("failed_scenarios_screenshots"):
            os.rmdir("failed_scenarios_screenshots")
            os.makedirs("failed_scenarios_screenshots")
        if context.config.userdata['ARCHIVE'] == "Yes":
            shutil.make_archive(
                time.strftime("%d_%m_%Y"),
                'zip',
                "failed_scenarios_screenshots")
