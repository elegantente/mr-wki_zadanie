#Pytanie - Po jakim czasie mam gwarancję że na tym kijku nie ma żadnej mrówki ? 

#Mój tok myślowy::
# mrówki które się zderzają odbijają się ale z punktu obserwatora nie ma to żadnego znaczenia i efekt jest taki sam jakby przez siebie przechodziły więc można założyć że są jak "duchy"
# liczymy maksymalny czas spadniecia wszystkich mrówek więc wystarczy policzyć maxymalny czas przejścia mrówki z jednego do drugiego końca kijka, więc liczba mrówek nie ma znacznia 



def mrówki(ilość_mrówek, prędkość_mrowki, kijek):

    maksymalny_czas = kijek / prędkość_mrowki  # maksymalny czas na przebycie jakiejkolwiek długości = długość / prędkość
    return maksymalny_czas

maks_czas = mrówki(3333, 0.1, 1)

print(f"po {maks_czas} sekundach na kijku nie będzie żadnej mrówki")