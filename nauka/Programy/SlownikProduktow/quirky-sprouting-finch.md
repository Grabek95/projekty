# Plan Nauki - ZAKTUALIZOWANY (17 Grudnia 2025)

## 🎯 Twój Profil

**Start:** 17 Grudnia 2025 (już w trakcie!)
**Meta:** Wrzesień 2026 (9 miesięcy)
**Dostępny czas:**
- Dni robocze: 3-4.5h (w pracy 2-3h + po pracy 1-1.5h)
- **Weekendy:** max 1-2h/dzień (elastycznie!)
- **Święta:** odpoczynek lub jeśli masz czas
**Cel:** Praca inżynierska - System w chmurze Azure

**Specjalizacja:** Technologia Chmury Obliczeniowej
**Wymagania uczelni:** Azure (obowiązkowe)
**Dodatkowe bazy:** MSSQL, Azure SQL Database, Oracle (opcjonalnie)

**WAŻNE:** Plan jest elastyczny! Jeśli w którymś tygodniu nie zdążysz - nic się nie stanie. Masz wystarczająco dużo czasu do września. Priorytet: **jakość > tempo**.

---

## 📊 Twój Obecny Poziom (17 Grudnia 2025)

### ✅ Co już umiesz:

**Python Podstawy:**
- [x] Zmienne, typy danych (int, float, str)
- [x] If-elif-else, while True, break
- [x] Listy (append, remove, sort, clear)
- [x] Słowniki (zagnieżdżone struktury)
- [x] Pętle for, enumerate(start=1)
- [x] Funkcje (def, return, docstringi)
- [x] Try-except (ValueError)
- [x] Walidacja danych (if value <= 0, if product in dict)
- [x] String manipulation (.lower(), .strip())
- [x] Obsługa plików (open, write, encoding="utf-8")
- [x] `if __name__ == "__main__":`
- [x] main() pattern

**Projekty ukończone:**
1. ✅ Lista zakupów (lista_zakupow.py) - 118 linii
2. ✅ Słownik produktów (Slownik_produktow.py) - w trakcie rozwijania

**Oszacowany postęp:** Jesteś w połowie Tygodnia 2 z oryginalnego planu!

---

### ❌ Czego jeszcze nie znasz:

- [ ] JSON (import json, dumps, loads)
- [ ] datetime (now, strftime, timedelta)
- [ ] List comprehensions
- [ ] Lambda functions
- [ ] Moduły (import własnych plików)
- [ ] Excel (openpyxl, pandas)
- [ ] Klasy i OOP
- [ ] SQL (podstawy, JOIN-y, transakcje)
- [ ] pyodbc / sqlalchemy
- [ ] pandas (DataFrame)
- [ ] Tkinter (GUI)
- [ ] Azure (Cloud, SQL Database, Storage, Functions)

---

## 🗺️ NOWY Plan Nauki (Grudzień 2025 - Wrzesień 2026)

### Różnice od pierwotnego planu:

1. **Tempo przyspieszone:** 3-4.5h/dzień = 2-3× szybciej
2. **Więcej czasu na podstawy:** Dodatkowe 2 tygodnie na Python
3. **Focus na Azure:** Cała Faza 6 poświęcona Azure
4. **SQL równolegle:** Uczysz się w pracy, więc szybciej przejdziesz teorię
5. **Projekt końcowy:** System w Azure (nie lokalny SQL Server)

### Timeline:

```
Grudzień 2025:      Python Fundamenty (dokończenie)    [██████░░░░░░░░░░]
Styczeń 2026:       Python Zaawansowany + JSON/Excel   [░░░░░░██████░░░░]
Luty 2026:          SQL Server + Azure SQL Database    [░░░░░░░░░░██████]
Marzec 2026:        OOP + pyodbc + architektura         [░░░░░░░░░░░░░░██]
Kwiecień 2026:      pandas + Excel + Azure Blob         [░░░░░░░░░░░░░░░░]
Maj 2026:           GUI Tkinter + integracja            [░░░░░░░░░░░░░░░░]
Czerwiec 2026:      Azure Cloud (Functions, App Service)[░░░░░░░░░░░░░░░░]
Lipiec 2026:        Projekt finałowy w Azure            [░░░░░░░░░░░░░░░░]
Sierpień 2026:      Dokumentacja + optymalizacja        [░░░░░░░░░░░░░░░░]
Wrzesień 2026:      Obrona pracy inżynierskiej          [░░░░░░░░░░░░░░░░]
```

---

## 📅 SZCZEGÓŁOWY PLAN MIESIĘCZNY

---

## GRUDZIEŃ 2025 (17-31 Grudnia) - Python Fundamenty

**Status:** W TRAKCIE (Tydzień 2)
**Czas dostępny:** 14 dni × 3.5h = 49 godzin

### Tydzień 2.5 (17-29 Grudnia): Dokończenie Słownika Produktów

**Cel:** Rozszerzyć słownik produktów o brakujące funkcje

**UWAGA:** 24-26 grudnia = Święta (mniej czasu), weekendy = max 1-2h/dzień

**Zadania (13 dni z przerwami = ~35h):**

**Dzień 1-3 (17-19 Gru, wt-cz): Dokończenie podstawowych funkcji** (~10h)
- [ ] Funkcja `edit_product()` - edycja ceny/ilości/kategorii
- [ ] Funkcja `show_products()` - ładne wyświetlanie (JUŻ ZACZĄŁEŚ!)
- [ ] Funkcja `sort_products()` - sortowanie (WIDZĘ LAMBDA - DOBRZE!)
- [ ] Funkcja `filter_by_category()` - filtrowanie po kategorii
- [ ] Dodaj walidację do wszystkich funkcji

**Dzień 4-5 (20-21 Gru, pt-sob): Zaawansowane funkcje** (~5h - weekend!)
- [ ] Funkcja `find_max_price()` - produkt z najwyższą ceną
- [ ] Funkcja `find_min_price()` - produkt z najniższą ceną
- [ ] Funkcja `calculate_total_value()` - wartość magazynu (cena × ilość)

**Dzień 6 (22 Gru, nd): Review** (~1h - weekend!)
- [ ] Testuj to co do tej pory
- [ ] Poprawki błędów

**Dzień 7-9 (23, 27-28 Gru): Przerwa + lekka praca** (~6h total)
- 23 Gru (pn): Normalna praca (~3h)
  - [ ] Funkcja `low_stock_alert()` - produkty o niskim stanie
- 24-26 Gru: ŚWIĘTA - odpoczynek lub max 1h/dzień jeśli chcesz
- 27-28 Gru (pt-sob): Weekend (~3h)
  - [ ] Testowanie wszystkich funkcji
  - [ ] Dodaj więcej walidacji

**Dzień 10-13 (29 Gru - 1 Sty): Finalizacja** (~14h)
- [ ] Refactoring kodu
- [ ] Popraw komunikaty błędów (czytelne)
- [ ] Kod zgodny z PEP 8
- [ ] Dokumentacja funkcji (docstringi)
- [ ] Commit do GitHub

**Weryfikacja:**
- [ ] Program ma 10+ funkcji
- [ ] Wszystkie funkcje działają bez błędów
- [ ] Walidacja w każdej funkcji
- [ ] Kod ~200 linii, czytelny i skomentowany

**Harmonogram elastyczny:** Jeśli w święta nie zdążysz - nic się nie stanie! Odrobisz w dni robocze (27-31 grudnia).

---

### Tydzień 3 (30 Gru - 5 Sty): JSON i datetime

**UWAGA:** 1 stycznia = Nowy Rok (odpoczynek), weekendy = max 1-2h

**Cel:** Nauczyć się JSON i datetime

**Zadania (7 dni, elastyczne ~20h):**

**Dzień 1-2 (30-31 Gru, pn-wt): JSON - Podstawy** (~7h)
```python
import json

# Zapis słownika do JSON
with open("produkty.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=4)

# Odczyt z JSON
with open("produkty.json", "r", encoding="utf-8") as f:
    products = json.load(f)
```

**Projekt:** Dodaj do słownika produktów:
- [ ] Funkcja `save_to_json()` - zapis do pliku JSON
- [ ] Funkcja `load_from_json()` - wczytanie z JSON
- [ ] Auto-load przy starcie programu (jeśli plik istnieje)
- [ ] Auto-save przy wyjściu

**Dzień 3 (1 Sty, śr): ODPOCZYNEK** - Nowy Rok!

**Dzień 4-5 (2-3 Sty, cz-pt): datetime - Podstawy** (~7h)
```python
from datetime import datetime, timedelta

# Aktualna data i czas
teraz = datetime.now()
print(teraz.strftime("%Y-%m-%d %H:%M:%S"))

# Data za 7 dni
za_tydzien = teraz + timedelta(days=7)
```

**Projekt:** Rozszerz słownik produktów:
- [ ] Dodaj pole `data_dodania` do każdego produktu
- [ ] Funkcja `show_recent_products(days=7)` - produkty dodane ostatnio
- [ ] Funkcja `product_age(product_name)` - ile dni temu dodano
- [ ] Logger: zapisuj wszystkie operacje z timestamp do `log.txt`

**Dzień 6-7 (4-5 Sty, sob-nd): Integracja JSON + datetime** (~3h - weekendy!)
- [ ] Zapisz produkty do JSON z datami (datetime → string)
- [ ] Wczytaj z JSON i konwertuj stringi → datetime
- [ ] Historia zmian: zapisuj edycje produktów z timestamp
- [ ] Raport: podsumowanie operacji za ostatni tydzień

**Podsumowanie Tygodnia 3:**
- [ ] Testuj zapis/odczyt JSON
- [ ] Testuj operacje z datami
- [ ] Kod czytelny, skomentowany

**Weryfikacja:**
- [ ] Potrafię zapisać/wczytać JSON
- [ ] Potrafię formatować daty (strftime)
- [ ] Rozumiem timedelta
- [ ] Program zachowuje dane między uruchomieniami

---

### Tydzień 4 (30-31 Grudnia + 1-5 Stycznia): List Comprehensions + Lambda

**Cel:** Zaawansowane techniki Python

**Zadania (7 dni × 3.5h = 24.5h):**

**Dzień 1-2: List Comprehensions**
```python
# Zamiast pętli:
numbers = []
for i in range(10):
    if i % 2 == 0:
        numbers.append(i * 2)

# List comprehension:
numbers = [i * 2 for i in range(10) if i % 2 == 0]

# Dictionary comprehension:
squares = {x: x**2 for x in range(5)}
```

**Ćwiczenia:**
- [ ] 20 prostych list comprehensions
- [ ] Przepisz pętle z istniejących programów
- [ ] Dictionary comprehensions
- [ ] Nested comprehensions (2D listy)

**Dzień 3-4: Lambda Functions**
```python
# Funkcja zwykła:
def square(x):
    return x ** 2

# Lambda:
square = lambda x: x ** 2

# Z sorted():
products_sorted = sorted(products.items(),
                         key=lambda item: item[1]['cena'])
```

**Ćwiczenia:**
- [ ] Sortowanie słownika po różnych kluczach (cena, ilość, nazwa)
- [ ] Filter + lambda (produkty droższe niż 100)
- [ ] Map + lambda (podwyżka cen o 10%)

**Dzień 5-7: PROJEKT - System Biblioteki v1.0**

**Wymagania:**
- Słownik książek: `{tytuł: {autor, ISBN, rok, wypożyczone: bool, data_wypożyczenia}}`
- Funkcje:
  - [ ] Dodaj książkę (z walidacją)
  - [ ] Usuń książkę
  - [ ] Edytuj książkę
  - [ ] Wypożycz książkę (ustaw `wypożyczone=True`, zapisz datę)
  - [ ] Zwróć książkę (ustaw `wypożyczone=False`)
  - [ ] Pokaż dostępne książki (list comprehension!)
  - [ ] Pokaż wypożyczone książki
  - [ ] Raport: najstarsze książki (sortowanie lambda)
  - [ ] Raport: książki wypożyczone >30 dni (datetime)
  - [ ] Zapis/odczyt JSON
  - [ ] Logger operacji
- Try-except w każdej funkcji
- Menu użytkownika
- ~300 linii kodu

**Weryfikacja końca Grudnia:**
- [ ] Potrafię list comprehensions
- [ ] Potrafię lambda functions
- [ ] System Biblioteki działa bez błędów
- [ ] JSON i datetime opanowane

---

## STYCZEŃ 2026 - Python Zaawansowany + Excel

**Cel:** Dokończyć Python fundamenty, nauczyć się Excel

**Czas dostępny:** 31 dni × 3.5h = 108.5 godzin

### Tydzień 5 (6-12 Stycznia): Moduły i Struktura Projektu

**Cel:** Nauczyć się organizować kod w wiele plików

**Dzień 1-3: Moduły własne**

Struktura projektu:
```
moj_projekt/
├── main.py
├── utils.py          # Funkcje pomocnicze
├── validators.py     # Walidacje
├── file_handler.py   # JSON read/write
└── constants.py      # Stałe (np. nazwy plików)
```

**Przykład:**
```python
# validators.py
def validate_price(price):
    if not isinstance(price, (int, float)):
        raise ValueError("Cena musi być liczbą")
    if price <= 0:
        raise ValueError("Cena musi być > 0")
    return True

# main.py
from validators import validate_price

price = float(input("Cena: "))
validate_price(price)
```

**Projekt:** Przepisz System Biblioteki na moduły:
- [ ] `main.py` - menu i główna pętla
- [ ] `book_manager.py` - operacje na książkach
- [ ] `file_handler.py` - JSON read/write
- [ ] `validators.py` - wszystkie walidacje
- [ ] `utils.py` - formatowanie dat, stringów
- [ ] `config.py` - stałe (nazwy plików, limity)

**Dzień 4-7: Zaawansowane try-except**
- [ ] Własne wyjątki (custom exceptions)
- [ ] Try-except-else-finally
- [ ] Raising exceptions
- [ ] Context managers (with statement)
- [ ] Przepisz cały kod z lepszą obsługą błędów

**Weryfikacja:**
- [ ] Rozumiem import i moduły
- [ ] Projekt podzielony na pliki
- [ ] Obsługa błędów profesjonalna

---

### Tydzień 6 (13-19 Stycznia): Excel - openpyxl

**Cel:** Nauczyć się czytać i pisać pliki Excel

**Dzień 1-2: Instalacja i podstawy**
```bash
pip install openpyxl
```

```python
from openpyxl import Workbook, load_workbook

# Tworzenie nowego pliku Excel
wb = Workbook()
ws = wb.active
ws.title = "Produkty"

# Nagłówki
ws['A1'] = "Nazwa"
ws['B1'] = "Cena"
ws['C1'] = "Ilość"

# Dane
ws.append(["Laptop", 2500, 10])
ws.append(["Mysz", 45, 50])

# Zapis
wb.save("produkty.xlsx")

# Odczyt
wb = load_workbook("produkty.xlsx")
ws = wb.active
for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)
```

**Dzień 3-4: Formatowanie**
- [ ] Szerokość kolumn (column_dimensions)
- [ ] Czcionki (Font)
- [ ] Kolory (PatternFill)
- [ ] Wyrównanie (Alignment)
- [ ] Obramowanie (Border)

**Dzień 5-7: PROJEKT - Eksport produktów do Excel**

**Wymagania:**
- [ ] Funkcja `export_to_excel(filename)`:
  - Nagłówki: Nazwa, Cena, Ilość, Kategoria, Data dodania, Wartość (cena×ilość)
  - Wszystkie produkty ze słownika
  - Formatowanie: nagłówki pogrubione, kolory naprzemienne
  - Auto-width kolumn
  - SUM na końcu (suma wartości)
- [ ] Funkcja `import_from_excel(filename)`:
  - Wczytaj produkty z Excel
  - Dodaj do słownika
  - Walidacja danych
- [ ] Menu: opcja "Eksportuj do Excel" i "Importuj z Excel"

**Weryfikacja:**
- [ ] Potrafię tworzyć pliki Excel
- [ ] Potrafię formatować komórki
- [ ] Eksport/import działa

---

### Tydzień 7 (20-26 Stycznia): Regular Expressions (Regex)

**Cel:** Walidacja zaawansowana (email, telefon, kody)

**Dzień 1-3: Podstawy regex**
```python
import re

# Wzorce
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
phone_pattern = r'^\+48\s?\d{3}\s?\d{3}\s?\d{3}$'

# Walidacja
if re.match(email_pattern, "user@example.com"):
    print("Email poprawny")
```

**Dzień 4-7: PROJEKT - Walidatory**
- [ ] `validate_email(email)` - regex
- [ ] `validate_phone(phone)` - regex
- [ ] `validate_postal_code(code)` - regex (XX-XXX)
- [ ] `validate_ISBN(isbn)` - regex
- [ ] Dodaj do systemu biblioteki walidację ISBN
- [ ] Dodaj do słownika produktów walidację kodów kreskowych

**Weryfikacja:**
- [ ] Rozumiem podstawy regex
- [ ] Potrafię walidować stringi

---

### Tydzień 8 (27 Stycznia - 2 Lutego): PROJEKT MIESIĄCA

**Cel:** System Zarządzania Sklepem v1.0 (Pure Python)

**Wymagania (7 dni × 4h = 28h):**

**Funkcjonalności:**
1. **Zarządzanie produktami:**
   - Dodaj/usuń/edytuj produkt
   - Słownik: `{nazwa: {cena, ilość, kategoria, kod_kreskowy, data_dodania}}`
   - Walidacja: cena > 0, ilość >= 0, kod_kreskowy (regex)

2. **Zarządzanie klientami:**
   - Dodaj/usuń/edytuj klienta
   - Słownik: `{email: {imię, nazwisko, telefon, adres, data_rejestracji}}`
   - Walidacja: email (regex), telefon (regex)

3. **Zamówienia:**
   - Złóż zamówienie (klient, lista produktów, ilości)
   - Lista: `[{id, klient_email, produkty: [{nazwa, ilość, cena}], data, wartość_total}]`
   - Automatyczne zmniejszanie stanu magazynowego
   - Walidacja: czy produkt dostępny, czy ilość wystarczająca

4. **Raporty:**
   - Produkty o niskim stanie (<5)
   - Top 5 najdroższych produktów (sorted + lambda)
   - Wartość magazynu (sum + list comprehension)
   - Zamówienia z ostatnich 7 dni (datetime)
   - Najlepsi klienci (najwięcej zamówień)

5. **Eksport/Import:**
   - Produkty → Excel
   - Klienci → Excel
   - Zamówienia → Excel
   - Wszystkie dane → JSON (backup)
   - Wczytanie backup z JSON

6. **Logger:**
   - Wszystkie operacje zapisywane do `shop_log.txt` z timestamp
   - Format: `[2026-01-15 14:23:11] Dodano produkt: Laptop`

**Struktura plików:**
```
sklep/
├── main.py
├── product_manager.py
├── customer_manager.py
├── order_manager.py
├── reports.py
├── file_handler.py     # JSON + Excel
├── validators.py
├── utils.py
├── constants.py
└── data/
    ├── products.json
    ├── customers.json
    ├── orders.json
    └── shop_log.txt
```

**Wymagania techniczne:**
- Minimum 500 linii kodu
- Try-except w każdej funkcji
- Docstringi dla wszystkich funkcji
- PEP 8 compliant
- Komentarze po polsku

**Weryfikacja końca Stycznia:**
- [ ] System sklepu w 100% funkcjonalny
- [ ] Wszystkie raporty działają
- [ ] Eksport do Excel działa
- [ ] JSON backup/restore działa
- [ ] Kod modularny i czysty
- [ ] **GOTOWY DO PREZENTACJI** (to będzie część portfolio!)

---

## LUTY 2026 - SQL Server + Azure SQL Database

**Cel:** Nauczyć się SQL (w pracy + po pracy)

**Czas:** 28 dni × 3.5h = 98 godzin

**Uwaga:** Masz SQL w pracy, więc teoria będzie szybsza!

### Tydzień 9 (3-9 Lutego): SQL Server - Instalacja i Podstawy

**W pracy (2h/dzień):**
- Instalacja SQL Server Express + SSMS
- Tworzenie bazy danych
- CREATE TABLE
- INSERT, SELECT, UPDATE, DELETE
- WHERE, ORDER BY

**Po pracy (1.5h/dzień):**
- Przepisywanie przykładów z pracy
- 50 prostych zapytań SELECT
- Własna baza "Kontakty"

**Projekt:** Baza danych kontaktów
```sql
CREATE DATABASE KontaktyDB;

CREATE TABLE kontakty (
    id INT IDENTITY(1,1) PRIMARY KEY,
    imie NVARCHAR(100),
    nazwisko NVARCHAR(100),
    email NVARCHAR(255),
    telefon NVARCHAR(20),
    data_dodania DATETIME DEFAULT GETDATE()
);
```

**Weryfikacja:**
- [ ] SQL Server zainstalowany
- [ ] Potrafię CREATE, INSERT, SELECT
- [ ] 50+ zapytań napisanych

---

### Tydzień 10 (10-16 Lutego): Typy Danych i Klucze Obce

**W pracy:**
- PRIMARY KEY, FOREIGN KEY
- IDENTITY (auto-increment)
- NVARCHAR vs VARCHAR
- DATETIME, DECIMAL
- Projektowanie schematu

**Po pracy:**
- Projektuj schemat bazy "Sklep"
- Diagramy ERD (Entity Relationship Diagram)

**Projekt:** Baza danych Sklep
```sql
CREATE TABLE klienci (
    id INT IDENTITY(1,1) PRIMARY KEY,
    email NVARCHAR(255) NOT NULL UNIQUE,
    imie NVARCHAR(100),
    nazwisko NVARCHAR(100),
    telefon NVARCHAR(20),
    adres NVARCHAR(500),
    data_rejestracji DATETIME DEFAULT GETDATE()
);

CREATE TABLE produkty (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nazwa NVARCHAR(255) NOT NULL,
    cena DECIMAL(10,2) NOT NULL,
    ilosc INT DEFAULT 0,
    kategoria NVARCHAR(100),
    kod_kreskowy NVARCHAR(50),
    data_dodania DATETIME DEFAULT GETDATE()
);

CREATE TABLE zamowienia (
    id INT IDENTITY(1,1) PRIMARY KEY,
    klient_id INT NOT NULL,
    data_zamowienia DATETIME DEFAULT GETDATE(),
    wartosc_total DECIMAL(10,2),
    status NVARCHAR(50) DEFAULT 'nowe',
    FOREIGN KEY (klient_id) REFERENCES klienci(id)
);

CREATE TABLE pozycje_zamowien (
    id INT IDENTITY(1,1) PRIMARY KEY,
    zamowienie_id INT NOT NULL,
    produkt_id INT NOT NULL,
    ilosc INT NOT NULL,
    cena_jednostkowa DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (zamowienie_id) REFERENCES zamowienia(id),
    FOREIGN KEY (produkt_id) REFERENCES produkty(id)
);
```

**Weryfikacja:**
- [ ] Rozumiem klucze obce
- [ ] Schemat bazy zaprojektowany

---

### Tydzień 11 (17-23 Lutego): Agregacje i GROUP BY

**W pracy:**
- COUNT, SUM, AVG, MIN, MAX
- GROUP BY, HAVING
- TOP N
- Subqueries

**Po pracy:**
- 30 zapytań z agregacjami
- Raporty z bazy Sklep

**Przykłady:**
```sql
-- Liczba produktów per kategoria
SELECT kategoria, COUNT(*) as liczba
FROM produkty
GROUP BY kategoria;

-- Top 5 klientów (wartość zamówień)
SELECT TOP 5 k.imie, k.nazwisko, SUM(z.wartosc_total) as suma
FROM klienci k
JOIN zamowienia z ON k.id = z.klient_id
GROUP BY k.id, k.imie, k.nazwisko
ORDER BY suma DESC;

-- Średnia wartość zamówienia
SELECT AVG(wartosc_total) as srednia
FROM zamowienia;
```

**Weryfikacja:**
- [ ] Potrafię COUNT, SUM, AVG
- [ ] Rozumiem GROUP BY

---

### Tydzień 12 (24 Lutego - 2 Marca): JOIN-y

**W pracy:**
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
- CROSS JOIN

**Po pracy:**
- 30 zapytań z JOIN-ami
- Złożone raporty (3+ tabele)

**Przykłady:**
```sql
-- Wszystkie zamówienia z danymi klientów i produktów
SELECT
    z.id,
    k.email,
    k.imie + ' ' + k.nazwisko as klient,
    p.nazwa as produkt,
    pz.ilosc,
    pz.cena_jednostkowa,
    (pz.ilosc * pz.cena_jednostkowa) as wartosc
FROM zamowienia z
INNER JOIN klienci k ON z.klient_id = k.id
INNER JOIN pozycje_zamowien pz ON z.id = pz.zamowienie_id
INNER JOIN produkty p ON pz.produkt_id = p.id
ORDER BY z.data_zamowienia DESC;

-- Klienci bez zamówień (LEFT JOIN)
SELECT k.email, k.imie, k.nazwisko
FROM klienci k
LEFT JOIN zamowienia z ON k.id = z.klient_id
WHERE z.id IS NULL;
```

**Weryfikacja:**
- [ ] Rozumiem INNER vs LEFT JOIN
- [ ] Potrafię łączyć 3+ tabele

---

### Tydzień 13 (3-9 Marca): Transakcje SQL

**W pracy:**
- BEGIN TRANSACTION
- COMMIT
- ROLLBACK
- Atomowość operacji

**Po pracy:**
- System zamówień z transakcjami
- Testowanie błędów i ROLLBACK

**Przykład:**
```sql
BEGIN TRANSACTION;

-- Sprawdź stan magazynowy
DECLARE @stan INT;
SELECT @stan = ilosc FROM produkty WHERE id = 1;

IF @stan >= 5
BEGIN
    -- Dodaj zamówienie
    INSERT INTO zamowienia (klient_id, wartosc_total)
    VALUES (1, 500);

    -- Zmniejsz stan
    UPDATE produkty
    SET ilosc = ilosc - 5
    WHERE id = 1;

    COMMIT; -- Zatwierdź
    PRINT 'Zamówienie złożone!';
END
ELSE
BEGIN
    ROLLBACK; -- Wycofaj
    PRINT 'Niewystarczający stan!';
END
```

**Weryfikacja:**
- [ ] Rozumiem transakcje
- [ ] Potrafię COMMIT/ROLLBACK

---

### Tydzień 14 (10-16 Marca): Azure SQL Database

**Cel:** Migracja z lokalnego SQL Server do Azure

**Dzień 1-2: Utworzenie Azure SQL Database**
- [ ] Rejestracja Azure (student account - darmowe credits!)
- [ ] Utworzenie Resource Group
- [ ] Utworzenie Azure SQL Server
- [ ] Utworzenie Azure SQL Database (Basic tier)
- [ ] Konfiguracja firewalla (dodaj swoje IP)

**Dzień 3-4: Migracja danych**
- [ ] Export lokalnej bazy do .bacpac
- [ ] Import do Azure SQL Database
- [ ] Połączenie przez SSMS
- [ ] Sprawdzenie czy wszystko działa

**Dzień 5-7: Różnice Azure SQL vs SQL Server**
- [ ] Connection string (format Azure)
- [ ] Authentication (Azure AD vs SQL)
- [ ] Pricing tiers (DTU vs vCore)
- [ ] Backup i restore w Azure
- [ ] Monitoring (Azure Portal)

**PROJEKT KOŃCA LUTEGO:**

**System Sklepu v2.0 - z Azure SQL Database**
- Przepisz projekt z Stycznia (Pure Python) na SQL
- Wszystkie dane w Azure SQL Database (nie słowniki!)
- Python jako frontend (menu, walidacja)
- SQL jako backend (wszystkie operacje CRUD)
- pyodbc do połączenia

**Weryfikacja końca Lutego:**
- [ ] Azure SQL Database skonfigurowana
- [ ] Dane zmigrowane z lokalnego SQL
- [ ] System Sklepu v2.0 działa z Azure SQL
- [ ] Rozumiem różnice Azure vs lokalny SQL

---

## MARZEC 2026 - OOP + pyodbc + Architektura

**Cel:** Programowanie obiektowe i integracja Python-SQL

**Czas:** 31 dni × 3.5h = 108.5 godzin

### Tydzień 15 (17-23 Marca): Klasy i Obiekty

**Dzień 1-3: Podstawy OOP**
```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"{self.name}: {self.price} zł (stan: {self.quantity})")

    def update_quantity(self, amount):
        self.quantity += amount

# Użycie
laptop = Product("Laptop", 2500, 10)
laptop.display()
laptop.update_quantity(-2)
```

**Dzień 4-7: Klasy dla systemu sklepu**
- [ ] Klasa `Product`
- [ ] Klasa `Customer`
- [ ] Klasa `Order`
- [ ] Klasa `OrderItem`
- [ ] Metody: `__str__`, `__repr__`
- [ ] Gettery i settery (@property)

**Weryfikacja:**
- [ ] Rozumiem klasę vs obiekt
- [ ] Potrafię `__init__`
- [ ] Rozumiem self

---

### Tydzień 16 (24-30 Marca): pyodbc - Python + Azure SQL

**Dzień 1-2: Instalacja i połączenie**
```bash
pip install pyodbc
```

```python
import pyodbc

# Connection string dla Azure SQL
server = 'twoj-serwer.database.windows.net'
database = 'SklepDB'
username = 'admin'
password = 'TwojeHaslo123!'

conn_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

# Połączenie
conn = pyodbc.connect(conn_string)
cursor = conn.cursor()

# SELECT
cursor.execute("SELECT * FROM produkty")
for row in cursor.fetchall():
    print(row)

# INSERT (WAŻNE: parametry!)
cursor.execute("""
    INSERT INTO produkty (nazwa, cena, ilosc)
    VALUES (?, ?, ?)
""", ('Laptop', 2500, 10))
conn.commit()

# Zamknięcie
cursor.close()
conn.close()
```

**Dzień 3-7: Klasa DatabaseManager**
```python
class DatabaseManager:
    def __init__(self, conn_string):
        self.conn_string = conn_string
        self.conn = None

    def connect(self):
        self.conn = pyodbc.connect(self.conn_string)

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()

    def execute_non_query(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.conn.commit()
```

**Weryfikacja:**
- [ ] pyodbc działa
- [ ] Połączenie z Azure SQL OK
- [ ] Potrafię SELECT, INSERT z parametrami

---

### Tydzień 17 (31 Marca - 6 Kwietnia): Architektura Warstwowa

**Cel:** Separacja Backend (SQL) od Frontend (Python menu)

**Struktura:**
```
sklep_v3/
├── main.py                # Frontend - menu
├── backend/
│   ├── database_manager.py
│   ├── product_repository.py
│   ├── customer_repository.py
│   └── order_repository.py
├── models/
│   ├── product.py
│   ├── customer.py
│   └── order.py
├── config.py
└── requirements.txt
```

**Przykład Repository Pattern:**
```python
# product_repository.py
class ProductRepository:
    def __init__(self, db_manager):
        self.db = db_manager

    def get_all(self):
        query = "SELECT * FROM produkty"
        rows = self.db.execute_query(query)
        return [Product.from_db_row(row) for row in rows]

    def get_by_id(self, product_id):
        query = "SELECT * FROM produkty WHERE id = ?"
        rows = self.db.execute_query(query, (product_id,))
        if rows:
            return Product.from_db_row(rows[0])
        return None

    def create(self, product):
        query = """
            INSERT INTO produkty (nazwa, cena, ilosc, kategoria)
            VALUES (?, ?, ?, ?)
        """
        self.db.execute_non_query(query, (
            product.name,
            product.price,
            product.quantity,
            product.category
        ))

    def update(self, product):
        query = """
            UPDATE produkty
            SET nazwa=?, cena=?, ilosc=?, kategoria=?
            WHERE id=?
        """
        self.db.execute_non_query(query, (
            product.name,
            product.price,
            product.quantity,
            product.category,
            product.id
        ))

    def delete(self, product_id):
        query = "DELETE FROM produkty WHERE id=?"
        self.db.execute_non_query(query, (product_id,))
```

**Weryfikacja:**
- [ ] Rozumiem separację Backend/Frontend
- [ ] Repository Pattern działa
- [ ] Kod modularny

---

### Tydzień 18 (7-13 Kwietnia): PROJEKT MIESIĄCA

**System Sklepu v3.0 - OOP + Azure SQL**

**Wymagania:**
- Klasy: Product, Customer, Order, OrderItem
- Repositories: ProductRepository, CustomerRepository, OrderRepository
- DatabaseManager (singleton pattern)
- Menu użytkownika (jak dotychczas)
- Wszystkie operacje przez repositories
- Transakcje przy składaniu zamówienia:
  ```python
  def create_order(self, customer_id, items):
      try:
          self.db.conn.autocommit = False  # Start transaction

          # Insert zamówienie
          order_id = self.insert_order(customer_id)

          # Insert pozycje + update stany
          for item in items:
              self.insert_order_item(order_id, item)
              self.update_product_stock(item.product_id, -item.quantity)

          self.db.conn.commit()  # Commit
          return True, "Zamówienie złożone!"
      except Exception as e:
          self.db.conn.rollback()  # Rollback
          return False, f"Błąd: {e}"
      finally:
          self.db.conn.autocommit = True
  ```

**Weryfikacja końca Marca:**
- [ ] System v3.0 w pełni funkcjonalny
- [ ] OOP + Azure SQL działa
- [ ] Transakcje poprawne
- [ ] Kod ~800 linii

---

## KWIECIEŃ 2026 - pandas + Excel + Azure Blob Storage

**Cel:** Raporty w Excel + storage w chmurze

**Czas:** 30 dni × 3.5h = 105 godzin

### Tydzień 19 (14-20 Kwietnia): pandas - Podstawy

**Dzień 1-3: DataFrame**
```python
import pandas as pd
import pyodbc

# Połączenie
conn = pyodbc.connect(conn_string)

# SQL → DataFrame
query = "SELECT * FROM produkty"
df = pd.read_sql(query, conn)

# Podstawowe operacje
print(df.head())        # Pierwsze 5 wierszy
print(df.info())        # Info o DataFrame
print(df.describe())    # Statystyki

# Filtrowanie
drogie = df[df['cena'] > 1000]

# Sortowanie
sorted_df = df.sort_values('cena', ascending=False)

# Nowa kolumna
df['wartosc'] = df['cena'] * df['ilosc']
```

**Dzień 4-7: Agregacje i GroupBy**
```python
# GroupBy
by_category = df.groupby('kategoria').agg({
    'cena': 'mean',
    'ilosc': 'sum',
    'nazwa': 'count'
})

# Merge (jak JOIN)
df_orders = pd.read_sql("SELECT * FROM zamowienia", conn)
df_customers = pd.read_sql("SELECT * FROM klienci", conn)

merged = df_orders.merge(
    df_customers,
    left_on='klient_id',
    right_on='id',
    how='inner'
)
```

**Weryfikacja:**
- [ ] Rozumiem DataFrame
- [ ] Potrafię pd.read_sql
- [ ] GroupBy i merge działają

---

### Tydzień 20 (21-27 Kwietnia): Excel zaawansowany + pandas

**Dzień 1-3: pandas → Excel**
```python
# Prosty eksport
df.to_excel('produkty.xlsx', index=False)

# Z formatowaniem (openpyxl)
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill

# Zapis
df.to_excel('raport.xlsx', index=False, engine='openpyxl')

# Formatowanie
wb = load_workbook('raport.xlsx')
ws = wb.active

# Nagłówki
for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill(start_color="4472C4", fill_type="solid")

# Auto-width
for column in ws.columns:
    max_length = max(len(str(cell.value)) for cell in column)
    ws.column_dimensions[column[0].column_letter].width = max_length + 2

wb.save('raport.xlsx')
```

**Dzień 4-7: Multiple sheets + wykresy**
```python
# Multiple sheets
with pd.ExcelWriter('raporty.xlsx', engine='openpyxl') as writer:
    df_products.to_excel(writer, sheet_name='Produkty', index=False)
    df_customers.to_excel(writer, sheet_name='Klienci', index=False)
    df_orders.to_excel(writer, sheet_name='Zamówienia', index=False)

# Wykresy (opcjonalnie)
from openpyxl.chart import BarChart, Reference

wb = load_workbook('raporty.xlsx')
ws = wb['Produkty']

chart = BarChart()
chart.title = "Produkty wg kategorii"
data = Reference(ws, min_col=2, min_row=1, max_row=10)
chart.add_data(data, titles_from_data=True)
ws.add_chart(chart, "E5")

wb.save('raporty.xlsx')
```

**Weryfikacja:**
- [ ] Eksport do Excel z formatowaniem
- [ ] Multiple sheets działa

---

### Tydzień 21 (28 Kwietnia - 4 Maja): Azure Blob Storage

**Cel:** Przechowywanie plików Excel w chmurze Azure

**Dzień 1-2: Utworzenie Storage Account**
- [ ] Azure Portal → Create Storage Account
- [ ] Utworzenie kontenera "raporty"
- [ ] Pobranie connection string

**Dzień 3-5: Upload/Download plików**
```bash
pip install azure-storage-blob
```

```python
from azure.storage.blob import BlobServiceClient

# Connection string
conn_str = "DefaultEndpointsProtocol=https;..."
blob_service = BlobServiceClient.from_connection_string(conn_str)

# Upload
with open("raport.xlsx", "rb") as data:
    blob_client = blob_service.get_blob_client(
        container="raporty",
        blob="raport_2026-04-30.xlsx"
    )
    blob_client.upload_blob(data, overwrite=True)

# Download
blob_client = blob_service.get_blob_client(
    container="raporty",
    blob="raport_2026-04-30.xlsx"
)
with open("downloaded.xlsx", "wb") as download_file:
    download_file.write(blob_client.download_blob().readall())

# Lista plików
container_client = blob_service.get_container_client("raporty")
for blob in container_client.list_blobs():
    print(blob.name)
```

**Dzień 6-7: Integracja z systemem**
- [ ] Funkcja `upload_report_to_azure(filename)`
- [ ] Funkcja `download_report_from_azure(blob_name)`
- [ ] Lista raportów w Azure
- [ ] Menu: "Prześlij raport do Azure"

**Weryfikacja:**
- [ ] Azure Blob Storage skonfigurowany
- [ ] Upload/download działa
- [ ] System zapisuje raporty w chmurze

---

### Tydzień 22 (5-11 Maja): PROJEKT MIESIĄCA

**System Sklepu v4.0 - Raporty w Excel + Azure**

**Wymagania:**
1. **5 raportów Excel:**
   - Raport produktów (z wartością magazynu)
   - Raport zamówień (ostatnie 30 dni)
   - Raport klientów (suma zamówień per klient)
   - Top 10 produktów (najczęściej kupowane)
   - Analiza sprzedaży per kategoria

2. **Każdy raport:**
   - Formatowanie (nagłówki, kolory, auto-width)
   - Timestamp w nazwie pliku
   - Automatyczny upload do Azure Blob Storage
   - Podsumowanie (SUM, AVG na końcu)

3. **Menu:**
   - "Generuj raport produktów"
   - "Generuj raport zamówień"
   - ... (dla każdego)
   - "Lista raportów w Azure"
   - "Pobierz raport z Azure"

**Weryfikacja końca Kwietnia:**
- [ ] 5 raportów działa
- [ ] Eksport do Excel z formatowaniem
- [ ] Upload do Azure automatyczny
- [ ] System v4.0 gotowy

---

## MAJ 2026 - GUI Tkinter + Integracja

**Cel:** Graficzny interfejs użytkownika

**Czas:** 31 dni × 3.5h = 108.5 godzin

### Tydzień 23 (12-18 Maja): Tkinter - Podstawy

**Dzień 1-3: Pierwsze okno**
```python
import tkinter as tk

# Okno
root = tk.Tk()
root.title("Moja aplikacja")
root.geometry("800x600")

# Label
label = tk.Label(root, text="Hello World", font=("Arial", 16))
label.pack(pady=20)

# Button
def on_click():
    label.config(text="Kliknięto!")

button = tk.Button(root, text="Kliknij mnie", command=on_click)
button.pack()

# Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Uruchomienie
root.mainloop()
```

**Dzień 4-7: Więcej widgetów**
- [ ] Listbox
- [ ] Combobox (ttk)
- [ ] Spinbox
- [ ] Checkbutton
- [ ] Radiobutton
- [ ] Text (wieloliniowy)
- [ ] Scrollbar

**Projekt:** Kalkulator GUI

**Weryfikacja:**
- [ ] Rozumiem widgety
- [ ] Potrafię tworzyć okna

---

### Tydzień 24 (19-25 Maja): Layout i Zakładki

**Dzień 1-3: Grid layout**
```python
# Grid - układ tabelaryczny
label1 = tk.Label(root, text="Nazwa:")
label1.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

entry1 = tk.Entry(root, width=30)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = tk.Label(root, text="Cena:")
label2.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

entry2 = tk.Entry(root, width=30)
entry2.grid(row=1, column=1, padx=10, pady=5)
```

**Dzień 4-7: Notebook (zakładki)**
```python
from tkinter import ttk

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Zakładka 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Produkty")

# Zakładka 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Klienci")

# Zakładka 3
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Zamówienia")
```

**Weryfikacja:**
- [ ] Grid layout działa
- [ ] Notebook (zakładki) OK

---

### Tydzień 25 (26 Maja - 1 Czerwca): Integracja GUI + Backend

**Dzień 1-3: Połączenie z bazą**
```python
class ShopGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("System Sklepu")

        # Backend
        self.db = DatabaseManager(conn_string)
        self.db.connect()
        self.product_repo = ProductRepository(self.db)

        self.create_gui()

    def create_gui(self):
        # Notebook
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True)

        # Zakładki
        self.create_products_tab(notebook)
        self.create_customers_tab(notebook)
        self.create_orders_tab(notebook)

    def create_products_tab(self, notebook):
        tab = ttk.Frame(notebook)
        notebook.add(tab, text="Produkty")

        # Listbox z produktami
        self.products_listbox = tk.Listbox(tab, width=50, height=20)
        self.products_listbox.pack(side=tk.LEFT, padx=10, pady=10)

        # Przyciski
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(side=tk.LEFT, padx=10, pady=10)

        ttk.Button(btn_frame, text="Dodaj produkt",
                   command=self.add_product).pack(pady=5)
        ttk.Button(btn_frame, text="Edytuj produkt",
                   command=self.edit_product).pack(pady=5)
        ttk.Button(btn_frame, text="Usuń produkt",
                   command=self.delete_product).pack(pady=5)
        ttk.Button(btn_frame, text="Odśwież",
                   command=self.load_products).pack(pady=5)

        # Ładowanie produktów
        self.load_products()

    def load_products(self):
        self.products_listbox.delete(0, tk.END)
        products = self.product_repo.get_all()
        for p in products:
            self.products_listbox.insert(tk.END,
                f"{p.name} - {p.price} zł (stan: {p.quantity})")

    def add_product(self):
        # Nowe okno (Toplevel)
        dialog = tk.Toplevel(self.root)
        dialog.title("Dodaj produkt")

        # Pola formularza
        tk.Label(dialog, text="Nazwa:").grid(row=0, column=0)
        name_entry = tk.Entry(dialog)
        name_entry.grid(row=0, column=1)

        tk.Label(dialog, text="Cena:").grid(row=1, column=0)
        price_entry = tk.Entry(dialog)
        price_entry.grid(row=1, column=1)

        # ... etc

        def save():
            product = Product(
                name=name_entry.get(),
                price=float(price_entry.get()),
                # ...
            )
            self.product_repo.create(product)
            self.load_products()
            dialog.destroy()

        tk.Button(dialog, text="Zapisz", command=save).grid(row=5, column=0)

    def run(self):
        self.root.mainloop()

# Uruchomienie
if __name__ == "__main__":
    app = ShopGUI()
    app.run()
```

**Dzień 4-7: Wszystkie zakładki**
- [ ] Zakładka Produkty (gotowa)
- [ ] Zakładka Klienci (analogicznie)
- [ ] Zakładka Zamówienia (formularz + lista)
- [ ] Zakładka Raporty (przyciski generowania)

**Weryfikacja:**
- [ ] GUI połączone z Azure SQL
- [ ] CRUD przez GUI działa
- [ ] Wszystkie zakładki OK

---

### Tydzień 26 (2-8 Czerwca): PROJEKT MIESIĄCA

**System Sklepu v5.0 - FINAŁ (GUI + Azure SQL + Blob Storage)**

**Wymagania:**

**4 zakładki:**
1. **Produkty:**
   - Listbox z produktami
   - Przyciski: Dodaj, Edytuj, Usuń, Odśwież
   - Dialog do dodawania/edycji (Grid layout)
   - Walidacja (try-except + messagebox)

2. **Klienci:**
   - Analogicznie jak Produkty
   - Walidacja email (regex)

3. **Zamówienia:**
   - Combobox wyboru klienta
   - Listbox produktów (multi-select)
   - Spinbox ilości
   - Przycisk "Złóż zamówienie"
   - Transakcja SQL (commit/rollback)
   - Messagebox z potwierdzeniem

4. **Raporty:**
   - 5 przycisków (dla każdego raportu)
   - Generowanie Excel
   - Upload do Azure Blob
   - Messagebox: "Raport wygenerowany i przesłany do Azure"
   - Przycisk "Lista raportów w Azure"
   - Przycisk "Pobierz raport"

**Technologie:**
- Frontend: Tkinter (4 zakładki)
- Backend: OOP (repositories)
- Database: Azure SQL Database
- Storage: Azure Blob Storage
- Raporty: pandas + openpyxl

**Wymagania techniczne:**
- ~1200 linii kodu
- Try-except + messagebox dla błędów
- PEP 8 compliant
- Docstringi

**Weryfikacja końca Maja:**
- [ ] System v5.0 w 100% funkcjonalny
- [ ] GUI profesjonalny
- [ ] Azure SQL + Blob działają
- [ ] **GOTOWY NA DEMO!**

---

## CZERWIEC 2026 - Azure Cloud (Functions, App Service)

**Cel:** Deployment aplikacji w Azure

**Czas:** 30 dni × 3.5h = 105 godzin

### Tydzień 27 (9-15 Czerwca): Azure Functions

**Dzień 1-3: Pierwsza Function**
- [ ] Utworzenie Function App w Azure
- [ ] Pierwsza HTTP triggered function (Python)
- [ ] Testowanie w przeglądarce

**Przykład:**
```python
# __init__.py
import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(
            f"Hello, {name}!",
            status_code=200
        )
    else:
        return func.HttpResponse(
            "Please pass a name",
            status_code=400
        )
```

**Dzień 4-7: Functions dla systemu**
- [ ] Function: GenerateProductReport (HTTP trigger)
- [ ] Function: GetProducts (HTTP trigger)
- [ ] Function: CreateOrder (HTTP trigger)
- [ ] Timer trigger: Auto-backup co 24h

**Weryfikacja:**
- [ ] Azure Functions działa
- [ ] HTTP triggers OK
- [ ] Timer trigger działa

---

### Tydzień 28 (16-22 Czerwca): Azure App Service

**Dzień 1-3: Flask API**
```python
# app.py
from flask import Flask, jsonify, request
import pyodbc

app = Flask(__name__)

# Connection string z environment variables
conn_string = os.environ.get('AZURE_SQL_CONNECTION_STRING')

@app.route('/api/products', methods=['GET'])
def get_products():
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produkty")
    products = []
    for row in cursor.fetchall():
        products.append({
            'id': row.id,
            'name': row.nazwa,
            'price': float(row.cena),
            'quantity': row.ilosc
        })
    conn.close()
    return jsonify(products)

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO produkty (nazwa, cena, ilosc)
        VALUES (?, ?, ?)
    """, (data['name'], data['price'], data['quantity']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product created'}), 201

if __name__ == '__main__':
    app.run()
```

**Dzień 4-7: Deployment do Azure App Service**
- [ ] Utworzenie Web App
- [ ] Deploy przez VS Code lub Azure CLI
- [ ] Konfiguracja environment variables
- [ ] Testowanie API

**Weryfikacja:**
- [ ] Flask API działa lokalnie
- [ ] Deployment do Azure OK
- [ ] API dostępne z internetu

---

### Tydzień 29 (23-29 Czerwca): Monitoring i Security

**Dzień 1-3: Application Insights**
- [ ] Dodanie Application Insights do Function App
- [ ] Monitoring logów
- [ ] Performance metrics
- [ ] Custom events

**Dzień 4-7: Security**
- [ ] Azure Key Vault (przechowywanie secrets)
- [ ] Managed Identity
- [ ] Connection strings z Key Vault
- [ ] HTTPS tylko (wymuszenie)

**Weryfikacja:**
- [ ] Monitoring działa
- [ ] Secrets w Key Vault
- [ ] Security best practices

---

### Tydzień 30 (30 Czerwca - 6 Lipca): PROJEKT MIESIĄCA

**System Sklepu v6.0 - Cloud Native**

**Architektura:**
```
Frontend (Tkinter Desktop App)
    ↓ (HTTP requests)
Azure App Service (Flask REST API)
    ↓ (pyodbc)
Azure SQL Database
    ↓ (backup)
Azure Blob Storage
    ↑ (monitoring)
Application Insights
```

**Komponenty:**

1. **Flask REST API** (Azure App Service):
   - Endpoints: GET/POST/PUT/DELETE dla produktów, klientów, zamówień
   - Autoryzacja (API key)
   - Error handling
   - Logging

2. **Tkinter Client** (Desktop):
   - Zamiast bezpośredniego połączenia z SQL → wywołania HTTP do API
   - Biblioteka `requests`
   - Wszystkie funkcje jak v5.0, ale przez API

3. **Azure Functions** (background tasks):
   - Daily backup (timer trigger)
   - Email notifications (queue trigger)
   - Report generation (HTTP trigger)

4. **Monitoring:**
   - Application Insights
   - Alerty (email gdy błąd)

**Weryfikacja końca Czerwca:**
- [ ] System v6.0 Cloud Native działa
- [ ] API w Azure App Service
- [ ] Desktop app przez API
- [ ] Azure Functions działają
- [ ] Monitoring OK

---

## LIPIEC 2026 - Projekt Finałowy (Praca Inżynierska)

**Cel:** Dokończyć i dopracować system na obronę

**Czas:** 31 dni × 4h = 124 godziny

### Tydzień 31 (7-13 Lipca): Dodatkowe funkcje

**Rozszerzenia:**
- [ ] Oracle Database (opcjonalnie - read-only)
- [ ] Databricks (podstawy - analityka)
- [ ] Power BI (wizualizacja raportów)
- [ ] Azure Logic Apps (automatyzacja workflow)
- [ ] Azure DevOps (CI/CD pipeline)

---

### Tydzień 32-33 (14-27 Lipca): Dokumentacja

**Wymagania:**

1. **README.md** (10+ stron):
   - Opis projektu
   - Architektura (diagramy!)
   - Technologie użyte
   - Instalacja (lokalna + Azure)
   - Konfiguracja
   - Użycie (screenshots!)
   - API documentation
   - Troubleshooting

2. **USER_GUIDE.md**:
   - Instrukcja dla użytkownika końcowego
   - Screenshots każdej funkcji
   - FAQ

3. **ARCHITECTURE.md**:
   - Szczegółowa architektura
   - Diagramy (draw.io / Lucidchart)
   - Database schema
   - API endpoints
   - Azure resources

4. **DEPLOYMENT.md**:
   - Krok po kroku deployment do Azure
   - Konfiguracja środowiska
   - Environment variables
   - Security checklist

---

### Tydzień 34 (28 Lipca - 3 Sierpnia): Testy i Optymalizacja

**Testy:**
- [ ] Unit testy (pytest)
- [ ] Integration testy
- [ ] Load testing (Azure Load Testing)
- [ ] Security testing (OWASP)

**Optymalizacja:**
- [ ] Indeksy w bazie danych
- [ ] Caching (Azure Cache for Redis - opcjonalnie)
- [ ] Query optimization
- [ ] Code refactoring

---

## SIERPIEŃ 2026 - Finalizacja

**Cel:** Prezentacja i obrona

**Tydzień 35-36 (4-17 Sierpnia): Prezentacja**

**Slajdy (20-25):**
1. Tytuł + autor
2. Problem biznesowy
3. Cel pracy
4. Technologie
5-8. Architektura (4 slajdy z diagramami)
9-12. Funkcjonalności (screenshots)
13-15. Azure Cloud (Functions, App Service, SQL, Blob)
16-17. Demo live
18. Wyniki (performance metrics)
19. Wnioski
20. Kierunki rozwoju (Oracle, Databricks, AI/ML)
21. Bibliografia
22. Pytania

**Przygotowanie demo:**
- [ ] Video demo (5 minut)
- [ ] Live demo (plan B jeśli internet nie działa)
- [ ] Backup prezentacji

**Tydzień 37 (18-24 Sierpnia): Rehearsal**
- [ ] Próba prezentacji (3×)
- [ ] Timing (20 minut maks)
- [ ] Odpowiedzi na możliwe pytania
- [ ] Feedback od kolegów

---

## WRZESIEŃ 2026 - Obrona!

**Tydzień 38+ (1-30 Września):**
- [ ] Ostatnie poprawki
- [ ] Druk pracy
- [ ] Złożenie pracy
- [ ] **OBRONA PRACY INŻYNIERSKIEJ** 🎓

---

## Podsumowanie - Co osiągniesz

### Projekty w portfolio:

1. ✅ Lista zakupów (Grudzień - DONE)
2. ✅ Słownik produktów (Grudzień - DONE)
3. System Biblioteki v1.0 (Grudzień)
4. System Sklepu v1.0 - Pure Python (Styczeń)
5. System Sklepu v2.0 - Azure SQL (Luty)
6. System Sklepu v3.0 - OOP + Azure (Marzec)
7. System Sklepu v4.0 - Excel + Blob (Kwiecień)
8. System Sklepu v5.0 - GUI Tkinter (Maj)
9. System Sklepu v6.0 - Cloud Native (Czerwiec)
10. **PRACA INŻYNIERSKA** - Finalna wersja (Lipiec-Sierpień)

### Technologie opanowane:

**Python:**
- Fundamenty (listy, słowniki, funkcje, klasy)
- JSON, datetime, regex
- List comprehensions, lambda
- Moduły, try-except zaawansowany
- openpyxl, pandas
- Tkinter (GUI)
- Flask (REST API)
- requests (HTTP client)
- pytest (testy)

**SQL:**
- SQL Server (lokalny)
- Azure SQL Database
- CREATE, INSERT, SELECT, UPDATE, DELETE
- JOIN-y, agregacje, GROUP BY
- Transakcje (COMMIT/ROLLBACK)
- Indeksy, optymalizacja

**Azure Cloud:**
- Azure SQL Database
- Azure Blob Storage
- Azure Functions
- Azure App Service
- Azure Key Vault
- Application Insights
- (opcjonalnie) Oracle, Databricks

**Narzędzia:**
- Git/GitHub
- VS Code
- Azure Portal
- SSMS
- Postman (API testing)

### Statystyki:

- **Godziny nauki:** ~900h (9 miesięcy × 100h/miesiąc)
- **Linie kodu:** ~15,000+
- **Commitów GitHub:** 200+
- **Dokumentacja:** 100+ stron
- **Prezentacja:** 25 slajdów

---

## Następne kroki - CO ROBIĆ TERAZ

### DZIŚ - 17 Grudnia (wtorek):
**Czas dostępny:** ~3-4h

**Priorytet 1: Dokończ `show_products()` i `sort_products()`**
- [ ] Widzę że zacząłeś `show_products()` - dokończ to!
- [ ] Widzę lambda w `sort_products()` - napraw błąd (linia 76: `key = lambda` jest niepoprawne)
  - Powinno być: `key=lambda item: item[0]` (sortowanie po nazwie)
  - Lub: `key=lambda item: item[1]['cena']` (sortowanie po cenie)
- [ ] Testuj te 2 funkcje z różnymi produktami

**Priorytet 2: Dodaj `edit_product()`**
- [ ] Funkcja do edycji produktu (zmiana ceny/ilości/kategorii)
- [ ] Walidacja jak w `add_product()`
- [ ] Testuj

**Jeśli zostanie czas:**
- [ ] GitHub: Jeśli nie masz repo - załóż! (c:\projekty\nauka → GitHub)
- [ ] Commit tego co masz

---

### 18-19 Grudnia (środa-czwartek):
**~6-8h total**
- [ ] `filter_by_category()` - pokaż tylko produkty z danej kategorii
- [ ] `find_max_price()` - znajdź najdroższy produkt
- [ ] `find_min_price()` - znajdź najtańszy produkt
- [ ] Wszystkie z walidacją!

---

### 20-22 Grudnia (pt-nd WEEKEND):
**~4-6h total (mniej w weekend!)**
- [ ] `calculate_total_value()` - suma wartości magazynu
- [ ] `low_stock_alert()` - produkty < 5 sztuk
- [ ] Review wszystkich funkcji
- [ ] Testy z różnymi danymi
- [ ] Commit do GitHub

---

### 23 Grudnia (pn):
**~3h**
- [ ] Refactoring kodu
- [ ] Dodaj docstringi do wszystkich funkcji
- [ ] PEP 8 formatting
- [ ] Ostatni commit przed świętami

---

### 24-26 Grudnia (ŚWIĘTA):
**Odpoczynek!** Lub max 1h/dzień jeśli masz ochotę i czas

---

### 27-29 Grudnia (pt-nd):
**~6h total**
- [ ] Ostatnie poprawki słownika produktów
- [ ] Przygotowanie do nauki JSON (poczytaj o module `json`)
- [ ] Lista funkcji które chcesz dodać w przyszłości

---

### 30-31 Grudnia (pn-wt):
**START Tygodnia 3: JSON!**
- [ ] Instalacja niczego nie trzeba - `json` to built-in
- [ ] Pierwszy zapis do JSON
- [ ] Pierwszy odczyt z JSON

**Szczegóły w planie powyżej (Tydzień 3)!**

---

**Powodzenia! Za 9 miesięcy będziesz inżynierem z pełnym systemem w Azure! 🚀**
