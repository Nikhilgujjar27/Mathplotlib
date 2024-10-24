# we make the values by using pie chart
import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,32,12,48])
plt.pie(x)
plt.show()

#we can give the labels for each of the elements
import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,32,12,48])
mylabels=['apple','banana','kivi','dragonfruit']
plt.pie(x,labels=mylabels)
plt.show()

#we can give the specified angle to it 
import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,32,12,48])
mylabels=['apple','banana','kivi','dragonfruit']
plt.pie(x,labels=mylabels,startangle=90)
plt.show()

#explode--- seperting the ledges or giving a speration amoung itself
import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,32,12,48])
mylabels=['apple','banana','kivi','dragonfruit']
myexplodes=[0.2,0,0,0]
plt.pie(x,labels=mylabels,explode=myexplodes)
plt.show()
 

 #we can create a shadows for them
import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,32,12,48])
mylabels=['apple','banana','kivi','dragonfruit']
myexplodes=[0.2,0,0,0]
plt.pie(x,labels=mylabels,explode=myexplodes,shadow=True)
plt.show()

#we can give the specify colors the diff wadges
import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,32,12,48])
mylabels=['apple','banana','kivi','dragonfruit']
mycolors=['k','r','g','y']
plt.pie(x,labels=mylabels,colors=mycolors)
plt.show()

#we can add the legends or list of explations
import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,32,12,48])
mylabels=['apple','banana','kivi','dragonfruit']
myexplodes=[0.2,0,0,0]
plt.pie(x,labels=mylabels,explode=myexplodes)
plt.legend()
plt.show()

#we can give the titles for the legends
import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,32,12,48])
mylabels=['apple','banana','kivi','dragonfruit']
myexplodes=[0.2,0,0,0]
plt.pie(x,labels=mylabels,explode=myexplodes)
plt.legend(title='fruits')
plt.show()