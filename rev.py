from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import lxml
from datetime import date, time, datetime
import io
import os
import pathlib
import time
from secrets import username, password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.rev.com/workspace/findwork'

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path="C:\\Users\\james\\Desktop\\geckodriver", log_path="C:\\Users\james\\Desktop\\geckodriver.log")
driver.get(url)

# Log in #
#login_button = '/html/body/div/nav/div/div/a[1]/span'
#driver.find_element_by_xpath(login_button).click()

username_xpath = '//*[@id="Email"]'
driver.find_element_by_xpath(username_xpath).send_keys(username)

next_button_xpath = '//*[@id="next-btn"]'
driver.find_element_by_xpath(next_button_xpath).click()

password_xpath = '//*[@id="Password"]'
WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, password_xpath))).send_keys(password)
# WebDriverWait line found at: https://stackoverflow.com/questions/56085152/selenium-python-error-element-could-not-be-scrolled-into-view
# to solve issue of element not being scrolled into view

sign_in_xpath = '//*[@id="login-btn"]'
driver.find_element_by_xpath(sign_in_xpath).click()

# Get amount of jobs/line jobs #

job_page_soup = BeautifulSoup(driver.page_source, 'lxml')

time.sleep(10) # Will not find element without waiting
number_of_jobs_xpath = '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/div/span[1]/a[1]/span[2]'
number_of_jobs = driver.find_element_by_xpath(number_of_jobs_xpath).text
number_of_jobs = number_of_jobs.replace("(", "").replace(")", "")

number_of_line_jobs_xpath = '/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/div/span[1]/a[3]/span[2]'
number_of_line_jobs = driver.find_element_by_xpath(number_of_line_jobs_xpath).text
number_of_line_jobs = number_of_line_jobs.replace("(", "").replace(")", "")

# Click line jobs to get more information specifically about line jobs available #

#line_jobs_button = '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[1]/div/span[1]/a[3]'
#driver.find_element_by_xpath(line_jobs_button).click()

# Save information to file/spreadsheet #
time_and_date = datetime.now()
string_time_and_date = time_and_date.strftime("%A %m/%d/%Y %I:%M %p")
file_name = "C:\\Users\\james\\Desktop\\Rev_Job_Trends\\rev_jobs.txt"
with open(file_name, "a+") as source_file:
    source_file.write(string_time_and_date + " " + number_of_jobs + " " + number_of_line_jobs + "\n")

driver.close()

# TODO: create new text files for each month to keep data separated for graphing
# TODO: add line jobs to file as well as overall jobs and plot them
# TODO: refactor/replaced deprecated commands
