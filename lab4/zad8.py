def ciag(a1 = 1, r = 1, ile = 10):
    an = a1 + (ile - 1) * r
    return (a1 + an)/2 * ile
print(ciag())
print(ciag(3, 5, 4))
