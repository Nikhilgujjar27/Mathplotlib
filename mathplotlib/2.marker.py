#here marker is a key word which is used for the ditection of the points
#ms--marker size , mec--marker edge size,  mfc--marker face size
#we can give any color by using #values of any color...
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([2,5,7,9,10])
plt.plot(ypoints,'o--b',ms='20',mec='y',mfc='r')
plt.show()
#if u want to change the line structure do not use marker keyword
