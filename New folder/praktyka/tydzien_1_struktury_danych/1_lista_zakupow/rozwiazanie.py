"""
ROZWIĄZANIE ZADANIA 1.1: Lista zakupów
======================================

WAŻNE: To jest kompletne rozwiązanie.
Zaglądaj tu TYLKO gdy kompletnie utkniesz!
Najpierw spróbuj sam!
"""


def wyswietl_menu():
    """Wyświetla menu opcji"""
    print("\n" + "="*30)
    print("=== LISTA ZAKUPÓW ===")
    print("="*30)
    print("1. Dodaj produkt")
    print("2. Usuń produkt")
    print("3. Wyświetl listę")
    print("4. Posortuj alfabetycznie")
    print("5. Wyjście")


def dodaj_produkt(zakupy):
    """Dodaje produkt do listy zakupów"""
    nazwa = input("Podaj nazwę produktu: ")
    zakupy.append(nazwa)
    print(f"Dodano produkt: {nazwa}")


def usun_produkt(zakupy):
    """Usuwa produkt z listy zakupów"""
    # Sprawdzenie czy lista jest pusta
    if len(zakupy) == 0:
        print("Lista jest pusta!")
        return

    nazwa = input("Podaj nazwę produktu do usunięcia: ")

    # Sprawdzenie czy produkt istnieje
    if nazwa in zakupy:
        zakupy.remove(nazwa)
        print(f"Usunięto produkt: {nazwa}")
    else:
        print("Produkt nie znaleziony!")


def wyswietl_liste(zakupy):
    """Wyświetla wszystkie produkty z listy"""
    if len(zakupy) == 0:
        print("Lista jest pusta!")
        return

    print("Twoja lista zakupów:")
    for index, produkt in enumerate(zakupy, start=1):
        print(f"{index}. {produkt}")


def sortuj_liste(zakupy):
    """Sortuje listę alfabetycznie"""
    zakupy.sort()
    print("Lista została posortowana!")


def main():
    """Główna funkcja programu"""
    zakupy = []

    while True:
        wyswietl_menu()
        wybor = input("\nWybierz opcję (1-5): ")

        if wybor == "1":
            dodaj_produkt(zakupy)
        elif wybor == "2":
            usun_produkt(zakupy)
        elif wybor == "3":
            wyswietl_liste(zakupy)
        elif wybor == "4":
            sortuj_liste(zakupy)
        elif wybor == "5":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór! Wybierz opcję 1-5.")


if __name__ == "__main__":
    main()
