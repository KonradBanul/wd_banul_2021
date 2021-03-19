def proste(a1,b1,a2,b2):
    if a1 == a2:
        return "Proste są równoległe"
    elif a1 * a2 == -1:
        return "Proste są prostopadłe"
    else:
        return "Proste nie są ani równoległe ani prostopadłe"
print(proste(2,3,3,1))
print(proste(2,4,2,5))
print(proste(2,3,-0.5,1))