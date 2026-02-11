class RolePage:
    def __init__(self, page):
        self.page = page

        self.proceed_btn = page.locator("button:has-text('Proceed')")

    def select_role(self, role_name):
        """
        role_name example:
        Teacher
        Special Educator
        CRE Programme
        Professionals
        Reviewer
        Others
        """
        self.page.locator(f"text={role_name}").click()

    def click_proceed(self):
        self.proceed_btn.click()
