#dataframes:Datastes in pandas are usally multidimensionalarray
#Dataframes are like tables and series are like coloums
import pandas as pd
x={"cal":[789,655,455],"duretion":[49,69,76]}
newx=pd.DataFrame(x)
print(newx)

#by using (loc) we can axcess the values
import pandas as pd
x={"cal":[789,655,455],"duretion":[49,69,76]}
newx=pd.DataFrame(x)
print(newx.loc[[0,1]])

#load the data from ur files by using (csv)
import pandas as pd
fileload=pd.read_csv("path")
print(fileload)

