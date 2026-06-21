import pandas as pd
df=pd.read_csv('Data.csv')#to read csv files
print(df)#return only first 5 rows and columns and last 5 rows and columns
print(df.to_string()) #to print entire dataframe we use to_string() method
print(pd.options.display.max_rows) #to see max rows returned by the system useing options.display.max_rows
pd.options.display.max_rows=100
print(df)
df1=pd.read_json('data.json')#to read json files,its also by default print only first and last 5 rows and columns
#json =python dictionary ,json obect have the same formats as python dictionary
data={
    "students":{
        "0":'venkat',
        "1":'ajay',
        "2":'nikhil'
        },
    "ages":{
        '0':23,
        '1':22,
        '2':23
        }
    }
df2=pd.DataFrame(data)
print(df2)
        
