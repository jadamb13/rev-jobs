from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
from config.config import get_config
import random


def apply_filters(driver):
    config = get_config()

    # Open "More" menu to select filters
    driver.find_element(By.XPATH, config['more_button_xpath']).click()

    # De-select "Verbatim" to remove verbatim category jobs
    driver.find_element(By.XPATH, config['verbatim_checkbox_xpath']).click()


def collect_times(driver):
    config = get_config()

    # Wait for notification pop-up
    sleep(random.randint(10, 14))  # Will not find element without waiting

    # Click "No, thanks" on notification pop up (if showing)
    try:
        driver.find_element(By.XPATH, config['notifications_popup_xpath']).click()
    except NoSuchElementException:
        print("News and Updates pop-up element not found. XPATH might be incorrect or doesn't exist.")

    # Collects time length of all jobs available
    times = []
    all_time_divs = driver.find_elements(By.XPATH, config['time_divs_xpath'])
    for time_div in all_time_divs:
        times.append(str(time_div.text))
    return times


def collect_job_data(driver):
    config = get_config()
    times = collect_times(driver)
    job_data = {}

    # Total jobs and total line jobs
    number_of_jobs = driver.find_element(By.XPATH, config['number_of_jobs_xpath']).text
    number_of_line_jobs = driver.find_element(By.XPATH, config['number_of_line_jobs_xpath']).text

    # Format total jobs
    number_of_jobs = number_of_jobs.replace("(", "").replace(")", "")
    number_of_line_jobs = number_of_line_jobs.replace("(", "").replace(")", "")

    # Jobs under ten and five minutes
    under_ten_count = str(sum(1 for t in times if int(t[:2]) < 10))
    under_five_count = str(sum(1 for t in times if int(t[:2]) < 5))

    # Audio and video jobs
    media_types = {}  # Dict to store future media types and counts
    number_of_audio_jobs = len(driver.find_elements(By.XPATH, config['audio_divs_xpath']))
    number_of_video_jobs = len(driver.find_elements(By.XPATH, config['video_divs_xpath']))

    # Find jobs that have been unclaimed <= 2 times
    unclaim_divs = driver.find_elements(By.XPATH, config['unclaim_divs_xpath'])
    unclaims = [int(div.text) for div in unclaim_divs]

    # Count of jobs with zero, one, and two unclaims
    zero_unclaim_count = str(unclaims.count(0))
    one_unclaim_count = str(unclaims.count(1))
    two_unclaim_count = str(unclaims.count(2))
    number_of_jobs_with_less_than_two_unclaims = int(one_unclaim_count) + int(two_unclaim_count) + int(zero_unclaim_count)

    # Store job data in dict
    job_data['under_ten_count'] = under_ten_count
    job_data['under_five_count'] = under_five_count
    job_data['audio_jobs'] = number_of_audio_jobs
    job_data['video_jobs'] = number_of_video_jobs
    job_data['zero_unclaim_count'] = zero_unclaim_count
    job_data['one_unclaim_count'] = one_unclaim_count
    job_data['two_unclaim_count'] = two_unclaim_count
    job_data['number_of_jobs_with_less_than_two_unclaims'] = number_of_jobs_with_less_than_two_unclaims
    job_data['number_of_jobs'] = number_of_jobs
    job_data['number_of_line_jobs'] = number_of_line_jobs

    return job_data





