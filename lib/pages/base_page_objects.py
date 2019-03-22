from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import traceback


class BasePage(object):

    def __init__(self, browser):
        self.browser = browser
        self.timeout = 30

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def visit(self, url):
        self.browser.get(url)

    @staticmethod
    def method_missing(item):
        print("There is no %s element.") % item

    def __getattr__(self, item):
        try:
            if item in self.locator_dictionary.keys():
                try:
                    WebDriverWait(self.browser, self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[item])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    WebDriverWait(self.browser, self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[item])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                return self.find_element(*self.locator_dictionary[item])

        except AttributeError:
            super(BasePage, self).__getattr__("method_missing")(item)
