import matplotlib.pyplot as plt
from datetime import datetime
from src.process_data import *
import os
import shutil

date = datetime.now()
today = date.today()
date_today = today.strftime("%b-%d-%Y")
current_month =  date.strftime("%B")
current_year = date.strftime("%Y")

x_axis = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sorted_unique_dates = list(sorted(unique_dates))

# Construct plots using data imported from process_data.py
plt.plot(x_axis, max_line_jobs_per_day)
plt.plot(x_axis, max_total_jobs_per_day)

# Formatting and labels
plt.title('Daily Maximum Jobs Available')
plt.xlabel('Days')
plt.ylabel('BLUE: Max Line Jobs / ORANGE: Max Total Jobs')
plt.grid(True)

# Creates local directories if needed and saves graph image
figure_filepath = os.path.join(os.getcwd(), 'Rev_Job_Trends', str(current_year), str(current_month), str(date_today))
file_name = 'job_data.png'
full_filepath = figure_filepath + '\\' + file_name
if not os.path.exists(figure_filepath):
    os.makedirs(figure_filepath)

# Actions to perform with the information
plt.savefig(full_filepath)
#plt.show()

# Copy current rev.py information to file in last week's job data folder
current_rev_file = os.path.join(os.getcwd(), 'Rev_Job_Trends', 'rev_jobs.txt')
destination_of_rev_file_information = os.path.join(os.getcwd(), 'Rev_Job_Trends', str(current_year), str(current_month), str(date_today), 'job_data.txt')

with open(destination_of_rev_file_information, 'w') as destination_file:
    shutil.copyfile(current_rev_file, destination_of_rev_file_information)

# Erase contents of rev.py file to start blank for new week
with open(current_rev_file, 'r+') as f:
    f.truncate(0)

### INCOMPLETE: Scatter Plot of line jobs and total jobs > over the course the day each day to visualize all jobs, not just maximums
## Information for setting ticks obtained at: https://stackabuse.com/change-tick-frequency-in-matplotlib/
#x = np.random.randint(low = 0, high = 23, size = len(alj_combined))
#plt.xticks(np.arange(0, len(x)+1, 2))
#plt.scatter(x, alj_combined)
#plt.scatter(x, atj_combined)
