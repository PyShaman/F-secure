from behave import *
from lib.pages import *
from selenium.webdriver.common.keys import Keys

from lib.pages.fsecure_careers_page import FsecureCareersPage


@given("User is on main page")
def step_impl(context):
    page_1 = FsecureHomePage(context)
    page_1.visit("https://www.f-secure.com/en/welcome")


@when('User navigates to "Careers" page')
def step_impl(context):
    page_1 = FsecureHomePage(context)
    page_1.careers().send_keys(Keys.ENTER)


@then('User is on "Careers" page')
def step_impl(context):
    page_2 = FsecureCareersPage(context)
    assert 'Careers | F-Secure' in page_2.page_title()


@when('User mouseover "Careers" top menu bar')
def step_impl(context):
    page_3 = FsecureCareersPage(context)



@when(u'User selects "Job openings" option')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User selects "Job openings" option')


@then(u'User is navigated to list of all jobs')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User is navigated to list of all jobs')


@when(u'User selects "Poznań" from drop down menu')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User selects "Poznań" from drop down menu')


@then(u'Job list is filtered to the one city')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Job list is filtered to the one city')


@when(u'User search for "Quality Engineer"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User search for "Quality Engineer"')


@when(u'Clicks on "View job"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Clicks on "View job"')


@then(u'new browser tab with "Quality Engineer" job details opens')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then new browser tab with "Quality Engineer" job details opens')
