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
file_name = 'maximum_jobs_daily.png'
full_filepath = figure_filepath + '/' + file_name
if not os.path.exists(figure_filepath):
    os.makedirs(figure_filepath)

# Actions to perform with the information
plt.savefig(full_filepath)
# plt.show()


# Initialize day indices and job lists
day_indices = []
alj_combined = []
atj_combined = []

# Populate the lists
for day_index, (day_name, day_data) in enumerate(daily_data.items()):
    num_entries = len(day_data['line_jobs'])  # Number of entries for the day
    day_indices.extend([day_index] * num_entries)  # Extend day_indices with the day_index
    alj_combined.extend(day_data['line_jobs'])  # Extend alj_combined with line_jobs
    atj_combined.extend(day_data['total_jobs'])  # Extend atj_combined with total_jobs

# Check if day_indices has the same length as alj_combined and atj_combined
assert len(day_indices) == len(alj_combined) == len(atj_combined), "Mismatch in list lengths!"

# Create the scatterplot
plt.figure(figsize=(10, 6))

# Scatterplot for line jobs
plt.scatter(day_indices, alj_combined, color='blue', label='Line Jobs Available')

# Scatterplot for total jobs
plt.scatter(day_indices, atj_combined, color='red', label='Total Jobs Available')

# Customize the plot
plt.title('Job Availability Throughout the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Jobs Available')
plt.xticks(ticks=range(7), labels=days)  # Label x-axis with day names
plt.legend()

# Show the plot
plt.show()