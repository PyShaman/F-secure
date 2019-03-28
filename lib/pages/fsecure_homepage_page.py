from selenium.webdriver.common.by import By

from lib.pages.common_elements import CommonElements


class FsecureHomePage(CommonElements):

    def __init__(self, context):
        CommonElements.__init__(self, context.browser)

    locator_dictionary = {
        'careers': (By.XPATH, '//*[@id="about"]/li[4]/a')
    }

    def careers(self):
        return self.find_element(*self.locator_dictionary['careers'])
