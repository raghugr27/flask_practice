# importing pytest module
import pytest
# importing the required modules
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

# Importing logger
import logging

# Create and configure logger
logging.basicConfig(
    filename="test_web.log", format="%(asctime)s %(message)s", filemode="w")

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to INFO
logger.setLevel(logging.INFO)
logger.info("Starting the Execution")
def test_add():
    assert (1+1)==2
logger.info("Successfully completed testing addition function")
@pytest.mark.parametrize(
  "a,b,expected",
  [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-3, 5, -15), (-4, -5, 20)])
def test_multiplication(a, b, expected):
  assert a * b == expected
logger.info("Successfully completed testing multiplication function")
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        var = 1 / 0
logger.info("Successfully completed testing division function")
logger.info("Starting for testing web page")
def test_basic_duckduckgo_search(browser):
    # Set up test case data
    PHRASE = 'panda'
    # Search for the phrase
    search_page = DuckDuckGoSearchPage(browser)

    search_page.load()
    logger.info("Loading the browser")
    search_page.search(PHRASE)
    logger.info("Searching for the phrase")
    # Verify that results appear
    result_page = DuckDuckGoResultPage(browser)

    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE
    logger.info("verifying the result")
    logger.info("test cases passed")

##############Script Details##################

# Script name :  testing web_url_task.py
# Script version :  3.8.5
# Prepared By : RAGHU G R
# Mail Id : Raghu.Ramakrishna@infinite.com
# Create Date : 07/06/2021
# Last Modification Date : 07/06/2021

################################################
