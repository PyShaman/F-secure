import traceback

from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class CommonElements(object):

    def __init__(self, browser):
        self.browser = browser
        self.timeout = 30

    def find_element(self, *loc):
        """
        :param loc: gives specific element from locator_directory
        :return: specific webdriver element
        """
        return self.browser.find_element(*loc)

    def visit(self, url):
        """
        :param url: url of website
        :return: forces webdriver to open specific url
        """
        self.browser.get(url)

    def switch_new_tab(self, i):
        """
        Function switches between tabs of browser
        :param i: index of tab to be switched (index starts from 0)
        :return: performs action of switching to specific tab
        """
        self.browser.switch_to_window(self.browser.window_handles[i])

    @staticmethod
    def method_missing(item):
        print("There is no %s element.") % item

    def __getattr__(self, item):
        """
        Function consolidates webdriver waits
        :param item: provided by locator dictionaries of elements present on the specific page
        :return: element from dictionary
        """
        try:
            if item in self.locator_dictionary.keys():
                try:
                    WebDriverWait(self.browser, self.timeout).until(
                        ec.presence_of_element_located(self.locator_dictionary[item])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    WebDriverWait(self.browser, self.timeout).until(
                        ec.visibility_of_element_located(self.locator_dictionary[item])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    WebDriverWait(self.browser, self.timeout).until(
                        ec.element_to_be_clickable(self.locator_directory[item])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                return self.find_element(*self.locator_dictionary[item])

        except AttributeError:
            super(CommonElements, self).__getattr__("method_missing")(item)
