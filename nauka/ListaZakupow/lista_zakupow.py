# lista_zakupow.py
# Mój pierwszy program - lista zakupów
# Data: 1 grudnia 2025

def show_menu():
    """Wyświetlanie menu opcji"""
    print("\n" + "="*30)
    print("=== LISTA ZAKUPÓW ===")
    print*("="*30)
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

    if produkt not in zakupy:
        zakupy.append(product)
        print(f"Dodano {product} do listy.")
    else:
        print("Produkt już istnieje na liście zakupów!")

def delete_product():
    if len(zakupy) == 0:
        print("Lista zakupów jest pusta!")
        return
        
    product = input("Podaj produkt do usunięcia: ").lower()

    if product in zakupy:
        
        zakupy.remove(product)
        print(f"Produkt {product} został usunięty!")

    else:
        print("Produkt nie znaleziony!")





zakupy = [] # pusta lista zakupów

while True:
    print("\n=== LISTA ZAKUPÓW ===")
    print("1. Dodaj produkt")
    print("2. Pokaż listę")
    print("3. Wyjście")

    wybor = input("Wybierz opcję (1-3): ")

    if wybor == "1":
        produkt = input("Nazwa produktu: ")
        zakupy.append(produkt)
        print(f"Dodano: {produkt}")

    elif wybor == "2":
        print("\n Twoja lista: ")
        if zakupy:
            for i, produkt in enumerate(zakupy, 1):
                print(f" {i}.{produkt}")
            else:
                print("Lista jest pusta!")
    elif wybor == "3":
        print("Do widzenia!")
        break
    else:
        print("Niepoprawna opcja!")