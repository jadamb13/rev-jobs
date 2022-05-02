import os

dates = []
daily_data = [ ['Sunday', [], [], []], ['Monday', [], [], []], ['Tuesday', [], [], []], ['Wednesday', [], [], []], ['Thusday', [], [], []], ['Friday', [], [], []], ['Saturday', [], [], []] ]

f = open('Rev_Job_Trends/rev_jobs.txt', 'r')

for row in f:
    row = row.split(' ')
    day = row[0] # First value from line of text file
    match day:
        case 'Sunday':
            daily_data[0][1].append(row[2] + " " + row[3])
            daily_data[0][2].append(row[5].rstrip(os.linesep).rstrip('\t#'))
            daily_data[0][3].append(row[4])
        case 'Monday':
            daily_data[1][1].append(row[2] + " " + row[3])
            daily_data[1][2].append(row[5].rstrip(os.linesep).rstrip('\t#'))
            daily_data[1][3].append(row[4])
        case 'Tuesday':
            daily_data[2][1].append(row[2] + " " + row[3])
            daily_data[2][2].append(row[5].rstrip(os.linesep).rstrip('\t#'))
            daily_data[2][3].append(row[4])
        case 'Wednesday':
            daily_data[3][1].append(row[2] + " " + row[3])
            daily_data[3][2].append(row[5].rstrip(os.linesep).rstrip('\t#'))
            daily_data[3][3].append(row[4])
        case 'Thursday':
            daily_data[4][1].append(row[2] + " " + row[3])
            daily_datas[4][2].append(row[5].rstrip(os.linesep).rstrip('\t#'))
            daily_data[4][3].append(row[4])
        case 'Friday':
            daily_data[5][1].append(row[2] + " " + row[3])
            daily_data[5][2].append(row[5].rstrip(os.linesep).rstrip('\t#'))
            daily_data[5][3].append(row[4])
        case 'Saturday':
            daily_data[6][1].append(row[2] + " " + row[3])
            daily_data[6][2].append(row[5].rstrip(os.linesep).rstrip('\t#'))
            daily_data[6][3].append(row[4])
    dates.append(row[1])

#for day in line_jobs:
#    print(day)
for day in daily_data:
    print(day)
