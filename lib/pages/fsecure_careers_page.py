from selenium.webdriver.common.by import By
from lib.pages.base_page_objects import BasePage


class FsecureCareersPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "page_title": 'Careers | F-Secure',
        "positions": (By.CLASS_NAME, 'btn btn-secondary btn-inverse m-t-1')
    }

    def page_title(self):
        return self.locator_dictionary['page_title']

    def positions(self):
        return self.browser.find_element(*self.locator_dictionary['positions'])
