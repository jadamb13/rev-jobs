import os

dates = []
line_jobs = []
total_jobs = []
times = [ ['Sunday', []], ['Monday', []], ['Tuesday', []], ['Wednesday',[]], ['Thusday', []], ['Friday', []], ['Saturday', []] ]



f = open('Rev_Job_Trends/rev_jobs.txt', 'r')

for row in f:
    row = row.split(' ')
    day = row[0] # First value from line of text file
    match day:
        case 'Sunday':
            times[0][1].append(row[2] + " " + row[3])
        case 'Monday':
            times[1][1].append(row[2] + " " + row[3])
        case 'Tuesday':
            times[2][1].append(row[2] + " " + row[3])
        case 'Wednesday':
            times[3][1].append(row[2] + " " + row[3])
        case 'Thursday':
            times[4][1].append(row[2] + " " + row[3])
        case 'Friday':
            times[5][1].append(row[2] + " " + row[3])
        case 'Saturday':
            times[6][1].append(row[2] + " " + row[3])
    dates.append(row[1])
    line_jobs.append(int(row[5].rstrip(os.linesep).rstrip('\t#')))

for day in times:
    print(day)
