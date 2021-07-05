import json  # importing json module
import pytest  # importing pytest module

# importing chrome and firefox search engines
from selenium.webdriver import Chrome, Firefox

# configuring the json file path
CONFIG_PATH = "tests/config.json"
# Initialising the wait time for browsers
DEFAULT_WAIT_TIME = 10
# Defining the browsers
SUPPORTED_BROWSERS = ["chrome", "firefox"]


# using the fixture so that below function runs only once at the beginning
# Below function is used to read config.json
@pytest.fixture(scope="session")
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


# using the fixture so that below function runs only once at the beginning
# Below function is used for validating browser choice
@pytest.fixture(scope="session")
def config_browser(config):
    # Validate and return the browser choice from the config data
    if "browser" not in config:
        raise Exception('The config file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]


# function to schedule wait time for browsers
@pytest.fixture(scope="session")
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config["wait_time"] if "wait_time" in config else DEFAULT_WAIT_TIME


# function to initialize the web drivers
@pytest.fixture
def browser(config_browser, config_wait_time):
    # Initialize WebDriver
    if config_browser == "chrome":
        driver = Chrome()
    elif config_browser == "firefox":
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()
