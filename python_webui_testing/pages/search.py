# importing the required modules from selenium package
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Declaring a class
class DuckDuckGoSearchPage:
    # Assigining the url to a variable
    URL = 'https://www.duckduckgo.com'
    # assigning the information to be searched to a variable
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    # initializing the constructor
    def __init__(self, browser):
        self.browser = browser
    # loading the url to the browser
    def load(self):
        self.browser.get(self.URL)
    # Performing the search opeartion using the below function
    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
