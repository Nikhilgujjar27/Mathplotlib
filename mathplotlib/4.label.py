#this is for the label nameing
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,4,7,8,10])
y=np.array([2,5,3,9,11])
plt.plot(x,y)
plt.xlabel("average health")
plt.ylabel("our calories")
plt.show()

#for giving tittle 
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,4,7,8,10])
y=np.array([2,5,3,9,11])
plt.plot(x,y)
plt.title("Our Health")
plt.xlabel("average health")
plt.ylabel("our calories")
plt.show()

#for giving location of the tittle use (loc)
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,4,7,8,10])
y=np.array([2,5,3,9,11])
plt.title("Our Health",loc='left')
plt.plot(x,y)
plt.xlabel("average health")
plt.ylabel("our calories")
plt.show()

#for giving font and also using color use dictionay
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,4,7,8,10])
y=np.array([2,5,3,9,11])
font1={'family':'serif','color':'blue','size':15}
font2={'family':'serif','color':'darkred','size':20}
plt.title("Our Health",fontdict=font1)
plt.plot(x,y)
plt.xlabel("average health",fontdict=font2)
plt.ylabel("our calories",fontdict=font2)
plt.show()