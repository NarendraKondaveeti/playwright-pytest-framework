from playwright.sync_api import Page
from config.settings import Settings

class ChallengingDomPage:

    def __init__(self, page: Page):
        self.page = page

        self.blue_button = page.locator("a.button").first
        self.red_button = page.locator("a.button.alert")
        self.green_button = page.locator("a.button.success")

        self.table_rows = page.locator("table tbody tr")

    def open(self):
        self.page.goto(f"{Settings.BASE_URL}/challenging_dom")

    def click_blue_button(self):
        self.blue_button.click()

    def click_red_button(self):
        self.red_button.click()

    def click_green_button(self):
        self.green_button.click()

    def get_total_rows(self):
        return self.table_rows.count()