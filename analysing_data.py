#head() method
import pandas as pd
df=pd.read_csv('Data.csv')
print(df.head(10)) #head() returns the headers and a specified number of rows, starting from the top.
#If head() not specify any value by default it returns top 5 header rows values
#tail() method return the rows from last ,if not specified it return last 5 rows of the data
print(df.tail(10))
#info() method is used to know the info about the datasets it will return no.of rows & columns and column names and no.of null values in the data set
print(df.info())
