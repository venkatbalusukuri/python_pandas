#to handle duplicates we have find duplicates by 'duplicated()' method
#it return boolean values that is true if row has duplicates other wise false
import pandas as pd
df=pd.read_csv('Data.csv')
print(df.duplicated())
#after finding the duplicates we have to remove duplicate rows by 'drop_duplicate()'
#it will delete all the duplicate rows from the data set
df.drop_duplicates()#drop duplicate rows from the data set
print(df)
