#!/usr/bin/python3.8

# Purpose of the script.
########################################################################################################################
# This script has been designed to test the 'Scenario for eCommerce Application'.

# Navigate to the corresponding URL and pass the value of email id and password.

# Then login to the ecommerce application by fetching the email id and password from credentials.py.

# Find the create account button 'user_submit’. and click them one after the other.

########################################################################################################################
# Below points has been consider in the script.
########################################################################################################################
# 1.Validate the sign up form based on success and failure conditions.

# 2.A log file has been created with the current date time stamp along with the message specified.

# 3.To generate HTML reports into pdf reports using the testproject-python-sdk.

########################################################################################################################
# Importing web driver from selenium
from src.testproject.sdk.drivers import webdriver
import time
import logging

# Importing action_chain method to perform automating actions on ecommerce website
from selenium.webdriver.common.action_chains import ActionChains

# importing user credentials from credentials.py file
import credentials

list_of_colors = ["rgba(196, 0, 0, 1)", "rgba(196, 0, 0, 1)", "rgba(221, 0, 0, 1)", "rgba(221, 0, 0, 1)"]
# Setting the loggers
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("creating and setting the value to logger")
logging.basicConfig(
    filename="logfile.log", format="%(asctime)s %(message)s", filemode="w"
)

logger.info("starting the execution of successful login function")


# function for successful login of user
def test_successful_sign_in():
    # creating a driver object
    driver = webdriver.Chrome(token="KjgxxhXB2W4veGLd1UJtz7XDVtYl5foXsAhkWgvbWEM1")

    # creating action chain object
    action = ActionChains(driver)
    time.sleep(1)

    #  Fetching amazon website url for testing
    logger.info(" fetching amazon website")
    driver.get('http://www.amazon.in')
    time.sleep(3)

    logger.info("navigating for sig-in page")
    # Assigning the xpath of account-list in amazon
    firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')

    # Moving the cursor towards account-list
    action.move_to_element(firstLevelMenu).perform()
    time.sleep(3)

    # Identifying the xpath for sign-in button
    secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')

    # Performing click operation on sign-in button
    secondLevelMenu.click()
    time.sleep(3)

    # Identifying the xpath of email box to provide email
    signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')

    # Providing user email
    signinelement.send_keys(credentials.USERNAME)
    logger.info("providing user email id")

    # Performing click operation on continue button
    cont = driver.find_element_by_xpath('//*[@id="continue"]')
    cont.click()
    time.sleep(3)

    # Identifying the xpath of password box to provide password
    passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')

    # Providing user password
    passwordelement.send_keys(credentials.PASSWORD)
    logger.info("providing user password")
    time.sleep(3)

    # Performing click operation on submit button
    login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
    logger.info("clicking on submit button")
    login.click()
    logger.info(" Successfuly logged In")
    time.sleep(3)
    driver.quit()


time.sleep(5)

logger.info("starting the execution of invalid mail function")


# function for testing invalid email-id
def test_invalid_email_id():
    time.sleep(1)

    # creating a driver object
    driver = webdriver.Chrome(token="KjgxxhXB2W4veGLd1UJtz7XDVtYl5foXsAhkWgvbWEM1")

    # creating action chain object
    action = ActionChains(driver)

    #  Fetching amazon website url for testing
    driver.get('http://www.amazon.in')
    time.sleep(3)

    # Assigning colour to a variable for testing purpose

    # Assigning message to a variable for testing purpose
    msg_to_be_obtained = "We cannot find an account with that email address"

    # Assigning the xpath of account-list in amazon
    firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')

    # Moving the cursor towards account-list
    action.move_to_element(firstLevelMenu).perform()
    time.sleep(3)

    # Identifying the xpath for sign-in button
    secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')

    # Performing click operation on sign-in button
    secondLevelMenu.click()
    time.sleep(3)
    logger.info(" providing invalid email")

    # Identifying the xpath of email box to provide email
    signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')

    # Providing invalid user email
    signinelement.send_keys(credentials.INVALID_EMAIL)

    # Performing click operation on continue button
    cont = driver.find_element_by_xpath('//*[@id="continue"]')
    logger.info("clicking on continue button")
    cont.click()
    time.sleep(5)

    # Fetching the xpath of error message to be obtained
    check_email_error = driver.find_element_by_xpath('//*[@id="auth-error-message-box"]')

    # Converting the error message to list to extract only error message
    error_msg = list(check_email_error.get_attribute('innerHTML').split("span")[1][1:-4])[33:82]
    obtained_error_msg = "".join(error_msg)

    # Fetching the xpath of error color to be obtained
    check_box_colour = driver.find_element_by_xpath('//*[@id="auth-error-message-box"]')

    # Assigning the  obtained error color  to a variable
    obtained_check_box_colour = check_box_colour.value_of_css_property('border-bottom-color')

    # Verifying the error message with a default message value
    assert msg_to_be_obtained == obtained_error_msg

    # Verifying the color message with a color message value
    assert obtained_check_box_colour in list_of_colors
    logger.info(f"Error:{obtained_error_msg}")
    time.sleep(3)
    driver.quit()

    logger.info("starting the execution of invalid password function")


time.sleep(10)


# function for checking the invalid password
def test_valid_email_invalid_password():
    # creating a driver object
    driver = webdriver.Chrome(token="KjgxxhXB2W4veGLd1UJtz7XDVtYl5foXsAhkWgvbWEM1")

    # creating action chain object
    action = ActionChains(driver)

    #  Fetching amazon website url for testing
    driver.get('http://www.amazon.in')

    # Assigning message to a variable for testing purpose
    msg_to_be_obtained = "Your password is incorrect"

    # Assigning color to a variable for testing purpose

    time.sleep(10)

    # Assigning the xpath of account-list in amazon
    firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')

    # Moving the cursor towards account-list
    action.move_to_element(firstLevelMenu).perform()
    time.sleep(5)

    # Identifying the xpath for sign-in button
    secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')

    # Performing click operation on sign-in button
    secondLevelMenu.click()
    time.sleep(5)

    # Identifying the xpath of email box to provide email
    signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')

    # Providing valid user email
    logger.info("Providing valid email")
    signinelement.send_keys(credentials.USERNAME)

    # Performing click operation on continue button
    cont = driver.find_element_by_xpath('//*[@id="continue"]')
    cont.click()
    logger.info("clicking on continue button")
    time.sleep(5)

    # Identifying the xpath of password box to provide password
    passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')

    # Providing user password
    passwordelement.send_keys(credentials.INVALID_PASSWORD)
    logger.info("providing password")
    time.sleep(5)

    # Performing click operation on submit button
    login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
    logger.info("click on submit button")
    login.click()

    # Fetching the xpath of error message to be obtained
    error = driver.find_element_by_xpath('//*[@id="auth-error-message-box"]/div/div/ul/li/span')

    # Converting the error message to list to extract only error message
    error_msg_obtained = list(error.get_attribute('innerHTML'))[13:39]
    error_msg_obtained = "".join(error_msg_obtained)

    # Fetching the xpath of error color to be obtained
    check_box_colour = driver.find_element_by_xpath('//*[@id="auth-error-message-box"]')

    # Assigning the  obtained error color  to a variable
    obtained_check_box_colour = check_box_colour.value_of_css_property('border-bottom-color')

    # Verifying the error message with a default message value
    assert msg_to_be_obtained == error_msg_obtained

    # Verifying the color message with a color message value
    assert obtained_check_box_colour in list_of_colors
    logger.info(f"Error:{error_msg_obtained}")
    time.sleep(3)
    driver.quit()

    logger.info("starting the execution of blank email id function")


time.sleep(10)


# Function for blank email id
def test_blank_id():
    # creating a driver object
    driver = webdriver.Chrome(token="KjgxxhXB2W4veGLd1UJtz7XDVtYl5foXsAhkWgvbWEM1")

    # creating action chain object
    action = ActionChains(driver)

    #  Fetching amazon website url for testing
    driver.get('http://www.amazon.in')

    # Assigning message to a variable for testing purpose
    msg_to_be_obtained = "Enter your email or mobile phone number"

    # Assigning colour to a variable for testing purpose
    time.sleep(10)
    logger.info("navigating for sign in page ")

    # Assigning the xpath of account-list in amazon
    firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')

    logger.info(" clicking on continue button without providing email")

    # Moving the cursor towards account-list
    action.move_to_element(firstLevelMenu).perform()
    time.sleep(5)

    # Identifying the xpath for sign-in button
    secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')

    # Performing click operation on sign-in button
    secondLevelMenu.click()
    time.sleep(5)

    # Identifying the xpath of email box to provide email
    signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')

    # Performing click operation on continue button
    cont = driver.find_element_by_xpath('//*[@id="continue"]')
    cont.click()
    time.sleep(5)

    # Assigning the  obtained error color  to a variable
    obtained_check_box_colour = signinelement.value_of_css_property('border-bottom-color')

    # Fetching the xpath of error message to be obtained
    error = driver.find_element_by_xpath('//*[@id="auth-email-missing-alert"]/div/div')

    # Converting the error message to list to extract only error message
    error_msg_obtained = list(error.get_attribute('innerHTML'))[3:42]
    error_msg_obtained = "".join(error_msg_obtained)

    # Verifying the error message with a default message value
    assert msg_to_be_obtained == error_msg_obtained

    # Verifying the color message with a color message value
    assert obtained_check_box_colour in list_of_colors
    logger.info(f"Error:{error_msg_obtained}")

    logger.info("starting the execution of blank password function")

    driver.quit()
time.sleep(10)


# function for blank password
def test_blank_password():
    # creating a driver object
    driver = webdriver.Chrome(token="KjgxxhXB2W4veGLd1UJtz7XDVtYl5foXsAhkWgvbWEM1")

    # creating action chain object
    action = ActionChains(driver)

    # Assigning message to a variable for testing purpose
    msg_to_be_obtained = "Enter your password"

    # Assigning colour to a variable for testing purpose

    #  Fetching amazon website url for testing
    driver.get('http://www.amazon.in')
    time.sleep(10)

    # Assigning the xpath of account-list in amazon
    firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')

    # Moving the cursor towards account-list
    action.move_to_element(firstLevelMenu).perform()
    time.sleep(5)

    # Identifying the xpath for sign-in button
    secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')

    # Performing click operation on sign-in button
    secondLevelMenu.click()
    time.sleep(5)

    # Identifying the xpath of email box to provide email
    signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')

    # Providing user email
    signinelement.send_keys(credentials.USERNAME)

    # Performing click operation on continue button
    cont = driver.find_element_by_xpath('//*[@id="continue"]')
    cont.click()
    time.sleep(5)

    # Identifying the xpath of password box to provide password
    passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
    time.sleep(5)

    # Performing click operation on submit button
    login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
    login.click()

    # Fetching the xpath of error message to be obtained
    error = driver.find_element_by_xpath('// *[ @ id = "auth-password-missing-alert"] / div / div')

    # Converting the error message to list to extract only error message
    error_msg_obtained = list(error.get_attribute('innerHTML'))[3:22]
    error_msg_obtained = "".join(error_msg_obtained)

    # Assigning the  obtained error color  to a variable
    obtained_check_box_colour = passwordelement.value_of_css_property('border-bottom-color')

    # Verifying the error message with a default message value
    assert msg_to_be_obtained == error_msg_obtained

    # Verifying the color message with a color message value
    assert obtained_check_box_colour in list_of_colors
    driver.quit()


logger.info("starting the execution of forgot password function")

time.sleep(10)


# function to check forgot password
def test_forgot_password():
    # creating a driver object
    driver = webdriver.Chrome(token="KjgxxhXB2W4veGLd1UJtz7XDVtYl5foXsAhkWgvbWEM1")

    # creating action chain object
    action = ActionChains(driver)

    # Assigning message to a variable for testing purpose
    msg_to_be_obtained = "Enter the email address or mobile phone number associated with your Amazon account"

    #  Fetching amazon website url for testing
    driver.get('http://www.amazon.in')
    time.sleep(10)

    # Assigning the xpath of account-list in amazon
    firstlevelmenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')

    # Moving the cursor towards account-list
    action.move_to_element(firstlevelmenu).perform()
    time.sleep(5)

    # Identifying the xpath for sign-in button
    secondlevelmenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')

    # Performing click operation on sign-in button
    secondlevelmenu.click()
    time.sleep(5)

    # Identifying the xpath of email box to provide email
    signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')

    # Providing user email
    signinelement.send_keys(credentials.USERNAME)

    # Performing click operation on continue button
    cont = driver.find_element_by_xpath('//*[@id="continue"]')
    cont.click()
    time.sleep(5)

    # Identifying the xpath of forgot password to perform click operation
    forget_password = driver.find_element_by_xpath('//*[@id="auth-fpp-link-bottom"]')

    # Performing click operation on forgot password link
    forget_password.click()
    time.sleep(3)

    # Fetching the xpath of  message to be obtained
    msg = driver.find_element_by_xpath('//*[@id="authportal-main-section"]/div[2]/div/div[1]/div/form/p')

    # Converting the error message to list to extract only error message
    error_msg_obtained = list(msg.get_attribute('innerHTML'))[9:91]
    error_msg_obtained = "".join(error_msg_obtained)

    # Verifying the  message with a default message value
    assert msg_to_be_obtained == error_msg_obtained
    time.sleep(3)
    driver.quit()
##########################################################################################################

# script details

# Script name               :       test_amazon_website.py
# Script version            :       1.0
# Prepared By               :       Raghu G.R
# Create Date               :       16-june-2021
# Last Modification Date    :       18-june-2021

##########################################################################################################
