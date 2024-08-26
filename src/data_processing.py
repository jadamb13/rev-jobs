import os

# Initialize daily data structure
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_data = {
    day: {'times': [], 'line_jobs': [], 'total_jobs': [], 'line_max': 0, 'total_max': 0, 'line_max_time': ''}
    for day in days}


def update_daily_data(day, time, total_jobs, line_jobs):
    daily_data[day]['times'].append(time)
    daily_data[day]['line_jobs'].append(line_jobs)
    daily_data[day]['total_jobs'].append(total_jobs)
    daily_data[day]['line_max'] = max(daily_data[day]['line_jobs'])
    daily_data[day]['total_max'] = max(daily_data[day]['total_jobs'])


def create_job_data_dict(file):

    dates = []
    with open(file) as f:
        for row in f:
            row = row.split()
            dates.append(row[1])
            day, time, total_jobs, line_jobs = row[0], f"{row[2]} {row[3]}", int(row[4]), int(
                row[5].rstrip(os.linesep).rstrip('\t#'))

            update_daily_data(day, time, total_jobs, line_jobs)

    return daily_data



