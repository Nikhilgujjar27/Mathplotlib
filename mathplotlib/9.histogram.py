#histogram--a graph showing the frequency of distribution
import matplotlib.pyplot as plt
import numpy as np
x=np.random.normal(170,10,250)
plt.hist(x,color='r')
plt.show() 