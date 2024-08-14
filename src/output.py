from config.config import get_config
from datetime import datetime


def save_data_to_file(data):
    config = get_config()

    # Format and save data
    time_and_date = datetime.now().strftime("%A %m/%d %I:%M %p")
    with open(config['data_file_path'], "a+") as source_file:
        source_file.write(f"{time_and_date} {data['number_of_jobs']} {data['number_of_line_jobs']}\n")
