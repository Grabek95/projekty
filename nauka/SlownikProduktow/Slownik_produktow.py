# slownik_produktow.py
# Mój drugi program - slownik produktów
# Data: 9 grudnia 2025

products = {}

def show_menu():
    # Wyświetlanie menu listy produktów
    print("\n" + "="*31)
    print(" "*5 + "=== LISTA PRODUKTÓW ===")
    print("="*31)
    print("1. Dodaj produkt.")
    print("2. Usuń produkt.")
    print("3. Edytuj produkt.")
    print("4. Posortuj produkty.")
    print("5. Pokaż produkt z najwyższą ceną.")
    print("6. Pokaż produkt z najniższą ceną.")
    print("7. Pokaż tylko produkt z kategorii: ")
    print("8. Zapisz do pliku.")
    print("9. Wyjście.")

def add_product(): # funkcja dodaj produkt do słownika

    product = input("Podaj nazwę produktu: ").lower().strip() # traktuje "Mleko" i "mleko" tak samo
    if product in products:
        print("Produkt już istnieje!") # walidacja czy produkt istnieje w slowniku
        return
    try: # try/except sprawdza czy int jest intem, a float floatem, 
        # w innym przyupadku wyrzuca błąd i cofa
        quantity = int(input("Podaj ilość produktów: "))
        if quantity <= 0: 
            print("Ilość nie może być mniejsza lub równa 0!") # walidacja czy ilosc jest mniejsza lub rowna 0
            return
        price = float(input("Podaj cenę produktu: "))
        if price <= 0:
            print("Cena nie może być mniejsza lub równa 0!") # walidacja czy cena jest mniejsza lub rowna 0
            return
    except ValueError: # ten except sprawia czy jest poprawna konwersja
        print("Niepoprawna wartość! Ilość powinna być liczbą całkowitą, a cena liczbą!")
        return
    category = input("Podaj kategorię produktu: ").lower().strip()

    products[product] = {
        "cena": price,
        "ilość": quantity,
        "kategoria": category
    }

    print("Produkt dodany pomyślnie!")

def delete_product():
    product = input("Podaj nazwę produktu do usunięcia: ").lower().strip()
    if product not in products:
        print("Produkt nie istnieje w słowniku!")
        return
    
    del products[product]
    print("Usunięto produkt ze słownika!")

def show_products(): # pokazywanie produktów
    if not products:
        print("Słownik produktów jest pusty!")
        return
    
    print("Twój słownik produktów:\n")
    for indeks, (nazwa, dane) in enumerate(products.items(), start=1):
        print(f'{indeks}. {nazwa}: "cena": {dane["cena"]}, '
            f'"ilość": {dane["ilość"]}, "kategoria": {dane["kategoria"]}'
        )

def sort_products(): # sortowanie produtków
    if not products:
        print("Słownik produktów jest pusty\nSortowanie niemożliwe!")
        return
    
    lambda: nazwa
    sorted_items = sorted(products.items(), key = lambda)

    print("Posortowany słownik produktów\n")
    for indeks, (nazwa, dane) in enumerate(sorted_items, start=1):
        print(f'{indeks}. {nazwa}: "cena": {dane["cena"]}, '
            f'"ilość": {dane["ilość"]}, {dane["kategoria"]}'
            )