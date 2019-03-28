from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from lib.pages.common_elements import CommonElements


class FsecureJobOpeningsPage(CommonElements):

    def __init__(self, context):
        CommonElements.__init__(self, context.browser)

    locator_dictionary = {
        "page_title": 'Job openings | F-Secure',
        "job_city": (By.ID, 'job-city'),
        "page_change_right": (By.XPATH, '//*[@id="p_p_id_56_INSTANCE_C7guYZjcAQo6_"]/div/div/div/div['
                                        '1]/section/div/div[2]/div[1]/div[2]/ul/li[5]/a'),
        "QA": (By.XPATH, '//*[@id="job-ads"]/article[9]/h2'),
        "view_job": (By.XPATH, '//*[@id="job-ads"]/article[9]/a')
    }

    def page_title(self):
        return self.locator_dictionary['page_title']

    def job_city(self):
        return self.browser.find_element(*self.locator_dictionary['job_city'])

    def select_city(self):
        return Select(self.browser.find_element(*self.locator_dictionary['job_city'])).select_by_value('Poznań')

    def page_change_right(self):
        return self.browser.find_element(*self.locator_dictionary['page_change_right'])

    def qa_search(self):
        return self.browser.find_element(*self.locator_dictionary['QA'])

    def view_job(self):
        return self.browser.find_element(*self.locator_dictionary['view_job'])
