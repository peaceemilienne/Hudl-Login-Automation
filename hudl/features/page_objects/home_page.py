import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    """
    Represents the homepage of the application.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.

    Attributes:
        driver (WebDriver): The Selenium WebDriver instance.
        url (str): The URL of the homepage.

    Methods:
        navigate: Navigates to the homepage.
        find_element: Finds a web element using Selenium WebDriverWait.
        login: Finds and returns the login element on the homepage.
        hudl_login: Finds and returns the Hudl login element on the homepage.
        click_login: Clicks the login element on the homepage.
        click_hudl_login: Clicks the Hudl login element on the homepage.
    """

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.hudl.com/"  # Set the login page URL

    def navigate(self):
        """
        Navigates to the homepage.
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

    def login(self):
        """
        Finds and returns the login element on the homepage.

        Returns:
            WebElement: The login element.
        """
        return self.find_element(
            By.CSS_SELECTOR, 'a.mainnav__item.mainnav__item--expandable[data-qa-id="login-select"]'
        )

    def hudl_login(self):
        """
        Finds and returns the Hudl login element on the homepage.

        Returns:
            WebElement: The Hudl login element.
        """
        return self.find_element(
            By.CSS_SELECTOR, 'a.subnav__item.subnavitem.subnavitem--icon[data-qa-id="login-hudl"]'
        )

    def click_login(self):
        """
        Clicks the login element on the homepage.
        """
        login_element = self.login()
        if login_element:
            login_element.click()
        else:
            logging.warning("Login button not found on the homepage")

    def click_hudl_login(self):
        """
        Clicks the Hudl login element on the homepage.
        """
        hudl_login_element = self.hudl_login()
        if hudl_login_element:
            hudl_login_element.click()
        else:
            logging.warning("Hudl login button not found on the homepage")

