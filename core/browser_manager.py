from playwright.sync_api import sync_playwright
from config.settings import Settings


class BrowserManager:

    @staticmethod
    def launch_browser():
        playwright = sync_playwright().start()

        if Settings.BROWSER == "chromium": # అంటే browser nameని functionకి పంపడం లేదు.Function directగా Settings.BROWSER చదువుతోంది.
            browser = playwright.chromium.launch(
                headless=Settings.HEADLESS,
                slow_mo=Settings.SLOW_MO
            )

        elif Settings.BROWSER == "firefox":
            browser = playwright.firefox.launch(
                headless=Settings.HEADLESS,
                slow_mo=Settings.SLOW_MO
            )

        elif Settings.BROWSER == "webkit":
            browser = playwright.webkit.launch(
                headless=Settings.HEADLESS,
                slow_mo=Settings.SLOW_MO
            )

        else:
            raise ValueError(f"Unsupported browser: {Settings.BROWSER}")

        return playwright, browser