>## Automated Transcription Job Notifier
Automates retrieval of transcription job data using Selenium, sends desktop notifications with job information, 
and creates historical reports of job availability using Matplotlib


### Project Overview

>#### Purpose
The purpose of this project is to reduce time spent manually tracking transcription jobs. Job availability 
frequently varies — sometimes unpredictably. As a result, a lot of time can be wasted either staying on the website 
and waiting for jobs to become available, or frequently logging in and applying filters to find preferential jobs. 
Contractors are only paid for completing a job — any additional time spent tracking or selecting tasks is unpaid.

>#### What the program does
The program will run automatically at user-set intervals and track job availability data by logging in, navigating 
to the job dashboard, applying user-set preferences (e.g. no Verbatim jobs; no Rush jobs), and sending a desktop 
notification if there are X or more jobs available (X set by the user). This will prevent the need to log in or 
constantly check if jobs meeting the user's preferences are available. 

The program also saves job information to the `all_job_data.txt` and `weekly_job_data.txt` files located in the `output` directory of the project. 
The data is stored in the format {Day of the week} {Month/Day} {Time in 12h time format} {AM/PM} {Total Jobs} 
{Line Jobs} {Non-Verbatim & Non-Rush Jobs} as shown below:

```
Wednesday 08/07 03:58 PM 23 0 14
```

This data is currently used by `plots.py` to create visualizations of job availability — for the week, and historically 
by day of the week. 

### Project Structure

The project is organized into several directories and a few root-level files: a `.gitignore` file, a `requirements.txt` 
file with program dependencies, `main.py` (entry point of the program), and the current `README.md` file.

>#### Directories and included files

- `config`: 
    - `config.py`: file to store configuration data such as:
      - URL to access job dashboard
      - File path to `geckodriver` web browser engine for Firefox WebDriver and output file(s)
      - Rev username and password (stored and accessed from local `.env` file)
      - XPATHs for page elements used by Selenium
- `src`:
    - `data_retrieval.py`: logic to control web scraper and filtering of job data
    - `data_processing.py`: logic to store job data from `weekly_job_data.txt` and `all_job_data.txt` into dictionaries for use in plots
    - `plots.py`: logic to create Matplotlib plots from job data
    - `driver_setup.py`: responsible for web scraper set up and tear down
    - `notification.py`: handles logic for sending notifications to desktop
    - `auth.py`: handles logic for logging into Rev
    - `output.py`: logic for saving job data to files
    - `job.py`: model class to represent a job on the Rev job dashboard
- `tests`: {Currently Empty} will be used to store unit tests

>#### Non-tracked (local) directories and files

- `output`:
    - `all_job_data.txt`: stores job data from all runs of the program 
    - `weekly_job_data.txt`: stores job data only for the current week
- `reports`:
    - `current`: directory to store reports about the current week
    - `historical`: directory to store historical reports 
      - `all_jobs.png`: scatter plot showing jobs available for each run of the program (by day of the week)
      - `{Year}/{Month}/{Date}/maximum_jobs_daily.png`: line plot showing maximum jobs available each day of the week for the previous week
      - `{Year}/{Month}/{Date}/prev_week_job_data.txt`: program-generated directories and file to store previous week's job data
- `.env`: file to store sensitive data locally for use by `config.py`

### Dependencies

### Installation

To run this program, you can follow these steps:

1. **Clone the Repository.** Start by cloning this repository to your local machine using the following command:

   ```bash
   git clone git@github.com:jadamb13/rev-jobs.git
   ```
2. **Navigate to the Project Directory.** Change your working directory to the project folder:

    ```bash
    cd rev-jobs
    ```
3. **Python Environment:** Ensure you have Python 3.12 or a higher version installed on your system. If not, you can 
download it from Python's official website.

4. **Install Dependencies.** Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

5. Run the Program: You can now execute the program by running the following command:

```bash
python main.py
```

### Usage

>### Future Improvements
  - Cross-platform standalone executable with installer and user guide
  - Machine learning model to predict future job availability
  - Database integration for persistent job data storage:
    - Train ML model
    - Create historical job availability reports
  - Front-end dashboard with authentication:
    - View job availability reports
    - Track long-term user metrics
  - Ability to claim jobs directly from desktop notifications
  - Auto-claim feature based on user-defined parameters