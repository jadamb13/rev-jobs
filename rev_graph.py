import matplotlib.pyplot as plt
from datetime import date, time, datetime
from process_data import *

date = datetime.now()
month =  date.strftime("%B")
unique_dates_list = list(unique_dates)
line_jobs = []
total_jobs = []
test_dates = ['05/02', '05/03', '05/04', '5/05', '5/06', '5/07', '5/08']

for i in range (0, 7):
    line_jobs.append(daily_data[i][4])
    total_jobs.append(daily_data[i][5])

plt.plot(test_dates, line_jobs)
plt.plot(test_dates, total_jobs)
plt.title('Daily Maximum Jobs Available')
plt.xlabel('Days')
plt.ylabel('BLUE: Max Line Jobs / ORANGE: Max Total Jobs')
plt.grid(True)
plt.show()
