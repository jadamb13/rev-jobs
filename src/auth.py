from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config.config import get_config
from time import sleep
import random
import sys


def random_sleep(min_time=1, max_time=5):
    sleep(random.randint(min_time, max_time))


def login(driver):

    config = get_config()

    # Log in #
    driver.get(config['url'])
    random_sleep()
    driver.find_element(By.XPATH, config['login_button_xpath']).click()
    driver.find_element(By.XPATH, config['username_xpath']).send_keys(config['username'])
    random_sleep()
    driver.find_element(By.XPATH, config['next_button_xpath']).click()

    # WebDriverWait line found at: https://stackoverflow.com/questions/56085152/selenium-python-error-element-could
    # -not-be-scrolled-into-view to solve issue of element not being scrolled into view
    WebDriverWait(driver, 30).until(
        ec.element_to_be_clickable((By.XPATH, config['password_xpath']))).send_keys(config['password'])
    random_sleep()
    driver.find_element(By.XPATH, config['sign_in_xpath']).click()
    random_sleep(3, 6)

    # Check for 2FA div
    try:
        driver.find_element(By.XPATH, config['two_factor_xpath'])
        print("Two-factor required.")
        sleep(30)
        #sys.exit(1)
    except NoSuchElementException:
        print("No two-factor authentication div found.")

    # Wait for notification pop-up
    random_sleep(4, 8)  # Will not find element without waiting

    # Click "No, thanks" on notification pop up (if showing)
    try:
        driver.find_element(By.XPATH, config['notifications_popup_xpath']).click()
    except NoSuchElementException:
        print("News and Updates pop-up element not found. XPATH might be incorrect or doesn't exist.")