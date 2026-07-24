from config.settings import Settings
from playwright.sync_api import Page


class SortableDataTablesPage:

    def __init__(self, page: Page):
        self.page = page

        self.table_rows = page.locator("#table1 tbody tr")

    def open(self):
        self.page.goto(f"{Settings.BASE_URL}/tables")

    def get_total_rows(self):
        return self.table_rows.count()

    def get_last_name(self, row):

        return (
            self.table_rows
            .nth(row - 1)
            .locator("td")
            .nth(0)
            .inner_text()
            .strip()
        )