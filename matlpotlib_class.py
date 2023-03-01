import numpy as np
from matplotlib import pyplot as plt

x = np.arange(15)
y = x**2
z = x**3
# plt.plot(x, y, marker='.', ms=4, c='red', linestyle='dashed') # markersize or ms= 10,2,3 anything, c=red, blue or any color
plt.plot(x,y, label='first graph')
plt.plot(x,x, label='second graph')
plt.plot(x,z, label='third graph')
plt.grid()
# plt.grid(axis='x')
# plt.grid(axis='y')
plt.legend()
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age VS Salary')
plt.show()
