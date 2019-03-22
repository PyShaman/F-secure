from selenium.webdriver.common.by import By
from features.lib.pages.base_page_objects import BasePage


class FsecureApplicationPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "title": (By.CLASS_NAME, 'lead'),
        "name": (By.ID, 'id_first_name'),
        "lastname": (By.ID, 'id_last_name'),
        "email": (By.ID, 'id_email')
    }
    # self.title = context.browser.find_element(By.CLASS_NAME, 'lead')
    # self.name = context.browser.find_element(By.ID, 'id_first_name')
    # self.lastname = context.browser.find_element(By.ID, 'id_last_name')
    # self.email = context.browser.find_element(By.ID, 'id_email')
