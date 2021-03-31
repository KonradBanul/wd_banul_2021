class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka = jednostka
        self.cena_jed = cena_jed
    def wyświetl_produkt(self):
        return self.nazwa_produktu + " " + str(self.ilosc) + " " + self.jednostka + " " + str(self.cena_jed) + " szt." 
    def ile_produktu(self):
        return "Ma być " + str(self.ilosc) + " " + self.jednostka
    def ile_kosztuje(self):
        ile = self.ilosc * self.cena_jed 
        return str(ile) + " zł"
obiekt = NaZakupy('marchew', 4, 'kg', 3)
print(obiekt.wyświetl_produkt())
print(obiekt.ile_produktu())
print(obiekt.ile_kosztuje())
