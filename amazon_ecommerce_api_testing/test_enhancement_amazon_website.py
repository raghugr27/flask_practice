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
    driver.get("http://www.amazon.in")
    time.sleep(3)

    # Assigning the xpath of account-list in amazon
    firstLevelMenu = driver.find_element_by_xpath(
        '//*[@id="nav-link-accountList"]/span'
    )

    # Moving the cursor towards account-list
    action.move_to_element(firstLevelMenu).perform()
    time.sleep(3)

    # Identifying the xpath for sign-in button
    secondLevelMenu = driver.find_element_by_xpath(
        '//*[@id="nav-flyout-ya-signin"]/a/span'
    )

    # Performing click operation on sign-in button
    secondLevelMenu.click()
    time.sleep(3)

    # Identifying the xpath of email box to provide email
    signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')

    # Providing user email
    signinelement.send_keys(credentials.USERNAME)
    # logger.info("providing user email id")

    # Performing click operation on continue button
    cont = driver.find_element_by_xpath('//*[@id="continue"]')
    cont.click()
    time.sleep(3)

    # Identifying the xpath of password box to provide password
    password_element = driver.find_element_by_xpath('//*[@id="ap_password"]')

    # Providing user password
    password_element.send_keys(credentials.PASSWORD)
    # logger.info("providing user password")
    time.sleep(3)

    # Performing click operation on submit button
    login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
    # logger.info("clicking on submit button")
    login.click()
    # logger.info(" Successfully logged In")
    time.sleep(15)
    # Navigating and
    search = driver.find_element_by_xpath('//*[@id="nav-hamburger-menu"]/span')
    search.click()
    time.sleep(5)
    search_bar = driver.find_element_by_xpath(
        '// *[ @ id = "hmenu-content"] / ul[1] / li[17] / a'
    )
    search_bar.click()
    time.sleep(10)
    tshirts = driver.find_element_by_xpath('//*[@id="hmenu-content"]/ul[10]/li[4]/a')
    tshirts.click()
    time.sleep(10)
    polo = driver.find_element_by_xpath(
        '//*[@id="a-page"]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/ul/li[2]/span/div/a/div[2]/div[2]/span'
    )
    polo.click()
    time.sleep(5)
    size_of_item = driver.find_element_by_xpath('//*[@id="native_size_name_2"]')
    size_of_item.click()
    time.sleep(2)
    quantity_of_item = driver.find_element_by_xpath('//*[@id="quantity"]/option[2]')
    quantity_of_item.click()
    time.sleep(5)
    cart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
    cart.click()
    time.sleep(5)
    cart_msg = driver.find_element_by_xpath(
        '//*[@id="huc-v2-order-row-confirm-text"]/h1'
    )
    cart_msg_color = cart_msg.value_of_css_property("color")
    assert cart_msg_color == "rgba(9, 151, 0, 1)"
    cart_success_msg = list(cart_msg.get_attribute("innerHTML"))[:23]
    cart_success_msg = (("".join(cart_success_msg)).lstrip()).rstrip()
    assert cart_success_msg == "Added to Cart"
    time.sleep(5)
    driver.close()
    proceed_to_buy = driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]')
    proceed_to_buy.click()
    time.sleep(5)
    delivery_address = driver.find_element_by_xpath(
        '//*[@id="address-book-entry-0"]/div[2]/span/a'
    )
    delivery_address.click()
    time.sleep(5)
    deliver_speed = driver.find_element_by_xpath(
        '//*[@id="order_0_ShippingSpeed_exp-in-nominated-day"]'
    )
    deliver_speed.click()
    time.sleep(5)
    continue_payment = driver.find_element_by_xpath(
        '//*[@id="shippingOptionFormId"]/div[1]/div[2]/div/span[1]/span/input'
    )
    continue_payment.click()
    time.sleep(5)
    payment_page = driver.find_element_by_xpath(
        '//*[@id="checkoutDisplayPage"]/div/div[2]/div[1]/h1'
    )
    payment_msg_obtained = list(payment_page.get_attribute("innerHTML"))[:23]
    payment_msg_obtained = "".join(payment_msg_obtained)
    assert payment_msg_obtained == "Select a payment method"


def test_verifying_wishlist():
    # creating a driver object
    driver = webdriver.Chrome()

    # creating action chain object
    action = ActionChains(driver)
    time.sleep(1)

    #  Fetching amazon website url for testing
    driver.get("http://www.amazon.in")
    time.sleep(3)
    search = driver.find_element_by_xpath('//*[@id="nav-hamburger-menu"]/span')
    search.click()
    time.sleep(5)
    search_bar = driver.find_element_by_xpath(
        '// *[ @ id = "hmenu-content"] / ul[1] / li[17] / a'
    )
    search_bar.click()
    time.sleep(10)
    tshirts = driver.find_element_by_xpath('//*[@id="hmenu-content"]/ul[10]/li[4]/a')
    tshirts.click()
    time.sleep(10)
    polo = driver.find_element_by_xpath(
        '//*[@id="a-page"]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/ul/li[2]/span/div/a/div[2]/div[2]/span'
    )
    polo.click()
    time.sleep(5)
    wish_list = driver.find_element_by_xpath('//*[@id="wishListMainButton"]/span/a')
    wish_list.click()
    time.sleep(5)
    wish_list_error_message = driver.find_element_by_xpath('//*[@id="authportal-main-section"]/div[2]/div/div['
                                                           '1]/form/div/div/div/h1')
    wish_list_error_message = list(wish_list_error_message.get_attribute("innerHTML"))[:23]
    wish_list_error_message = (("".join(wish_list_error_message)).lstrip()).rstrip()
    assert wish_list_error_message == "Sign-In"
    time.sleep(5)
    # Identifying the xpath of email box to provide email
    signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')

    # Providing user email
    signinelement.send_keys(credentials.USERNAME)
    # logger.info("providing user email id")

    # Performing click operation on continue button
    cont = driver.find_element_by_xpath('//*[@id="continue"]')
    cont.click()
    time.sleep(3)

    # Identifying the xpath of password box to provide password
    password_element = driver.find_element_by_xpath('//*[@id="ap_password"]')

    # Providing user password
    password_element.send_keys(credentials.PASSWORD)
    # logger.info("providing user password")
    time.sleep(3)

    # Performing click operation on submit button
    login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
    # logger.info("clicking on submit button")
    login.click()
    time.sleep(15)

    wish_list = driver.find_element_by_xpath('// *[ @ id = "add-to-wishlist-button-submit"]')
    wish_list.click()
    time.sleep(5)
    wish_list_success_msg = driver.find_element_by_xpath('//*[@id="WLHUC_result_listName"]/a')
    wish_list_success_msg = list(wish_list_success_msg.get_attribute('innerHTML'))[:]
    wish_list_success_msg = "".join(wish_list_success_msg)
    test_msg = "item added to Shopping List"
    assert test_msg == f"item added to {wish_list_success_msg}"

# logger.info("starting the execution of invalid mail function")
def test_shopping_cart_summary_page():
    driver = webdriver.Chrome()

    # creating action chain object
    action = ActionChains(driver)
    time.sleep(1)

    #  Fetching amazon website url for testing
    # logger.info(" fetching amazon website")
    driver.get("http://www.amazon.in")
    time.sleep(3)

    # logger.info("navigating for sig-in page")
    # Assigning the xpath of account-list in amazon
    firstLevelMenu = driver.find_element_by_xpath(
        '//*[@id="nav-link-accountList"]/span'
    )

    # Moving the cursor towards account-list
    action.move_to_element(firstLevelMenu).perform()
    time.sleep(3)

    # Identifying the xpath for sign-in button
    secondLevelMenu = driver.find_element_by_xpath(
        '//*[@id="nav-flyout-ya-signin"]/a/span'
    )

    # Performing click operation on sign-in button
    secondLevelMenu.click()
    time.sleep(3)

    # Identifying the xpath of email box to provide email
    signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')

    # Providing user email
    signinelement.send_keys(credentials.USERNAME)
    # logger.info("providing user email id")

    # Performing click operation on continue button
    cont = driver.find_element_by_xpath('//*[@id="continue"]')
    cont.click()
    time.sleep(3)

    # Identifying the xpath of password box to provide password
    passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')

    # Providing user password
    passwordelement.send_keys(credentials.PASSWORD)
    # logger.info("providing user password")
    time.sleep(3)

    # Performing click operation on submit button
    login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
    # logger.info("clicking on submit button")
    login.click()
    # logger.info(" Successfuly logged In")
    time.sleep(15)
    search = driver.find_element_by_xpath('//*[@id="nav-hamburger-menu"]/span')
    search.click()
    time.sleep(5)
    search_bar = driver.find_element_by_xpath(
        '// *[ @ id = "hmenu-content"] / ul[1] / li[17] / a'
    )
    search_bar.click()
    time.sleep(10)
    tshirts = driver.find_element_by_xpath('//*[@id="hmenu-content"]/ul[10]/li[4]/a')
    tshirts.click()
    time.sleep(10)
    polo = driver.find_element_by_xpath(
        '//*[@id="a-page"]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/ul/li[2]/span/div/a/div[2]/div[2]/span'
    )
    polo.click()
    time.sleep(5)
    size_of_item = driver.find_element_by_xpath('//*[@id="native_size_name_2"]')
    size_of_item.click()
    time.sleep(10)

    cart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
    cart.click()
    time.sleep(10)
    item_price = driver.find_element_by_xpath('//*[@id="hlb-subcart"]/div[1]/span/span[2]')
    item_price = list(item_price.get_attribute("innerHTML"))[1:]
    item_price = (int(float("".join(item_price)))) * 2
    cart_change_quantity = driver.find_element_by_xpath('//*[@id="hlb-view-cart-announce"]')
    cart_change_quantity.click()
    time.sleep(5)
    click_to_change = driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]')
    click_to_change.click()
    time.sleep(5)
    click_to_change = driver.find_element_by_xpath('//*[@id="a-popover-2"]/div/div/ul/li[3]')
    click_to_change.click()
    time.sleep(5)

    changed_price = driver.find_element_by_xpath('//*[@id="sc-subtotal-amount-activecart"]/span')
    changed_price = list(changed_price.get_attribute("innerHTML"))[:]
    changed_price = int(float(("".join(changed_price[45:])).replace(",", "")))
    assert item_price == changed_price




    # proceed_to_buy = driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]')
    # proceed_to_buy.click()
    # time.sleep(5)
    # delivery_address = driver.find_element_by_xpath(
    #     '//*[@id="address-book-entry-0"]/div[2]/span/a'
    # )
    # delivery_address.click()
    # time.sleep(5)
    # deliver_speed = driver.find_element_by_xpath(
    #     '//*[@id="order_0_ShippingSpeed_exp-in-nominated-day"]'
    # )
    # deliver_speed.click()
    # time.sleep(5)
    # change_quantities = driver.find_element_by_xpath(
    #     '//*[@id="shippingOptionFormId"]/div[2]/div/div[1]/div/div/a'
    # )
    # change_quantities.click()
    # time.sleep(5)
    # quantity_of_item = driver.find_element_by_xpath(
    #     '//*[@id="changeQuantityFormId"]/div[4]/div[3]/div/div['
    #     "1]/span/span/span/span"
    # )
    # quantity_of_item.click()
    # time.sleep(5)
    # changing_quantity = driver.find_element_by_xpath(
    #     '//*[@id="1_dropdown_combobox"]/li[2]/a'
    # )
    # changing_quantity.click()
    # time.sleep(5)
    # retrieve_change_quantity=driver.find_element_by_xpath('//*[@id="changeQuantityFormId"]/div[4]/div[3]/div/div['
    #                                                       '1]/span/span/span/span/span')
    # retrieve_change_quantity=str(retrieve_change_quantity.get_attribute("innerHTML"))
    # retrieve_change_quantity=int(retrieve_change_quantity)
    # print(retrieve_change_quantity*item_price)
    # time.sleep(5)
    # continue_payment = driver.find_element_by_xpath(
    #     '//*[@id="changeQuantityFormId"]/div[6]/div/div/span/span/input'
    # )
    # continue_payment.click()
    # time.sleep(10)
    # providing_cvv=driver.find_element_by_xpath('//*[@id="pp-f4Jbnj-121"]')
    # providing_cvv.send_keys(123)
    # time.sleep(3)
    # final_payment=driver.find_element_by_xpath('//*[@id="pp-f4Jbnj-162"]/span/input')
    # final_payment.click()
    # time.sleep(5)
    #


def test_search_product_function():
    # creating a driver object
    driver = webdriver.Chrome()

    # creating action chain object
    action = ActionChains(driver)
    time.sleep(1)
    driver.get("http://www.amazon.in")
    time.sleep(3)
    search = driver.find_element_by_xpath('//*[@id="nav-hamburger-menu"]/span')
    search.click()
    time.sleep(5)
    search_bar = driver.find_element_by_xpath(
        '// *[ @ id = "hmenu-content"] / ul[1] / li[17] / a'
    )
    search_bar.click()
    time.sleep(2)
    shirts = driver.find_element_by_xpath('//*[@id="hmenu-content"]/ul[10]/li[5]/a')
    shirts.click()
    time.sleep(10)
    item = driver.find_element_by_xpath('//*[@id="a-page"]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/ul/li['
                                        '1]/span/div/a/div[2]/div[2]/span')
    item_name = list(item.get_attribute('innerHTML'))[:]
    item_name = ("".join(item_name).lstrip()).rstrip()
    back_to_menu = driver.find_element_by_xpath('//*[@id="nav-logo-sprites"]')
    back_to_menu.click()
    time.sleep(5)
    search_bar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
    search_bar.send_keys(item_name)
    time.sleep(5)
    search_bar_input_submit = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
    search_bar_input_submit.click()
    time.sleep(5)
    obtained_product_name = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div['
                                                         '3]/div/span/div/div/div/div/div[3]/div[2]/h2/a')
    obtained_product_name.click()
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    obtained_product_name = driver.find_element_by_xpath('//*[@id="productTitle"]')
    obtained_product_name = list(obtained_product_name.get_attribute("innerHTML"))[:]
    obtained_product_name = ("".join(obtained_product_name).lstrip()).rstrip()
    assert obtained_product_name == item_name
