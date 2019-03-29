from selenium.webdriver.common.by import By
from lib.pages.common_elements import CommonElements


class FsecureApplicationPage(CommonElements):

    def __init__(self, context):
        CommonElements.__init__(self, context.browser)

    locator_dictionary = {
        "title": (By.PARTIAL_LINK_TEXT, 'want to be part of us?'),
        "positions": (By.CLASS_NAME, 'btn btn-secondary btn-inverse m-t-1')
    }
