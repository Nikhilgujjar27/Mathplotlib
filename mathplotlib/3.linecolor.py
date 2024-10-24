#for changing the line style use linestyle (ls)
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([1,3,7,8,10])
plt.plot(ypoints,ls='dotted')
plt.show()

#for changing the linecolor(c)
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([1,3,7,8,10])
plt.plot(ypoints,ls='dotted',c='r')
plt.show()

#for changing the line width(lw)
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([1,8,4,2,10])
plt.plot(ypoints,ls='dotted',c='r',lw='10')
plt.show()

#for printing multiple lines
import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([1,3,5,6])
xpoints=np.array([2,6,2,9])
plt.plot(ypoints)
plt.plot(xpoints)
plt.show()

