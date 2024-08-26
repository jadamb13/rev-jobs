from src.driver_setup import setup_driver, teardown_driver
from src.auth import login
from src.data_retrieval import apply_filters, collect_job_data
from src.notification import send_notification
from src.output import update_job_data_files, save_prev_week_job_data, erase_weekly_job_data_file, first_run_of_week
from src.create_graphs import create_scatter_plot

def main():

    driver = setup_driver()

    try:

        # Save last week's job data, max jobs plot, and reset weekly job data txt file
        if first_run_of_week():
            save_prev_week_job_data()
            erase_weekly_job_data_file()

        login(driver)
        apply_filters(driver)
        data = collect_job_data(driver)
        update_job_data_files(data)
        create_scatter_plot()

        '''
        # Send notifications

        # if int(number_of_jobs) > 10:
        send_notification(
            "Available Job Information",
            f"Total jobs: {data['number_of_jobs']} | Line jobs: {data['number_of_line_jobs']} \n"
            f"0 unclaims: {data['zero_unclaim_count']} | 0-2 unclaims: {data['number_of_jobs_with_less_than_two_unclaims']} \n"
            f"10 minutes or less: {data['under_ten_count']} | 5 minutes or less: {data['under_five_count']} \n"
        )
        '''

    finally:
        teardown_driver(driver)


if __name__ == "__main__":
    main()
