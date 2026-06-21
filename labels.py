import pandas as pd
a=[1,2,3,4]
var=pd.Series(a)#series are 1d array shows in a column format
print(var)
print(var[1])#label is indexing to access values in the column
var=pd.Series(a,index=['a','b','c','d']) #to create index we  use index=[index elements]
print(var)
print(var['d'])#accesing by the index elements
#key value objects useing dictionary in series
b={'name':'venkat','age':23,'loc':'wgl'}
var1=pd.Series(b) # here keys are the lables(index)
print(var1)      
#to select only few items we use indexing in series
var2=pd.Series(b,['name','age']) # only name,age will come in the series
print(var2) 


                       
