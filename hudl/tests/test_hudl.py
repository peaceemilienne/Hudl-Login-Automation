"""
TestHudl Module

This module defines the TestHudl class, which is responsible for creating and running a test suite for Hudl login-related tests.

Attributes:
    TestHudl (class): A class containing methods for creating and running a test suite.
"""

import unittest
from test_credentials.test_password_recovery import TestPasswordRecovery
from hudl.tests.test_login_case_sensitivity import TestLoginCaseSensitivity
from test_credentials.test_login_with_invalid_credentials import TestLoginWithInvalidCredentials
from test_credentials.test_login_with_valid_credentials import TestLoginWithValidCredentials
from test_credentials.test_login_with_empty_fields import TestLoginWithEmptyFields


class TestHudl(unittest.TestCase):
    """
    TestHudl Class

    A class for creating and running a test suite for Hudl login-related tests.

    Methods:
        test_suite(): Creates and returns a test suite containing various login-related test cases.
    """

    def test_suite(self):
        """
        Create a test suite.

        Returns:
            TestSuite: A test suite containing various login-related test cases.
        """
        # Create a test suite
        test_suite = unittest.TestSuite()

        # Add an instance of TestLoginSuite to the test suite
        test_suite.addTest(TestLoginWithValidCredentials())
        test_suite.addTest(TestLoginWithInvalidCredentials())
        test_suite.addTest(TestLoginCaseSensitivity())
        test_suite.addTest(TestLoginWithEmptyFields())
        test_suite.addTest(TestPasswordRecovery())

        return test_suite


if __name__ == "__main__":
    # Run the test suite using the custom test runner
    unittest.main()
