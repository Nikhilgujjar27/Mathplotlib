#grid lines plotting using grid function
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,4,7,8,10])
y=np.array([2,5,3,9,11])
font1={'family':'serif','color':'blue','size':15}
font2={'family':'serif','color':'darkred','size':20}
plt.title("Our Health",fontdict=font1,size=20)
plt.xlabel("average health",fontdict=font2)
plt.ylabel("our calories",fontdict=font2)
plt.grid()
plt.plot(x,y)
plt.show()

#by defining the lines of the axis 
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,4,7,8,10])
y=np.array([2,5,3,9,11])
font1={'family':'serif','color':'blue','size':15}
font2={'family':'serif','color':'darkred','size':20}
plt.title("Our Health",fontdict=font1,size=20)
plt.xlabel("average health",fontdict=font2)
plt.ylabel("our calories",fontdict=font2)
plt.grid(axis='x')
plt.plot(x,y)
plt.show()

#by giving the line disign of grid lines
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,4,7,8,10])
y=np.array([2,5,3,9,11])
font1={'family':'serif','color':'blue','size':15}
font2={'family':'serif','color':'darkred','size':20}
plt.title("Our Health",fontdict=font1,size=20)
plt.xlabel("average health",fontdict=font2)
plt.ylabel("our calories",fontdict=font2)
plt.grid(color='g',ls='--',lw=0.5)
plt.plot(x,y)
plt.show()