from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Hotel_Site:

    def __init__(self, driver):
        self.driver = driver

    # Verify name from trivago hotel name and from 3rd deal
    def get_hotel_name(self, wait, trivago_hotel_name):

        try:
            new_hotel_name = wait.until( 
                EC.element_to_be_clickable((By.XPATH, 
                                            "//*[contains(translate(text(), \
                                            'ABCDEFGHIJKLMNOPQRSTUVWXYZ', \
                                            'abcdefghijklmnopqrstuvwxyz'), '" 
                                            + trivago_hotel_name.text.lower() + "')]"
                                            )))
            return new_hotel_name.text
        except:
            assert False, "Hotel name was not found!"