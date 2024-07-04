from selenium.webdriver.support.wait import WebDriverWait

from page.main import Trivago_Main
from page.search import Hotel_Search
from page.hotel_site import Hotel_Site


def test_trivago(chrome_browser):

    URL = "https://www.trivago.com/"
    CITY = "Hamburg"
    DATE_START = '2024-07-16'
    DATE_END = '2024-07-23'

    wait = WebDriverWait(chrome_browser, 20)

    # Initializations
    main_page = Trivago_Main(chrome_browser)
    search_page = Hotel_Search(chrome_browser)
    hotel_page = Hotel_Site(chrome_browser)
    
    main_page.open_page(URL)
    main_page.input_name(wait, CITY)
    main_page.enter_dates(wait, DATE_START, DATE_END)
    main_page.search(wait)

    search_page.open_hotel_3rd_deal(wait)
    search_page.get_second_hotel(wait)

    assert hotel_page.get_hotel_name(wait, search_page.get_second_hotel(wait))