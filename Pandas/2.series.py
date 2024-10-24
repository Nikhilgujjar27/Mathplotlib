#it is for giving the inputs in series and with the index values
import pandas as pd 
nikki=[2,4,7]
nikkinew=pd.Series(nikki)
print(nikkinew)

#for accessing the single value in  the series
import pandas as pd 
nikki=[2,4,7]
nikkinew=pd.Series(nikki)
print(nikkinew[0])

#for giving the labels for the index values
import pandas as pd 
nikki=[2,4,7]
nikkinew=pd.Series(nikki,index=["x","y","z"])
print(nikkinew)

#by using the dictionary we can create the pandas series
import pandas as pd
x={"day1":450,"day2":789,"day3":123}
newx=pd.Series(x)
print(newx)

#we can get the indexes of dictionary which is required for us
import pandas as pd
x={"day1":450,"day2":789,"day3":123}
newx=pd.Series(x,index=["day1","day3"])
print(newx)

#for multidimensnal arrays
#DataFrames:datasetes in panda are usally mutidimensnal array
#series are like colums and data frames are like table.....
import pandas as pd
x={"cal":[789,655,455],"duretion":[49,69,76]}
newx=pd.DataFrame(x)
print(newx)

