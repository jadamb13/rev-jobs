from config.config import get_config
from datetime import datetime
import os
import shutil
from src.plots import save_weekly_max_plot

config = get_config()


def get_last_line(file):
    with open(file) as f:
        # Check for empty file
        if f.read(1):
            # Get the last line of the file
            for line in f:
                pass
            last_line = line
    return last_line


def first_run_of_week():

    first_run = False
    last_line = get_last_line(config['weekly_data_filepath'])
    # If the last run was on Sunday, and today is Monday: it's the first run of the week
    if last_line.split(' ')[0] == 'Sunday' and datetime.now().strftime('%A') == 'Monday':
        first_run = True
        print("It's the first run on Monday. The weekly data file will be reset.")

    return first_run


def update_job_data_files(data):

    # Time and date: {Full weekday name} {mm/dd} {12 hour time} {AM/PM}
    time_and_date = datetime.now().strftime("%A %m/%d %I:%M %p")

    with open(config['all_job_data_filepath'], "a+") as all_data_file:
        all_data_file.write(f"{time_and_date} {data['number_of_jobs']} {data['number_of_line_jobs']} "
                            f"{data['number_of_non_verbatim_or_rush_jobs']}\n")
    with open(config['weekly_data_filepath'], "a+") as weekly_data_file:
        weekly_data_file.write(f"{time_and_date} {data['number_of_jobs']} {data['number_of_line_jobs']} "
                               f"{data['number_of_non_verbatim_or_rush_jobs']}\n")
    print("Saved job data to weekly_job_data.txt and all_job_data.txt.")


def save_prev_week_job_data():

    date = config['date_info']

    # Copy weekly_job_data.txt to file in last week's job data folder
    current_weekly_data_file = config['weekly_data_filepath']
    destination_directory = os.path.join(config['historical_report_directory'],
                                         str(date['current_year']), str(date['current_month']), str(date['date_today']))

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Create filepath to store previous week job data
    previous_week_data_filepath = os.path.join(destination_directory, 'prev_week_job_data.txt')

    # Copy information from weekly_job_data.txt to previous_week_job_data.txt
    with open(previous_week_data_filepath, 'w'):
        shutil.copyfile(current_weekly_data_file, previous_week_data_filepath)

    # Save previous week's maximum job plot
    previous_week_max_jobs_plot_filepath = os.path.join(destination_directory, 'prev_week_max_jobs_plot.png')
    save_weekly_max_plot(previous_week_max_jobs_plot_filepath)


def erase_file(file):

    # Erase contents of weekly job data file to start blank for new week
    with open(file, 'r+') as f:
        f.truncate(0)

