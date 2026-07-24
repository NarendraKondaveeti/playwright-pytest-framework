from pages.multiple_windows_page import MultipleWindowsPage


def test_multiple_windows(page):

    multiple_windows_page = MultipleWindowsPage(page)

    multiple_windows_page.open()

    child_page = multiple_windows_page.open_child_window()

    actual_heading = (
        child_page.locator("h3")
        .inner_text()
        .strip()
    )

    expected_heading = "New Window"

    assert actual_heading == expected_heading, (
        f"New Window validation failed.\n"
        f"Expected : '{expected_heading}'\n"
        f"Actual   : '{actual_heading}'"
    )

    child_page.close()