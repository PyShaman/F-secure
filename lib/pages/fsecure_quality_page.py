from selenium.webdriver.common.by import By
from lib.pages.base_page_objects import BasePage


class FsecureQualityEngineerPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "title": (By.CLASS_NAME, 'job-title'),
        "button": (By.CLASS_NAME, 'btn btn-huge btn-success btn-embossed btn-block mbl')
    }
    # self.title = context.browser.find_element(By.CLASS_NAME, 'job-title')
    # self.button = context.browser.find_element(By.CLASS_NAME, 'btn btn-huge btn-success btn-embossed btn-block mbl')
