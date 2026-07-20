from config.settings import Settings
from playwright.sync_api import Page


class AddRemovePage:

    URL = f"{Settings.BASE_URL}/add_remove_elements/"

    def __init__(self, page: Page):

        self.page = page

        self.add_button = page.get_by_role(
            "button",
            name="Add Element"
        )

        self.delete_button = page.get_by_role(
            "button",
            name="Delete"
        )

    def open(self):
        self.page.goto(self.URL)

    def click_add_element(self):
        self.add_button.click()

    def is_delete_button_visible(self):
        return self.delete_button.is_visible()