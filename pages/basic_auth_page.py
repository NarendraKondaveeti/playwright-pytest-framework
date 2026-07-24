from playwright.sync_api import Page


class BasicAuthPage:

    def __init__(self, page: Page):
        self.page = page
        self.success_message = page.locator("#content p")

    def open(self, username, password):
        auth_url = (
            f"https://{username}:{password}"
            "@the-internet.herokuapp.com/basic_auth"
        )
        self.page.goto(auth_url)

    def get_success_message(self):
        return self.success_message.inner_text().strip()