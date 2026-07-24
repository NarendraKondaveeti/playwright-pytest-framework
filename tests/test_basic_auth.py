from pages.basic_auth_page import BasicAuthPage
from utilities.json_reader import JsonReader


test_data = JsonReader.read_json("testdata/basic_auth.json")


def test_basic_auth(page):

    basic_auth_page = BasicAuthPage(page)

    basic_auth_page.open(
        test_data["username"],
        test_data["password"]
    )

    actual_text = basic_auth_page.get_success_message()

    expected_text = (
    "Congratulations! You must have the proper credentials."
    )
    assert actual_text == expected_text, (
        f"Basic Authentication Failed.\n"
        f"Expected : '{expected_text}'\n"
        f"Actual   : '{actual_text}'"

)