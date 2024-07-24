from interactions.helper.helper import Helper
from pages.home.locators import *


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_for_phone_icon(self):
        Helper(self.driver).is_element_present_by_id(PHONE_ICON)

    def user_change_the_temperature(self):
        Helper(self.driver).enter_text_by_id(TEMPERATURE_FIELD)

    def get_text_from_temperature_widget(self):
        Helper(self.driver).get_text_from_the_element(HOME_PAGE_TEMPERATURE)


