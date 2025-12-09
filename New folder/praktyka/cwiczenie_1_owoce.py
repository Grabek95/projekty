# -*- coding: utf-8 -*-
"""
ĆWICZENIE 1: Lista owoców
Czas: 5-10 minut
Cel: Nauczyć się podstawowego użycia append()
"""

print("=" * 50)
print("ĆWICZENIE 1: LISTA OWOCÓW")
print("=" * 50)
print()

# Tworzymy pustą listę
owoce = []

print("Dodajemy 3 owoce do listy...")
print()

# TODO: Dodaj swój kod tutaj!
# Instrukcja:
# 1. Poproś użytkownika o nazwę pierwszego owocu (użyj input)
# 2. Dodaj go do listy 'owoce' (użyj append)
# 3. Powtórz dla drugiego i trzeciego owocu

owoc1 = input("Dodaj pierwszy owoc: ")
owoce.append(owoc1)
print(f"Lista po dodaniu: {owoce}")
print()

owoc2 = input("Dodaj drugi owoc: ")
owoce.append(owoc2)
print(f"Lista po dodaniu: {owoce}")
#print()

owoc3 = input("Dodaj trzeci owoc: ")
owoce.append(owoc3)
print(f"Lista po dodaniu: {owoce}")
print()

# Na koniec wyświetl całą listę
print("=" * 50)
print("TWOJA LISTA OWOCÓW:")
print("=" * 50)
for i, owoc in enumerate(owoce, 1):
    print(f"{i}. {owoc}")

print()
print(f"Łącznie masz {len(owoce)} owoce/ów na liście!")
