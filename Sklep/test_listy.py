# -*- coding: utf-8 -*-
"""
INTERAKTYWNY TEST - Metody listy
Krok po kroku zrozumienie append()
"""

# Konfiguracja UTF-8 dla Windows
import sys
import os
if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    try:
        os.system('chcp 65001 >nul 2>&1')
    except:
        pass

print("=" * 60)
print("TEST 1: Tworzenie pustej listy")
print("=" * 60)

# Tworzymy pustą listę
zakupy = []
print(f"Pusta lista: {zakupy}")
print(f"Długość listy: {len(zakupy)}")
print()

print("=" * 60)
print("TEST 2: Dodawanie pierwszego elementu")
print("=" * 60)

# Dodajemy pierwszy element
zakupy.append("Chleb")
print(f"Po dodaniu 'Chleb': {zakupy}")
print(f"Długość listy: {len(zakupy)}")
print()

print("=" * 60)
print("TEST 3: Dodawanie kolejnych elementów")
print("=" * 60)

# Dodajemy więcej elementów
zakupy.append("Mleko")
print(f"Po dodaniu 'Mleko': {zakupy}")

zakupy.append("Jajka")
print(f"Po dodaniu 'Jajka': {zakupy}")

zakupy.append("Masło")
print(f"Po dodaniu 'Masło': {zakupy}")

print(f"Długość listy: {len(zakupy)}")
print()

print("=" * 60)
print("TEST 4: Dostęp do elementów listy")
print("=" * 60)

# Indeksowanie (numerowanie od 0!)
print(f"Pierwszy element (indeks 0): {zakupy[0]}")
print(f"Drugi element (indeks 1): {zakupy[1]}")
print(f"Ostatni element (indeks -1): {zakupy[-1]}")
print()

print("=" * 60)
print("TEST 5: Iteracja po liście")
print("=" * 60)

# Sposób 1: Prosta pętla
print("\nWersja 1 - Prosta pętla:")
for produkt in zakupy:
    print(f"- {produkt}")

# Sposób 2: Z numeracją
print("\nWersja 2 - Z numeracją (enumerate):")
for i, produkt in enumerate(zakupy):
    print(f"{i}. {produkt}")

# Sposób 3: Z numeracją od 1
print("\nWersja 3 - Numeracja od 1:")
for i, produkt in enumerate(zakupy, 1):
    print(f"{i}. {produkt}")

print()

print("=" * 60)
print("TEST 6: Sprawdzanie czy element jest w liście")
print("=" * 60)

# Operator 'in'
if "Mleko" in zakupy:
    print("✓ Mleko jest na liście!")
else:
    print("✗ Mleka nie ma na liście")

if "Ser" in zakupy:
    print("✓ Ser jest na liście!")
else:
    print("✗ Sera nie ma na liście")

print()

print("=" * 60)
print("TEST 7: Inne przydatne metody")
print("=" * 60)

# count() - ile razy element występuje
zakupy.append("Mleko")  # Dodajemy duplikat
print(f"Lista z duplikatem: {zakupy}")
print(f"Ile razy 'Mleko' występuje: {zakupy.count('Mleko')}")

# index() - na jakiej pozycji jest element
pozycja = zakupy.index("Jajka")
print(f"'Jajka' są na pozycji: {pozycja}")

# remove() - usuń pierwszy pasujący element
zakupy.remove("Mleko")
print(f"Po usunięciu pierwszego 'Mleko': {zakupy}")

# pop() - usuń i zwróć ostatni element
ostatni = zakupy.pop()
print(f"Usunięty ostatni element: {ostatni}")
print(f"Lista po pop(): {zakupy}")

# insert() - wstaw na konkretną pozycję
zakupy.insert(1, "Ser")  # Wstaw "Ser" na pozycję 1
print(f"Po wstawieniu 'Ser' na pozycję 1: {zakupy}")

# sort() - sortuj alfabetycznie
zakupy.sort()
print(f"Po sortowaniu: {zakupy}")

# reverse() - odwróć kolejność
zakupy.reverse()
print(f"Po odwróceniu: {zakupy}")

# clear() - wyczyść całą listę
kopia = zakupy.copy()  # Najpierw zrób kopię
zakupy.clear()
print(f"Po clear(): {zakupy}")
print(f"Kopia (zachowana): {kopia}")

print()

print("=" * 60)
print("TEST 8: List comprehension (zaawansowane)")
print("=" * 60)

# Tworzenie listy w jednej linii
liczby = [1, 2, 3, 4, 5]
kwadraty = [x**2 for x in liczby]
print(f"Liczby: {liczby}")
print(f"Kwadraty: {kwadraty}")

# Filtrowanie
parzyste = [x for x in liczby if x % 2 == 0]
print(f"Parzyste: {parzyste}")

print()
print("=" * 60)
print("KONIEC TESTÓW!")
print("=" * 60)
