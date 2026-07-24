from config.settings import Settings
from playwright.sync_api import Page


class CheckboxesPage:

    def __init__(self, page: Page):
        self.page = page

        self.checkbox1 = page.locator("input[type='checkbox']").nth(0)
        self.checkbox2 = page.locator("input[type='checkbox']").nth(1)

    def open(self):
        self.page.goto(f"{Settings.BASE_URL}/checkboxes")

    def check_checkbox1(self):
        self.checkbox1.check()

    def uncheck_checkbox1(self):
        self.checkbox1.uncheck()

    def check_checkbox2(self):
        self.checkbox2.check()

    def uncheck_checkbox2(self):
        self.checkbox2.uncheck()

    def is_checkbox1_checked(self):
        return self.checkbox1.is_checked()

    def is_checkbox2_checked(self):
        return self.checkbox2.is_checked()