from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Mobile number input
        self.mobile_input = page.locator(
            "input[placeholder='Enter Username or Mobile number.']"
        )

        # Proceed button
        self.proceed_btn = page.locator("button:has-text('Proceed')")

        # Error message (adjust text if exact message available)
        self.error_msg = page.locator("text=Invalid")

        # Password page identifier
        self.password_heading = page.locator(
            "text=Enter your current password"
        )

    def enter_mobile(self, mobile: str):
        self.mobile_input.fill(mobile)

    def click_proceed(self):
        self.proceed_btn.click()

    def is_password_page_displayed(self) -> bool:
        self.password_heading.wait_for(state="visible")
        return self.password_heading.is_visible()

    def is_mobile_error_displayed(self) -> bool:
        return self.error_msg.is_visible()
