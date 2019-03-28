from selenium.webdriver.common.by import By
from lib.pages.common_elements import CommonElements


class FsecureCareersPage(CommonElements):

    def __init__(self, context):
        CommonElements.__init__(self, context.browser)

    locator_dictionary = {
        "page_title": 'Careers | F-Secure',
        "job_openings": (By.XPATH, '//*[@id="p_p_id_56_INSTANCE_gJitE6b6gf8s_"]/div/div/div/div[1]/section/div/div['
                                   '2]/div[2]/div/a')
    }

    def page_title(self):
        return self.locator_dictionary['page_title']

    def job_openings(self):
        return self.browser.find_element(*self.locator_dictionary['job_openings'])
