from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
from config.config import get_config
import random


def apply_filters(driver):
    config = get_config()
    driver.find_element(By.XPATH, config['more_button_xpath']).click()
    driver.find_element(By.XPATH, config['verbatim_checkbox_xpath']).click()


def collect_times(driver):
    config = get_config()

    # Wait for notification pop-up
    sleep(random.randint(10, 14))  # Will not find element without waiting

    # Click "No, thanks" on notification pop up
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

    number_of_jobs = driver.find_element(By.XPATH, config['number_of_jobs_xpath']).text
    number_of_line_jobs = driver.find_element(By.XPATH, config['number_of_line_jobs_xpath']).text
    under_ten_count = sum(1 for t in times if int(t[:2]) < 10)
    under_five_count = sum(1 for t in times if int(t[:2]) < 5)

    job_data['under_ten_count'] = under_ten_count
    job_data['under_five_count'] = under_five_count

    # Retrieves number of audio and video jobs available
    media_types = []
    all_audio_divs = driver.find_elements(By.XPATH, config['audio_divs_xpath'])
    all_video_divs = driver.find_elements(By.XPATH, config['video_divs_xpath'])
    audio_jobs = len(all_audio_divs)
    video_jobs = len(all_video_divs)
    job_data['audio_jobs'] = audio_jobs
    job_data['video_jobs'] = video_jobs

    # Retrieves number of unclaims per job
    unclaim_divs = driver.find_elements(By.XPATH, config['unclaim_divs_xpath'])
    unclaims = [int(div.text) for div in unclaim_divs]

    zero_unclaim_count = unclaims.count(0)
    one_unclaim_count = unclaims.count(1)
    two_unclaim_count = unclaims.count(2)
    job_data['zero_unclaim_count'] = zero_unclaim_count
    job_data['one_unclaim_count'] = one_unclaim_count
    job_data['two_unclaim_count'] = two_unclaim_count

    # Format data
    number_of_jobs = number_of_jobs.replace("(", "").replace(")", "")
    number_of_line_jobs = number_of_line_jobs.replace("(", "").replace(")", "")
    job_data['number_of_jobs'] = number_of_jobs
    job_data['number_of_line_jobs'] = number_of_line_jobs

    return job_data


def save_data_to_file(driver):
    config = get_config()
    data = collect_job_data(driver)
    # Save information to file #
    time_and_date = datetime.now()
    string_time_and_date = time_and_date.strftime("%A %m/%d %I:%M %p")
    hour_of_time_now = time_and_date.strftime("%I")

    with open(config['data_file_path'], "a+") as source_file:
        source_file.write(string_time_and_date + " " + data['number_of_jobs'] + " " + data['number_of_line_jobs'] + "\n")


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
