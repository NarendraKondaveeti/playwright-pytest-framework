from pages.add_remove_page import AddRemovePage


def test_add_element(page):

    add_remove = AddRemovePage(page)

    add_remove.open()

    add_remove.click_add_element()

    assert add_remove.is_delete_button_visible()