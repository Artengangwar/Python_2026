from playwright.sync_api import Page


class LanguagePage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.english_language = page.locator("text=English")
        self.proceed_button = page.locator("button:has-text('Proceed')")

    def select_english(self):
        self.english_language.click()

    def click_proceed(self):
        self.proceed_button.click()

    def is_english_selected(self):
        # usually selected language gets active/selected class
        return self.english_language.get_attribute("class") is not None
