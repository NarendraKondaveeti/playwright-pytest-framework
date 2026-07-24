from pages.checkboxes_page import CheckboxesPage


def test_checkboxes(page):

    checkboxes_page = CheckboxesPage(page)

    checkboxes_page.open()

    # Checkbox 1
    checkboxes_page.check_checkbox1()

    assert checkboxes_page.is_checkbox1_checked(), (
        "Checkbox 1 should be checked."
    )

    # Checkbox 2
    checkboxes_page.uncheck_checkbox2()

    assert not checkboxes_page.is_checkbox2_checked(), (
        "Checkbox 2 should be unchecked."
    )