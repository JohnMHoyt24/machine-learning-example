import numpy
import pandas as pd
from matplotlib import pyplot as plt


filename='C:/datasets/RAW_us_deaths.csv'

names = ['Province_State', 'Lat', 'Long', 'Combined_Key', 'Population']

df = pd.read_csv(filename, names=names)

print("**************Data Shape******************")
print(df.shape) #rows and columns
#print("*******************Data Types***************")
#print(df.dtypes) #types of data
#print(df.head(1))
#print(df.describe())
print(df)












