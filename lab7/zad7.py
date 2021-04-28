import numpy as np

a = np.array([3,5,2,7,4,6]).reshape(2,3)
a = np.sin(a)
print(a)

b = np.array([5,3,2,1,5,2]).reshape(2,3)
b = np.cos(b)
print(b)

c = a + b
print(c) 