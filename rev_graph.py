import matplotlib.pyplot as plt
from datetime import date, time, datetime

date = datetime.now()
month =  date.strftime("%B")
for i in range (0,len(line_jobs_maxes)):
    plt.text(unique_dates[i], max_line_jobs, max_times[i], rotation=90)

plt.scatter(dates, line_jobs, s=15, color='b')
plt.plot(dates_represented_on_graph, line_jobs_maxes, color='k')
plt.ylabel('Jobs Available', fontsize=18)
plt.suptitle("Rev Line Job Availability Trend", fontsize=20)
plt.xticks(rotation=90)

mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
plt.savefig('C:\\Users\\james\\Desktop\\Rev_Job_Trends\\' + month + '\\' + 'jobs.png')
