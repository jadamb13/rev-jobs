# Automated Transcription Job Notifier
### Program to automate filtering and retrieval of transcription job data using Selenium and send desktop notifications 


## Project Overview

The purpose of this project is to reduce time spent manually tracking Rev transcription jobs. Job availability 
frequently varies — sometimes unpredictably. As a result, a lot of time can be wasted either staying on the website 
and waiting for jobs to become available, or frequently logging in and applying filters to find preferential jobs. 
Contractors are only paid for completing a job — any additional time spent tracking or selecting tasks is unpaid.

The program will run automatically at user-set intervals and track job availability data by logging in, navigating to 
the job dashboard, applying user-set preferences (e.g. no Verbatim jobs; no Rush jobs), and sending a desktop 
notification if there are X or more jobs available (X set by the user). This will prevent the need to log in or 
constantly check if jobs meeting the users’ preferences are available. 

In its current iteration, the program uses `win10toast` to provide notifications for Windows 10 operating systems. 
However, current refactoring will replace `win10toast` with `pyler` for cross-platform (Windows, macOS, Linux) 
notifications. 