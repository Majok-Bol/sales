import pandas as pd 
import numpy as np 
#check version of pandas
print("Pandas version: ",pd.__version__)
#check versio of numpy
print("Numpy version: ",np.__version__)
#read csv data
sales=pd.read_csv("sales_data.csv")
# print(sales)