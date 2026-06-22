import pandas as pd
df=pd.read_csv('Data.csv')
print(df.to_string()) #to load full data
#we can fix wrong_data by removing extreme values with other values
df.loc[79,'Duration']=180 #replace the  wrong value with 180 at index 79 and duration column by df.loc[index,'column__name']=new_data
print(df.to_string()) 
#to replace with small data its easy .to replace the large data it may difficult so we use boundary values like if it exceed the vlaue we have to replace the value with boundary value
#we use for loop
for x in df.index:#used for loop to check the full data by index 
    if df.loc[x,'Duration']>150:#here we taken boundary value as 150 if it excced 150 the duration column
        df.loc[x,'Duration']=150 #it will replace with the boundary value 



print(df.to_string())
#instead of replaceing the values even we can delete rows by dropna()
fox x in df.index:
    if df.loc[x,'Duration']>150: #check duration column if the duration exceed 150 
        df.dropna(inplace=True) #it will remove the particular column
