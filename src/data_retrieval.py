from selenium import webdriver
from selenium.common import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
# import lxml
from datetime import datetime
# import io
# import os
# import pathlib
from time import sleep
# from win10toast import ToastNotifier
from config.config import get_config
import random


def check_for_jobs():
    config = get_config()

    # Set up web driver #
    options = Options()
    options.headless = False
    options.set_preference("profile", str(config['firefox_profile_path']))
    s = Service(config['gecko_driver_path'])
    driver = webdriver.Firefox(service=s, options=options)
    driver.get(config['url'])

    # Log in #
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

    # Retrieve 2FA code from email
    try:
        driver.find_element(By.XPATH, config['two_factor_xpath'])
    except NoSuchElementException:
        print("No two-factor authentication div found.")

    sleep(random.randint(10, 14))  # Will not find element without waiting

    # Click "No, thanks" on notification pop up
    try:
        driver.find_element(By.XPATH, config['notifications_popup_xpath']).click()
    except NoSuchElementException:
        print("News and Updates pop-up element not found. XPATH might be incorrect or doesn't exist.")

    number_of_jobs = driver.find_element(By.XPATH, config['number_of_jobs_xpath']).text
    number_of_line_jobs = driver.find_element(By.XPATH, config['number_of_line_jobs_xpath']).text

    # Set filter to ignore Verbatim jobs
    driver.find_element(By.XPATH, config['more_button_xpath']).click()
    driver.find_element(By.XPATH, config['verbatim_checkbox_xpath']).click()

    # Collects time length of all jobs available
    times = []

    try:
        all_time_divs = driver.find_elements(By.XPATH, config['time_divs_xpath'])
        for div in all_time_divs:
            times.append(str(div.text))

        under_ten_count = 0
        under_five_count = 0
        for time in times:
            if int(time[:2]) < 10:
                under_ten_count += 1
            if int(time[:2]) < 5:
                under_five_count += 1

        # Retrieves number of audio and video jobs available
        media_types = []
        all_audio_divs = driver.find_elements(By.XPATH, config['audio_divs_xpath'])
        all_video_divs = driver.find_elements(By.XPATH, config['video_divs_xpath'])
        audio_jobs = len(all_audio_divs)
        video_jobs = len(all_video_divs)

        # Retrieves number of unclaims per job
        unclaim_divs = driver.find_elements(By.XPATH, config['unclaim_divs_xpath'])
        unclaims = []
        zero_unclaim_count = 0
        one_unclaim_count = 0
        two_unclaim_count = 0
        for div in unclaim_divs:
            unclaims.append(int(div.text))
        for unclaim in unclaims:
            if unclaim == 0:
                zero_unclaim_count += 1
            if unclaim == 1:
                one_unclaim_count += 1
            if unclaim == 2:
                two_unclaim_count += 1

        number_of_jobs_with_one_or_two_unclaims = one_unclaim_count + two_unclaim_count
        if (len(unclaims)) > 0:
            percentage_of_jobs_with_under_two_unclaims = (number_of_jobs_with_one_or_two_unclaims / len(unclaims))
        else:
            percentage_of_jobs_with_under_two_unclaims = 0.0
    except NoSuchElementException:
        print("Time div elements not found. XPATH might be incorrect or doesn't exist.")
    driver.close()

    # Format data
    number_of_jobs = number_of_jobs.replace("(", "").replace(")", "")
    number_of_line_jobs = number_of_line_jobs.replace("(", "").replace(")", "")

    # Save information to file #
    time_and_date = datetime.now()
    string_time_and_date = time_and_date.strftime("%A %m/%d %I:%M %p")
    hour_of_time_now = time_and_date.strftime("%I")

    with open(config['data_file_path'], "a+") as source_file:
        source_file.write(string_time_and_date + " " + number_of_jobs + " " + number_of_line_jobs + "\n")


'''
### Send notifications to desktop (Windows 10)

# Sends first notification with number of total jobs and line jobs
# Customized to send if greater than X number of total jobs


toast = ToastNotifier()

if (int(number_of_jobs) > 10):
    toast.show_toast("Rev Jobs Available", "There are " + number_of_jobs + " total jobs, and " + number_of_line_jobs + " line jobs currently available.")
    toast.show_toast("Jobs with 0 unclaims: " + str(zero_unclaim_count) + "/" + str(len(unclaims)) + " | Jobs with 1-2 unclaims: " + str(number_of_jobs_with_one_or_two_unclaims) + "/" + str(len(unclaims)) +"(" + str(percentage_of_jobs_with_under_two_unclaims * 100) + "%)")


# Send second notification with number of jobs under 5 and 10 minutes
if (under_ten_count > 5 or under_five_count > 2):
    toast.show_toast("There are " + str(under_ten_count) + " jobs under 10 minutes and " + str(under_five_count) + " jobs under 5 minutes.")


'''
