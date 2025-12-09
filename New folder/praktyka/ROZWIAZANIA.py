# -*- coding: utf-8 -*-
"""
ROZWIĄZANIA DO ĆWICZEŃ 1-3
⚠️ NIE ZAGLĄDAJ OD RAZU! Najpierw spróbuj sam! ⚠️
"""

print("=" * 60)
print("ROZWIĄZANIA - NIE ZAGLĄDAJ PRZED ZROBIENIEM ĆWICZEŃ!")
print("=" * 60)
print()

# ============================================================
# ROZWIĄZANIE ĆWICZENIE 1: OWOCE
# ============================================================

def rozwiazanie_1():
    print("\n" + "="*60)
    print("ROZWIĄZANIE ĆWICZENIE 1: LISTA OWOCÓW")
    print("="*60 + "\n")

    owoce = []

    # Sposób 1: Trzy oddzielne input()
    owoc1 = input("Podaj pierwszy owoc: ")
    owoce.append(owoc1)

    owoc2 = input("Podaj drugi owoc: ")
    owoce.append(owoc2)

    owoc3 = input("Podaj trzeci owoc: ")
    owoce.append(owoc3)

    print(f"\nTwoja lista: {owoce}")
    print(f"Łącznie: {len(owoce)} owoce/ów")

    # Sposób 2 (lepszy): Użycie pętli
    print("\n--- ALTERNATYWNE ROZWIĄZANIE Z PĘTLĄ ---")
    owoce2 = []
    for i in range(3):
        owoc = input(f"Podaj owoc {i+1}: ")
        owoce2.append(owoc)
    print(f"Lista: {owoce2}")


# ============================================================
# ROZWIĄZANIE ĆWICZENIE 2: KOLORY
# ============================================================

def rozwiazanie_2():
    print("\n" + "="*60)
    print("ROZWIĄZANIE ĆWICZENIE 2: ULUBIONE KOLORY")
    print("="*60 + "\n")

    kolory = []

    for i in range(5):
        kolor = input(f"Kolor {i+1}: ")

        if kolor.lower() == 'stop':
            print("Przerwano dodawanie.")
            break

        # To jest kluczowa linijka!
        kolory.append(kolor)

    print(f"\nTwoje kolory: {kolory}")

    # Wyświetlanie
    for kolor in kolory:
        print(f"- {kolor}")

    # Bonus
    if 'czerwony' in [k.lower() for k in kolory]:
        print("✓ Czerwony jest na liście!")
    else:
        print("✗ Czerwonego nie ma")


# ============================================================
# ROZWIĄZANIE ĆWICZENIE 3: LICZBY
# ============================================================

def rozwiazanie_3():
    print("\n" + "="*60)
    print("ROZWIĄZANIE ĆWICZENIE 3: KALKULATOR LICZB")
    print("="*60 + "\n")

    liczby = []

    while True:
        wejscie = input("Podaj liczbę (0 = koniec): ")
        liczba = float(wejscie)

        if liczba == 0:
            break

        # Kluczowa linijka!
        liczby.append(liczba)
        print(f"Dodano! Lista: {liczby}")

    if len(liczby) > 0:
        print(f"\nLiczby: {liczby}")

        # Obliczenia
        suma = sum(liczby)
        srednia = suma / len(liczby)
        najmniejsza = min(liczby)
        najwieksza = max(liczby)

        print(f"Suma: {suma}")
        print(f"Średnia: {srednia}")
        print(f"Najmniejsza: {najmniejsza}")
        print(f"Największa: {najwieksza}")


# ============================================================
# MENU
# ============================================================

if __name__ == "__main__":
    print("\nKtóre rozwiązanie chcesz zobaczyć?")
    print("1 - Ćwiczenie 1 (owoce)")
    print("2 - Ćwiczenie 2 (kolory)")
    print("3 - Ćwiczenie 3 (liczby)")
    print("4 - Wszystkie")

    wybor = input("\nWybór: ")

    if wybor == '1':
        rozwiazanie_1()
    elif wybor == '2':
        rozwiazanie_2()
    elif wybor == '3':
        rozwiazanie_3()
    elif wybor == '4':
        rozwiazanie_1()
        rozwiazanie_2()
        rozwiazanie_3()
    else:
        print("Nieprawidłowy wybór!")

    print("\n" + "="*60)
    print("PAMIĘTAJ: Najlepiej się uczysz robiąc błędy!")
    print("Nie kopiuj rozwiązań - próbuj sam, nawet jeśli nie wychodzi!")
    print("="*60)
