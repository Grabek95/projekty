# -*- coding: utf-8 -*-
"""
ZADANIA PRAKTYCZNE - TYDZIEŃ 1
Struktury danych w Python
"""

# ============================================================================
# ZADANIE 1.1: LISTA ZAKUPÓW
# ============================================================================
# Cel: Nauczyć się operacji na listach

def lista_zakupow():
    """
    Program do zarządzania listą zakupów.
    Funkcje: dodaj, usuń, wyświetl, sortuj
    """
    zakupy = []  # Pusta lista na początek

    while True:
        print("\n" + "="*50)
        print("LISTA ZAKUPÓW - MENU")
        print("="*50)
        print("1. Dodaj produkt")
        print("2. Usuń produkt")
        print("3. Wyświetl listę")
        print("4. Posortuj alfabetycznie")
        print("5. Wyjście")
        print("="*50)

        wybor = input("Wybierz opcję (1-5): ")

        if wybor == '1':
            # TODO: Napisz kod dodający produkt do listy
            # Podpowiedź: użyj input() i lista.append()
            produkt = input("Podaj nazwę produktu: ")
            zakupy.append(produkt)
            print(f"✓ Dodano: {produkt}")

        elif wybor == '2':
            # TODO: Napisz kod usuwający produkt
            # Podpowiedź: użyj lista.remove() lub lista.pop()
            if len(zakupy) == 0:
                print("Lista jest pusta!")
            else:
                print("Aktualna lista:", zakupy)
                produkt = input("Podaj nazwę produktu do usunięcia: ")
                if produkt in zakupy:
                    zakupy.remove(produkt)
                    print(f"✓ Usunięto: {produkt}")
                else:
                    print("Produkt nie istnieje na liście!")

        elif wybor == '3':
            # TODO: Wyświetl listę
            print("\n" + "-"*50)
            print("LISTA ZAKUPÓW:")
            print("-"*50)
            if len(zakupy) == 0:
                print("Lista jest pusta!")
            else:
                for i, produkt in enumerate(zakupy, 1):
                    print(f"{i}. {produkt}")
            print("-"*50)

        elif wybor == '4':
            # TODO: Posortuj listę alfabetycznie
            # Podpowiedź: użyj lista.sort() lub sorted()
            zakupy.sort()
            print("✓ Lista posortowana alfabetycznie")

        elif wybor == '5':
            print("Do widzenia!")
            break

        else:
            print("Nieprawidłowa opcja!")


# ============================================================================
# ZADANIE 1.2: SŁOWNIK PRODUKTÓW
# ============================================================================
# Cel: Nauczyć się operacji na słownikach

def slownik_produktow():
    """
    Program zarządzający cenami produktów.
    Słownik: {'nazwa produktu': cena}
    """
    produkty = {
        'Laptop': 4999.00,
        'Monitor': 1299.00,
        'Mysz': 129.00
    }

    def dodaj_produkt():
        """Dodaj nowy produkt do słownika"""
        # TODO: Pobierz nazwę i cenę, dodaj do słownika
        nazwa = input("Nazwa produktu: ")
        cena = float(input("Cena produktu: "))
        produkty[nazwa] = cena
        print(f"✓ Dodano: {nazwa} - {cena} PLN")

    def usun_produkt():
        """Usuń produkt ze słownika"""
        # TODO: Usuń produkt używając del lub pop()
        nazwa = input("Nazwa produktu do usunięcia: ")
        if nazwa in produkty:
            del produkty[nazwa]
            print(f"✓ Usunięto: {nazwa}")
        else:
            print("Produkt nie istnieje!")

    def wyswietl_produkty():
        """Wyświetl wszystkie produkty"""
        # TODO: Iteruj po słowniku i wyświetl produkty
        print("\n" + "-"*50)
        print("PRODUKTY I CENY:")
        print("-"*50)
        for nazwa, cena in produkty.items():
            print(f"{nazwa:20} {cena:10.2f} PLN")
        print("-"*50)

    def najtanszy_produkt():
        """Znajdź najtańszy produkt"""
        # TODO: Użyj min() z key=lambda
        if produkty:
            nazwa = min(produkty, key=produkty.get)
            print(f"Najtańszy: {nazwa} - {produkty[nazwa]} PLN")
        else:
            print("Brak produktów!")

    def najdrozszy_produkt():
        """Znajdź najdroższy produkt"""
        # TODO: Użyj max() z key=lambda
        if produkty:
            nazwa = max(produkty, key=produkty.get)
            print(f"Najdroższy: {nazwa} - {produkty[nazwa]} PLN")
        else:
            print("Brak produktów!")

    # Menu główne
    while True:
        print("\n" + "="*50)
        print("ZARZĄDZANIE PRODUKTAMI")
        print("="*50)
        print("1. Dodaj produkt")
        print("2. Usuń produkt")
        print("3. Wyświetl wszystkie")
        print("4. Najtańszy produkt")
        print("5. Najdroższy produkt")
        print("6. Wyjście")

        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            dodaj_produkt()
        elif wybor == '2':
            usun_produkt()
        elif wybor == '3':
            wyswietl_produkty()
        elif wybor == '4':
            najtanszy_produkt()
        elif wybor == '5':
            najdrozszy_produkt()
        elif wybor == '6':
            break


# ============================================================================
# ZADANIE 1.3: ANALIZA ZAMÓWIEŃ
# ============================================================================
# Cel: Praca z listą tuple, obliczenia

def analiza_zamowien():
    """
    Analiza zamówień sklepu.
    Format: (nazwa_produktu, cena_jednostkowa, ilosc)
    """
    zamowienia = [
        ('Laptop Dell XPS 15', 4999.00, 2),
        ('Monitor Samsung 27"', 1299.00, 3),
        ('Mysz bezprzewodowa', 129.00, 5),
        ('Klawiatura mechaniczna', 449.00, 2),
        ('Monitor Samsung 27"', 1299.00, 1),  # Duplikat produktu
        ('Laptop Dell XPS 15', 4999.00, 1),   # Duplikat produktu
    ]

    # TODO 1: Oblicz sumę wszystkich zamówień
    # Podpowiedź: suma = cena * ilosc dla każdego zamówienia
    suma_zamowien = sum(cena * ilosc for _, cena, ilosc in zamowienia)
    print(f"Suma wszystkich zamówień: {suma_zamowien:.2f} PLN")

    # TODO 2: Oblicz średnią cenę produktu
    srednia_cena = sum(cena for _, cena, _ in zamowienia) / len(zamowienia)
    print(f"Średnia cena produktu: {srednia_cena:.2f} PLN")

    # TODO 3: Znajdź najczęściej zamawiany produkt
    # Podpowiedź: użyj słownika do zliczania
    licznik_produktow = {}
    for produkt, _, ilosc in zamowienia:
        if produkt in licznik_produktow:
            licznik_produktow[produkt] += ilosc
        else:
            licznik_produktow[produkt] = ilosc

    najczestszy = max(licznik_produktow, key=licznik_produktow.get)
    print(f"Najczęściej zamawiany: {najczestszy} ({licznik_produktow[najczestszy]} szt.)")

    # TODO 4: Wyświetl top 3 najdroższych zamówień
    print("\nTop 3 najdroższych zamówień:")
    posortowane = sorted(zamowienia, key=lambda x: x[1] * x[2], reverse=True)
    for i, (produkt, cena, ilosc) in enumerate(posortowane[:3], 1):
        wartosc = cena * ilosc
        print(f"{i}. {produkt}: {wartosc:.2f} PLN ({ilosc} szt. x {cena:.2f})")


# ============================================================================
# URUCHOMIENIE PROGRAMU
# ============================================================================

if __name__ == "__main__":
    print("ZADANIA TYDZIEŃ 1 - STRUKTURY DANYCH")
    print("="*50)
    print("1. Lista zakupów")
    print("2. Słownik produktów")
    print("3. Analiza zamówień")
    print("="*50)

    wybor = input("Które zadanie chcesz uruchomić? (1-3): ")

    if wybor == '1':
        lista_zakupow()
    elif wybor == '2':
        slownik_produktow()
    elif wybor == '3':
        analiza_zamowien()
    else:
        print("Nieprawidłowy wybór!")


# ============================================================================
# DODATKOWE WYZWANIE (opcjonalne)
# ============================================================================
#
# Stwórz program łączący wszystkie trzy zadania:
#
# 1. Słownik produktów (nazwa -> cena)
# 2. Lista zakupów (produkty do kupienia)
# 3. Kalkulator koszyka:
#    - Dodaj produkty z listy zakupów
#    - Podaj ilość każdego
#    - Oblicz sumę do zapłaty
#    - Wyświetl paragon
#
# Przykład:
# Produkty: {'Chleb': 3.50, 'Mleko': 4.20, 'Jajka': 12.00}
# Lista zakupów: ['Chleb', 'Mleko', 'Jajka']
# Ilości: Chleb x2, Mleko x1, Jajka x1
#
# PARAGON:
# Chleb       2 x   3.50 =   7.00 PLN
# Mleko       1 x   4.20 =   4.20 PLN
# Jajka       1 x  12.00 =  12.00 PLN
# --------------------------------
# SUMA:                     23.20 PLN
#
# ============================================================================
