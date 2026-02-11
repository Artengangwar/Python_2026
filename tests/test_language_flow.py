from pages.language_page import LanguagePage


def test_language_selection_and_proceed(page):
    language = LanguagePage(page)

    # Step 1: English language select
    language.select_english()
    assert language.is_english_selected(), "English language not selected"

    # Step 2: Proceed button click
    language.click_proceed()

    # Step 3: Verify navigation to role page
    assert "role" in page.url or "usertype" in page.url
