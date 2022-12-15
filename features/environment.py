from browser import Browser
from pages.home_page import HomePage


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage(context.browser.driver)


def after_all(context):
    context.browser.close()
