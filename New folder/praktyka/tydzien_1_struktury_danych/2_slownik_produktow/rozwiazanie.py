"""
ROZWIĄZANIE ZADANIA 1.2: Słownik produktów
==========================================

WAŻNE: To jest kompletne rozwiązanie.
Zaglądaj tu TYLKO gdy kompletnie utkniesz!
"""


def wyswietl_menu():
    """Wyświetla menu opcji"""
    print("\n" + "="*30)
    print("=== SŁOWNIK PRODUKTÓW ===")
    print("="*30)
    print("1. Dodaj produkt")
    print("2. Usuń produkt")
    print("3. Wyświetl wszystkie produkty")
    print("4. Znajdź najtańszy produkt")
    print("5. Znajdź najdroższy produkt")
    print("6. Wyjście")


def dodaj_produkt(produkty):
    """Dodaje produkt do słownika"""
    nazwa = input("Podaj nazwę produktu: ")
    cena = float(input("Podaj cenę produktu: "))
    produkty[nazwa] = cena
    print(f"Dodano: {nazwa} - {cena:.2f} PLN")


def usun_produkt(produkty):
    """Usuwa produkt ze słownika"""
    if len(produkty) == 0:
        print("Słownik jest pusty!")
        return

    nazwa = input("Podaj nazwę produktu do usunięcia: ")

    if nazwa in produkty:
        del produkty[nazwa]
        print(f"Usunięto: {nazwa}")
    else:
        print("Produkt nie znaleziony!")


def wyswietl_produkty(produkty):
    """Wyświetla wszystkie produkty"""
    if len(produkty) == 0:
        print("Słownik jest pusty!")
        return

    print("Lista produktów:")
    for nazwa, cena in produkty.items():
        print(f"- {nazwa}: {cena:.2f} PLN")


def znajdz_najtanszy(produkty):
    """Znajduje i wyświetla najtańszy produkt"""
    if len(produkty) == 0:
        print("Słownik jest pusty!")
        return

    najtanszy = min(produkty, key=produkty.get)
    cena = produkty[najtanszy]
    print(f"Najtańszy: {najtanszy} - {cena:.2f} PLN")


def znajdz_najdrozszy(produkty):
    """Znajduje i wyświetla najdroższy produkt"""
    if len(produkty) == 0:
        print("Słownik jest pusty!")
        return

    najdrozszy = max(produkty, key=produkty.get)
    cena = produkty[najdrozszy]
    print(f"Najdroższy: {najdrozszy} - {cena:.2f} PLN")


def main():
    """Główna funkcja programu"""
    produkty = {}

    while True:
        wyswietl_menu()
        wybor = input("\nWybierz opcję (1-6): ")

        if wybor == "1":
            dodaj_produkt(produkty)
        elif wybor == "2":
            usun_produkt(produkty)
        elif wybor == "3":
            wyswietl_produkty(produkty)
        elif wybor == "4":
            znajdz_najtanszy(produkty)
        elif wybor == "5":
            znajdz_najdrozszy(produkty)
        elif wybor == "6":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór! Wybierz opcję 1-6.")


if __name__ == "__main__":
    main()
