# test the pypplot library 
# Author: wang ta-dau 
# Email: yiyingchen@gate.sinica.edu.tw

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("/lfs/home/ychen/lfs_dir/scripts/python/test_day1/lena.png")

plt.imshow(img)
plt.show()



# add some data
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# start to use matplotlib pyplot 
plt.plot(x, y1, label = "sin")
plt.plot(x, y2, linestyle = "--", label = "cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()
plt.show()





  
