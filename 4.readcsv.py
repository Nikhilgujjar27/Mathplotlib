#load the data from the csv file into data frame ie data.csv
#read the csv file(comma seperated files)way to store the big and biggest data sets csv file contain plane text
#loading csv into dataframes
import pandas as pd
print(pd.options.display.max_rows)

#by using the to_string() it will give the all output which is in the file 
import pandas as pd
df=pd.read_csv('data.csv')
print(df.to_string())

#without using to_string ()
import pandas as pd
df=pd.read_csv('data.csv')
print(df)


#this is by giving the extra memory more than 60 and it is used to handle large datas
import pandas as pd
df=pd.read_csv('data.csv')
pd.options.display.max_rows=9999
print(df)