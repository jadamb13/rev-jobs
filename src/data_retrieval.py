from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config.config import get_config

config = get_config()


def apply_filters(driver):

    print("Applying filters...")
    try:
        # Select only non-verbatim/rush jobs
        WebDriverWait(driver, 30).until(
            ec.element_to_be_clickable(
                (By.XPATH, config['no_verbatim_or_rush_button_xpath'])
            )
        ).click()
    except TimeoutException:
        print("Timed out waiting for No Verbatim, No Rush filter to be clickable.")

    # Open "More" menu to select filters
    # driver.find_element(By.XPATH, config['more_button_xpath']).click()

    # De-select "Verbatim" from "More" menu to remove verbatim category jobs only
    # driver.find_element(By.XPATH, config['verbatim_checkbox_xpath']).click()


def collect_job_lengths(driver):

    # Collects time length of all jobs available
    job_lengths = []
    all_time_divs = driver.find_elements(By.XPATH, config['time_divs_xpath'])
    for time_div in all_time_divs:
        job_lengths.append(str(time_div.text))
    return job_lengths


def collect_job_data(driver):

    job_data = {}

    # Total jobs, total line jobs, and total non-verbatim/rush jobs
    job_data['number_of_jobs'] = driver.find_element(
        By.XPATH, config['number_of_jobs_xpath']).text.replace("(", "").replace(")", "")
    job_data['number_of_line_jobs'] = driver.find_element(
        By.XPATH, config['number_of_line_jobs_xpath']).text.replace("(", "").replace(")", "")
    job_data['number_of_non_verbatim_or_rush_jobs'] = driver.find_element(
        By.XPATH, config['no_verbatim_or_rush_jobs_number']).text.replace("(", "").replace(")", "")

    # Jobs under ten and five minutes
    job_lengths = collect_job_lengths(driver)
    job_data['under_ten_count'] = str(sum(1 for t in job_lengths if int(t[:2]) < 10))
    job_data['under_five_count'] = str(sum(1 for t in job_lengths if int(t[:2]) < 5))

    # Audio and video jobs
    media_types = {}  # Dict to store future media types and counts
    job_data['audio_jobs'] = len(driver.find_elements(By.XPATH, config['audio_divs_xpath']))
    job_data['video_jobs'] = len(driver.find_elements(By.XPATH, config['video_divs_xpath']))

    # Find jobs that have been unclaimed <= 2 times
    unclaim_divs = driver.find_elements(By.XPATH, config['unclaim_divs_xpath'])
    unclaims = [int(div.text) for div in unclaim_divs]

    # Count of jobs with zero, one, and two unclaims
    job_data['zero_unclaim_count'] = str(unclaims.count(0))
    job_data['one_unclaim_count'] = str(unclaims.count(1))
    job_data['two_unclaim_count'] = str(unclaims.count(2))
    job_data['number_of_jobs_with_less_than_two_unclaims'] = (int(job_data['zero_unclaim_count']) +
                                                              int(job_data['one_unclaim_count']) +
                                                              int(job_data['two_unclaim_count'])
                                                              )

    return job_data
