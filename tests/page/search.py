from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


class Hotel_Search:

    def __init__(self, driver):
        self.driver = driver

    # Find second hotel from list
    def get_second_hotel(self, wait):

        # Find second hotel from list
        try:
            second_hotel_found = more_deals[1].find_element(By.XPATH, "..//..//..//span[@itemprop='name']")
        except exceptions.NoSuchElementException as e:
            print('{0} >> {1}'.format('second_hotel_found', e))

        return second_hotel_found

    # Opens deals panel for second hotel
    def open_hotel_3rd_deal(self, wait):

        global more_deals

        # Click on button 'More Deals'
        try:
            more_deals = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[@data-testid='more-deals']"))
            )
        except exceptions.NoSuchElementException as e:
            print('{0} >> {1}'.format('more_deals', e))

        more_deals[1].click()

        # Click on 'Visit Site' on 3rd hotel in a list
        try:
            visit_site = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li[data-testid='deal-list-item']"))
            )
        except exceptions.NoSuchElementException as e:
            print('{0} >> {1}'.format('visit_site', e))

        # Checks for number of deals
        if len(visit_site) > 2:
            visit_site[2].click()
        elif len(visit_site) == 2:
            visit_site[1].click()
        else:
            visit_site[0].click()