import pandas as pd
import numpy as np 

df=pd.read_csv(r"D:\M Arian Rasyid S\File Organization\Learning\Data Science\AppleStore.csv")
opened_file = open('D:\M Arian Rasyid S\File Organization\Learning\Data Science\AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)