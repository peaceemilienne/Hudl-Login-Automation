import unittest
from hudl.features.browser_navigator import BrowserNavigator
from hudl.utilities.setup_webdriver import setup_webdriver
from hudl.config import EMAIL, PASSWORD, BROWSER


class TestLoginWithEmptyFields(unittest.TestCase):
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
        # Define sub-tests for empty fields
        sub_tests = [
            (self.navigator.validate_empty_fields(), "validate_empty_fields"),
            (self.navigator.validate_empty_email_field(PASSWORD), "validate_empty_email_field"),
            (self.navigator.validate_empty_password_field(EMAIL), "validate_empty_password_field")
        ]

        # Iterate through sub-tests
        for sub_test, sub_test_name in sub_tests:
            result, message = sub_test

            # Print the result with color-coded output
            color_code = '\033[92m' if result else '\033[91m'  # Green for Pass, Red for Fail
            print(f"{color_code}test {sub_test_name}: {'Pass' if result else 'Fail'} - {message}")


if __name__ == "__main__":
    # Run the test using the default test runner
    unittest.main(defaultTest='runTest')
