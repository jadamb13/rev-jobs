import matplotlib.pyplot as plt
from datetime import datetime
from src.data_processing import *
import os
from config.config import get_config

x_axis = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sorted_unique_dates = list(sorted(unique_dates))

# Construct plots using data imported from data_processing.py
plt.plot(x_axis, max_line_jobs_per_day, color='blue', label='Line Jobs')
plt.plot(x_axis, max_total_jobs_per_day, color='Red', label='Total Jobs')

# Formatting and labels
plt.title('Daily Maximum Jobs Available')
plt.xlabel('Days')
plt.ylabel('Number of Jobs Available')
plt.grid(True)
plt.legend()

# Creates local directories if needed and saves graph image
config = get_config()

destination_directory = config['current_report_directory']
max_jobs_file_name = 'maximum_jobs_daily.png'
max_jobs_full_filepath = destination_directory + '/' + max_jobs_file_name
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

plt.savefig(max_jobs_full_filepath)


# Function to convert time to a fraction of a day
def time_to_fraction_of_day(time_str):
    time_obj = datetime.strptime(time_str, '%I:%M %p')  # Convert string to time object
    total_minutes = time_obj.hour * 60 + time_obj.minute  # Calculate total minutes from midnight
    fraction_of_day = total_minutes / (24 * 60)  # Convert to fraction of a day
    return fraction_of_day


# Initialize lists to store data for plotting
day_indices = []
alj_combined = []
atj_combined = []

# Populate day_indices, alj_combined, and atj_combined from daily_data
for day_index, (day_name, day_data) in enumerate(daily_data.items()):
    for time_str, line_jobs, total_jobs in zip(day_data['times'], day_data['line_jobs'], day_data['total_jobs']):
        time_fraction = time_to_fraction_of_day(time_str)
        adjusted_day_index = day_index + time_fraction
        day_indices.append(adjusted_day_index)
        alj_combined.append(line_jobs)
        atj_combined.append(total_jobs)

# Check if day_indices has the same length as alj_combined and atj_combined
assert len(day_indices) == len(alj_combined) == len(atj_combined), "Mismatch in list lengths!"

# Create the scatterplot
plt.figure(figsize=(14, 6))

# Scatterplot for line jobs
plt.scatter(day_indices, alj_combined, color='blue', label='Line Jobs')

# Scatterplot for total jobs
plt.scatter(day_indices, atj_combined, color='red', label='Total Jobs')

# Customize the plot
plt.title('Job Availability by Weekday | August 01, 2024 — Present')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Jobs Available')

# Set x-ticks for each day with 3-hour increments
ticks = []
labels = []
for i, day in enumerate(days):
    for hour in range(0, 24, 3):
        ticks.append(i + hour / 24)
    labels.append(day)

# Plot x-axis ticks for every 3 hours
plt.xticks(ticks=ticks, labels=[''] * len(ticks))  # Remove default labels
plt.gca().set_xticks([i + 0.5 for i in range(len(days))], minor=True)  # Add minor ticks for day separators

# Label days at the start of each day
for i, day in enumerate(days):
    plt.axvline(x=i, color='gray', linestyle='--', linewidth=0.7)  # Vertical lines for days
    plt.text(i + 0.5, min(alj_combined + atj_combined), day, ha='center', va='bottom')

plt.legend(loc="upper right")

# Save the plot
plt.tight_layout()
all_job_data_filename = 'all_jobs.png'
all_jobs_full_filepath = os.path.join(config['historical_report_directory'], all_job_data_filename)
plt.savefig(all_jobs_full_filepath)
