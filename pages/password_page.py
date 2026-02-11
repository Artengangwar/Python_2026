from playwright.sync_api import Page


class PasswordPage:
    def __init__(self, page: Page):
        self.page = page

        # Password input
        self.password_input = page.locator(
            "input[placeholder='Enter Password']"
        )

        # Proceed button
        self.proceed_btn = page.locator("button:has-text('Proceed')")

        # Invalid password error message
        self.invalid_password_msg = page.locator(
            "text=Invalid password"
        )

        # Successful login identifier
        self.dashboard_identifier = page.locator(
            "text=Dashboard"
        )

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_proceed(self):
        self.proceed_btn.click()

    def is_login_successful(self) -> bool:
        self.dashboard_identifier.wait_for(state="visible")
        return self.dashboard_identifier.is_visible()

    def is_invalid_password_displayed(self) -> bool:
        return self.invalid_password_msg.is_visible()
