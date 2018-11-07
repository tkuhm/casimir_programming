import numpy as np
import pandas as pd


#import excel file (file name, number of first rows to skip, number of rows to use, which cols to use)
df = pd.read_excel('Ilses_biotek_exp.xlsx', skiprows=30, nrows=481, usecols="B:CU")

#print the column names
print(df.columns)

#get the values for a given column
values = df['Time'].values
print(values)

#get a data frame with selected columns
FORMAT = ['Time', 'A1', 'A2']
df_selected = df[FORMAT]
print(df_selected)
