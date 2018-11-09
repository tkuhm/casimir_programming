import numpy as np
import pandas as pd
from datetime import timedelta
import matplotlib
matplotlib.use("Agg") # this you need for new version of matplotlib to work
import matplotlib.pyplot as plt
from scipy.stats import stats



#nr. of timesteps
nrows = 481

#to fix timesteps
time_step_seconds = 360 # steps between measurements
time_start_seconds = 310 # first measurement starts at 5 min and 10 s

#import excel file (file name, number of first rows to skip, number of rows to use, which cols to use)
df = pd.read_excel('Ilses_biotek_exp.xlsx', skiprows=30, nrows=nrows, usecols="B:CU")

#input
mfw_input = input("Please enter your favorite well: ")

#choosing well to work with
mfw = df[mfw_input] #my favorite well


#new timesteps
seconds_since_start = np.arange(nrows)*time_step_seconds+time_start_seconds
time_since_start = pd.to_timedelta(seconds_since_start, unit='s') # input unit
df['Time'] = time_since_start


#sets time as index
df.set_index('Time', inplace=True)

#plots a graph showing the growth curve
fig, ax = plt.subplots()
df[mfw_input].plot()
plt.xlabel(r'timestep', size=15)
plt.ylabel(r'OD600', size=15)
plt.title('growth curve of '+mfw_input, size=20)

#saves the figure
fig.savefig('plots/'+mfw_input+'.png')
print('saved: plots/'+mfw_input+'.png')

##Fitting the data

#using log data
logmfw = np.log2(mfw)

#linear model for fitting
def modelmfw(x):
    return interceptmfw + slopemfw*x

# choose intervals
starts = list(range(0, nrows-70))
ends = list(range(70, nrows))
pairs = list(zip(starts, ends))


# choose best interval
results = np.zeros((5,len(pairs)))

for k,(i,j) in enumerate(pairs):
    results[:, k] = stats.linregress(seconds_since_start[i:j], logmfw[i:j])
    
#find best R-squared (best fit)
np.argmax(results[2,:])
startmfw, endmfw = pairs[np.argmax(results[2,:])]


#Generating best fit
slopemfw, interceptmfw, rvaluemfw, pvaluemfw, stderrmfw = stats.linregress(seconds_since_start[startmfw:endmfw], logmfw[startmfw:endmfw])

#plotting best fit
fig, ax = plt.subplots()
plt.plot(seconds_since_start, logmfw)
plt.plot(seconds_since_start[startmfw-50:endmfw+50], modelmfw(seconds_since_start[startmfw-50:endmfw+50]))

#ax.set_yscale('log')
plt.xlabel(r'# of seconds', size=15)
plt.ylabel(r'log of OD600', size=15)
plt.title('growth curve of '+mfw_input, size=20)

#saves the figure
fig.savefig('plots/'+mfw_input+'_fit.png')
print('saved: plots/'+mfw_input+'_fit.png')

#calculates the doubling time and growth rate
doublingtime_insec = np.log(2)/slopemfw
doublingtime_inmin = doublingtime_insec/60

gr_min = slopemfw*60 #conversion to minutes, slopemfw is growth rate per sec


#saves the output
f = open('output/'+mfw_input+'_output.txt', 'w+')

str_gr_min = str(gr_min)
str_dt = str(doublingtime_inmin)
str_startmfw = str(startmfw)
str_endmfw = str(endmfw)
f.write('The doubling time of '+mfw_input+' is: '+str_dt+' min.\nThe growth rate per min for '+mfw_input+' is: '+str_gr_min+'.\nStart fit: '+str_startmfw+'\nEnd fit: '+str_endmfw)
print('saved: output/'+mfw_input+'_output.txt, containing doubling time, growth rate and start/end fit')