from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import lxml
from datetime import date, time, datetime
import io
import os
import pathlib
import time
from secrets import username, password
from win10toast import ToastNotifier


url = 'https://www.rev.com/workspace/findwork'

# Set up web driver #
options = Options()
options.headless = True
s = Service("C:\\Users\\james\\Desktop\\geckodriver")
driver = webdriver.Firefox(service=s, options=options)
driver.get(url)

# Log in #
username_xpath = '//*[@id="Email"]'
next_button_xpath = '//*[@id="next-btn"]'
password_xpath = '//*[@id="Password"]'
sign_in_xpath = '//*[@id="login-btn"]'

driver.find_element(By.XPATH, username_xpath).send_keys(username)
driver.find_element(By.XPATH, next_button_xpath).click()
WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, password_xpath))).send_keys(password)
driver.find_element(By.XPATH, sign_in_xpath).click()
# WebDriverWait line found at: https://stackoverflow.com/questions/56085152/selenium-python-error-element-could-not-be-scrolled-into-view
# to solve issue of element not being scrolled into view

time.sleep(10) # Will not find element without waiting

# Retrieve job data #
number_of_jobs_xpath = '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/div/span[1]/a[1]/span[2]'
number_of_line_jobs_xpath = '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/div/span[1]/a[3]/span[2]'

number_of_jobs = driver.find_element(By.XPATH, number_of_jobs_xpath).text
number_of_line_jobs = driver.find_element(By.XPATH, number_of_line_jobs_xpath).text

driver.close()

number_of_jobs = number_of_jobs.replace("(", "").replace(")", "")
number_of_line_jobs = number_of_line_jobs.replace("(", "").replace(")", "")

# Save information to file #
time_and_date = datetime.now()
string_time_and_date = time_and_date.strftime("%A %m/%d %I:%M %p")
file_name = "C:\\Users\\james\\Desktop\\Rev_Job_Trends\\rev_jobs.txt"

with open(file_name, "a+") as source_file:
    source_file.write(string_time_and_date + " " + number_of_jobs + " " + number_of_line_jobs + "\n")

toast = ToastNotifier()
if (int(number_of_jobs) > 30):
    toast.show_toast("Rev Jobs Available", "There are " + number_of_jobs + " total jobs, and " + number_of_line_jobs + " line jobs currently available.")

# TODO: refactor/replaced deprecated commands for Selenium/BS4
