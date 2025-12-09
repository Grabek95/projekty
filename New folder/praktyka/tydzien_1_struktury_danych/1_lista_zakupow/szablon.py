"""
ZADANIE 1.1: Lista zakupów
==========================

Program do zarządzania listą zakupów z interaktywnym menu.

Przeczytaj plik 'zadanie.md' aby poznać szczegóły.
"""


def wyswietl_menu():
    """Wyświetla menu opcji"""
    print("\n" + "="*30)
    print("=== LISTA ZAKUPÓW ===")
    print("="*30)
    # TODO: Wyświetl opcje 1-5
    # 1. Dodaj produkt
    print("1. Dodaj produkt")
    # 2. Usuń produkt
    print("2. Usuń produkt")
    # 3. Wyświetl listę
    print("3. Wyświetl listę")
    # 4. Posortuj alfabetycznie
    print("4. Posortuj alfabetycznie")
    # 5. Wyjście
    print("5. Wyjście")
    # 6. Licznik
    print("6. Licznik")
    # 7. Wyczysc liste
    print("7. Wyczyść listę")
    # 8. Zapisz do .txt
    print("8. Zapisz do .txt")






def dodaj_produkt(zakupy):
    """Dodaje produkt do listy zakupów"""
    # TODO: Zapytaj użytkownika o nazwę produktu
    produkt = input("Podaj produkt: ").lower()

    # TODO: Sprawdź czy produkt już istnieje
    if produkt not in zakupy:
        zakupy.append(produkt)
    # TODO: Wyświetl komunikat: "Dodano produkt: {nazwa}"   
        print(f"Dodano produkt: {produkt}")
    else:
        print("Produkt już istnieje na liście zakupów!")

def usun_produkt(zakupy):
    """Usuwa produkt z listy zakupów"""
    # TODO: Sprawdź czy lista jest pusta
    # Jeśli tak, wyświetl "Lista jest pusta!" i zakończ funkcję (return)
    if len(zakupy) == 0:
        print("Lista jest pusta!")
        return

    # TODO: Zapytaj użytkownika o nazwę produktu do usunięcia
    produkt = input("Podaj nazwę produktu do usunięcia: ").lower()

    # TODO: Sprawdź czy produkt istnieje w liście
    # Wskazówka: if produkt in zakupy:
    if produkt in zakupy:

        # TODO: Usuń produkt z listy
        zakupy.remove(produkt)

        # TODO: Wyświetl "Usunięto produkt: {nazwa}"
        print(f"Usunięto produkt: {produkt}")

    # TODO: Obsłuż przypadek gdy produktu nie ma (else)
    # Wyświetl "Produkt nie znaleziony!"
    else:
        print("Produkt nie znaleziony!")



def wyswietl_liste(zakupy):
    """Wyświetla wszystkie produkty z listy"""
    # TODO: Sprawdź czy lista jest pusta
    # Jeśli tak, wyświetl "Lista jest pusta!" i zakończ (return)
    if len(zakupy) == 0:
        print("Lista jest pusta!")
        return

    # TODO: Wyświetl nagłówek "Twoja lista zakupów:"
    print("Twoja lista zakupów:")

    # TODO: Wyświetl produkty z numerami
    # Wskazówka: użyj enumerate(zakupy, start=1)
    for index, produkt in enumerate(zakupy, start=1):
        print(f"{index}. {produkt}")



def sortuj_liste(zakupy):
    """Sortuje listę alfabetycznie"""
    # TODO: Posortuj listę
    # Wskazówka: zakupy.sort()
    zakupy.sort()


    # TODO: Wyświetl "Lista została posortowana!"
    print("Lista została posortowana!")

def licznik_listy(zakupy):
    """Zlicza aktualną listę"""
    licznik = len(zakupy)

    if licznik == 0:
        print("Lista zakupów jest aktualnie pusta!")
    else:
        print(f"Liczba produktów na liście wynosi {licznik}")

def wyczysc_liste(zakupy):
    potwierdzenie = input("Czy na pewno chcesz wyczyścić listę? (tak/nie)").lower()
    if potwierdzenie == "tak": # dodano warunek, który sprawdza czy na pewno chcemy wyczyścić listę
        zakupy.clear() # usuwamy wszystkie elementy listy
        print("Lista została wyczyszczona!")
    else:
        print("Anulowano czysczenie.")

def zapisz_do_txt(zakupy):
    if len(zakupy) == 0:  # ← Sprawdź czy lista pusta
        print("Lista zakupów jest pusta! Nie można zapisać.")
    else:  # ← Zapisz tylko gdy lista NIE jest pusta
        with open('lista_zakupow.txt', 'w', encoding='utf-8') as plik:
            for produkt in zakupy:
                plik.write(produkt + '\n')
        print("Plik został zapisany!")

def main():
    """Główna funkcja programu"""

    # TODO: Stwórz pustą listę zakupów
    zakupy = []

    # TODO: Stwórz pętlę nieskończoną (while True)
    while True:

        # TODO: Wyświetl menu
        # Wskazówka: wywołaj funkcję wyswietl_menu()
        wyswietl_menu()

        # TODO: Pobierz wybór użytkownika
        choice = input("\nWybierz opcję 1-8: \n")


        # TODO: Obsłuż wybór opcji (if/elif/else)
        # Opcja "1" -> wywołaj dodaj_produkt(zakupy)
        if choice == "1":
            dodaj_produkt(zakupy)
        # Opcja "2" -> wywołaj usun_produkt(zakupy)
        elif choice == "2":
            usun_produkt(zakupy)
        # Opcja "3" -> wywołaj wyswietl_liste(zakupy)
        elif choice == "3":
            wyswietl_liste(zakupy)
        # Opcja "4" -> wywołaj sortuj_liste(zakupy)
        elif choice == "4":
            sortuj_liste(zakupy)
        # Opcja "5" -> wyświetl "Do widzenia!" i zakończ (break)
        elif choice == "5":
            print("Do widzenia!")
            break
        # Opcja "6" -> wywołaj wyswietl_licznik(zakupy)
        elif choice == "6":
            licznik_listy(zakupy)
        # Opcja "7" -> wywolaj wyczysc_liste(zakupy)
        elif choice == "7":
            wyczysc_liste(zakupy)
        # Opcja "8" -> wywolaj zapisz_do_txt(zakupy)
        elif choice == "8":
            zapisz_do_txt(zakupy)
        # Inne -> wyświetl "Nieprawidłowy wybór!"
        else:
            print("Nieprawidłowy wybór!")




if __name__ == "__main__":
    main()
