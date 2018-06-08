import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([5,6,7,8,9])
c = list(set(x) - set(y))
print(c)

