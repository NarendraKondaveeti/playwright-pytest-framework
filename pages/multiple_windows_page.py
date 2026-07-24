from config.settings import Settings
from playwright.sync_api import Page


class MultipleWindowsPage:

    def __init__(self, page: Page):
        self.page = page

        self.click_here = page.locator("a[href='/windows/new']")

    def open(self):
        self.page.goto(f"{Settings.BASE_URL}/windows")

    def open_child_window(self):

        with self.page.expect_popup() as popup_info:
            self.click_here.click()

        child_page = popup_info.value

        child_page.wait_for_load_state()

        return child_page