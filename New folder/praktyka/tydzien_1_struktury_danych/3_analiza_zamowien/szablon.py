"""
ZADANIE 1.3: Analiza zamówień
==============================

Analiza danych zamówień (tuple) - obliczanie statystyk.

Przeczytaj plik 'zadanie.md' aby poznać szczegóły.
"""


def wyswietl_zamowienia(zamowienia):
    """Wyświetla listę wszystkich zamówień"""
    print("=== ANALIZA ZAMÓWIEŃ ===\n")
    print("LISTA ZAMÓWIEŃ:")

    # TODO: Iteruj po zamówieniach z numeracją
    # Wskazówka: for i, (nazwa, cena, ilosc) in enumerate(zamowienia, start=1):


        # TODO: Oblicz wartość pozycji (cena * ilosc)


        # TODO: Wyświetl w formacie:
        # 1. Laptop: 3500.00 PLN x 2 szt. = 7000.00 PLN



def oblicz_statystyki(zamowienia):
    """Oblicza i wyświetla statystyki zamówień"""

    print("\n" + "="*40)
    print("STATYSTYKI:")
    print("="*40)

    # 1. LICZBA ZAMÓWIEŃ
    # TODO: Oblicz liczbę zamówień
    # Wskazówka: len(zamowienia)


    # TODO: Wyświetl liczbę zamówień



    # 2. SUMA CEN JEDNOSTKOWYCH
    # TODO: Oblicz sumę wszystkich cen (bez uwzględniania ilości)
    # Wskazówka: suma = 0, potem w pętli suma += cena


    # TODO: Wyświetl sumę cen



    # 3. ŚREDNIA CENA
    # TODO: Oblicz średnią cenę produktu
    # Wskazówka: srednia = suma_cen / liczba_zamowien


    # TODO: Wyświetl średnią



    # 4. NAJTAŃSZY PRODUKT
    # TODO: Znajdź produkt o najmniejszej cenie
    # Wskazówka: Użyj pętli i sprawdzaj if cena < min_cena


    # TODO: Wyświetl najtańszy produkt (nazwa i cena)



    # 5. NAJDROŻSZY PRODUKT
    # TODO: Znajdź produkt o największej cenie
    # Wskazówka: Podobnie jak najtańszy, ale if cena > max_cena


    # TODO: Wyświetl najdroższy produkt



    # 6. CAŁKOWITA WARTOŚĆ ZAMÓWIEŃ
    # TODO: Oblicz sumę (cena * ilosc) dla wszystkich zamówień


    # TODO: Wyświetl całkowitą wartość



    # 7. NAJCZĘŚCIEJ ZAMAWIANY PRODUKT
    # TODO: Znajdź produkt o największej ilości


    # TODO: Wyświetl produkt najczęściej zamawiany




def main():
    """Główna funkcja programu"""

    # TODO: Skopiuj dane z pliku dane_testowe.py
    # lub stwórz własną listę zamówień
    # Format: zamowienia = [ ("nazwa", cena, ilosc), ... ]

    zamowienia = [
        # TODO: Wpisz swoje zamówienia tutaj
        # Przykład:
        # ("Laptop", 3500.00, 2),
        # ("Mysz", 45.50, 5),
    ]

    # TODO: Wyświetl zamówienia
    # Wskazówka: wywołaj wyswietl_zamowienia(zamowienia)


    # TODO: Oblicz i wyświetl statystyki
    # Wskazówka: wywołaj oblicz_statystyki(zamowienia)



if __name__ == "__main__":
    main()
