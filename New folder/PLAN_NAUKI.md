# 📚 PLAN NAUKI PROGRAMOWANIA - 90 DNI

## 🎯 Cel: Zostać samodzielnym programistą Python/SQL

---

## MIESIĄC 1: FUNDAMENTY

### ✅ Tydzień 1: Python - Struktury Danych

**Teoria do nauki:**
- Listy: append(), remove(), sort(), len()
- Słowniki: keys(), values(), items()
- Tuple (krotki) - niezmienność
- Zbiory (sets) - unikalne wartości

**Zadania praktyczne:**

[ ] **Zadanie 1.1:** Lista zakupów
```python
# Stwórz program z menu:
# 1. Dodaj produkt
# 2. Usuń produkt
# 3. Wyświetl listę
# 4. Posortuj alfabetycznie
# 5. Wyjście
```

[ ] **Zadanie 1.2:** Słownik produktów
```python
# Stwórz słownik: {'nazwa': 'cena'}
# Funkcje: dodaj, usuń, znajdź najtańszy, najdroższy
```

[ ] **Zadanie 1.3:** Analiza danych
```python
# Lista zamówień: [(produkt, cena, ilosc), ...]
# Oblicz: suma zamówień, średnia cena, najczęstszy produkt
```

**Materiały:**
- Python Docs: https://docs.python.org/3/tutorial/datastructures.html
- W3Schools Python Lists: https://www.w3schools.com/python/python_lists.asp

---

### ✅ Tydzień 2: Python - Funkcje i Moduły

**Teoria do nauki:**
- def, return, parametry
- *args, **kwargs
- Dokumentacja funkcji (docstrings)
- import, from ... import

**Zadania praktyczne:**

[ ] **Zadanie 2.1:** Kalkulator funkcji
```python
def dodaj(a, b):
    """Dodaje dwie liczby"""
    return a + b

# Stwórz: odejmij, pomnoz, podziel, potega
```

[ ] **Zadanie 2.2:** Moduł matematyczny
```python
# Stwórz plik math_utils.py z funkcjami:
# - silnia(n)
# - fibonacci(n)
# - czy_pierwsza(n)
# Zaimportuj i użyj w głównym programie
```

[ ] **Zadanie 2.3:** Refaktoryzacja projektu
```python
# Przepisz fragment system_automatyzacji_sqlserver.py
# Wyodrębnij funkcje: polacz_z_baza(), wykonaj_zapytanie()
```

**Materiały:**
- Real Python: Functions - https://realpython.com/defining-your-own-python-function/

---

### ✅ Tydzień 3: Python - Programowanie Obiektowe

**Teoria do nauki:**
- Klasy i obiekty
- __init__, self
- Metody, atrybuty
- Enkapsulacja, dziedziczenie

**Zadania praktyczne:**

[ ] **Zadanie 3.1:** Klasa Produkt
```python
class Produkt:
    def __init__(self, nazwa, cena, vat=23):
        self.nazwa = nazwa
        self.cena = cena
        self.vat = vat

    def cena_brutto(self):
        return self.cena * (1 + self.vat/100)

    def __str__(self):
        return f"{self.nazwa}: {self.cena_brutto():.2f} PLN"
```

[ ] **Zadanie 3.2:** Klasa Klient
```python
# Stwórz klasę Klient z metodami:
# - dodaj_zamowienie()
# - historia_zamowien()
# - suma_wydatkow()
```

[ ] **Zadanie 3.3:** Dziedziczenie
```python
# Klasa bazowa: Osoba
# Klasy pochodne: Klient, Pracownik
# Pracownik ma dodatkowe pole: pensja
```

**Materiały:**
- Real Python OOP: https://realpython.com/python3-object-oriented-programming/

---

### ✅ Tydzień 4: SQL - Podstawy

**Teoria do nauki:**
- SELECT, WHERE, ORDER BY
- LIKE, IN, BETWEEN
- JOIN (INNER, LEFT, RIGHT)
- GROUP BY, HAVING

**Zadania praktyczne:**

[ ] **Zadanie 4.1:** 10 zapytań SQL
```sql
-- 1. Wszystkie produkty z kategorii "Audio"
SELECT * FROM produkty WHERE kategoria = 'Audio';

-- 2. Klienci z Warszawy
-- 3. Produkty droższe niż 1000 PLN
-- 4. Top 5 najdroższych produktów
-- 5. Liczba produktów w każdej kategorii
-- 6. Zamówienia klienta "Jan Kowalski"
-- 7. Produkty ze stanem < 20
-- 8. Średnia cena produktów per kategoria
-- 9. Klienci którzy nie złożyli zamówień (LEFT JOIN)
-- 10. Suma sprzedaży per klient
```

[ ] **Zadanie 4.2:** Złożone JOIN-y
```sql
-- Raport: Klient | Produkt | Cena | Data zamówienia
-- Użyj JOIN na 3 tabelach
```

[ ] **Zadanie 4.3:** Agregacje
```sql
-- Raport sprzedaży per miesiąc
-- Użyj: GROUP BY YEAR(), MONTH()
```

**Materiały:**
- SQLZoo: https://sqlzoo.net/
- W3Schools SQL: https://www.w3schools.com/sql/

---

## MIESIĄC 2: ROZBUDOWA PROJEKTU

### ✅ Tydzień 5: Tkinter GUI

**Teoria do nauki:**
- tk.Tk(), mainloop()
- Widgety: Label, Button, Entry, Text
- Layout: pack(), grid(), place()
- Event handling

**Zadania praktyczne:**

[ ] **Zadanie 5.1:** Kalkulator GUI
```python
import tkinter as tk

def oblicz():
    wynik = float(pole1.get()) + float(pole2.get())
    etykieta_wynik.config(text=f"Wynik: {wynik}")

# Stwórz okno z 2 polami, przyciskiem i wynikiem
```

[ ] **Zadanie 5.2:** Lista TODO
```python
# GUI z:
# - Entry (dodaj zadanie)
# - Listbox (lista zadań)
# - Przyciski: Dodaj, Usuń, Oznacz jako wykonane
```

[ ] **Zadanie 5.3:** Formularz klienta
```python
# Dodaj do projektu okno dialogowe:
# Pola: Nazwa, Email, Telefon, Adres
# Przyciski: Zapisz, Anuluj
# Po zapisie -> INSERT do bazy
```

---

### ✅ Tydzień 6: Tkinter Zaawansowany

**Teoria do nauki:**
- ttk.Treeview (tabele)
- Scrollbar
- Messagebox, Filedialog
- Walidacja danych

**Zadania praktyczne:**

[ ] **Zadanie 6.1:** Tabela z danymi
```python
# Wyświetl tabelę produktów w Treeview
# Kolumny: ID, Nazwa, Kategoria, Cena, Stan
# Pobierz dane z SQL
```

[ ] **Zadanie 6.2:** Edycja produktu
```python
# Okno dialogowe do edycji:
# 1. Kliknij produkt w tabeli
# 2. Otwórz okno z formularzem
# 3. Zapisz zmiany (UPDATE SQL)
```

[ ] **Zadanie 6.3:** Eksport do pliku
```python
# Przycisk "Eksportuj do CSV"
# Użyj tkinter.filedialog.asksaveasfilename()
# Zapisz dane z Treeview
```

---

### ✅ Tydzień 7-8: Projekt - System Logowania

**Cel:** Dodać autentykację użytkowników

[ ] **Krok 1:** Stwórz tabelę użytkowników
```sql
CREATE TABLE uzytkownicy (
    id INT IDENTITY(1,1) PRIMARY KEY,
    login NVARCHAR(50) UNIQUE NOT NULL,
    haslo_hash NVARCHAR(255) NOT NULL,
    rola NVARCHAR(20) DEFAULT 'user',
    data_utworzenia DATETIME DEFAULT GETDATE()
);
```

[ ] **Krok 2:** Hashowanie haseł
```python
import hashlib

def hash_haslo(haslo):
    return hashlib.sha256(haslo.encode()).hexdigest()

def sprawdz_haslo(haslo, hash):
    return hash_haslo(haslo) == hash
```

[ ] **Krok 3:** Okno logowania
```python
# login_window.py
# Pola: Login, Hasło
# Przyciski: Zaloguj, Zarejestruj
# Po zalogowaniu -> otwórz główne okno
```

[ ] **Krok 4:** Role użytkowników
```python
# admin - pełny dostęp
# user - tylko przeglądanie raportów
# Ukryj/pokaż przyciski w zależności od roli
```

---

## MIESIĄC 3: ZAAWANSOWANE TECHNIKI

### ✅ Tydzień 9: Obsługa Błędów

**Teoria do nauki:**
- try, except, finally
- raise, własne wyjątki
- logging (DEBUG, INFO, WARNING, ERROR)

**Zadania praktyczne:**

[ ] **Zadanie 9.1:** Obsługa błędów SQL
```python
def wykonaj_zapytanie(query):
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except pyodbc.Error as e:
        print(f"Błąd SQL: {e}")
        return None
    finally:
        cursor.close()
```

[ ] **Zadanie 9.2:** Logowanie
```python
import logging

logging.basicConfig(
    filename='sklep.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Aplikacja uruchomiona")
logging.error("Błąd połączenia z bazą")
```

[ ] **Zadanie 9.3:** Walidacja danych
```python
def waliduj_email(email):
    if '@' not in email:
        raise ValueError("Nieprawidłowy email")
    return email
```

---

### ✅ Tydzień 10: Testy Jednostkowe

**Teoria do nauki:**
- unittest.TestCase
- setUp(), tearDown()
- assertEqual, assertTrue, assertRaises

**Zadania praktyczne:**

[ ] **Zadanie 10.1:** Test funkcji matematycznych
```python
import unittest

class TestMathUtils(unittest.TestCase):
    def test_dodawanie(self):
        self.assertEqual(dodaj(2, 3), 5)

    def test_dzielenie_przez_zero(self):
        with self.assertRaises(ZeroDivisionError):
            podziel(5, 0)
```

[ ] **Zadanie 10.2:** Test połączenia z bazą
```python
# Stwórz testową bazę danych
# Test: czy tabele istnieją
# Test: czy dane są poprawnie zapisywane
```

[ ] **Zadanie 10.3:** Test GUI
```python
# Test czy okno się otwiera
# Test czy przyciski działają
# (użyj unittest.mock)
```

---

### ✅ Tydzień 11-12: Refaktoryzacja i Modularyzacja

**Cel:** Podzielić projekt na moduły

[ ] **Krok 1:** Struktura katalogów
```
sklep/
├── main.py
├── config.ini
├── models/
│   ├── database.py
│   ├── klient.py
│   └── produkt.py
├── views/
│   ├── main_window.py
│   ├── login_window.py
│   └── raport_window.py
├── controllers/
│   ├── klient_controller.py
│   └── zamowienie_controller.py
└── utils/
    ├── logger.py
    └── validator.py
```

[ ] **Krok 2:** database.py
```python
class Database:
    def __init__(self, config_file):
        self.config = self.load_config(config_file)
        self.connection = None

    def connect(self):
        # Nawiązanie połączenia

    def execute_query(self, query, params=None):
        # Wykonanie zapytania

    def close(self):
        # Zamknięcie połączenia
```

[ ] **Krok 3:** MVC Pattern
```python
# Model (models/klient.py)
class Klient:
    @staticmethod
    def pobierz_wszystkich():
        # SELECT * FROM klienci

# View (views/klient_view.py)
class KlientView:
    def wyswietl_liste(self, klienci):
        # Wyświetl w Treeview

# Controller (controllers/klient_controller.py)
class KlientController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def laduj_klientow(self):
        klienci = self.model.pobierz_wszystkich()
        self.view.wyswietl_liste(klienci)
```

---

### ✅ Tydzień 13: PROJEKT KOŃCOWY - Generator Faktur VAT

**Specyfikacja:**

[ ] **Funkcjonalność:**
- Generowanie faktury PDF dla zamówienia
- Numeracja automatyczna (FV/001/2025)
- Logo firmy, dane sprzedawcy/kupującego
- Tabela z pozycjami (produkt, ilość, cena netto, VAT, brutto)
- Suma netto, VAT, brutto
- Zapis w bazie: tabela `faktury`

[ ] **Technologia:**
```python
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generuj_fakture(zamowienie_id, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    c.drawString(100, 800, "FAKTURA VAT")
    # ... reszta implementacji
    c.save()
```

[ ] **Baza danych:**
```sql
CREATE TABLE faktury (
    id INT IDENTITY(1,1) PRIMARY KEY,
    numer NVARCHAR(50) UNIQUE,
    zamowienie_id INT,
    data_wystawienia DATE,
    kwota_netto DECIMAL(10,2),
    kwota_vat DECIMAL(10,2),
    kwota_brutto DECIMAL(10,2),
    plik_pdf NVARCHAR(500),
    FOREIGN KEY (zamowienie_id) REFERENCES zamowienia(id)
);
```

[ ] **GUI:**
- Zakładka "Faktury" w głównym oknie
- Przycisk "Generuj fakturę" przy zamówieniu
- Lista faktur z możliwością podglądu PDF

---

## 📊 Tracking Postępów

**Zaznaczaj ukończone zadania:**
- [ ] = Do zrobienia
- [x] = Ukończone

**Po każdym tygodniu:**
1. Oceń swoje postępy (1-10)
2. Zapisz trudności/pytania
3. Przejrzyj kod sprzed tygodnia - co możesz poprawić?

**Co miesiąc:**
- Mini projekt łączący wiedzę z całego miesiąca
- Code review - poproś kogoś o sprawdzenie kodu

---

## 🎓 Dodatkowe Zasoby

### Książki:
1. "Python dla każdego" - Allen B. Downey
2. "Automatyzacja nudnych zadań" - Al Sweigart
3. "Clean Code" - Robert C. Martin (po angielsku)

### Kursy online:
1. Codecademy - Python Course (darmowy)
2. freeCodeCamp - Python for Beginners (YouTube)
3. Microsoft Learn - SQL tutorials

### Społeczności:
1. Stack Overflow - pytania techniczne
2. Reddit r/learnpython
3. Discord - Python Community

---

## 💪 Motywacja

**Pamiętaj:**
- Każdy programista kiedyś zaczynał od zera
- Błędy to najlepsza nauka
- Konsystencja > intensywność (lepiej 30 min dziennie niż 5h raz w tygodniu)
- Kod który napisałeś miesiąc temu będzie wyglądał źle - to znak postępu!

**Zasada 10 000 godzin:**
- 2h dziennie = 730h/rok
- Za 3 lata będziesz ekspertem!

---

**Powodzenia w nauce! 🚀**
