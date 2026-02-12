import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL, TIMEOUT, SLOW_MO
from pages.language_page import LanguagePage
from pages.user_type_page import RolePage


@pytest.fixture(scope="session")
def playwright_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=SLOW_MO
        )
        yield browser
        browser.close()


@pytest.fixture
def page(playwright_browser):
    context = playwright_browser.new_context()
    page = context.new_page()
    page.set_default_timeout(TIMEOUT)
    page.goto(f"{BASE_URL}/user/language")
    yield page
    context.close()


@pytest.fixture
def language_selected(page):
    language = LanguagePage(page)
    language.select_english()
    language.click_proceed()
    return page


@pytest.fixture
def role_selected(language_selected):
    role = RolePage(language_selected)
    role.select_role("Teacher")   # 👈 UPDATED
    role.click_proceed()
    return language_selected


