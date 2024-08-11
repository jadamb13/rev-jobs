from driver_setup import setup_driver, teardown_driver
from auth import login
from data_retrieval import apply_filters, collect_job_data
from notification import send_notification
from output.output import save_data_to_file


def main():

    driver = setup_driver()

    try:
        login(driver)
        apply_filters(driver)
        data = collect_job_data(driver)
        save_data_to_file(data)

        # Send notifications

        # if int(number_of_jobs) > 10:
        send_notification("Rev Jobs Available",
                          f"There are {data['number_of_jobs']} total jobs,"
                          f" and {data['number_of_line_jobs']} line jobs currently available.")
        send_notification("Job Details",
                          f"Jobs with 0 unclaims: {data['zero_unclaim_count']} | "
                          f"Jobs with 1-2 unclaims: {data['number_of_jobs_with_less_than_two_unclaims']}")

        # if under_ten_count > 5 or under_five_count > 2:
        send_notification("Job Times",
                          f"There are {data['under_ten_count']} jobs under 10 minutes "
                          f"and {data['under_five_count']} jobs under 5 minutes.")

    finally:
        teardown_driver(driver)


if __name__ == "__main__":
    main()
