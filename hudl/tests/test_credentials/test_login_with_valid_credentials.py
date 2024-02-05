import unittest
from hudl.features.browser_navigator import BrowserNavigator
from hudl.utilities.setup_webdriver import setup_webdriver
from hudl.config import EMAIL, PASSWORD, BROWSER


class TestLoginWithValidCredentials(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment before each test.
        """
        # Set up the WebDriver
        self.driver = setup_webdriver(BROWSER)

        # Create a BrowserNavigator instance
        self.navigator = BrowserNavigator(self.driver)

    def tearDown(self):
        """
        Clean up the test environment after each test.
        """
        # Close the browser window after the test
        self.driver.quit()

    def runTest(self):
        """
        Run the actual test.
        """
        # Use the web_browser_navigator module to validate valid credentials
        result, message = self.navigator.validate_valid_credentials(EMAIL, PASSWORD)

        # Print test result with color-coded output
        color_code = '\033[92m' if result else '\033[91m'  # Green for Pass, Red for Fail
        print(f"{color_code}test validate_valid_credentials: {'Pass' if result else 'Fail'} - {message}")


if __name__ == "__main__":
    # Run the test using the default test runner
    unittest.main(defaultTest='runTest')
