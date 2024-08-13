import matplotlib.pyplot as plt
from datetime import datetime
from src.data_processing import *
import os
import shutil

date = datetime.now()
today = date.today()
date_today = today.strftime("%b-%d-%Y")
current_month = date.strftime("%B")
current_year = date.strftime("%Y")

x_axis = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sorted_unique_dates = list(sorted(unique_dates))

# Construct plots using data imported from data_processing.py
plt.plot(x_axis, max_line_jobs_per_day)
plt.plot(x_axis, max_total_jobs_per_day)

# Formatting and labels
plt.title('Daily Maximum Jobs Available')
plt.xlabel('Days')
plt.ylabel('BLUE: Max Line Jobs / ORANGE: Max Total Jobs')
plt.grid(True)

# Creates local directories if needed and saves graph image
figure_filepath = os.path.join(os.getcwd(), '../output')
file_name = 'job_trends.png'
full_filepath = figure_filepath + '/' + file_name
if not os.path.exists(figure_filepath):
    os.makedirs(figure_filepath)

# Actions to perform with the information
plt.savefig(full_filepath)
# plt.show()


