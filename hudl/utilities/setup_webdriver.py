from selenium import webdriver


def setup_webdriver(web_browser):

    # Validate and set the browser choice
    if web_browser.lower() == 'safari':
        driver = webdriver.Safari()
    else:
        # Default to Chrome if no choice or an invalid choice is provided
        driver = webdriver.Chrome()

    # Maximize the browser window
    driver.maximize_window()

    return driver
