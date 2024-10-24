# To draw a straight line by using pyplot.....
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([0,6])
ypoints=np.array([0,250])
plt.plot(xpoints,ypoints)
plt.show()

#The code for the zig zag line in the given graph
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([0,2,4,6,5,9,10])
ypoints=np.array([0,5,3,2,8,9,12])
plt.plot(xpoints,ypoints)
plt.show()

#if we do not specify the size of the any points(x,y) by default it will take the values
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([0,4,5,6])
plt.plot(ypoints,'*:r')
plt.show()

#we donot want a line we can use 
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([0,6,])
ypoints=np.array([0,250,])
plt.plot(xpoints,ypoints,'o')
plt.show()