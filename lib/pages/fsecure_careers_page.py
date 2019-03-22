from selenium.webdriver.common.by import By
from features.lib.pages.base_page_objects import BasePage


class FsecureCareersPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "title": (By.LINK_TEXT, 'What do we stand for – want to be part of us?'),
        "positions": (By.CLASS_NAME, 'btn btn-secondary btn-inverse m-t-1')
    }
    # self.title = context.browser.find_element(By.LINK_TEXT, 'What do we stand for – want to be part of us?')
    # self.positions = context.browser.find_element(By.CLASS_NAME, 'btn btn-secondary btn-inverse m-t-1')
