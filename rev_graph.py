import matplotlib.pyplot as plt
from datetime import date, time, datetime
from process_data import *
import numpy as np

date = datetime.now()
current_month =  date.strftime("%B")
test_dates = ['05/02', '05/03', '05/04', '5/05', '5/06', '5/07', '5/08']

# Construct plots
plt.plot(test_dates, max_line_jobs_per_day)
plt.plot(test_dates, max_total_jobs_per_day)

# Formatting and labels
plt.title('Daily Maximum Jobs Available')
plt.xlabel('Days')
plt.ylabel('BLUE: Max Line Jobs / ORANGE: Max Total Jobs')
plt.grid(True)

# Actions to perform with the information
plt.show()
plt.savefig('books_read.png')

### INCOMPLETE: Scatter Plot of line jobs and total jobs > over the course the day each day to visualize all jobs, not just maximums
## Information for setting ticks obtained at: https://stackabuse.com/change-tick-frequency-in-matplotlib/
#x = np.random.randint(low = 0, high = 23, size = len(alj_combined))
#plt.xticks(np.arange(0, len(x)+1, 2))
#plt.scatter(x, alj_combined)
#plt.scatter(x, atj_combined)
