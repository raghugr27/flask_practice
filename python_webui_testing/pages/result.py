# importing the modules
from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    # Verify that results appear on the results page
    LINK_DIVS = (By.CSS_SELECTOR, '#links > div')
    # Find the search input element
    # In the DOM, it has an 'id' attribute of 'search_form_input_homepage'
    SEARCH_INPUT = (By.ID, 'search_form_input')

    @classmethod
    def PHRASE_RESULTS(cls, phrase):
        # Verify that at least one search result contains the search phrase
        xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
        return (By.XPATH, xpath)

    def __init__(self, browser):
        self.browser = browser
    # verifying the  count of result
    def link_div_count(self):
        link_divs = self.browser.find_elements(*self.LINK_DIVS)
        return len(link_divs)
    # verifying the phrase is present or not
    def phrase_result_count(self, phrase):
        phrase_results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
        return len(phrase_results)
    # returning the obtained result value
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')