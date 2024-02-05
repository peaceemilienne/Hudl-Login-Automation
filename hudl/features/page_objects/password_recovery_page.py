import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PasswordRecoveryPage:
    """
    Represents the Password Recovery page of the application.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.

    Attributes:
        driver (WebDriver): The Selenium WebDriver instance.

    Methods:
        find_element: Finds a web element using Selenium WebDriverWait.
        forgot_password_title: Returns the web element representing the Forgot Password title.
        find_forgot_password_title: Finds and returns the text of the Forgot Password title.
    """

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        """
        Finds a web element using Selenium WebDriverWait.

        Args:
            by: The locator strategy (e.g., By.CSS_SELECTOR).
            value: The value to locate the web element.

        Returns:
            WebElement: The located web element.
        """
        return WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((by, value))
        )

    def forgot_password_title(self):
        """
        Returns the web element representing the Forgot Password title.

        Returns:
            WebElement: The Forgot Password title element.
        """
        return self.find_element(By.CSS_SELECTOR, 'h2.headline.uni-headline--1.page-title')

    def find_forgot_password_title(self):
        """
        Finds and returns the text of the Forgot Password title.

        Returns:
            str: The text of the Forgot Password title, or False if the element is not found.
        """
        element = self.forgot_password_title()
        # wait for the element to appear
        time.sleep(5)
        return "Forgot Password" in element.text if element else False
