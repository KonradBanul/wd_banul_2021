class CiagAryt:
    a1 = 4
    r = 3
    n = 7
    an = a1 + (n - 1) * r
    def wyświetl_dane(self):
        return "a1=" + str(self.a1) + " r=" + str(self.r) + " n=" + str(self.n) + " an=" + str(self.an)
    def pobierz_parametry(self):
        a1 = input("a1=")
        r = input("r=")
        n = input("n=")
        return a1, r, n
    def suma(self):
        return (self.a1 + self.an) / 2 * self.n 
obiekt = CiagAryt()
#print(obiekt.wyświetl_dane())
#print(obiekt.pobierz_parametry())
print("suma ciągu = " + str(obiekt.suma()))