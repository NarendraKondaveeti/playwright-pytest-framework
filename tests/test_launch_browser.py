from config.settings import Settings
from pages.home_page import HomePage


def test_home_page(page):

    home = HomePage(page)

    home.open(Settings.BASE_URL)

    assert home.get_title() == "The Internet"

    assert home.get_heading() == "Welcome to the-internet"