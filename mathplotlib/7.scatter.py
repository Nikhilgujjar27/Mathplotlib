#by using scatter funtion we can get only dots
'''import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,20,4,14,19,16,14,25])
y=np.array([99,66,76,98,54,100,80,100])
plt.scatter(x,y)
plt.show()

#we can give multiple valus in sane plot
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,20,4,14,19,16,14,25])
y=np.array([99,66,76,98,54,100,80,100])
plt.scatter(x,y)
#another plotiing
x=np.array([22,3,14,5,6,11,30,])
y=np.array([87,66,90,56,78,98,100])
plt.scatter(x,y)
plt.show()

#we can give the color whatever we want in it
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,20,4,14,19,16,14,25])
y=np.array([99,66,76,98,54,100,80,100])
plt.scatter(x,y,color='g')
#another plotiing
x=np.array([22,3,14,5,6,11,30,])
y=np.array([87,66,90,56,78,98,100])
plt.scatter(x,y)
plt.show()

#we can give a specified color to each name
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,20,4,14,19,16,14,25])
y=np.array([99,66,76,98,54,100,80,100])
plt.scatter(x,y)
#another plotiing
x=np.array([22,3,14,5,6,11,30,])
y=np.array([87,66,90,56,78,98,100])
colors=(['red','green','hotpink','blue','grey','brown','yellow'])
plt.scatter(x,y,c=colors)
plt.show()

#we can use  the colors by default color of mathplot lib
import matplotlib.pyplot as plt
import numpy as np
x=np.array([22,3,14,5,6,11,30,])
y=np.array([87,66,90,56,78,98,100])
colors=np.array([0,10,20,30,40,50,60])
plt.scatter(x,y,c=colors,cmap='viridis')
plt.show()

#we can use color bar also for the indicating colors
import matplotlib.pyplot as plt
import numpy as np
x=np.array([22,3,14,5,6,11,30,])
y=np.array([87,66,90,56,78,98,100])
colors=np.array([0,10,20,30,40,50,60])
plt.scatter(x,y,c=colors,cmap='viridis')
plt.colorbar()
plt.show()

#we can give various for the dots
import matplotlib.pyplot as plt
import numpy as np
x=np.array([22,3,14,5,6,11,30,])
y=np.array([87,66,90,56,78,98,100])
colors=np.array([0,10,20,30,40,50,60])
sizes=np.array([100,23,55,6,77,88,90,])
plt.scatter(x,y,c=colors,cmap='viridis',s=sizes)
plt.colorbar()
plt.show()

#by using alpha-- we can adjust the transparency of the dots
import matplotlib.pyplot as plt
import numpy as np
x=np.array([22,3,14,5,6,11,30,])
y=np.array([87,66,90,56,78,98,100])
plt.scatter(x,y,alpha=0.5)
plt.show()'''

#by using random values and also by some random colos by nipy_spectral
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))
colors=np.random.randint(100,size=(100))
sizes=np.random.randint(100,size=(100))
plt.scatter(x,y,c=colors,alpha=0.5,s=sizes,cmap='nipy_spectral')
plt.colorbar()
plt.show()



