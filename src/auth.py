from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config.config import get_config
from time import sleep
import random


def login(driver):

    config = get_config()

    # Log in #
    driver.get(config['url'])
    sleep(random.randint(1, 5))
    driver.find_element(By.XPATH, config['login_button_xpath']).click()
    driver.find_element(By.XPATH, config['username_xpath']).send_keys(config['username'])
    sleep(random.randint(1, 5))
    driver.find_element(By.XPATH, config['next_button_xpath']).click()

    # WebDriverWait line found at: https://stackoverflow.com/questions/56085152/selenium-python-error-element-could
    # -not-be-scrolled-into-view to solve issue of element not being scrolled into view
    WebDriverWait(driver, random.randint(950000, 1000000)).until(
        ec.element_to_be_clickable((By.XPATH, config['password_xpath']))).send_keys(config['password'])
    sleep(random.randint(1, 5))
    driver.find_element(By.XPATH, config['sign_in_xpath']).click()
    sleep(random.randint(30, 45))

    # Check for 2FA div
    try:
        driver.find_element(By.XPATH, config['two_factor_xpath'])
    except NoSuchElementException:
        print("No two-factor authentication div found.")

    # Wait for notification pop-up
    sleep(random.randint(10, 14))  # Will not find element without waiting

    # Click "No, thanks" on notification pop up (if showing)
    try:
        driver.find_element(By.XPATH, config['notifications_popup_xpath']).click()
    except NoSuchElementException:
        print("News and Updates pop-up element not found. XPATH might be incorrect or doesn't exist.")