import numpy as np
import pandas as pd
from datetime import timedelta
import matplotlib
matplotlib.use("Agg") # this you need for new version of matplotlib to work
import matplotlib.pyplot as plt


#nr. of timesteps
nrows = 481

#to fix timesteps
time_step_seconds = 360 # steps between measurements
time_start_seconds = 310 # first measurement starts at 5 min and 10 s

#import excel file (file name, number of first rows to skip, number of rows to use, which cols to use)
df = pd.read_excel('Ilses_biotek_exp.xlsx', skiprows=30, nrows=nrows, usecols="B:CU")


#new timesteps
seconds_since_start = np.arange(nrows)*time_step_seconds+time_start_seconds
time_since_start = pd.to_timedelta(seconds_since_start, unit='s') # input unit
df['Time'] = time_since_start


#sets time as index
df.set_index('Time', inplace=True)

#plots a graph showing the growth curve
fig, ax = plt.subplots()
df.C11.plot()
plt.xlabel(r'timestep', size=15)
plt.ylabel(r'OD600', size=15)
plt.title('growth curve of C11', size=20)

#saves the figure
fig.savefig('c11.png')