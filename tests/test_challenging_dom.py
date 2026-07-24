from pages.challenging_dom_page import ChallengingDomPage


def test_challenging_dom(page):

    challenging_page = ChallengingDomPage(page)

    challenging_page.open()

    challenging_page.click_blue_button()

    challenging_page.click_red_button()

    challenging_page.click_green_button()

    actual_rows = challenging_page.get_total_rows()

    expected_rows = 10

    assert actual_rows == expected_rows, (
        f"Table row count mismatch.\n"
        f"Expected : {expected_rows}\n"
        f"Actual   : {actual_rows}"
    )