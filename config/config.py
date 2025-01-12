import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


def get_config():
    return {
        # Web Driver
        'url': 'https://www.rev.com',
        'gecko_driver_path': os.getenv('GECKO_DRIVER_PATH'),
        'firefox_profile_path': os.getenv('FIREFOX_DRIVER_PATH'),
        'firefox_binary_path': os.getenv('FIREFOX_BINARY_PATH'),

        # Login
        'login_button_xpath': '//*[@id="navbar-login"]',
        'username': os.getenv('REV_USERNAME'),
        'password': os.getenv('REV_PASSWORD'),
        'username_xpath': '//*[@id="email-input"]',
        'next_button_xpath': '//*[@id="submit-button"]',
        'password_xpath': '//*[@id="password-input"]',
        'sign_in_xpath': '//*[@id="submit-button"]',
        'two_factor_xpath': '//*[@id="mfa-code-input"]',
        'gmail_username': os.getenv('GMAIL_USERNAME'),
        'gmail_password': os.getenv('GMAIL_PASSWORD'),

        # Elements on job dashboard
        'notifications_popup_xpath': '//*[@id="pushActionRefuse"]',
        'no_verbatim_or_rush_jobs_number': '/html/body/div[1]/div/div[2]/div/div/div/div[3]'
                                           '/div/div[1]/div[1]/div/span[1]/span/a/span[2]',
        'no_verbatim_or_rush_button_xpath': '/html/body/div[1]/div/div[2]/div/div/div/div[3]'
                                            '/div/div[1]/div[1]/div/span[1]/span/a',
        'number_of_jobs_xpath': '/html/body/div[1]/div/div[2]/div/div/div/div[3]'
                                '/div/div[1]/div[1]/div/span[1]/a[1]/span[2]',
        'number_of_line_jobs_xpath': '/html/body/div[1]/div/div[2]/div/div/div'
                                     '/div[3]/div/div[1]/div[1]/div/span[1]/a[3]/span[2]',
        'more_button_xpath': '/html/body/div[1]/div/div[2]/div/div/div/div[3]'
                             '/div/div[1]/div[2]/div/div[1]/div[5]/div/div/div/i',
        'verbatim_checkbox_xpath': '/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/'
                                   'div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/label/input',
        'time_divs_xpath': "//div[@class='length-text']",
        'audio_divs_xpath': "//span[@class='media-type-icon audio']",
        'video_divs_xpath': "//span[@class='media-type-icon video']",
        'unclaim_divs_xpath': "//span[@class='unclaim-count']",

        # Output
        'all_job_data_filepath': os.getenv('ALL_JOB_DATA_FILEPATH'),
        'weekly_data_filepath': os.getenv('WEEKLY_DATA_FILEPATH'),
        'current_report_directory': os.getenv('CURRENT_REPORT_DIRECTORY'),
        'historical_report_directory': os.getenv('HISTORICAL_REPORT_DIRECTORY'),
        'date_info': get_date_info(),
    }


def get_date_info():
    date_info = {}
    date = datetime.now()
    today = date.today()
    date_info['date_today'] = today.strftime("%b-%d-%Y")
    date_info['current_month'] = date.strftime("%B")
    date_info['current_year'] = date.strftime("%Y")
    return date_info
