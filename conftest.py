import pytest

from playwright.sync_api import Page


@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height':1080, 'width': 1920})
    yield page
