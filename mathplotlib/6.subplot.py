#subplotting the plots as we want
'''import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,2,4,6,8])
y=np.array([2,8,5,9,10])
plt.subplot(2,1,1)   #here 2--rows, 1--colom,  1--plot number
plt.suptitle('my company')
plt.title('sales',color='r')
plt.plot(x,y)'''



#plot 2--
import matplotlib.pyplot  as plt
import numpy as np
x=np.array([0,2,4,6])
y=np.array([10,20,30,40])
plt.subplot(2,1,2)
plt.title('sales')
plt.plot(x,y)
plt.show()