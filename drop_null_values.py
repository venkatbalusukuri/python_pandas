import pandas as pd
df=pd.read_csv('Data.csv')
df1=df.dropna() #dropna() to remove null values from the data set
print(df1)
#Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

#to change the original dataset use inplace=true
df.dropna(inplace=True)
print(df)
