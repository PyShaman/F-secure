from selenium.webdriver.common.by import By
from lib.pages.base_page_objects import BasePage


class FsecureCareersPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "title": (By.XPATH, '//*[@id="p_p_id_56_INSTANCE_QfaI9ELwQzF3_"]/div/div/div/div[1]/section/div/div/div/div/h2'),
        "positions": (By.CLASS_NAME, 'btn btn-secondary btn-inverse m-t-1')
    }

    def title(self):
        return self.browser.find_element(*self.locator_dictionary['title'])

    def positions(self):
        return self.browser.find_element(*self.locator_dictionary['positions'])
