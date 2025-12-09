"""
DANE TESTOWE - Przykładowe zamówienia
======================================

Ten plik zawiera gotowe dane testowe które możesz użyć w swoim programie.

Możesz skopiować te dane do swojego pliku szablon.py lub stworzyć własne!
"""

# ZESTAW 1: Elektronika (5 pozycji)
zamowienia_elektronika = [
    ("Laptop", 3500.00, 2),
    ("Mysz", 45.50, 5),
    ("Klawiatura", 120.00, 3),
    ("Monitor", 890.00, 1),
    ("Słuchawki", 180.00, 4)
]

# ZESTAW 2: Artykuły spożywcze (7 pozycji)
zamowienia_spozywcze = [
    ("Mleko", 3.50, 10),
    ("Chleb", 4.20, 5),
    ("Masło", 6.50, 3),
    ("Ser", 12.00, 2),
    ("Jajka", 8.00, 6),
    ("Jogurt", 2.50, 8),
    ("Woda", 1.50, 12)
]

# ZESTAW 3: Książki (4 pozycje)
zamowienia_ksiazki = [
    ("Python dla każdego", 45.00, 1),
    ("Clean Code", 89.00, 2),
    ("Algorytmy", 120.00, 1),
    ("Django Tutorial", 65.00, 1)
]

# ZESTAW 4: Mieszany (6 pozycji)
zamowienia_mieszane = [
    ("Telefon", 2500.00, 1),
    ("Ładowarka", 35.00, 3),
    ("Etui", 25.00, 2),
    ("Powerbank", 80.00, 1),
    ("Kabel USB", 15.00, 5),
    ("Szkło ochronne", 20.00, 2)
]

# ZESTAW 5: Mini (tylko 2 pozycje - do testowania edge cases)
zamowienia_mini = [
    ("Produkt A", 100.00, 1),
    ("Produkt B", 200.00, 1)
]


# ============================================
# FUNKCJE POMOCNICZE
# ============================================

def wyswietl_zamowienia(zamowienia, nazwa_zestawu="Zamówienia"):
    """Wyświetla zamówienia w czytelnej formie"""
    print(f"\n=== {nazwa_zestawu.upper()} ===")
    for i, (nazwa, cena, ilosc) in enumerate(zamowienia, start=1):
        wartosc = cena * ilosc
        print(f"{i}. {nazwa}: {cena:.2f} PLN x {ilosc} szt. = {wartosc:.2f} PLN")
    print()


def wyswietl_wszystkie_zestawy():
    """Wyświetla wszystkie dostępne zestawy danych"""
    print("="*50)
    print("DOSTĘPNE ZESTAWY DANYCH TESTOWYCH")
    print("="*50)

    wyswietl_zamowienia(zamowienia_elektronika, "1. Elektronika")
    wyswietl_zamowienia(zamowienia_spozywcze, "2. Spożywcze")
    wyswietl_zamowienia(zamowienia_ksiazki, "3. Książki")
    wyswietl_zamowienia(zamowienia_mieszane, "4. Mieszane")
    wyswietl_zamowienia(zamowienia_mini, "5. Mini")


# ============================================
# URUCHOMIENIE
# ============================================

if __name__ == "__main__":
    # Uruchom ten plik aby zobaczyć wszystkie zestawy
    wyswietl_wszystkie_zestawy()

    print("\n" + "="*50)
    print("JAK UŻYĆ TYCH DANYCH?")
    print("="*50)
    print("""
W swoim pliku szablon.py możesz skopiować wybrany zestaw:

    zamowienia = [
        ("Laptop", 3500.00, 2),
        ("Mysz", 45.50, 5),
        ...
    ]

Lub zaimportować z tego pliku:

    from dane_testowe import zamowienia_elektronika

    zamowienia = zamowienia_elektronika

Wybierz jeden z 5 zestawów i rozpocznij analizę!
    """)
