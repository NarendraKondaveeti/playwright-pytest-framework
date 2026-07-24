from pages.file_upload_page import FileUploadPage


def test_file_upload(page):

    file_upload_page = FileUploadPage(page)

    file_upload_page.open()

    file_upload_page.upload_file("testdata/sample.txt")

    file_upload_page.click_upload()

    actual_file_name = file_upload_page.get_uploaded_file_name()

    expected_file_name = "sample.txt"

    assert actual_file_name == expected_file_name, (
        f"File Upload Failed.\n"
        f"Expected : '{expected_file_name}'\n"
        f"Actual   : '{actual_file_name}'"
    )