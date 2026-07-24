from pages.frames_page import FramesPage


def test_frames(page):

    frames_page = FramesPage(page)

    frames_page.open()

    actual_text = frames_page.get_content()

    expected_text = "Your content goes here."

    assert actual_text == expected_text, (
        f"Frame content mismatch.\n"
        f"Expected : '{expected_text}'\n"
        f"Actual   : '{actual_text}'"
    )