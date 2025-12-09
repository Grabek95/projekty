"""
ROZWIĄZANIE ZADANIA 1.3: Analiza zamówień
=========================================

WAŻNE: To jest kompletne rozwiązanie.
Zaglądaj tu TYLKO gdy kompletnie utkniesz!
"""


def wyswietl_zamowienia(zamowienia):
    """Wyświetla listę wszystkich zamówień"""
    print("=== ANALIZA ZAMÓWIEŃ ===\n")
    print("LISTA ZAMÓWIEŃ:")

    for i, (nazwa, cena, ilosc) in enumerate(zamowienia, start=1):
        wartosc = cena * ilosc
        print(f"{i}. {nazwa}: {cena:.2f} PLN x {ilosc} szt. = {wartosc:.2f} PLN")


def oblicz_statystyki(zamowienia):
    """Oblicza i wyświetla statystyki zamówień"""

    print("\n" + "="*40)
    print("STATYSTYKI:")
    print("="*40)

    # 1. Liczba zamówień
    liczba_zamowien = len(zamowienia)
    print(f"Liczba zamówień:              {liczba_zamowien}")

    # 2. Suma cen jednostkowych
    suma_cen = 0
    for nazwa, cena, ilosc in zamowienia:
        suma_cen += cena
    print(f"Suma cen jednostkowych:       {suma_cen:.2f} PLN")

    # 3. Średnia cena
    srednia_cena = suma_cen / liczba_zamowien
    print(f"Średnia cena produktu:        {srednia_cena:.2f} PLN")

    # 4. Najtańszy produkt
    min_cena = float('inf')
    min_nazwa = ""
    for nazwa, cena, ilosc in zamowienia:
        if cena < min_cena:
            min_cena = cena
            min_nazwa = nazwa
    print(f"Najtańszy produkt:            {min_nazwa} ({min_cena:.2f} PLN)")

    # 5. Najdroższy produkt
    max_cena = 0
    max_nazwa = ""
    for nazwa, cena, ilosc in zamowienia:
        if cena > max_cena:
            max_cena = cena
            max_nazwa = nazwa
    print(f"Najdroższy produkt:           {max_nazwa} ({max_cena:.2f} PLN)")

    # 6. Całkowita wartość zamówień
    calkowita_wartosc = 0
    for nazwa, cena, ilosc in zamowienia:
        calkowita_wartosc += cena * ilosc
    print(f"Całkowita wartość zamówień:   {calkowita_wartosc:.2f} PLN")

    # 7. Najczęściej zamawiany produkt
    max_ilosc = 0
    max_ilosc_nazwa = ""
    for nazwa, cena, ilosc in zamowienia:
        if ilosc > max_ilosc:
            max_ilosc = ilosc
            max_ilosc_nazwa = nazwa
    print(f"Najczęściej zamawiany:        {max_ilosc_nazwa} ({max_ilosc} szt.)")


def main():
    """Główna funkcja programu"""

    # Dane testowe - elektronika
    zamowienia = [
        ("Laptop", 3500.00, 2),
        ("Mysz", 45.50, 5),
        ("Klawiatura", 120.00, 3),
        ("Monitor", 890.00, 1),
        ("Słuchawki", 180.00, 4)
    ]

    wyswietl_zamowienia(zamowienia)
    oblicz_statystyki(zamowienia)


# ============================================
# ALTERNATYWNE ROZWIĄZANIE
# (Bardziej pythonowe - używa list comprehensions i funkcji wbudowanych)
# ============================================

def oblicz_statystyki_alternatywne(zamowienia):
    """
    ALTERNATYWNE ROZWIĄZANIE - bardziej zaawansowane
    Używa list comprehensions i funkcji min/max z lambda
    """

    print("\n" + "="*40)
    print("STATYSTYKI (wersja zaawansowana):")
    print("="*40)

    # 1. Liczba zamówień
    print(f"Liczba zamówień:              {len(zamowienia)}")

    # 2. Suma cen (list comprehension)
    suma_cen = sum(cena for nazwa, cena, ilosc in zamowienia)
    print(f"Suma cen jednostkowych:       {suma_cen:.2f} PLN")

    # 3. Średnia
    srednia = suma_cen / len(zamowienia)
    print(f"Średnia cena produktu:        {srednia:.2f} PLN")

    # 4. Najtańszy (min z lambda)
    najtanszy = min(zamowienia, key=lambda x: x[1])
    print(f"Najtańszy produkt:            {najtanszy[0]} ({najtanszy[1]:.2f} PLN)")

    # 5. Najdroższy (max z lambda)
    najdrozszy = max(zamowienia, key=lambda x: x[1])
    print(f"Najdroższy produkt:           {najdrozszy[0]} ({najdrozszy[1]:.2f} PLN)")

    # 6. Całkowita wartość
    total = sum(cena * ilosc for nazwa, cena, ilosc in zamowienia)
    print(f"Całkowita wartość zamówień:   {total:.2f} PLN")

    # 7. Najczęściej zamawiany
    najczestszy = max(zamowienia, key=lambda x: x[2])
    print(f"Najczęściej zamawiany:        {najczestszy[0]} ({najczestszy[2]} szt.)")


def demo_obu_wersji():
    """Demonstracja obu wersji rozwiązania"""

    zamowienia = [
        ("Laptop", 3500.00, 2),
        ("Mysz", 45.50, 5),
        ("Klawiatura", 120.00, 3),
        ("Monitor", 890.00, 1),
        ("Słuchawki", 180.00, 4)
    ]

    wyswietl_zamowienia(zamowienia)

    print("\n" + "="*60)
    print("PORÓWNANIE DWÓCH ROZWIĄZAŃ:")
    print("="*60)

    oblicz_statystyki(zamowienia)
    oblicz_statystyki_alternatywne(zamowienia)

    print("\n" + "="*60)
    print("OBA ROZWIĄZANIA DAJĄ IDENTYCZNE WYNIKI!")
    print("Wersja podstawowa: łatwiejsza do zrozumienia")
    print("Wersja zaawansowana: krótsza, bardziej 'pythonowa'")
    print("="*60)


if __name__ == "__main__":
    # Uruchom podstawową wersję
    main()

    # Odkomentuj poniższą linię aby zobaczyć porównanie obu wersji:
    # demo_obu_wersji()
