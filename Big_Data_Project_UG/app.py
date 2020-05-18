from WebScrapping import WebScrapper
from AppSettings import AppSettings
from DataAnalyzer import DataAnalyzer

# TODO squash commits wyjebka elo

# kolekcja o nazwie drony
# cana : liczba

# kolekcja o nazwie gopro
# cana : liczba

# 1 WEB SKRAPUJEMY
# 2 ZAPISUJEMY DO BAZY
# 3 ZCZYTUJEMY BO Wymagane
# 4 Uzywamy na wykresiku

drony_ceny = [123, 23, 123, 22, 313]
drony_popularnosc = [1223, 223, 44, 4, 4]
lista_tupelkow = []

for i in range(len(drony_ceny) - 1):
    lista_tupelkow.append((drony_ceny[i], drony_popularnosc[i]))

print(lista_tupelkow)

# multiple_series = {
#     'cena': pandas.Series(drony_ceny, index=['1', '2', '2', '3', '4']),
#     'ilosc_osob': pandas.Series(drony_popularnosc, index=['1', '2', '2', '3', '4'])
# }
# data_frame = pandas.DataFrame(multiple_series)
# data_frame.plot(x='cena', y='ilosc_osob', kind='bar', title='Drony')
# plot.show()

DataAnalyzer.analyze_data(lista_tupelkow, 'cena', 'ilosc_osob', 'dronne drony')
