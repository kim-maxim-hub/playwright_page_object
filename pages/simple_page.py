from playwright.sync_api import expect
from pages.base_page import BasePage


BUTTON = '#submit-id-submit'
RESULT = '#result-text'


class SimplePage(BasePage):
    
    url = 'https://www.qa-practice.com/elements/button/simple'

    def check_button_exists(self):
        button = self.page.locator(BUTTON)
        expect(button).to_be_visible()

    def click_button(self):
        button = self.page.locator(BUTTON)
        button.click()

    def check_result_text_is_(self, text):
        result = self.page.locator(RESULT)
        expect(result).to_have_text(text)
