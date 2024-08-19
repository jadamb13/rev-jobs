from selenium.webdriver.common.by import By
from config.config import get_config


def apply_filters(driver):
    config = get_config()

    # Open "More" menu to select filters
    driver.find_element(By.XPATH, config['more_button_xpath']).click()

    # De-select "Verbatim" to remove verbatim category jobs
    driver.find_element(By.XPATH, config['verbatim_checkbox_xpath']).click()


def collect_job_lengths(driver):
    config = get_config()

    # Collects time length of all jobs available
    job_lengths = []
    all_time_divs = driver.find_elements(By.XPATH, config['time_divs_xpath'])
    for time_div in all_time_divs:
        job_lengths.append(str(time_div.text))
    return job_lengths


def collect_job_data(driver):
    config = get_config()

    # Total jobs, total line jobs, and total non-verbatim/rush jobs
    number_of_jobs = driver.find_element(By.XPATH, config['number_of_jobs_xpath']).text
    number_of_line_jobs = driver.find_element(By.XPATH, config['number_of_line_jobs_xpath']).text
    number_of_non_verbatim_or_rush_jobs = driver.find_element(By.XPATH, config['number_of_non_verbatim_or_rush_jobs_xpath'])

    # Format total jobs, line jobs, and non-verbatim/rush jobs
    number_of_jobs = number_of_jobs.replace("(", "").replace(")", "")
    number_of_line_jobs = number_of_line_jobs.replace("(", "").replace(")", "")
    number_of_non_verbatim_or_rush_jobs = number_of_non_verbatim_or_rush_jobs.replace("(", "").replace(")", "")

    # Jobs under ten and five minutes
    job_lengths = collect_job_lengths(driver)
    jobs_under_ten_minutes = str(sum(1 for t in job_lengths if int(t[:2]) < 10))
    jobs_under_five_minutes = str(sum(1 for t in job_lengths if int(t[:2]) < 5))

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
    job_data = {
        'under_ten_count': jobs_under_ten_minutes, 'under_five_count': jobs_under_five_minutes,
        'audio_jobs': number_of_audio_jobs, 'video_jobs': number_of_video_jobs,
        'zero_unclaim_count': zero_unclaim_count, 'one_unclaim_count': one_unclaim_count,
        'two_unclaim_count': two_unclaim_count,
        'number_of_jobs_with_less_than_two_unclaims': number_of_jobs_with_less_than_two_unclaims,
        'number_of_jobs': number_of_jobs, 'number_of_line_jobs': number_of_line_jobs,
        'non_verbatim_or_rush_jobs': number_of_non_verbatim_or_rush_jobs,
    }

    return job_data





