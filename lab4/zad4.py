def monoton(a,b):
    if a > 0:
        return "Funkcja jest rosnąca"
    elif a == 0:
        return "Funkcja jest stała"
    else:
        return "Funkcja jest malejąca"
print(monoton(4,2))
print(monoton(0,5))
print(monoton(-6,-2))