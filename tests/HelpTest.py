from pages.BasePageHelper import BasePageHelper
from core.BaseTest import browser
from pages.HelpPage import  HelpPageHelper, HelpPageLocators
from pages.AdvertisementCabinetHelp import AdvertisementCabinetHelpHelper


BASE_URL = "https://ok.ru/help"

def test_help_page(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scroll_to_item(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementPage = AdvertisementCabinetHelpHelper(browser)
    AdvertisementPage.check_page()


