import numpy as np

a = np.array([4,3,5,7,2,7,5,4,2]).reshape(3,3)
print(a.min(axis=0))
print(a.min(axis=1))
b = np.array([2,6,5,3,8,6,4,3,0,3,6,2,3,5,1,6]).reshape(4,4)
print(b.min(axis=0))
print(b.min(axis=1))
