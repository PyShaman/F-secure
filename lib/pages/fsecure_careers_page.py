from selenium.webdriver.common.by import By
from lib.pages.base_page_objects import BasePage


class FsecureCareersPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "page_title": 'Careers | F-Secure',
        "careers_menu": (By.XPATH, '//*[@id="p4-section-subnav"]/li[3]'),
        "job_openings": (By.XPATH, '//*[@id="p4-section-subnav"]/li[3]/ul/li[2]/a')
    }

    def page_title(self):
        return self.locator_dictionary['page_title']

    def careers_menu(self):
        return self.browser.find_element(*self.locator_dictionary['positions'])

    def job_openings(self):
        return self.browser.find_element(*self.locator_dictionary['job_openings'])
