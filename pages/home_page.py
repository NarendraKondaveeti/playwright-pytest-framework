from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.heading = page.locator("h1")

    def open(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def get_heading(self):
        return self.heading.text_content().strip()