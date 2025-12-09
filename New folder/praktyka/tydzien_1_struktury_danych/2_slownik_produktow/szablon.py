"""
ZADANIE 1.2: Słownik produktów
===============================

Program do zarządzania produktami (nazwa → cena) używając słownika.

Przeczytaj plik 'zadanie.md' aby poznać szczegóły.
"""


def wyswietl_menu():
    """Wyświetla menu opcji"""
    print("\n" + "="*30)
    print("=== SŁOWNIK PRODUKTÓW ===")
    print("="*30)
    # TODO: Wyświetl opcje 1-6
    print("1. Dodaj produkt")
    print("2. Usuń produkt")
    print("3. Wyświetl wszystkie produkty")
    print("4. Znajdź najtańszy produkt")
    print("5. Znajdź najdroższy produkt")
    print("6. Wyjście")
    print("7. Posortuj słownik.\n")

def dodaj_produkt(produkty):
    """Dodaje produkt do słownika"""
    # TODO: Zapytaj o nazwę produktu
    produkt = input("Podaj produkt: ").lower()

    # TODO: Zapytaj o cenę produktu i zamień na float
    # Wskazówka: cena = float(input(...))
    cena = float(input("Podaj cenę produktu: "))

    # TODO: Dodaj produkt do słownika
    # Wskazówka: produkty[nazwa] = cena
    produkty[produkt] = cena

    # TODO: Wyświetl komunikat z formatowaniem ceny (.2f)
    print(f"Dodano produkt: {produkt} - Cena: {cena:.2f} PLN")


def usun_produkt(produkty):
    """Usuwa produkt ze słownika"""
    # TODO: Sprawdź czy słownik jest pusty
    if len(produkty) == 0:
        print("Słownik produktów jest pusty!")
        return

    # TODO: Zapytaj o nazwę produktu do usunięcia
    produkt = input("Podaj produkt do usunięcia: ").lower()

    # TODO: Sprawdź czy produkt istnieje w słowniku
    # Wskazówka: if nazwa in produkty:
    if produkt in produkty:

        # TODO: Usuń produkt
        # Wskazówka: del produkty[nazwa]
        del produkty[produkt]

        # TODO: Wyświetl komunikat
        print(f"Produkt {produkt} został usunięty ze słownika!")

    # TODO: Obsłuż przypadek gdy produktu nie ma (else)
    else:
        print("Produkt nie istnieje!")


def wyswietl_produkty(produkty):
    """Wyświetla wszystkie produkty"""
    # TODO: Sprawdź czy słownik jest pusty
    if len(produkty) == 0:
        print("Słownik produktów jest pusty")
        return

    # TODO: Wyświetl nagłówek
    print("Lista produktów: ")

    # TODO: Iteruj po słowniku i wyświetl każdy produkt
    # Wskazówka: for nazwa, cena in produkty.items():
    # Format: - Mleko: 3.50 PLN
    for produkt, cena in produkty.items():
        print(f"- {produkt}: {cena:.2f} PLN")


def znajdz_najtanszy(produkty):
    """Znajduje i wyświetla najtańszy produkt"""
    # TODO: Sprawdź czy słownik jest pusty
    if len(produkty) == 0:
        print("Słownik produktów jest pusty")
        return

    # TODO: Znajdź nazwę produktu z minimalną ceną
    # Wskazówka: najtanszy = min(produkty, key=produkty.get)
    najtanszy = min(produkty, key=produkty.get)

    # TODO: Pobierz cenę tego produktu
    # Wskazówka: cena = produkty[najtanszy]
    cena = produkty[najtanszy]

    # TODO: Wyświetl wynik z formatowaniem
    print(f"Najtańszy produkt to: {najtanszy} - Cena: {cena:.2f} PLN")


def znajdz_najdrozszy(produkty):
    """Znajduje i wyświetla najdroższy produkt"""
    # TODO: Sprawdź czy słownik jest pusty
    if len(produkty) == 0:
        print("Słownik produktów jest pusty")
        return

    # TODO: Znajdź nazwę produktu z maksymalną ceną
    # Wskazówka: najdrozszy = max(produkty, key=produkty.get)
    najdrozszy = max(produkty, key=produkty.get)

    # TODO: Pobierz cenę tego produktu
    cena = produkty[najdrozszy]

    # TODO: Wyświetl wynik z formatowaniem
    print(f"Najdroższy produkt to: {najdrozszy} - Cena: {cena:.2f} PLN")

def posortuj_slownik(produkty):
    produkty.sort()



def main():
    """Główna funkcja programu"""

    # TODO: Stwórz pusty słownik produktów
    produkty = {
        
    }

    # TODO: Pętla nieskończona
    while True:

        # TODO: Wyświetl menu
        wyswietl_menu()

        # TODO: Pobierz wybór użytkownika
        choice = input("Wybierz opcję (1-6): ")

        # TODO: Obsłuż wybór (if/elif/else)
        # 1 -> dodaj_produkt(produkty)
        if choice == "1":
            dodaj_produkt(produkty)
        # 2 -> usun_produkt(produkty)
        elif choice == "2":
            usun_produkt(produkty)
        # 3 -> wyswietl_produkty(produkty)
        elif choice == "3":
            wyswietl_produkty(produkty)
        # 4 -> znajdz_najtanszy(produkty)
        elif choice == "4":
            znajdz_najtanszy(produkty)
        # 5 -> znajdz_najdrozszy(produkty)
        elif choice == "5":
            znajdz_najdrozszy(produkty)
        # 6 -> wyświetl "Do widzenia!" i break
        elif choice == "6":
            print("Do widzenia!")
            break
        # 7 -> Posrotuj słownik
        elif choice == "7":
            print("Lista została posortowana.")
        # inne -> "Nieprawidłowy wybór!"
        else:
            print("Nieprawidłowy wybór!")




if __name__ == "__main__":
    main()
