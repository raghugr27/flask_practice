from src.testproject.sdk.drivers import webdriver
import logging

# Create and configure logger
logging.basicConfig(
    filename="test_web.log", format="%(asctime)s %(message)s", filemode="w")

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to INFO
logger.setLevel(logging.INFO)
def test_simple():
    logger.info("Starting the Execution")
    driver = webdriver.Chrome(token="KjgxxhXB2W4veGLd1UJtz7XDVtYl5foXsAhkWgvbWEM1")
    driver.get("https://example.testproject.io/web/")
    logger.info("loading the browser")

    driver.find_element_by_css_selector("#name").send_keys("John Smith")
    logger.info("providing user name")
    driver.find_element_by_css_selector("#password").send_keys("12345")
    logger.info("providing user password")
    driver.find_element_by_css_selector("#login").click()
    logger.info("verifying the credentials")

    passed = driver.find_element_by_css_selector("#logout").is_displayed()
    logger.info("logging out!.........")

    print("Test passed") if passed else print("Test failed")
    logger.info("All the test cases passed")

    driver.quit()


if __name__ == "__main__":
    test_simple()