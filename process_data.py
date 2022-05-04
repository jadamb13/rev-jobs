import os

dates = []
max_total_jobs = []
max_line_jobs = []


### [ [Day of the week, [Time of day], [Line Jobs Available], [Total Jobs Available],
###   Line Jobs Daily Max, Total Jobs Daily Max, Time of Line Job Daily Max ]
daily_data = [ ['Monday', [], [0], [0], 0, 0, ''], ['Tuesday', [], [0], [0], 0, 0, ''], ['Wednesday', [], [0], [0], 0, 0, ''],
             ['Thursday', [], [0], [0], 0, 0, ''], ['Friday', [], [0], [0], 0, 0, ''], ['Saturday', [], [0], [0], 0, 0, ''],
             ['Sunday', [], [0], [0], 0, 0, ''] ]

f = open('Rev_Job_Trends/rev_jobs.txt', 'r')

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

### Gets unique dates and max job data for rev_graph.py
unique_dates = set(dates)

for day in daily_data:
    max_total_jobs.append(day[5])
    max_line_jobs.append(day[4])

# Remove leading placeholder '0' from line and total jobs lists (throws off index
#   that is necessary for rev_graph.py)
for day in daily_data:
    if (len(day[2]) > 1):
        day[2].pop(0)
    if(len(day[3]) > 1):
        day[3].pop(0)


for day in daily_data:
    max_line_job_index = day[2].index(day[4])

    if len(day[1]) > 0:
        day[6] = day[1][max_line_job_index]
    else:
        day[6] = "N/A"



# TODO: Will run into problem when weeks roll over -- I want the time of maximum jobs for THIS Sunday, not all Sundays, etc.
    # > Set up folders and files for year > month > week and start fresh with new text file each Monday
        # >> Add a method that will aggregate data over specified time period for larger than weekly graph

# TODO: Create UI for desktop that will pop up and update once every morning with current Dashboard stats

'''
    If it's Monday: (When is this determined, and by what program -- the script, the rev program?)
        - Use data from that month to create a graph and save the graph image to {.../Desktop/Rev_Job_Trends/Year/Month} directory
            - Append rev_jobs txt file to {.../Desktop/Rev_Job_Trends/Year/Month/jobs.txt}
                - After saving file successfully, delete all data from rev_jobs txt file to clear for new week and avoid mixing data

'''
