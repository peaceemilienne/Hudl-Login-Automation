import unittest
from hudl.features.browser_navigator import BrowserNavigator
from hudl.utilities.setup_webdriver import setup_webdriver
from hudl.config import EMAIL, PASSWORD, BROWSER


class TestLoginCaseSensitivity(unittest.TestCase):
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
        # Define sub-tests for case sensitivity
        sub_tests = [
            self.navigator.validate_case_sensitivity_password,
            self.navigator.validate_case_sensitivity_email
        ]

        # Iterate through sub-tests
        for sub_test in sub_tests:
            with self.subTest(sub_test.__name__):
                # Run the sub-test and get the result
                result, message = sub_test(EMAIL, PASSWORD)


                # Print the result with color-coded output
                color_code = '\033[92m' if result else '\033[91m'  # Green for Pass, Red for Fail
                print(f"{color_code}test {sub_test.__name__}: {'Pass' if result else 'Fail'} - {message}")


if __name__ == "__main__":
    # Run the test using the default test runner
    unittest.main(defaultTest='runTest')
