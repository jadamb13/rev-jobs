import matplotlib.pyplot as plt
import os

dates = []
line_jobs = []
times = []

f = open('Rev_Job_Trends/rev_jobs.txt', 'r')

index=0
for row in f:
    row = row.split(' ')
    dates.append(row[0][:3] + " " + row[1][3:5])
    line_jobs.append(int(row[5].rstrip(os.linesep).rstrip('\t#')))
    times.append(row[2] + " " + row[3])
    index = index + 1

line_jobs_maxes = []
dates_represented_on_graph = []
max_times = []

max = int(line_jobs[0])
day_of_the_week = dates[0][:3]
dates_represented_on_graph.append(dates[0])

index = 1
for day in dates:
    while(index < len(dates)):

        if day_of_the_week == dates[index][:3]:
            if int(line_jobs[index]) > max:
                max = line_jobs[index]
                index = index + 1
            else:
                index = index + 1

        else:
            dates_represented_on_graph.append(dates[index])
            line_jobs_maxes.append(max)
            max_times.append(times[line_jobs.index(max)])
            max = int(line_jobs[index])
            day_of_the_week = dates[index][:3]
            index = index + 1

max_times.append(times[line_jobs.index(max)])
line_jobs_maxes.append(max)
for i in range (0,len(line_jobs_maxes)):
    plt.text(dates_represented_on_graph[i], line_jobs_maxes[i], max_times[i], rotation=90)

plt.scatter(dates, line_jobs, s=15, color='b')
plt.plot(dates_represented_on_graph, line_jobs_maxes, color='k')
plt.ylabel('Jobs Available', fontsize=18)
plt.suptitle("Rev Line Job Availability Trend", fontsize=20)
plt.xticks(rotation=90)

mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.show()
