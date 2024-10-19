from playwright.sync_api import Page
from pages.like_button_page import LikeButtonPage


def test_like_a_button_exists(page: Page):
    like_button_page = LikeButtonPage(page)
    like_button_page.open_page()
    like_button_page.check_button_visible()

def test_like_a_button_click(page: Page):
    like_button_page = LikeButtonPage(page)
    like_button_page.open_page()
    like_button_page.click_the_button()
    like_button_page.check_result_text_is_('Submitted')
