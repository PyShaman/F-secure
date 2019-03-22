from selenium.webdriver.common.by import By
from features.lib.pages.base_page_objects import BasePage


class FsecurePositionsPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.browser)

    locator_dictionary = {
        "join": (By.CLASS_NAME, 'h2 m-b-0 text-headline'),
        "city": (By.XPATH, '//*[@id="job-city"]/option[4]'),
        "page": (By.XPATH, '//*[@id="p_p_id_56_INSTANCE_C7guYZjcAQo6_"]'
                           '/div/div/div/div[1]/section/div/div[2]'
                           '/div[1]/div[2]/ul/li[3]/a'),
        "position": (By.XPATH, '//*[@id="job-ads"]/article[7]/a')
    }
    # self.join = context.browser.find_element(By.CLASS_NAME, 'h2 m-b-0 text-headline')
    # self.city = context.browser.find_element(By.XPATH, '//*[@id="job-city"]/option[4]')
    # self.page = context.browser.find_element(By.XPATH, '//*[@id="p_p_id_56_INSTANCE_C7guYZjcAQo6_"]'
    #                                                    '/div/div/div/div[1]/section/div/div[2]'
    #                                                    '/div[1]/div[2]/ul/li[3]/a')
    # self.position = context.browser.find_element(By.XPATH, '//*[@id="job-ads"]/article[7]/a')
