from config.settings import Settings
from playwright.sync_api import Page


class FramesPage:

    def __init__(self, page: Page):
        self.page = page

        self.frame = page.frame_locator("#mce_0_ifr")
        self.content = self.frame.locator("#tinymce")

    def open(self):
        self.page.goto(f"{Settings.BASE_URL}/iframe")

    def get_content(self):
        return self.content.inner_text().strip()