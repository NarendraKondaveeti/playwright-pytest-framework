from pathlib import Path
from config.settings import Settings
from playwright.sync_api import Page


class FileUploadPage:

    def __init__(self, page: Page):
        self.page = page

        self.file_input = page.locator("#file-upload")
        self.upload_button = page.locator("#file-submit")
        self.uploaded_file = page.locator("#uploaded-files")

    def open(self):
        self.page.goto(f"{Settings.BASE_URL}/upload")

    def upload_file(self, relative_file_path):

        project_root = Path(__file__).resolve().parent.parent

        full_path = project_root / relative_file_path

        self.file_input.set_input_files(str(full_path))

    def click_upload(self):
        self.upload_button.click()

    def get_uploaded_file_name(self):
        return self.uploaded_file.inner_text().strip()