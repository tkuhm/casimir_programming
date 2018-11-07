import numpy as np
import pandas as pd

df = pd.read_excel('Ilses_biotek_exp.xlsx', skiprows=30)



df_time = df['Time']
df_time_data = df_time[1:480]
print(df_time_data)


#print the column names
print(df.columns)

# #get the values for a given column
values = df['Time'].values

print(values)

# #get a data frame with selected columns
# FORMAT = ['Time', 'A1', 'A2']
# df_selected = df[FORMAT]

# print(df_selected)
# # print(df_data['Time', 'A1'])