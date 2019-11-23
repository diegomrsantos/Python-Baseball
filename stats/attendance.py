import pandas as pd
import matplotlib.pyplot as plt
from data import games

info_filter = games['type'] == 'info'
attendance_filter = games['multi2'] == 'attendance'
attendance = games.loc[info_filter & attendance_filter, ['year', 'multi3']]

attendance.columns = ['year', 'attendance']

attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])

attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')
plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y=attendance['attendance'].mean(), label='Mean', linestyle='--', color='green')
plt.show()
