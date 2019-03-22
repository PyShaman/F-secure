from behave import *
from features.lib.pages import *


@given("User is on main page")
def step_impl(context):
    page = FsecureHomePage(context)
    page.visit("https://www.f-secure.com/en/welcome")


@when("User navigates to 'Careers' page")
def step_impl(context):
    page = FsecureHomePage(context)
    page.
