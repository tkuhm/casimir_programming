import numpy as np
import pandas as pd

excel_file = 'Ilses_biotek_exp.xlsx'
movies = pd.read_excel(excel_file, skiprows = 30, nrows = 481, usecols = ["B:CU"])

print(movies.shape)

print(movies.head())

movies.write(“newfile.txt”) 