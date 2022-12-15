from behave import *
from time import sleep


@given(u'I am on the homepage')
def go_home_page(context):
    context.home_page.go_to_home_page()


@when(u'I keep the mouse cursor on the carousel images')
def hover_carousel(context):
    context.home_page.hover_mouse_on_carousel_images()


@then(u'The carousel image stop at the current images')
def check_carousel_stop(context):
    image_name = context.home_page.check_carousel_current_image()
    sleep(6)
    assert image_name == context.home_page.check_carousel_current_image()


@when(u'I don\'t keep the mouse cursor on the carousel images')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I don\'t keep the mouse cursor on the carousel images')


@then(u'The carousel image move automatically')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The carousel image move automatically')


@when(u'I press the right arrow from the carousel images')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I press the right arrow from the carousel images')


@then(u'The carousel image change to next image')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The carousel image change to next image')


@when(u'I press the left arrow from the carousel images')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I press the left arrow from the carousel images')


@then(u'The carousel image change to previous image')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The carousel image change to previous image')


@when(u'I press first slide button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I press first slide button')


@then(u'The carousel image is Samsung1.jpg')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The carousel image is Samsung1.jpg')


@when(u'I press second slide button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I press second slide button')


@then(u'The carousel image is nexus1.jpg')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The carousel image is nexus1.jpg')


@when(u'I press third slide button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I press third slide button')


@then(u'The carousel image is iphone1.jpg')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The carousel image is iphone1.jpg')
