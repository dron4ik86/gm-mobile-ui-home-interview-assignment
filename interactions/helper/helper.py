from interactions.helper import android_helper


class Helper:
    """
    The Helper class makes it easy to interact with the app's UI elements like clicking buttons or entering text.
    It automatically adjusts to work with both iOS and Android.
    """
    def __init__(self, driver):
        """
        Initializes the Helper with the driver. It determines the device's platform (iOS or Android)
        and selects the appropriate set of tools (iOS_helper or android_helper) for that platform.
        """
        self.driver = driver
        self.platform_helper = None
        self._initialize_platform_helper()

    def _initialize_platform_helper(self):
        """Chooses the correct set of tools based on whether the app is running on iOS or Android."""
        if self.driver.capabilities.get('platformName') == 'Android':
            self.platform_helper = android_helper

    def click_by_action_id(self, element):
        self.platform_helper.click_by_action_id(self.driver, element)

    def enter_text_by_id(self, element):
        self.platform_helper.enter_text_by_id(self.driver, element)

    def is_element_present_by_id(self, element):
        self.platform_helper.is_element_present_by_id(element)

    def get_text_from_the_element(self, element):
        self.platform_helper.get_text_from_the_element(element)
