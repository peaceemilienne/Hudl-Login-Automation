import time
from .page_objects.home_page import HomePage
from .page_objects.login_page import LoginPage
from .page_objects.password_recovery_page import PasswordRecoveryPage


class BrowserNavigator:
    """
    A class representing the browser navigation and validation for various scenarios.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
    """

    def __init__(self, driver):
        """
        Initializes the BrowserNavigator.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.

        Attributes:
            driver (WebDriver): The Selenium WebDriver instance.
            home_page (HomePage): An instance of the HomePage model.
            login_page (LoginPage): An instance of the LoginPage model.
            password_recovery_page (PasswordRecoveryPage): An instance of the PasswordRecoveryPage model.
        """
        self.driver = driver
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.password_recovery_page = PasswordRecoveryPage(self.driver)

    def validate_valid_credentials(self, email, password):
        """
        Validates login with valid credentials.

        Args:
            email (str): The valid email.
            password (str): The valid password.

        Returns:
            tuple: A tuple containing the validation result and a message.
        """
        try:
            self.home_page.navigate()
            self.home_page.click_login()
            self.home_page.click_hudl_login()
            self.login_page.set_email(email)
            self.login_page.set_password(password)
            self.login_page.click_submit()
            time.sleep(3)
            return (
                self.login_page.find_home_button(),
                "User successfully logged in using valid credentials"
            )
        except Exception as e:
            return False, f"User couldn't log in using valid credentials"

    def validate_invalid_credentials(self, email, password):
        """
        Validates login with invalid credentials.

        Args:
            email (str): The invalid email.
            password (str): The invalid password.

        Returns:
            tuple: A tuple containing the validation result and a message.
        """
        try:
            self.login_page.navigate()
            self.login_page.set_email(email[::-1])
            self.login_page.set_password(password[::-1])
            self.login_page.click_submit()
            return (
                self.login_page.find_unknown_credentials_error(),
                "Unknown user error message is displayed using invalid credentials"
            )
        except Exception as e:
            return False, f"Failed to display unknown user error message using invalid credentials"

    def validate_invalid_email_credential(self, email, password):
        """
        Validates login with invalid email.

        Args:
            email (str): The invalid email.
            password (str): The valid password.

        Returns:
            tuple: A tuple containing the validation result and a message.
        """
        try:
            self.login_page.navigate()
            self.login_page.set_email(email[::-1])  # email reversed to be invalid
            self.login_page.set_password(password)
            self.login_page.click_submit()
            time.sleep(2)
            return (
                self.login_page.find_unknown_credentials_error(),
                "Unknown user error message is displayed using invalid email"
            )
        except Exception as e:
            return False, f"Failed to display unknown user error message using invalid email"

    def validate_invalid_password_credential(self, email, password):
        """
        Validates login with invalid password.

        Args:
            email (str): The valid email.
            password (str): The invalid password.

        Returns:
            tuple: A tuple containing the validation result and a message.
        """
        try:
            self.login_page.navigate()
            self.login_page.set_email(email)
            self.login_page.set_password(password[::-1])  # password reversed to be invalid
            self.login_page.click_submit()
            time.sleep(2)
            return (
                self.login_page.find_unknown_credentials_error(),
                "Unknown user error message is displayed using invalid password"
            )
        except Exception as e:
            return False, f"Failed to display unknown user error message using invalid password"

    def validate_case_sensitivity_email(self, email, password):
        """
        Validates login with case-insensitive email.

        Args:
            email (str): The case-sensitive email.
            password (str): The valid password.

        Returns:
            tuple: A tuple containing the validation result and a message.
        """
        try:
            self.login_page.navigate()
            self.login_page.set_email(email.upper())
            self.login_page.set_password(password)
            self.login_page.click_submit()
            time.sleep(2)
            return (
                self.login_page.find_home_button(),
                "User logged in, case sensitivity for user's email successfully ignored"
            )
        except Exception as e:
            return False, f"User can't log in, case sensitivity is applied in user's email"

    def validate_case_sensitivity_password(self, email, password):
        """
        Validates login with case-insensitive password.

        Args:
            email (str): The valid email.
            password (str): The case-sensitive password.

        Returns:
            tuple: A tuple containing the validation result and a message.
        """
        try:
            self.login_page.navigate()
            self.login_page.set_email(email)
            self.login_page.set_password(password.lower())
            self.login_page.click_submit()
            time.sleep(2)
            return (
                self.login_page.find_unknown_credentials_error(),
                "Unknown user error message is displayed using invalid password due to case sensitivity"
            )
        except Exception as e:
            return False, f"Failed to display unknown user error message using invalid password due to case sensitivity"

    def validate_empty_fields(self):
        """
        Validates login with empty email and password fields.

        Returns:
            tuple: A tuple containing the validation result and a message.
        """
        try:
            self.login_page.navigate()
            self.login_page.set_email("")
            self.login_page.set_password("")
            self.login_page.click_submit()
            time.sleep(2)
            return (
                self.login_page.find_fill_in_fields_error(),
                "Fill in all of the required fields error message displayed for empty fields"
            )
        except Exception as e:
            return False, f"Failed to display fill in all of the required fields error message for empty fields"

    def validate_empty_email_field(self, password):
        """
        Validates login with empty email field.

        Args:
            password (str): The valid password.

        Returns:
            tuple: A tuple containing the validation result and a message.
        """
        try:
            self.login_page.navigate()
            self.login_page.set_email("")
            self.login_page.set_password(password)
            self.login_page.click_submit()
            time.sleep(2)
            return (
                self.login_page.find_fill_in_fields_error(),
                "Fill in all of the required fields error message displayed with empty email"
            )
        except Exception as e:
            return False, f"Failed to display fill in all of the required fields error message with empty email"

    def validate_empty_password_field(self, email):
        """
        Validates login with empty password field.

        Args:
            email (str): The valid email.

        Returns:
            tuple: A tuple containing the validation result and a message.
        """
        try:
            self.login_page.navigate()
            self.login_page.set_email(email)
            self.login_page.set_password("")
            self.login_page.click_submit()
            time.sleep(2)
            return (
                self.login_page.find_fill_in_fields_error(),
                "Fill in all of the required fields error message displayed with empty password"
            )
        except Exception as e:
            return False, f"Failed to display fill in all of the required fields error message with empty password"

    def validate_password_recovery(self):
        """
        Validates the password recovery process.

        Returns:
            tuple: A tuple containing the validation result and a message.
        """
        try:
            self.home_page.navigate()
            self.home_page.click_login()
            self.home_page.click_hudl_login()
            time.sleep(3)
            self.login_page.click_forgot_password()
            time.sleep(3)
            return (
                self.password_recovery_page.forgot_password_title(),
                "Forgot password recovery page successfully displayed"
            )
        except Exception as e:
            return False, f"Failed to display forgot password recovery page"
