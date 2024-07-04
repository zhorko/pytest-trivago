from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


class Trivago_Main:
    
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    # Inputs name of hotel in a search field and selects from dropdown list
    def input_name(self, wait, city_name):
        
        # Click on button to enable writing 
        try:
            wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='search-form-destination']"))
            ).click()
        except exceptions.NoSuchElementException as e:
            print('{0} = {1}'.format('where_to_button', e))
        
        # Find text box and inseret 'hotel_name' in
        try:
            wait.until(
            EC.element_to_be_clickable((By.ID, "input-auto-complete"))
            ).send_keys("Hamburg")
        except exceptions.NoSuchElementException as e:
            print('{0} = {1}'.format('where_to_input', e))

        # Click on button with 'hotel_name' text
        try:
            wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '" + city_name + "')]"))
            ).click()
        except exceptions.NoSuchElementException as e:
            print('{0} >> {1}'.format('search_btn', e))
    
    # Select 'start' and 'end' date
    def enter_dates(self, wait, start_date, end_date):
        
        # Date format: '2024-06-06'

        START_DATE = ''.join(['valid-calendar-day-', start_date])
        END_DATE = ''.join(['valid-calendar-day-', end_date])
        
        # Accept Cookies
        try:
            accept_cookies = self.driver.execute_script('''return document.querySelector('#usercentrics-root').shadowRoot.querySelector('button[data-testid="uc-accept-all-button"]')''')
        except exceptions.NoSuchElementException as e:
            print('{0} >> {1}'.format('accept_cookies', e))

        if accept_cookies == None:
            return
        else:
            accept_cookies.click()

        # Select checkin
        try:
            wait.until(
            EC.visibility_of_element_located((By.XPATH, "//button[@data-testid='"+ START_DATE +"']"))
            ).click()
        except exceptions.StaleElementReferenceException as e:
            print('{0} >> {1}'.format("checkin", 'Message: stale element reference: stale element not found in the current frame'))

        # Select checkout
        try:
            wait.until(
            EC.visibility_of_element_located((By.XPATH, "//button[@data-testid='"+ END_DATE +"']"))
            ).click()
        except exceptions.StaleElementReferenceException as e:
            print('{0} >> {1}'.format('checkout', e))

        # Click on button with 'Apply dates' text
        try:
            wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Apply dates')]"))
            ).click()
        except exceptions.NoSuchElementException as e:
            print('{0} >> {1}'.format('date_confirm', e))

    # Searches hotel 
    def search(self, wait):
        
        # Click on button 'Search' 
        try:
            wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='guest-selector-apply']"))
            ).click()
        except exceptions.NoSuchElementException as e:
            print('{0} >> {1}'.format('search_main', e))