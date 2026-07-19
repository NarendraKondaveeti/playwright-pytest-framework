import pytest
from core.browser_manager import BrowserManager

@pytest.fixture(scope="function")
def page():

    playwright, browser = BrowserManager.launch_browser()

    context = browser.new_context()

    page = context.new_page()

    yield page

    page.close()
    context.close()
    browser.close()
    playwright.stop()