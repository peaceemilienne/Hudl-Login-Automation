import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Represents the Login page of the application.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.

    Attributes:
        driver (WebDriver): The Selenium WebDriver instance.
        url (str): The URL of the login page.

    Methods:
        navigate: Navigates to the login page.

        find_element: Finds a web element using Selenium WebDriverWait.
        email_input: Returns the web element representing the email input field.
        password_input: Returns the web element representing the password input field.
        submit_button: Returns the web element representing the submit button.
        forgot_password: Returns the web element representing the forgot password link.
        fill_in_required_fields_message: Returns the web element representing the error message for required fields.
        unknown_credentials_message: Returns the web element representing the error message for unknown credentials.
        home_page: Returns the web element representing the Home button.
        set_email: Sets the value of the email input field.
        set_password: Sets the value of the password input field.
        click_forgot_password: Clicks the forgot password link.
        click_submit: Clicks the submit button.
        find_home_message: Finds and returns whether the Home page message is displayed.
        find_unknown_credentials_error: Finds and returns whether the unknown credentials error message is displayed.
        find_fill_in_fields_error: Finds and returns whether the fill in fields error message is displayed.
    """

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.hudl.com/login"  # Set the login page URL

    def navigate(self):
        """
        Navigates to the login page.
        """
        self.driver.get(self.url)

    def find_element(self, by, value):
        """
        Finds a web element using Selenium WebDriverWait.

        Args:
            by: The locator strategy (e.g., By.CSS_SELECTOR).
            value: The value to locate the web element.

        Returns:
            WebElement: The located web element.
        """
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, value))
        )

    def email_input(self):
        """
        Returns the web element representing the email input field.

        Returns:
            WebElement: The email input field.
        """
        return self.find_element(By.ID, "email")

    def password_input(self):
        """
        Returns the web element representing the password input field.

        Returns:
            WebElement: The password input field.
        """
        return self.find_element(By.ID, "password")

    def submit_button(self):
        """
        Returns the web element representing the submit button.

        Returns:
            WebElement: The submit button.
        """
        return self.find_element(By.ID, "logIn")

    def forgot_password(self):
        """
        Returns the web element representing the forgot password link.

        Returns:
            WebElement: The forgot password link.
        """
        return self.find_element(By.ID, 'forgot-password')

    def fill_in_required_fields_message(self):
        """
        Returns the web element representing the error message for required fields.

        Returns:
            WebElement: The error message element.
        """
        return self.find_element(By.XPATH, '//p[text()="Please fill in all of the required fields"]')

    def unknown_credentials_message(self):
        """
        Returns the web element representing the error message for unknown credentials.

        Returns:
            WebElement: The error message element.
        """
        return self.find_element(By.XPATH, '//p[text()="We don\'t recognize that email and/or password"]')

    def home_button(self):
        """
        Returns the web element representing the Home button.

        Returns:
            WebElement: The Home page link.
        """
        return self.find_element(By.XPATH, "//span[text()='Home']")

    def set_email(self, email):
        """
        Sets the value of the email input field.

        Args:
            email (str): The email to be set.
        """
        element = self.email_input()
        if element:
            element.send_keys(email)

    def set_password(self, password):
        """
        Sets the value of the password input field.

        Args:
            password (str): The password to be set.
        """
        element = self.password_input()
        if element:
            element.send_keys(password)

    def click_forgot_password(self):
        """
        Clicks the forgot password link.
        """
        element = self.forgot_password()
        if element:
            element.click()

    def click_submit(self):
        """
        Clicks the submit button.
        """
        element = self.submit_button()
        if element:
            element.click()

    def find_home_button(self):
        """
        Finds and returns whether the Home page message is displayed.

        Returns:
            bool: True if the Home page message is displayed, False otherwise.
        """
        element = self.home_button()
        # wait for the home button to appear
        time.sleep(5)
        if element:
            return element.is_displayed()
        else:
            raise Exception("Element not found")

    def find_unknown_credentials_error(self):
        """
        Finds and returns whether the unknown credentials error message is displayed.

        Returns:
            bool: True if the unknown credentials error message is displayed, False otherwise.
        """
        element = self.unknown_credentials_message()
        # wait for the error message to appear
        time.sleep(5)
        if element:
            return element.is_displayed()
        else:
            raise Exception("Element not found")

    def find_fill_in_fields_error(self):
        """
        Finds and returns whether the fill in fields error message is displayed.

        Returns:
            bool: True if the fill in fields error message is displayed, False otherwise.
        """
        element = self.fill_in_required_fields_message()
        # wait for the error message to appear
        time.sleep(5)
        if element:
            return element.is_displayed()
        else:
            raise Exception("Element not found")
