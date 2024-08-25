from config.config import get_config
from datetime import datetime
import os
import shutil


config = get_config()


def first_run_of_week():
    first_run = False

    with open(config['weekly_data_filepath']) as f:
        for line in f:
            pass
        last_line = line

    if last_line.split(' ')[0] == 'Sunday' and datetime.now().strftime('%A') == 'Monday':
        first_run = True
        print("It's the first run on Monday. The weekly data file has been reset.")
    else:
        print("It's not the first run on Monday. The weekly data file has not been reset.")

    return first_run


def update_all_job_data(data):

    # Format and save data
    time_and_date = datetime.now().strftime("%A %m/%d %I:%M %p")
    with open(config['all_job_data_filepath'], "a+") as source_file:
        source_file.write(f"{time_and_date} {data['number_of_jobs']} {data['number_of_line_jobs']}\n")


def save_weekly_job_data():

    date = datetime.now()
    today = date.today()
    date_today = today.strftime("%b-%d-%Y")
    current_month = date.strftime("%B")
    current_year = date.strftime("%Y")

    # Copy current rev.py information to file in last week's job data folder
    current_weekly_data_file = config['weekly_data_filepath']
    destination_directory = os.path.join(config['historical_report_directory'], current_year, current_month, date_today)

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    previous_week_data_filepath = os.path.join(destination_directory, 'prev_week_job_data.txt')

    with open(previous_week_data_filepath, 'w'):
        shutil.copyfile(current_weekly_data_file, previous_week_data_filepath)


def erase_weekly_job_data_file():

    # Erase contents of rev.py file to start blank for new week
    with open(config['weekly_data_filepath'], 'r+') as f:
        f.truncate(0)

# def save_weekly_max_jobs_graph():
