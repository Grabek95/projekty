# lista_zakupow.py
# Mój pierwszy program - lista zakupów
# Data: 1 grudnia 2025

def show_menu():
    """Wyświetlanie menu opcji"""
    print("\n" + "="*31)
    print(" "*5 + "=== LISTA ZAKUPÓW ===")
    print("="*31)
    print("1. Dodaj produkt")
    print("2. Usuń produkt")
    print("3. Wyświetl listę")
    print("4. Posortuj alfabetycznie")
    print("5. Wyjście")
    print("6. Licznik")
    print("7. Wyczyść listę")
    print("8. Zapisz do .txt")


def add_product():
    product = input("Podaj produkt: ").lower()

    if product not in zakupy:
        zakupy.append(product)
        print(f"Dodano {product} do listy.")
    else:
        print("Produkt już istnieje na liście zakupów!")

def delete_product():
    if not zakupy:
        print("Lista zakupów jest pusta!")
        return
        
    product = input("Podaj produkt do usunięcia: ").lower()

    if product in zakupy:
        
        zakupy.remove(product)
        print(f"Produkt {product} został usunięty!")

    else:
        print("Produkt nie znaleziony!")

def show_list():
    if not zakupy:
        print("Lista zakupów jest pusta!")
        return

    print("Twoja lista zakupów:\n")
    for indeks, element in enumerate(zakupy, start=1):
        print(f"{indeks}. {element}")

def sort_list():
    if not zakupy:
        print("Lista zakupów jest pusta!\nSortowanie niemożliwe!")
        return
    
    zakupy.sort()
    print("Posrotowana lista zakupów!")

def counter():
    if not zakupy:
        print("Lista zakupów jest pusta\nPrzeliczenie niemożliwe!")
        return
    count = len(zakupy)
    print(f"Liczba produktów w liście to: {count}")

def clear_list():
    if not zakupy:
        print("Lista zakupów jest pusta\nWyczyszczenie listy niemożliwe!")
        return
    zakupy.clear()
    print("Lista została wyczyszczona!")

def save_to_txt():
    if not zakupy:
        print("Lista zakupów jest pusta!\nZapis do pliku niemożliwy!")
        return
    
    with open ("zakupy.txt", "w", encoding = "utf-8") as plik:
        for indeks, element in enumerate(zakupy, start=1):
            plik.write(f"{indeks}. {element}\n")

    print("Zapisano do pliku!")

zakupy = [] # pusta lista zakupów

def main():

    while True:
        show_menu()

        choice = input("Wybierz opcję: ")

        if choice == "1": # dodaj produkt
            add_product() 
        elif choice == "2": # usuń produkt
            delete_product() 
        elif choice == "3": # pokaż listę
            show_list()
        elif choice == "4": # posortuj listę
            sort_list()
        elif choice == "5": # wyjście
            print("Do widzenia!")
            break
        elif choice == "6": # licznik
            counter()
        elif choice == "7": # wyczyść listę
            clear_list()
        elif choice == "8": # zapis do pliku
            save_to_txt()
        else:
            print("Nieprawidłowa opcja!")

        input("\nNaciśnij Enter, aby kontynuować...")

if __name__ == "__main__":
    main()