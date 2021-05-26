import numpy as np
import pandas as pd
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

def zad2a():
    print(df[(df.Liczba > 1000)])

def zad2b():
    print(df[(df.Imie == 'KONRAD')])

def zad2c():
    print(df.agg({'Liczba':['sum']}))

def zad2d():
    print(df[(df.Rok >= 2000) & (df.Rok <= 2005)].agg({'Liczba':['sum']}))

def zad2e():
    print(df[(df.Plec == 'K')].agg({'Liczba':['sum']}))
    print(df[(df.Plec == 'M')].agg({'Liczba':['sum']}))

def zad2f():
    print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())

def zad2g():
    print(df[(df.Plec == 'M')].groupby(['Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending=False).iloc[0])
    print(df[(df.Plec == 'K')].groupby(['Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending=False).iloc[0])


#zad2a()
#zad2b()
#zad2c()
#zad2d()
#zad2e()
zad2f()
#zad2g()