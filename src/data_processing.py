import os

dates = []
max_total_jobs_per_day = []
max_line_jobs_per_day = []
alj_combined = []
atj_combined = []

### [ [Day of the week, [Time of day], [Line Jobs Available], [Total Jobs Available],
###   Line Jobs Daily Max, Total Jobs Daily Max, Time of Line Job Daily Max ]
daily_data = [ ['Monday', [], [0], [0], 0, 0, ''], ['Tuesday', [], [0], [0], 0, 0, ''], ['Wednesday', [], [0], [0], 0, 0, ''],
             ['Thursday', [], [0], [0], 0, 0, ''], ['Friday', [], [0], [0], 0, 0, ''], ['Saturday', [], [0], [0], 0, 0, ''],
             ['Sunday', [], [0], [0], 0, 0, ''] ]

f = open(os.path.join(os.getcwd(), '../output/job_data.txt'), 'r')

for row in f:

    row = row.split(' ')
    dates.append(row[1])
    day = row[0] # First value from line of text file
    match day:
        case 'Monday':
            daily_data[0][4] = max(daily_data[0][2])
            daily_data[0][5] = max(daily_data[0][3])

            daily_data[0][1].append(row[2] + " " + row[3])
            daily_data[0][2].append(int(row[5].rstrip(os.linesep).rstrip('\t#')))
            daily_data[0][3].append(int(row[4]))
        case 'Tuesday':
            daily_data[1][4] = max(daily_data[1][2])
            daily_data[1][5] = max(daily_data[1][3])

            daily_data[1][1].append(row[2] + " " + row[3])
            daily_data[1][2].append(int(row[5].rstrip(os.linesep).rstrip('\t#')))
            daily_data[1][3].append(int(row[4]))
        case 'Wednesday':
            daily_data[2][4] = max(daily_data[2][2])
            daily_data[2][5] = max(daily_data[2][3])

            daily_data[2][1].append(row[2] + " " + row[3])
            daily_data[2][2].append(int(row[5].rstrip(os.linesep).rstrip('\t#')))
            daily_data[2][3].append(int(row[4]))
        case 'Thursday':
            daily_data[3][4] = max(daily_data[3][2])
            daily_data[3][5] = max(daily_data[3][3])

            daily_data[3][1].append(row[2] + " " + row[3])
            daily_data[3][2].append(int(row[5].rstrip(os.linesep).rstrip('\t#')))
            daily_data[3][3].append(int(row[4]))
        case 'Friday':
            daily_data[4][4] = max(daily_data[4][2])
            daily_data[4][5] = max(daily_data[4][3])

            daily_data[4][1].append(row[2] + " " + row[3])
            daily_data[4][2].append(int(row[5].rstrip(os.linesep).rstrip('\t#')))
            daily_data[4][3].append(int(row[4]))
        case 'Saturday':
            daily_data[5][4] = max(daily_data[5][2])
            daily_data[5][5] = max(daily_data[5][3])

            daily_data[5][1].append(row[2] + " " + row[3])
            daily_data[5][2].append(int(row[5].rstrip(os.linesep).rstrip('\t#')))
            daily_data[5][3].append(int(row[4]))
        case 'Sunday':
            daily_data[6][4] = max(daily_data[6][2])
            daily_data[6][5] = max(daily_data[6][3])

            daily_data[6][1].append(row[2] + " " + row[3])
            daily_data[6][2].append(int(row[5].rstrip(os.linesep).rstrip('\t#')))
            daily_data[6][3].append(int(row[4]))

### Gets unique dates and max job data for create_graphs.py
unique_dates = set(dates)

for day in daily_data:
    max_total_jobs_per_day.append(day[5])
    max_line_jobs_per_day.append(day[4])
    line_job_list = day[2]
    total_job_list = day[3]
    for job in line_job_list:
        if job > 0:
            alj_combined.append(job)
    for job in total_job_list:
        if job > 0:
            atj_combined.append(job)


# Remove leading placeholder '0' from line and total jobs lists (throws off index
#   that is necessary for create_graphs.py)
for day in daily_data:
    if (len(day[2]) > 1):
        day[2].pop(0)
    if(len(day[3]) > 1):
        day[3].pop(0)


