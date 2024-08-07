import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        'url': 'https://www.rev.com/workspace/findwork',
        'username': os.getenv('REV_USERNAME'),
        'password': os.getenv('REV_PASSWORD'),
        'gecko_driver_path': os.getenv('GECKO_DRIVER_PATH', '/usr/local/bin/geckodriver'),
        'data_file_path': os.getenv('DATA_FILE_PATH', '../output/job_data.txt'),
        'username_xpath': '//*[@id="email-input"]',
        'next_button_xpath': '//*[@id="submit-button"]',
        'password_xpath': '//*[@id="password-input"]',
        'sign_in_xpath': '//*[@id="submit-button"]',
        'notifications_popup_xpath': '//*[@id="pushActionRefuse"]',
        'number_of_jobs_xpath': '/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div[1]/div/span[1]/a[1]/span[2]',
        'number_of_line_jobs_xpath': '/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div[1]/div/span[1]/a[3]/span[2]',
        'more_button_xpath': '/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div/div[1]/div[5]/div/div/div/i',
        'verbatim_checkbox_xpath': '/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/label/input',
        'time_divs_xpath': "//div[@class='length-text']",
        'audio_divs_xpath': "//span[@class='media-type-icon audio']",
        'video_divs_xpath': "//span[@class='media-type-icon video']",
        'unclaim_divs_xpath': "//span[@class='unclaim-count']"
    }
