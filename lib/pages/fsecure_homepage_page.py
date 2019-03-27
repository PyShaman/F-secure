from selenium.webdriver.common.by import By

from lib.pages.base_page_objects import BasePage


class FsecureHomePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        'careers': (By.XPATH, '//*[@id="about"]/li[4]/a')
    }

    def careers(self):
        return self.find_element(*self.locator_dictionary['careers'])
