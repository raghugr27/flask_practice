from selenium import webdriver
import time
import credentials
from selenium.webdriver.common.action_chains import ActionChains
def test_successful_item_purchase():
    """
    This function is used to demonstrate and verify successful item purchase in a ecommerce website.

    """

    # creating a driver object
    driver = webdriver.Chrome()

    # creating action chain object
    action = ActionChains(driver)
    time.sleep(1)

    #  Fetching amazon website url for testing
    driver.get("http://automationpractice.com/index.php")
    time.sleep(10)

    firstLevelMenu=driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[1]/a')
    # Moving the cursor towards account-list
    action.move_to_element(firstLevelMenu).perform()
    time.sleep(10)