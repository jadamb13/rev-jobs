## Automated Transcription Job Notifier
Program to automate filtering and retrieval of transcription job data using Selenium and send desktop notifications 


### Project Overview

#### Purpose:
The purpose of this project is to reduce time spent manually tracking Rev transcription jobs. Job availability 
frequently varies — sometimes unpredictably. As a result, a lot of time can be wasted either staying on the website 
and waiting for jobs to become available, or frequently logging in and applying filters to find preferential jobs. 
Contractors are only paid for completing a job — any additional time spent tracking or selecting tasks is unpaid.

#### What the program does:
The program will run automatically at user-set intervals and track job availability data by logging in, navigating 
to the job dashboard, applying user-set preferences (e.g. no Verbatim jobs; no Rush jobs), and sending a desktop 
notification if there are X or more jobs available (X set by the user). This will prevent the need to log in or 
constantly check if jobs meeting the users’ preferences are available. 

The program also saves job information to the `job_data.txt` file located in the `output` directory of the project. 
The data is stored in the format {Day of the week} {Month/Day} {Time in 12h time format} {AM/PM} {Total Jobs} 
{Line Jobs} as shown below:

```
Wednesday 08/07 03:58 PM 23 0
```

This data is currently used by `create_graphs.py` to create visualizations of job availability over the course of a week.

#### Ongoing development considerations:
In its current iteration, the program uses `win10toast` to provide notifications for Windows 10 operating systems. 
However, current refactoring will replace `win10toast` with `pyler` for cross-platform (Windows, macOS, Linux) 
notifications.

### Project Structure

The project is organized into several directories and a few root-level files: a `.gitignore` file, a `requirements.txt` 
file with program dependencies, and the current `README.md` file.

#### Directories and included files:

- `config`: 
    - `config.py`: file to store configuration data such as:
      - URL to access job dashboard
      - File paths to drivers for web scraper and output file(s)
      - Rev username and password (stored and accessed from local `.env` file)
      - XPATHs for page elements used by Selenium
- `output`:
    - `job_data.txt`: stores job data from each run of the program
- `src`:
    - `main.py`: entry point of the program
    - `data_retrieval.py`: logic to control web scraper and filtering of job data
    - `data_processing.py`: logic to store job data from `job_data.txt` into data structures for use in visualizations 
created in `create_graphs.py`
    - `create_graphs.py`: logic to create Matplotlib visualizations at the end of each week
    - `driver_setup.py`: {Currently Empty} will be used to separate web scraper set up and tear down
    - `notifications.py`: {Currently Empty} will be used to separate notification logic
- `tests`: {Currently Empty} will be used to store unit tests

### Dependencies:

**Python Standard Libraries:** The following Python standard libraries are used in this project:

### Installation:

### Usage:

### Future Improvements: 

#### Future project goals and feature development:
  - Create cross-platform standalone executable with installer and user guide
  - Implement a machine learning model to predict future job availability
  - Integrate database for persistent job data storage to train ML model and create historical job availability reports
  - Front-end dashboard with authentication to view job availability reports and track long-term user metrics
  - Ability to claim jobs directly from desktop notifications
  - Auto-claim feature based on user-defined parameters