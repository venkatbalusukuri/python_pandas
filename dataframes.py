import pandas as pd
data={'name':['venkat','ajay','nikhil'],
      'age':[23,22,23]
      }
var=pd.DataFrame(data) #dataframe is the 2-dimension like a table 
print(var)
#locate row we use loc[index] for acces rows in the dataframe
print(var.loc[0])
print(var.loc[[0,1]]) #for multiple rows we use loc[[index1,index2,...indexn]]
#name index to give names to index rather than default values like o,1,2 ,same like series
var1=pd.DataFrame(data,index=['a','b','c']) #useing index=[elements]
print(var1)
print(var1.loc['b'])#to locate rows useing index names useing loc[]
print(var1.loc[['c','a']])#for multiple rows we use loc[[index names]]
print(var1.head()) #To display top 5 rows and colums of the data
var1.head(10) #To display mentioned number of rows and columns of the data
