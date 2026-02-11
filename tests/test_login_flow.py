from pages.login_page import LoginPage
from pages.password_page import PasswordPage
from utils.config import VALID_MOBILE, VALID_PASSWORD, INVALID_PASSWORD


def test_login_with_valid_password(role_selected):
    page = role_selected

    login = LoginPage(page)
    password = PasswordPage(page)

    # Step 1: Enter valid mobile number
    login.enter_mobile(VALID_MOBILE)
    login.click_proceed()

    # Step 2: Verify password page
    assert login.is_password_page_displayed(), "Password page not displayed"

    # Step 3: Enter valid password & proceed
    password.enter_password(VALID_PASSWORD)
    password.click_proceed()

    # Step 4: Verify successful login
    assert password.is_login_successful(), "Login failed with valid password"


def test_login_with_invalid_password(role_selected):
    page = role_selected

    login = LoginPage(page)
    password = PasswordPage(page)

    # Step 1: Enter valid mobile number
    login.enter_mobile(VALID_MOBILE)
    login.click_proceed()

    # Step 2: Enter invalid password
    password.enter_password(INVALID_PASSWORD)
    password.click_proceed()

    # Step 3: Verify error message
    assert password.is_invalid_password_displayed(), \
        "Invalid password message not shown"
