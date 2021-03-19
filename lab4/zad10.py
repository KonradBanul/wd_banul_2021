def zakupy(**produkty):
    return sum([int(a) for a in produkty.values()])
print(zakupy(banany=4, pomidory=5, ogórki=6))


