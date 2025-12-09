# lista_zakupow.py
# Mój pierwszy program - lista zakupów
# Data: 1 grudnia 2025

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