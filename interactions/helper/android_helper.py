from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException


def click_by_action_id(driver, resource_id):
    try:
        element = driver.find_element(AppiumBy.ID, resource_id)
        element.click()
    except NoSuchElementException:
        raise NoSuchElementException(f"The element with ID '{resource_id}' cannot be found on the page")


def enter_text_by_id(driver, resource_id, value):
    try:
        element = driver.find_element(AppiumBy.ID, resource_id)
        element.send_keys(value)
    except NoSuchElementException:
        raise NoSuchElementException(f"Element with ID '{resource_id}' not found. Can't send text.")


def is_element_present_by_id(driver, resource_id):
    try:
        is_element_present = driver.find_element(AppiumBy.ID, resource_id).is_displayed()
        return is_element_present
    except NoSuchElementException:
        raise NoSuchElementException(f"The element with ID '{resource_id}' cannot be found on the page")


def get_text_from_the_element(driver, resource_id):
    try:
        element = driver.find_element(AppiumBy.ID, resource_id)
        return element.text
    except NoSuchElementException:
        raise NoSuchElementException(f"The element with ID '{resource_id}' cannot be found on the page")
