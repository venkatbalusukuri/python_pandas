import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Data.csv')
df.plot()#pandas method to create a diagram
plt.show()
#scatter plot is a type of plot we can mention scatter plot by kind argument
df.plot(kind='scatter',x='Calories',y='Duration')#scatter plt required x,y arguments here this are nothing but column names
#by kind='scatter' we mentioning that we need scatter plot
plt.show()
#scatter plot where no relation between the columns
df.plot(kind='scatter',x='Duration',y='Maxpulse')#mentioning scatter plot with requried arguments
plt.show()
#histogram is a type of graph its need only one column and it describes the frequence of intervals
#kind='hist' means specifing that we need histogram
df['Duration'].plot(kind='hist') #mentioning histogram
plt.show()
