from pages.user_type_page import RolePage


def test_select_teacher_role(language_selected):
    role = RolePage(language_selected)

    # Step 1: Select Teacher role
    role.select_teacher()
    assert role.is_role_selected(), "Teacher role not selected"

    # Step 2: Click Proceed
    role.click_proceed()

    # Step 3: Verify navigation to login page
    assert "login" in language_selected.url
