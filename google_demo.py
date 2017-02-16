from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from hamcrest import assert_that
from hamcrest import is_
from splinter import Browser


@given('I Load "{url}"')
def open_url(context, url):
    context.browser = Browser('chrome')
    context.browser.visit("http://www.google.com/")

@when('Fill in the form with "{search_phrase}"')
def fill_the_search_form(context, search_phrase):
    # fill in 'test' in search filed
    context.browser.find_by_id("lst-ib").fill(search_phrase)
    # click 'search' button
    context.browser.find_by_name('btnG').click()

    # wait for the results page
    WebDriverWait(context.browser.driver, 120).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="hdtb-mitem hdtb-msel hdtb-imb"]')))

@then('I can see that page title starts with "{search_phrase}"')
def check_title(context, search_phrase):
   title = context.browser.title
   assert_that(search_phrase in title,
               is_(True),
               "No test in title")