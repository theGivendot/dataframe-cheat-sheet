import sys
import scipy
import numpy
import matplotlib
import pandas as pd
import os

# https://www.geeksforgeeks.org/how-to-pretty-print-an-entire-pandas-series-or-dataframe/

# https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm 

trends = pd.read_csv('trends.csv')
def writeToFile(): 
    file = open('/Users/danielluciani/Desktop/pythonpracticing/datasetsinfo.txt', 'w+')
    file.write(
        str(trends.head()) + '\n \n' + 
        str(trends.size) + '\n \n' + 
        str(trends.shape) + '\n \n' + 
        str(trends) + '\n \n' 
    
    )
    file.close 
searched_data = trends.drop(columns=['year', 'location'])
location_search_rank = trends.drop(columns=['year', 'query', 'category'])

# Comman + / to comment out highlighted code 

# Creating a dataframe from a dictionary 
# df = pd.DataFrame({
#   'Product_id': ['ABC', 'DEF', 'GHI', 'JKL', 
#                  'MNO', 'PQR', 'STU', 'VWX'],
    
#   'Stall_no': [37, 38, 9, 50, 7, 23, 33, 4],
#   'Grade': [1, 0, 0, 2, 0, 1, 3, 0],
    
#   'Category': ['Fashion', 'Education', 'Technology', 
#                'Fashion', 'Education', 'Technology', 
#                'Fashion', 'Education'],
    
#   'Demand': [10, 12, 14, 15, 13, 20, 10, 15],
#   'charges1': [376, 397, 250, 144, 211, 633, 263, 104],
#   'charges2': [11, 12, 9, 13, 4, 6, 13, 15],
#   'Max_Price': [4713, 10352, 7309, 20814, 9261, 
#                 6104, 5257, 5921],
    
#   'Selling_price': [4185.9477, 9271.490256, 6785.701362, 
#                     13028.91782, 906.553935, 5631.247872, 
#                     3874.264992, 4820.943]})
# # print(df)

# Creating and empty dataframe 
newDF = pd.DataFrame()
# print(newDF) 

# Creating a dataframe from a list 
listData = [1, 2, 4, 8, 16]
listdf = pd.DataFrame(listData) 
# print(listdf) 

# Creating a dataframe with from a list and giving it labels 
dataList = [['Carl', 16], ['James', 17], ['Jeff', 18]]
dataframeList = pd.DataFrame(dataList, columns=['Name', 'Age']) 
# dtype can be added with columns to change what the values will be shown as 
# index can be added to change what the rows will be called 
# print(dataframeList) 
# dataframelist.append() will add rows at the end 
# same thing for with drop(), this will drop rows with the chosen label 

# Creating a dataframe from a list of dictionaries 
datadictionary = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
dataFromDictionary = pd.DataFrame(datadictionary)
# print(dataFromDictionary) 
