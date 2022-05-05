import matplotlib.pyplot as plt
from datetime import date, time, datetime
from process_data import *
import numpy as np
import sys
import os

date = datetime.now()
today = date.today()
date_today = today.strftime("%b-%d-%Y")
current_month =  date.strftime("%B")
current_year = date.strftime("%Y")

test_dates = ['05/02', '05/03', '05/04', '5/05', '5/06', '5/07', '5/08']

# Construct plots
plt.plot(test_dates, max_line_jobs_per_day)
plt.plot(test_dates, max_total_jobs_per_day)

# Formatting and labels
plt.title('Daily Maximum Jobs Available')
plt.xlabel('Days')
plt.ylabel('BLUE: Max Line Jobs / ORANGE: Max Total Jobs')
plt.grid(True)

# Creating local directories to save graph image

figure_filepath = os.path.join(os.getcwd(), 'Rev_Job_Trends', str(current_year), str(current_month), str(date_today))
file_name = 'job_data.png'
full_filepath = figure_filepath + '\\' + file_name
if not os.path.exists(figure_filepath):
    os.makedirs(figure_filepath)

# Actions to perform with the information
plt.savefig(full_filepath)
#plt.show()



'''
plt.savefig(os.path.join(os.getcwd()' + 'Rev_Job_Trends' + 'str(current_year)' + str(current_month))

(os.path.join('Screenshots/Blaze/screenshot_' + time.asctime() + '.png'))

email_save_path = os.path.join(os.getcwd(), "emails", date_, subject_)
if not os.path.exists(email_save_path):
    os.makedirs(email_save_path)
    with open(os.path.join(email_save_path, filename), 'wb') as fp:
        fp.write(part.get_payload(decode=True))
'''
### INCOMPLETE: Scatter Plot of line jobs and total jobs > over the course the day each day to visualize all jobs, not just maximums
## Information for setting ticks obtained at: https://stackabuse.com/change-tick-frequency-in-matplotlib/
#x = np.random.randint(low = 0, high = 23, size = len(alj_combined))
#plt.xticks(np.arange(0, len(x)+1, 2))
#plt.scatter(x, alj_combined)
#plt.scatter(x, atj_combined)
