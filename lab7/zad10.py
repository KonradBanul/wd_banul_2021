import numpy as np

a = np.arange(81).reshape(9,9)
print(a)
b = a.reshape((1,81))
print(b)
c = a.reshape((3,27))
print(c)
d = a.reshape((27,3))
print(d)
e = a.reshape((81,1))
print(e)