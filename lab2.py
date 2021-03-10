#zadanie 1
#a = input("Napisz jakieś zdanie: ")
#print(a.count(' '))

#zadanie 2
#import sys
#print("Podaj pierwszą liczbe: ")
#a = sys.stdin.readline()
#print("Podaj drugą liczbę: ")
#b = sys.stdin.readline()
#wynik = int(a) * int(b)
#sys.stdout.write(str(wynik))

#zadanie 3
# operatory porównania
#if liczba1 > liczba2
#if liczba1 <= liczba2
#if liczba1 == liczba2
#if liczba1 != liczba2

#zadanie 4
#a = input('Podaj liczbę: ')
#a = int(a)
#if a < 0:  
#    a = a * (-1)                    
#    print('Wartość bezwzględna = ' + str(a))
#else:
#    print('Wartość bezwzględna = ' + str(a))

#zadanie 5
a = input('Podaj liczbę a: ')
b = input('Podaj liczbę b: ')
c = input('Podaj liczbę c: ')
a = int(a)
b = int(b)
c = int(c)
if a > 0 and a <= 10:
    print('Liczba a zawiera się w przedziale (0,10]')
else:
    print('Liczba a nie zawiera się w przedziale (0,10]')
if a > b:
    print('a > b')
else:
    print('b > a')
if b > c:
    print('b > c')
else:
    print('c > b')