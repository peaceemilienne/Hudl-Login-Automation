## Hudl Login Automation

### Overview

This project automates functional tests for the login page on [hudl.com](https://www.hudl.com/). Utilizing Selenium 4.17.2 and respective browser drivers, it ensures the reliability of login processes, covering scenarios such as valid and invalid credentials, case sensitivity, and more.

Refer to [Automated Tests](#automated-tests) for details and [Running Tests](#running-tests) for running tests in the specified environment.


### Automated Tests

This project includes a comprehensive set of automated tests to ensure the functionality of the hudl login form. The tests cover various scenarios to provide thorough validation.

#### Test Scenarios:

1. **Validate Successful Login:**
   - [ ] Ensure a user can successfully log in with a valid email and password.

2. **Validate Failed Login Attempts:**
   - [ ] Verify that a user cannot log in with an invalid email and password.
   - [ ] Confirm that a user cannot log in with an invalid email and valid password.
   - [ ] Confirm that a user cannot log in with a valid email and invalid password.

3. **Validate Case Sensitivity:**
   - [ ] Ensure case sensitivity isn't applied to the email, allowing users to log in with a capital letter email and a valid password.
   - [ ] Confirm that case sensitivity is applied to the password, requiring users to enter the correct case; otherwise, the password is considered invalid.

4. **Validate Empty Fields:**
   - [ ] Verify that users cannot log in with empty fields, and an appropriate error message is displayed.
   - [ ] Confirm that users cannot log in with an empty email field, and a relevant error message is displayed.
   - [ ] Confirm that users cannot log in with an empty password field, and an appropriate error message is displayed.

5. **Validate Forgot Password Functionality:**
   - [ ] Ensure the "Forgot Password" link leads to the password recovery page.


### Project Structure

This project follows a modular and organized structure to facilitate maintainability, readability, and scalability.

#### Directory Structure

##### `hudl/`
This directory contains the core implementation of the project.

- **`features/`**: This directory holds features related to browser navigation and page objects.
    - **`browser_navigator.py`**: Implements functionality for navigating the web browser.
    - **`page_objects/`**: Contains page objects representing different web pages.
        - `forgot_password_page.py`: Page object for the Forgot Password page.
        - `login_page.py`: Page object for the Login page.
        - `home_page.py`: Page object for the Home page.

- **`tests/`**: This directory houses all test modules.
    - **`test_credentials/`**: Test suite for various login scenarios.
        - `test_invalid_credentials.py`: Tests for invalid login credentials.
        - `test_valid_credentials.py`: Tests for valid login credentials.
        - `test_empty_fields.py`: Tests for login with empty fields.
        - `test_forgot_password.py`: Tests for the Forgot Password functionality.
    - `test_login_case_insensitivity.py`: Additional test for login case insensitivity.
    - `test_hudl.py`: Main test module that runs all the test cases.

#### `config.py`
Configuration file containing parameters for the project.

#### `utilities/`
Utility setup scripts.

- **`setup_webdriver.py`**: Script for setting up the WebDriver for browser automation.

### Dependencies

This project relies on the following dependencies:

- **Selenium:** Version 4.17.2 [![Selenium](https://img.shields.io/badge/Selenium-4.17.2-brightgreen)](https://www.selenium.dev/)
- **ChromeDriver:** Version 121.0.6167.85 [![ChromeDriver](https://img.shields.io/badge/ChromeDriver-121.0.6167.85-blue)](https://googlechromelabs.github.io/chrome-for-testing/)
- **SafariDriver:** Version 6.7 (Included in Safari)
- **Python:** Version 3.10.1 [![Python](https://img.shields.io/badge/Python-3.10.1-blue)](https://www.python.org/)

Ensure these dependencies are installed in your environment before running the tests.

### Test Environment

The tests have been developed and verified in the following environment:

- **Chrome Browser:** Version 121.0.6167.139
- **Safari Browser:** Version 4.17.2

**Optional:** For an enhanced development experience, you may choose to use the [PyCharm IDE](https://www.jetbrains.com/pycharm/), which offers robust features for Python development, debugging, and test execution.

Make sure your local environment matches or exceeds these versions for optimal test execution. You may need to download the appropriate driver versions (ChromeDriver and SafariDriver) compatible with your browser versions.

### Running Tests:

1. Clone the repository.
2. Set up the virtual environment and install dependencies.
3. Configure parameters in `config.py`.
4. Run tests using the main test module: `python hudl/tests/test_hudl.py`.

**Note: Avoid Navigating Between Windows During Test Execution**

While the automation is running, refrain from manually navigating between various windows or tabs in the browser, as this may interfere with the test execution and lead to unexpected results. If multiple windows are opened during the test, it can cause the test to fail due to overlapping windows. Allow the automation to run undisturbed to ensure accurate test results.


### Test result output sample

![image](Screenshot%202024-02-03%20at%206.35.47%E2%80%AFPM.png)