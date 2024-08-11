from driver_setup import setup_driver, teardown_driver
from auth import login
from data_retrieval import apply_filters, collect_job_data
from notifications import send_notification
from config.config import get_config
from datetime import datetime


def main():
    config = get_config()
    driver = setup_driver()
    try:
        login(driver)
        apply_filters(driver)
        data = collect_job_data(driver)

        # Format and save data
        time_and_date = datetime.now().strftime("%A %m/%d %I:%M %p")
        with open(config['data_file_path'], "a+") as source_file:
            source_file.write(f"{time_and_date} {data['number_of_jobs']} {data['number_of_line_jobs']}\n")

        '''
        # Send notifications
        if int(number_of_jobs) < 10:
            send_notification("Rev Jobs Available",
                              f"There are {number_of_jobs} total jobs, and {number_of_line_jobs} line jobs currently available.")
            send_notification("Job Details",
                              f"Jobs with 0 unclaims: {zero_unclaim_count}/{len(unclaims)} | Jobs with 1-2 unclaims: {number_of_jobs_with_one_or_two_unclaims}/{len(unclaims)} ({percentage_of_jobs_with_under_two_unclaims * 100}%)")

        if under_ten_count > 5 or under_five_count > 2:
            send_notification("Job Times",
                              f"There are {under_ten_count} jobs under 10 minutes and {under_five_count} jobs under 5 minutes.")
    '''
    finally:
        teardown_driver(driver)


if __name__ == "__main__":
    main()
