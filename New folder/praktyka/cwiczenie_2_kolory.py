# -*- coding: utf-8 -*-
"""
ĆWICZENIE 2: Ulubione kolory
Czas: 5-10 minut
Cel: Nauczyć się append() + warunek if
"""

print("=" * 50)
print("ĆWICZENIE 2: ULUBIONE KOLORY")
print("=" * 50)
print()

# Tworzymy pustą listę
kolory = []

print("Dodaj 5 ulubionych kolorów!")
print("(jeśli wpiszesz 'stop', program się zakończy)")
print()

# TODO: Napisz pętlę która 5 razy zapyta o kolor
# Wskazówka: użyj for i range(5)

# Przykład dla pierwszego koloru:

    # TODO: Dodaj kolor do listy używając append()
    # Twój kod tutaj:
for i in range(5):
    kolor = input(f"Kolor {i+1}: ")
    kolory.append(kolor)
    print(f"Dodano kolor {kolor}")
    print(f"Aktualna lista kolorów: {kolory}")

print()
print("=" * 50)
print("TWOJE ULUBIONE KOLORY:")
print("=" * 50)

# TODO: Wyświetl wszystkie kolory
# Wskazówka: użyj pętli for
for kolor in kolory:
    print(f"- {kolor}")

print()
print(f"Zapisałeś {len(kolory)} kolorów!")

# BONUS: Sprawdź czy 'czerwony' jest na liście
print()
print("BONUS: Sprawdzamy czy 'czerwony' jest na liście...")
if 'czerwony' in kolory or 'Czerwony' in kolory:
    print("✓ TAK! Czerwony jest na liście!")
else:
    print("✗ NIE, czerwonego nie ma na liście.")

print()
print("Sprawdzamy czy mamy 5 kolorów...")
if len(kolory) == 5:
    print("TAK")
else: 
    print("NIE")