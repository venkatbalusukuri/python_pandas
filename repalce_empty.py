import pandas as pd
df=pd.read_csv('Data.csv')
df.fillna(120,inplace=True) #to replace every null column with 120 fillna(value)
#print(df.to_string())
#to replace the null values of specific columns
df.fillna({'calories':120},inplace=True)# fillna({'cloumn':value})
print(df)
#replace the null(empty) values with mean(),median(),mode()
df1=pd.read_csv('Data.csv')
x=df1['Calories'].mean() #finding mean of the calories column
df1.fillna({'calories':x},inplace=True)    #replaceing null of calories with mean of the calories data 
print(df1)
y=df1['Calories'].median() 
df1.fillna({'Calories':y},inplace=True) #filling the null with median
print(df1)
z=df['Calories'].mode() 
df1.fillna({'Calories':z},inplace=True) #filling the null with mode
