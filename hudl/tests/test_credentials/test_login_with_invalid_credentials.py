import unittest
from hudl.features.browser_navigator import BrowserNavigator
from hudl.utilities.setup_webdriver import setup_webdriver
from hudl.config import EMAIL, PASSWORD, BROWSER


class TestLoginWithInvalidCredentials(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment before each test.
        """
        # Set up the WebDriver
        self.driver = setup_webdriver(BROWSER)

        # Create a BrowserNavigator instance
        self.navigator = BrowserNavigator(self.driver)

        # Uncomment the line below if you need to navigate to a specific URL
        # self.driver.get("https://www.hudl.com/")

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
        # Define sub-tests for invalid credentials
        sub_tests = [
            self.navigator.validate_invalid_credentials,
            self.navigator.validate_invalid_email_credential,
            self.navigator.validate_invalid_password_credential
        ]

        results = []

        # Iterate through sub-tests
        for sub_test in sub_tests:
            with self.subTest(sub_test.__name__):
                result, message = sub_test(EMAIL, PASSWORD)

                # Print the result with color-coded output
                color_code = '\033[92m' if result else '\033[91m'  # Green for Pass, Red for Fail
                print(f"{color_code}test {sub_test.__name__}: {'Pass' if result else 'Fail'} - {message}")


if __name__ == "__main__":
    # Run the test using the default test runner
    unittest.main(defaultTest='runTest')
