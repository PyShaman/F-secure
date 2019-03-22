from selenium.webdriver.common.by import By
from features.lib.pages.base_page_objects import BasePage


class FsecureHomePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_directory = {
        "careers": (By.XPATH, '//*[@id="about"]/li[4]/a'),
        "detection": (By.CLASS_NAME, 'h5 m-y-0 m-l-h font-gray-9')
    }
    # self.careers = context.browser.find_element(By.XPATH, '//*[@id="about"]/li[4]/a')
    # self.detection = context.browser.find_element(By.CLASS_NAME, 'h5 m-y-0 m-l-h font-gray-9')
