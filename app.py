import pandas as pd 
import numpy as np 
import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
#check version of pandas
print("Pandas version: ",pd.__version__)
#check versio of numpy
print("Numpy version: ",np.__version__)
print("Matplotlib version: ",matplotlib.__version__)
print("Matplotlib backend: ",matplotlib.get_backend())
#read csv data
sales=pd.read_csv("sales_data.csv")
# print(sales)
sales.head()