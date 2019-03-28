from selenium.webdriver.common.by import By
from lib.pages.common_elements import CommonElements


class FsecureQualityEngineerPage(CommonElements):

    def __init__(self, context):
        CommonElements.__init__(self, context.browser)

    locator_dictionary = {
        "job_title": (By.CLASS_NAME, 'job-title'),
        "job_announcement": (By.XPATH, '//*[@id="canvas-ad-container"]/div[2]/div/div[2]/div/p[1]/strong')
    }

    def title(self):
        return self.browser.find_element(*self.locator_dictionary['job_title'])

    def announcement(self):
        return self.browser.find_element(*self.locator_dictionary['job_announcement'])
