#zadanie 6
#for x in range(0, 51, 1):
#    if x % 5 == 0:
#        print(str(x))

#zadanie 7
#for a in range(1, 10, 1):
#    a = input(' ')
#    a = int(a)
#    a = a * a
#    print(str(a))

#zadanie 8 ???
#a = input("Podaj liczby:")
#lista = []
#while(len(lista)<5):
#    lista.append(a)
#print(lista)


#zadanie 9
#a = input("Podaj liczbę: ")
#suma = 0
#a = int(a)
#while a > 0:
#    suma += a % 10
#    a //= 10
#print(int(suma))

#zadanie 10
#import sys
#a = input("Podaj liczbę a < 11: ")
#a = int(a)
#if a < 11:
#    for i in range(1, a+1):
#        for j in range(0, i):
#            sys.stdout.write('A')
#        print(end='\n')
#else:
#    print("Podałeś za dużą liczbę!")

#zadanie 11 ???
#import sys
#a = input("Podaj wysokość wieży a < 10: ")
#a = int(a)
#for i in range(a - a // 2):
#    print(" " * (a - i - 1) + "o" * (2 * i + 1))
#for i in range(a - a // 2 - 2, -1, -1):
#    print(" " * (a - i - 1) + "o" * (2 * i + 1))

#zadanie 12
#import sys
#for i in range(1, 21, 1):
#    for j in range(1, 21, 1):
#        sys.stdout.write(str(i*j) + ' ')
#    sys.stdout.write('\n')
    
#zadanie 1
#A=[1/x for x in range(1, 11)]
#print(A)       
#B=[2 ** i for i in range(11)]      
#print(B)      
#C=[x for x in B if x % 4 == 0]
#print(C)

#zadanie 2
#A = [[1, 2, 3, 4],
#    [5, 6, 7, 8],
#    [9, 10, 11, 12],
#    [13, 14, 15, 16]]
#B = [i for i in range(1, 17, 5)]
#print(B)

#zadanie 3 ???
#produkty = {"mąka": "kg",
#"jajka": "sztuki",
#"banany": "sztuki",
#"cukier": "kg",
#"orzechy": "gramy"}
#sztuki = 
    
#print(produkty)
#print(sztuki)