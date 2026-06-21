import pandas as pd
df=pd.read_csv('Data.csv')
print(df.to_string())
df['date']=pd.to_datetime(df['date'],format='mixed') #to_datetime() method make the date formate fix in the column
print(df)
#next option is by removing null useing dropna()
df.dropna(subset=['date'],inplace=True)
print(df)
