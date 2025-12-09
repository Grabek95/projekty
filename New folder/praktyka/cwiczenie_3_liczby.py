# -*- coding: utf-8 -*-
"""
ĆWICZENIE 3: Kalkulator liczb
Czas: 10-15 minut
Cel: append() + obliczenia matematyczne
"""

print("=" * 50)
print("ĆWICZENIE 3: KALKULATOR LICZB")
print("=" * 50)
print()

# Tworzymy pustą listę na liczby
liczby = []

print("Dodaj liczby, a potem obliczę ich sumę i średnią!")
print("(wpisz '0' aby zakończyć)")
print()

# TODO: Pętla która dodaje liczby do listy
# Wskazówka: użyj while True i break

while True:
    # Pobieramy liczbę od użytkownika
    wejscie = input("Podaj liczbę (0 = koniec): ")

    # Konwertujemy na liczbę
    liczba = float(wejscie)

    # Jeśli 0, kończymy
    if liczba == 0:
        print("Zakończono dodawanie.")
        break

    # TODO: Dodaj liczbę do listy
    # Twój kod tutaj:
    liczby.append(liczba)

    print(f"Dodano! Aktualna lista: {liczby}")

print()
print("=" * 50)
print("WYNIKI:")
print("=" * 50)

# Sprawdzamy czy lista nie jest pusta
if len(liczby) == 0:
    print("Nie dodałeś żadnych liczb!")
else:
    # Wyświetlamy wszystkie liczby
    print(f"Twoje liczby: {liczby}")
    print()

    # TODO: Oblicz sumę wszystkich liczb
    # Wskazówka: użyj funkcji sum()
    suma = sum(liczby)  # Zmień to na sum(liczby)
    print(f"Suma: {suma}")

    # TODO: Oblicz średnią
    # Wskazówka: średnia = suma / ilość liczb
    srednia = suma / len(liczby) # Oblicz średnią
    print(f"Średnia: {srednia}")

    # TODO: Znajdź najmniejszą liczbę
    # Wskazówka: użyj funkcji min()
    najmniejsza = min(liczby)  # Zmień to
    print(f"Najmniejsza: {najmniejsza}")

    # TODO: Znajdź największą liczbę
    # Wskazówka: użyj funkcji max()
    najwieksza = max(liczby )# Zmień to
    print(f"Największa: {najwieksza}")

print()
print("Gratulacje! Ukończyłeś ćwiczenie 3! 🎉")
