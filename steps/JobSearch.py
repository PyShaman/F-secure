import time

from behave import *
from selenium.webdriver.common.keys import Keys

from lib.pages import *
from lib.pages.common_elements import CommonElements as Ce
from lib.pages.fsecure_careers_page import FsecureCareersPage
from lib.pages.fsecure_job_openings_page import FsecureJobOpeningsPage
from lib.pages.fsecure_quality_page import FsecureQualityEngineerPage


@given("User is on main page")
def step_impl(context):
    page = FsecureHomePage(context)
    page.visit("https://www.f-secure.com/en/welcome")


@when('User navigates to "Careers" page')
def step_impl(context):
    page = FsecureHomePage(context)
    page.careers().send_keys(Keys.ENTER)


@then('User is on "Careers" page')
def step_impl(context):
    page = FsecureCareersPage(context)
    assert 'Careers | F-Secure' in page.page_title()


@when('User clicks on "See our open positions" button')
def step_impl(context):
    page = FsecureCareersPage(context)
    page.job_openings().send_keys(Keys.ENTER)


@then('User is navigated to list of all jobs')
def step_impl(context):
    page = FsecureJobOpeningsPage(context)
    assert 'Job openings | F-Secure' in page.page_title()


@when('User selects "Poznań" from drop down menu')
def step_impl(context):
    page = FsecureJobOpeningsPage(context)
    page.job_city().click()
    page.select_city()


@when('User search for "Quality Engineer"')
def step_impl(context):
    page = FsecureJobOpeningsPage(context)
    page.page_change_right().send_keys(Keys.ENTER + Keys.HOME)
    time.sleep(1)
    assert 'Quality Engineer' in page.qa_search().text


@when(u'User clicks on "View job"')
def step_impl(context):
    page = FsecureJobOpeningsPage(context)
    page.view_job().click()
    # sleep because new tab will be opened
    time.sleep(5)


@then('New browser tab with "Quality Engineer" job details opens')
def step_impl(context):
    Ce.switch_new_tab(context, 1)
    page = FsecureQualityEngineerPage(context)
    assert "Quality Engineer" in page.title().text
    assert "Quality Engineer wanted to work with our key corporate security products!" in page.announcement().text
