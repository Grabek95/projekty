# Plan Nauki: Od Zera do Systemu Automatyzacji Raportów

> **Termin realizacji:** 1 Grudnia 2025 - 30 Września 2026 (9 miesięcy)
> **Czas dzienny:** 30-90 minut (średnio 60 min)
> **Cel końcowy:** Praca inżynierska - System Automatyzacji Raportów SQL Server

---

## 📊 Twój Obecny Poziom

**Co już umiesz:**
- ✅ Podstawy Python: if, while, for
- ✅ Listy i słowniki
- ✅ Input/append, iteracje
- ✅ Podstawowe menu z opcją wyboru
- ✅ Konwersja liczb, max/min
- ✅ Podstawy SQL i baz danych

**Dokąd zmierzasz:**
- 🎯 System automatyzacji raportów (2385 linii kodu)
- 🎯 Backend: Python + SQL Server + pyodbc + pandas
- 🎯 Frontend: GUI Tkinter z zakładkami
- 🎯 Funkcje: Raporty Excel, zamówienia, transakcje
- 🎯 Praca inżynierska gotowa do obrony

---

## 🗺️ Mapa Podróży (36 Tygodni)

```
Miesiąc 1-2: Python Fundamenty        [████████░░░░░░░░] Tyg 1-8
Miesiąc 3:   SQL Server + Bazy        [░░░░░░░░████░░░░] Tyg 9-14
Miesiąc 4-5: OOP + pyodbc             [░░░░░░░░░░░░████] Tyg 15-20
Miesiąc 5:   pandas + Excel           [░░░░░░░░░░░░░░░░] Tyg 21-24
Miesiąc 6:   GUI Tkinter              [░░░░░░░░░░░░░░░░] Tyg 25-28
Miesiąc 7-9: Integracja + Projekt     [░░░░░░░░░░░░░░░░] Tyg 29-36
```

### Harmonogram Miesięczny

| Miesiąc | Faza | Technologie | Projekt Główny |
|---------|------|-------------|----------------|
| **Grudzień 2025** | Python Fundamenty 1/2 | Listy, funkcje, pliki, błędy | - |
| **Styczeń 2026** | Python Fundamenty 2/2 | Comprehensions, datetime, stringi | **System Biblioteki** |
| **Luty 2026** | SQL Server Podstawy | CREATE, INSERT, SELECT, JOIN | - |
| **Marzec 2026** | SQL + OOP Start | Transakcje, klasy | **System Sklepu - SQL** |
| **Kwiecień 2026** | Programowanie Obiektowe | OOP, pyodbc, architektura | - |
| **Maj 2026** | OOP + pandas | Backend, DataFrame, Excel | **System v1.0 + v2.0** |
| **Czerwiec 2026** | GUI Tkinter | Widgety, zakładki, messagebox | **System v3.0 (GUI)** |
| **Lipiec 2026** | Integracja | Refactoring, clean code | - |
| **Sierpień 2026** | Projekt Docelowy | Reprodukcja + rozszerzenia | **System Finałowy** |
| **Wrzesień 2026** | Praca Inżynierska | Databricks, dokumentacja | **Obrona** |

---

## 📚 FAZA 1: Python Fundamenty (Tygodnie 1-8)

### Tydzień 1: Listy i Słowniki
**📅 Czas:** 7 × 60 min = 7 godzin

**🎯 Cel:** Opanować podstawowe struktury danych

**📝 Program tygodnia:**
```
Dzień 1-2: Lista zakupów z menu
Dzień 3-4: Słownik produktów z cenami
Dzień 5-6: Operacje (append, remove, sort, max/min)
Dzień 7: Review + testy
```

**💻 Projekt:** Program "Sklep spożywczy"
```python
# Menu:
# 1. Dodaj produkt (nazwa + cena)
# 2. Usuń produkt
# 3. Wyświetl wszystkie (posortowane)
# 4. Najdroższy/najtańszy
```

**✅ Checklist:**
- [ ] Potrafię stworzyć i modyfikować listę
- [ ] Potrafię iterować po słowniku
- [ ] Rozumiem różnicę między listą a słownikiem
- [ ] Program działa bez błędów

**🔗 Odniesienie:** `system_automatyzacji_sqlserver.py` linie 1642-1681

---

### Tydzień 2: Funkcje i Modularyzacja
**📅 Czas:** 7 × 60 min = 7 godzin

**🎯 Cel:** Wydzielać logikę do funkcji

**📝 Program:**
```
Dzień 1-2: Przepisz program z tyg. 1 na funkcje
Dzień 3-4: Kalkulator z funkcjami
Dzień 5-6: Manager kontaktów
Dzień 7: Refactoring
```

**💻 Projekt:** Manager Kontaktów
```python
def dodaj_kontakt(slownik, nazwa, telefon):
    slownik[nazwa] = telefon

def znajdz_kontakt(slownik, nazwa):
    return slownik.get(nazwa, "Nie znaleziono")
```

**✅ Checklist:**
- [ ] Potrafię stworzyć funkcję z parametrami
- [ ] Rozumiem return
- [ ] Kod jest czytelniejszy niż bez funkcji

**🔗 Odniesienie:** Linie 1015-1080, 1282-1369

---

### Tydzień 3: Obsługa Plików
**📅 Czas:** 7 × 60 min = 7 godzin

**🎯 Cel:** Zapisywać dane do plików

**📝 Program:**
```
Dzień 1-2: Zapis do .txt
Dzień 3-4: JSON (słownik → plik)
Dzień 5-6: Logger operacji
Dzień 7: Backup system
```

**💻 Projekt:** Notatnik z persistence

**✅ Checklist:**
- [ ] Potrafię zapisać/wczytać z pliku
- [ ] Rozumiem JSON
- [ ] Program zachowuje dane po zamknięciu

**🔗 Odniesienie:** Linie 1370-1449

---

### Tydzień 4: Try-Except
**📅 Czas:** 7 × 60 min = 7 godzin

**🎯 Cel:** Obsługiwać błędy elegancko

**💻 Projekt:** Bank Account Simulator

**✅ Checklist:**
- [ ] Rozumiem ValueError, KeyError
- [ ] Program nie crashuje przy złych danych

**🔗 Odniesienie:** Linie 1002-1008

---

### Tydzień 5: List Comprehensions
**💻 Projekt:** Analiza zamówień

**✅ Checklist:**
- [ ] Potrafię użyć list comprehension
- [ ] Rozumiem enumerate()

---

### Tydzień 6: Daty i Czas
**💻 Projekt:** Task Tracker z deadline

**✅ Checklist:**
- [ ] Potrafię formatować daty (strftime)
- [ ] Rozumiem timedelta

**🔗 Odniesienie:** Linia 1377-1378

---

### Tydzień 7: String Manipulation
**💻 Projekt:** Contact Validator

**✅ Checklist:**
- [ ] Potrafię parsować stringi (split, strip)
- [ ] Rozumiem f-strings

**🔗 Odniesienie:** Linia 1379

---

### Tydzień 8: 🎖️ PROJEKT FAZY 1
**📅 Czas:** 7 × 90 min = 10.5 godzin

**💻 PROJEKT GŁÓWNY:** System Zarządzania Biblioteką

**Wymagania:**
- Dodaj/usuń książkę (słownik z tytułem, autorem, ISBN)
- Wyszukaj po tytule/autorze
- Wypożycz/zwróć (zapisz kto i kiedy)
- Raport: najczęściej wypożyczane
- Eksport/import JSON
- Logger wszystkich operacji
- Try-except wszędzie
- Menu użytkownika

**🏆 Weryfikacja końca Fazy 1:**
- [ ] Program 200+ linii działa
- [ ] Obsługa plików OK
- [ ] Try-except poprawnie
- [ ] Kod czytelny i skomentowany

---

## 💾 FAZA 2: SQL + Bazy Danych (Tygodnie 9-14)

### Tydzień 9: SQL Server - Podstawy
**📅 Czas:** 7 × 60 min = 7 godzin

**🎯 Cel:** Skonfigurować środowisko, podstawy SQL

**📝 Program:**
```
Dzień 1: Instalacja SQL Server Express + SSMS
Dzień 2: CREATE DATABASE
Dzień 3: CREATE TABLE
Dzień 4-5: INSERT, SELECT
Dzień 6: UPDATE, DELETE
Dzień 7: 50 zapytań SELECT
```

**💻 Projekt:** Baza kontaktów w SQL
```sql
CREATE DATABASE KontaktyDB;

CREATE TABLE kontakty (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nazwa NVARCHAR(100),
    email NVARCHAR(100),
    telefon NVARCHAR(20)
);

INSERT INTO kontakty (nazwa, email, telefon)
VALUES ('Jan Kowalski', 'jan@email.pl', '123456789');
```

**✅ Checklist:**
- [ ] SQL Server zainstalowany i działa
- [ ] Potrafię CREATE TABLE
- [ ] Potrafię INSERT, SELECT

**🔗 Odniesienie:** Linie 166-410

---

### Tydzień 10: Klucze Obce
**💻 Projekt:** Schemat bazy Sklep (klienci, produkty, zamówienia)

**✅ Checklist:**
- [ ] Rozumiem PRIMARY KEY vs FOREIGN KEY
- [ ] Rozumiem IDENTITY i NVARCHAR

**🔗 Odniesienie:** Linie 247-340

---

### Tydzień 11: WHERE, Agregacje
**💻 Projekt:** Raporty ze sklepu

**✅ Checklist:**
- [ ] Potrafię WHERE, ORDER BY
- [ ] Rozumiem COUNT, SUM, AVG

**🔗 Odniesienie:** Linie 1528-1570

---

### Tydzień 12: JOIN
**💻 Projekt:** Raport sprzedaży z JOIN

**✅ Checklist:**
- [ ] Rozumiem INNER vs LEFT JOIN
- [ ] Potrafię połączyć 3 tabele

**🔗 Odniesienie:** Linie 1029-1058

---

### Tydzień 13: Transakcje
**💻 Projekt:** Zamówienie = INSERT + UPDATE (atomowo)

**✅ Checklist:**
- [ ] Rozumiem COMMIT i ROLLBACK
- [ ] Wiem czym jest atomowość

**🔗 Odniesienie:** Linie 1282-1427

---

### Tydzień 14: 🎖️ PROJEKT FAZY 2
**📅 Czas:** 7 × 90 min = 10.5 godzin

**💻 PROJEKT GŁÓWNY:** System Sklepu - pure SQL

**Wymagania:**
- Schemat 4 tabel (klienci, produkty, ceny, zamówienia)
- Przykładowe dane (10 klientów, 20 produktów)
- **10 raportów SQL:**
  1. Wszystkie zamówienia ostatnich 7 dni
  2. Top 5 klientów (wartość zamówień)
  3. Produkty o niskim stanie (<10)
  4. Średnia wartość zamówienia
  5. Liczba zamówień per klient
  6. Najczęściej kupowany produkt
  7. Wartość magazynu (stan × cena)
  8. Klienci bez zamówień (LEFT JOIN)
  9. Historia cen produktu X
  10. Zamówienia z wartością >1000 PLN
- Procedura składania zamówienia (transakcja)

**🏆 Weryfikacja końca Fazy 2:**
- [ ] Schemat bazy z kluczami obcymi
- [ ] SELECT, INSERT, UPDATE, DELETE biegle
- [ ] JOIN-y bez problemu
- [ ] Transakcje działają

---

## 🎨 FAZA 3: OOP + pyodbc (Tygodnie 15-20)

### Tydzień 15: Klasy i Obiekty
**💻 Projekt:** Klasy dla sklepu (Klient, Produkt, Zamówienie)

**✅ Checklist:**
- [ ] Rozumiem klasę vs obiekt
- [ ] Potrafię stworzyć `__init__`
- [ ] Rozumiem self

**🔗 Odniesienie:** Linia 58, linie 64-113

---

### Tydzień 16: Enkapsulacja
**💻 Projekt:** Klasa Database wrapper

**✅ Checklist:**
- [ ] Rozumiem enkapsulację
- [ ] Klasy są logiczne

---

### Tydzień 17: Dziedziczenie i Kompozycja
**💻 Projekt:** System OOP (Shop, Customer, Product, Order)

**✅ Checklist:**
- [ ] Rozumiem dziedziczenie
- [ ] Rozumiem kompozycję

**🔗 Odniesienie:** Linia 1652 (kompozycja!)

---

### Tydzień 18: pyodbc
**💻 Projekt:** Python + SQL Manager

**✅ Checklist:**
- [ ] pyodbc działa
- [ ] Potrafię execute i fetchall
- [ ] Używam parametrów (?)

**🔗 Odniesienie:** Linie 31, 116-163, 1024-1068

---

### Tydzień 19: Architektura Warstwowa
**💻 Projekt:** Sklep z architekturą warstwową (Backend + Frontend)

**✅ Checklist:**
- [ ] Backend nie wie o interfejsie
- [ ] Frontend deleguje do backendu

**🔗 Odniesienie:** Linie 58-1449 (backend), 1631-2311 (frontend)

---

### Tydzień 20: 🎖️ PROJEKT FAZY 3
**📅 Czas:** 7 × 90 min = 10.5 godzin

**💻 PROJEKT GŁÓWNY:** System Sklepu v1.0 - Backend

**Wymagania:**
- Klasa ShopBackend z pyodbc
- Metody: get_customers(), get_products(), create_order()
- Raporty: generate_sales_report(), generate_inventory_report()
- Transakcje (commit/rollback)
- Obsługa błędów (try-except)
- Frontend tekstowy z menu

**🏆 Weryfikacja końca Fazy 3:**
- [ ] OOP - klasy i metody OK
- [ ] pyodbc biegle
- [ ] Architektura warstwowa działa
- [ ] System bez błędów

---

## 📊 FAZA 4: pandas + Excel (Tygodnie 21-24)

### Tydzień 21: pandas - Wprowadzenie
**💻 Projekt:** Analiza SQL w pandas

**✅ Checklist:**
- [ ] Rozumiem DataFrame
- [ ] Potrafię pd.read_sql

**🔗 Odniesienie:** Linie 34, 1062

---

### Tydzień 22: pandas - Zaawansowane
**💻 Projekt:** Raport sprzedaży w pandas (GroupBy, merge)

**✅ Checklist:**
- [ ] Potrafię groupby i merge
- [ ] Agregacje działają

---

### Tydzień 23: openpyxl
**💻 Projekt:** Generator raportów Excel

**✅ Checklist:**
- [ ] to_excel() działa
- [ ] Pliki otwierają się w Excel

**🔗 Odniesienie:** Linie 1370-1449

---

### Tydzień 24: 🎖️ PROJEKT FAZY 4
**📅 Czas:** 7 × 90 min = 10.5 godzin

**💻 PROJEKT GŁÓWNY:** System Sklepu v2.0 - z raportami Excel

**Wymagania:**
- Rozszerzenie v1.0 o pandas i Excel
- generate_sales_report_excel()
- generate_inventory_report_excel()
- generate_customer_report_excel()
- Timestamp w nazwach plików
- Wszystkie raporty → pliki .xlsx

**🏆 Weryfikacja końca Fazy 4:**
- [ ] pandas biegle
- [ ] Eksport do Excel działa
- [ ] System generuje 3 raporty

---

## 🖼️ FAZA 5: GUI Tkinter (Tygodnie 25-28)

### Tydzień 25: Tkinter - Podstawy
**💻 Projekt:** Kalkulator GUI

**✅ Checklist:**
- [ ] Rozumiem okno, widgety
- [ ] Button z command działa

**🔗 Odniesienie:** Linie 40, 1631, 1639-1645

---

### Tydzień 26: Widgety Zaawansowane
**💻 Projekt:** Formularz zamówienia GUI (Combobox, Spinbox, Text)

**✅ Checklist:**
- [ ] Combobox działa
- [ ] Text + Scrollbar OK

**🔗 Odniesienie:** Linie 1703-1889

---

### Tydzień 27: Zakładki i Messagebox
**💻 Projekt:** GUI z 3 zakładkami + messagebox

**✅ Checklist:**
- [ ] Notebook działa
- [ ] messagebox info/error OK
- [ ] GUI połączone z backendem

**🔗 Odniesienie:** Linie 1647-1673, 2184+

---

### Tydzień 28: 🎖️ PROJEKT FAZY 5
**📅 Czas:** 7 × 90 min = 10.5 godzin

**💻 PROJEKT GŁÓWNY:** System Sklepu v3.0 - z GUI

**Wymagania:**
- Backend z Fazy 3-4 + GUI Tkinter
- **3 zakładki:**
  1. **Raporty:** 3 buttony + Text preview
  2. **Zamówienia:** Combobox × 2 + Spinbox + Button
  3. **Statystyki:** Text stats + Button refresh
- Wszystkie widgety (Button, Combobox, Text, Spinbox)
- Callbacki z messagebox

**🏆 Weryfikacja końca Fazy 5:**
- [ ] GUI z 3 zakładkami
- [ ] Wszystkie funkcje działają przez GUI
- [ ] Kod modularny

---

## 🚀 FAZA 6: Integracja + Praca Inżynierska (Tygodnie 29-36)

### Tydzień 29-30: Połączenie Wszystkiego
**📅 Czas:** 14 × 60 min = 14 godzin

**Zadania:**
- Clean code, docstringi, komentarze
- Obsługa błędów wszędzie
- Walidacja inputu
- Testy manualne wszystkich ścieżek

---

### Tydzień 31-32: Reprodukcja Projektu Docelowego
**📅 Czas:** 14 × 90 min = 21 godzin

**Zadanie:** Przepisz `system_automatyzacji_sqlserver.py` linia po linii

**Metoda:**
- Czytaj kod źródłowy ze zrozumieniem
- Przepisuj (NIE kopiuj!)
- Dodawaj komentarze własnymi słowami
- Testuj każdą metodę

**✅ Weryfikacja:**
- [ ] System identyczny jak docelowy
- [ ] Wszystkie 3 raporty działają
- [ ] Składanie zamówień działa
- [ ] Transakcje (commit/rollback) OK
- [ ] GUI identyczne
- [ ] Komentarze własne

---

### Tydzień 33-34: Rozszerzenia Własne
**📅 Czas:** 14 × 90 min = 21 godzin

**Dodaj 5+ nowych funkcji:**
1. ✨ Filtrowanie raportów po dacie (od-do)
2. ✏️ Edycja klienta/produktu (GUI + SQL UPDATE)
3. 📈 Wykresy matplotlib (sprzedaż w czasie)
4. 📄 Eksport do CSV (oprócz Excel)
5. 📥 Import produktów z CSV (bulk insert)
6. 📜 Historia zmian cen (raport)
7. 💾 Backup bazy danych (przycisk w GUI)
8. 📝 Logger operacji (zapis do pliku)
9. 📊 Multi-sheet Excel (wszystkie raporty w jednym pliku)

**✅ Weryfikacja:**
- [ ] Co najmniej 5 funkcji działa
- [ ] Kod spójny ze stylem projektu
- [ ] Dokumentacja zaktualizowana

---

### Tydzień 35: Azure Databricks - Wprowadzenie
**📅 Czas:** 7 × 60 min = 7 godzin

**Cel:** Poznać Azure Databricks (przygotowanie do pracy inżynierskiej)

**Program:**
```
Dzień 1-2: Rejestracja Azure (free tier)
Dzień 3-4: Pierwszy notebook - analiza danych
Dzień 5-6: Migracja zapytań SQL do Databricks
Dzień 7: Porównanie SQL Server vs Databricks
```

**💻 Projekt:** Raport sprzedaży w Databricks (PySpark)

**✅ Checklist:**
- [ ] Azure Databricks skonfigurowany
- [ ] Potrafię stworzyć notebook
- [ ] Rozumiem PySpark DataFrame

---

### Tydzień 36: 🏆 PROJEKT FINAŁOWY - Praca Inżynierska
**📅 Czas:** 7 × 120 min = 14 godzin

**🎯 CEL:** Przygotować kompletny system + dokumentację na obronę

**Wymagania:**

### 1. Kod Produkcyjny
- ✅ Wszystkie funkcje projektu bazowego
- ✅ 5+ rozszerzeń własnych
- ✅ Komentarze i docstringi
- ✅ Clean code (PEP 8)
- ✅ Obsługa błędów wszędzie

### 2. Dokumentacja
**README.md:**
- Opis projektu
- Instrukcja instalacji (SQL Server, Python, biblioteki)
- Konfiguracja (config.ini)
- Screenshot GUI
- Lista funkcjonalności
- Architektura (diagramy)
- Przykłady użycia

**USER_GUIDE.md:**
- Jak używać każdej funkcji
- Screenshoty
- FAQ

### 3. Prezentacja (15-20 slajdów)
1. Slajd tytułowy
2. Problem biznesowy
3. Rozwiązanie techniczne
4. Technologie (Python, SQL Server, Tkinter, pandas)
5-10. Architektura + diagramy
11-15. Demo live (screenshoty)
16-18. Wyniki i wnioski
19. Kierunki rozwoju (Azure Databricks)
20. Podziękowania

### 4. Testy
- Scenariusze testowe (test plan)
- Bug report (znalezione i naprawione)
- Performance metrics (czas generowania raportów)

### 5. Struktura Projektu
```
projekt_inzynierski/
├── src/
│   ├── backend.py              # Klasa ReportAutomationSystem
│   ├── gui.py                  # Klasa ShopGUI
│   ├── database.py             # Wrapper pyodbc
│   └── utils.py                # Funkcje pomocnicze
├── config/
│   ├── config.ini              # Konfiguracja
│   └── config.example.ini      # Przykład
├── docs/
│   ├── README.md               # Dokumentacja główna
│   ├── USER_GUIDE.md           # Instrukcja użytkownika
│   └── ARCHITECTURE.md         # Architektura systemu
├── tests/
│   ├── test_backend.py         # Testy backendu
│   └── test_plan.md            # Plan testów
├── screenshots/
│   ├── gui_main.png
│   ├── raport_excel.png
│   └── database_stats.png
├── requirements.txt            # Zależności Python
├── setup.py                    # Instalator
└── LICENSE
```

**🏆 WERYFIKACJA KOŃCOWA:**
- [ ] System w 100% funkcjonalny
- [ ] Dokumentacja kompletna
- [ ] Prezentacja gotowa
- [ ] Projekt na GitHub (portfolio!)
- [ ] **GOTOWY DO OBRONY PRACY INŻYNIERSKIEJ**

---

## 📋 Master Checklist - Wszystkie Umiejętności

### ✅ Python Podstawy (Faza 1)
- [ ] Zmienne i typy danych (int, float, str, bool)
- [ ] Operatory (arytmetyczne, logiczne, porównania)
- [ ] If-elif-else (warunki)
- [ ] While i for (pętle)
- [ ] Lista (tworzenie, append, remove, sort, len)
- [ ] Słownik (tworzenie, keys, values, items, get)
- [ ] Tuple (niezmienne kolekcje)
- [ ] Funkcje (def, parametry, return)
- [ ] Obsługa plików (open, read, write, with)
- [ ] JSON (loads, dumps)
- [ ] Try-except (obsługa błędów)
- [ ] List comprehensions
- [ ] Datetime (now, strftime, timedelta)
- [ ] String manipulation (split, strip, upper, lower, f-strings)
- [ ] Import modułów

### ✅ SQL Server (Faza 2)
- [ ] Instalacja SQL Server Express
- [ ] SSMS (SQL Server Management Studio)
- [ ] CREATE DATABASE
- [ ] CREATE TABLE (typy danych)
- [ ] PRIMARY KEY, FOREIGN KEY
- [ ] IDENTITY (auto-increment)
- [ ] NVARCHAR vs VARCHAR
- [ ] INSERT INTO
- [ ] SELECT (podstawy)
- [ ] WHERE (warunki)
- [ ] ORDER BY (sortowanie)
- [ ] TOP N (limit wyników)
- [ ] COUNT, SUM, AVG, MIN, MAX (agregacje)
- [ ] GROUP BY
- [ ] INNER JOIN
- [ ] LEFT JOIN
- [ ] JOIN wielu tabel
- [ ] UPDATE
- [ ] DELETE
- [ ] BEGIN TRANSACTION
- [ ] COMMIT
- [ ] ROLLBACK
- [ ] GETDATE() i inne funkcje SQL Server

### ✅ Programowanie Obiektowe (Faza 3)
- [ ] Klasa i obiekt - różnica
- [ ] Konstruktor `__init__`
- [ ] Atrybuty (self.nazwa)
- [ ] Metody instancji
- [ ] Enkapsulacja
- [ ] Dziedziczenie
- [ ] super()
- [ ] Kompozycja
- [ ] Architektura warstwowa (backend/frontend)
- [ ] pyodbc (instalacja)
- [ ] Connection string
- [ ] pyodbc.connect()
- [ ] cursor.execute()
- [ ] cursor.fetchall(), fetchone()
- [ ] conn.commit(), conn.rollback()
- [ ] Parametryzowane zapytania (?)
- [ ] Zamykanie połączeń

### ✅ pandas + Excel (Faza 4)
- [ ] pandas instalacja
- [ ] DataFrame vs Series
- [ ] Tworzenie DataFrame
- [ ] pd.read_sql()
- [ ] df.head(), df.info(), df.describe()
- [ ] Filtrowanie DataFrame
- [ ] Sortowanie (sort_values)
- [ ] GroupBy
- [ ] Agregacje (.agg, .sum, .mean)
- [ ] Merge (łączenie)
- [ ] Apply (własne funkcje)
- [ ] openpyxl instalacja
- [ ] df.to_excel()
- [ ] Timestamp w nazwach plików

### ✅ GUI Tkinter (Faza 5)
- [ ] Tworzenie okna (tk.Tk())
- [ ] Label (etykiety)
- [ ] Button (przyciski)
- [ ] Entry (input tekstowy)
- [ ] Event handling (command=)
- [ ] Grid layout
- [ ] Pack layout
- [ ] ttk (themed widgets)
- [ ] ttk.Combobox (dropdown)
- [ ] Text widget (wieloliniowy)
- [ ] Scrollbar
- [ ] Spinbox (liczby)
- [ ] ttk.Notebook (zakładki)
- [ ] messagebox.showinfo()
- [ ] messagebox.showerror()
- [ ] Organizacja kodu

### ✅ Integracja (Faza 6)
- [ ] Clean code (PEP 8)
- [ ] Docstringi
- [ ] Komentarze
- [ ] Modularyzacja
- [ ] Try-except wszędzie
- [ ] Walidacja inputu
- [ ] Performance
- [ ] Dokumentacja (README)
- [ ] Git + GitHub
- [ ] Azure Databricks (podstawy)
- [ ] PySpark DataFrame
- [ ] Prezentacja projektu

---

## 🎯 Projekty - Twoje Portfolio

Po zakończeniu planu będziesz miał **9 projektów** w portfolio:

1. **Sklep spożywczy** (Tydzień 1) - Listy i słowniki
2. **Manager Kontaktów** (Tydzień 2) - Funkcje
3. **Notatnik** (Tydzień 3) - Pliki i JSON
4. **Bank Simulator** (Tydzień 4) - Try-except
5. **🏆 System Biblioteki** (Tydzień 8) - Projekt Fazy 1
6. **🏆 System Sklepu - SQL** (Tydzień 14) - Projekt Fazy 2
7. **🏆 System Sklepu v1.0** (Tydzień 20) - Backend OOP
8. **🏆 System Sklepu v2.0** (Tydzień 24) - + pandas/Excel
9. **🏆 System Sklepu v3.0** (Tydzień 28) - + GUI Tkinter
10. **🏆🏆🏆 System Automatyzacji Raportów** (Tydzień 36) - PROJEKT FINAŁOWY

**Każdy projekt na GitHub = Twoje CV!**

---

## 📚 Zasoby Nauki

### Python
- 📖 [Python.org Tutorial](https://docs.python.org/3/tutorial/) - Oficjalna dokumentacja
- 🎥 [Kurs Python - Pasja Informatyki](https://www.youtube.com/playlist?list=PL6aekdNhY7DBgI8MFu7kIz7YtCgQOobFz) - PL, YouTube
- 📝 [RealPython Tutorials](https://realpython.com/) - Praktyczne artykuły
- 💻 [Exercism Python Track](https://exercism.org/tracks/python) - Ćwiczenia z mentorem
- 🎓 [W3Schools Python](https://www.w3schools.com/python/) - Interaktywne

### SQL Server
- 📖 [Microsoft SQL Docs](https://docs.microsoft.com/sql/) - Oficjalna dokumentacja
- 📝 [W3Schools SQL](https://www.w3schools.com/sql/) - Tutorial
- 💻 [SQLZoo](https://sqlzoo.net/) - Interaktywne ćwiczenia
- 🎥 [Kurs SQL - Pasja Informatyki](https://www.youtube.com/watch?v=RMN8-hEWU04) - PL, YouTube
- 🎓 [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/) - Zaawansowane

### Programowanie Obiektowe
- 📝 [RealPython - OOP](https://realpython.com/python3-object-oriented-programming/)
- 🎥 [Corey Schafer - OOP Series](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- 🎓 [Python OOP - Programiz](https://www.programiz.com/python-programming/object-oriented-programming)

### pandas + Excel
- 📖 [pandas Documentation](https://pandas.pydata.org/docs/) - Oficjalna
- 📝 [Pandas - W3Schools](https://www.w3schools.com/python/pandas/)
- 🎥 [Data School - pandas](https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y)
- 📖 [openpyxl Docs](https://openpyxl.readthedocs.io/)

### Tkinter
- 📖 [tkinter Documentation](https://docs.python.org/3/library/tkinter.html) - Oficjalna
- 📝 [TkDocs Tutorial](https://tkdocs.com/tutorial/)
- 🎥 [Corey Schafer - Tkinter](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
- 🎓 [RealPython - Tkinter](https://realpython.com/python-gui-tkinter/)

### Azure Databricks
- 📖 [Azure Databricks Docs](https://docs.microsoft.com/azure/databricks/)
- 🎓 [Databricks Academy](https://www.databricks.com/learn/training)
- 📝 [PySpark Tutorial](https://spark.apache.org/docs/latest/api/python/)

### Dodatkowe
- 💬 [Stack Overflow](https://stackoverflow.com/) - Q&A
- 🎮 [HackerRank - Python](https://www.hackerrank.com/domains/python) - Challenges
- 💻 [Codecademy - Python](https://www.codecademy.com/learn/learn-python-3)

---

## 🚀 Pierwsze Kroki - START JUTRO!

### Dzień 1 (1 Grudnia 2025): Pierwszy Program

**1. Stwórz folder projektu:**
```bash
mkdir C:\nauka_python\tydzien_1_struktury_danych
cd C:\nauka_python\tydzien_1_struktury_danych
```

**2. Otwórz edytor (VS Code / PyCharm / Notepad++)**

**3. Stwórz plik `lista_zakupow.py` i napisz:**

```python
# lista_zakupow.py
# Mój pierwszy program - Lista zakupów
# Data: 1 Grudnia 2025

zakupy = []

while True:
    print("\n=== LISTA ZAKUPÓW ===")
    print("1. Dodaj produkt")
    print("2. Pokaż listę")
    print("3. Wyjście")

    wybor = input("Wybierz opcję (1-3): ")

    if wybor == "1":
        produkt = input("Nazwa produktu: ")
        zakupy.append(produkt)
        print(f"✅ Dodano: {produkt}")

    elif wybor == "2":
        print("\n📋 Twoja lista:")
        if zakupy:
            for i, produkt in enumerate(zakupy, 1):
                print(f"  {i}. {produkt}")
        else:
            print("  (pusta)")

    elif wybor == "3":
        print("👋 Do widzenia!")
        break

    else:
        print("❌ Niepoprawna opcja!")
```

**4. Uruchom:**
```bash
python lista_zakupow.py
```

**5. Testuj:**
- Dodaj 3 produkty (mleko, chleb, masło)
- Wyświetl listę
- Wyjdź z programu

**🎉 GRATULACJE! Właśnie napisałeś swój pierwszy program!**

### Checklist Pierwszych 7 Dni:

- [ ] **Dzień 1:** Pierwszy program - lista zakupów ✅
- [ ] **Dzień 2:** Rozszerz o usuwanie produktów
- [ ] **Dzień 3:** Dodaj sortowanie alfabetyczne
- [ ] **Dzień 4:** Słownik produktów (nazwa → cena)
- [ ] **Dzień 5:** Funkcja "najtańszy produkt"
- [ ] **Dzień 6:** Funkcja "najdroższy produkt"
- [ ] **Dzień 7:** Review tygodnia + testy

---

## 💡 Tips & Tricks

### 🔥 Jak utrzymać motywację?

1. **Wizualizuj cel**
   - Wydrukuj screenshot projektu docelowego
   - Powieś nad biurkiem
   - Patrz na niego codziennie

2. **Tracking postępów**
   - Zaznaczaj checklisty w tym pliku
   - Commituj do GitHub codziennie
   - Prowadź dziennik nauki

3. **Mini-cele**
   - "Dziś nauczę się słowników" ✅
   - Nie: "Nauczę się Pythona" ❌

4. **Celebrate wins**
   - Ukończony tydzień = nagroda (film, kawa, coś dobrego)
   - Ukończona faza = większa nagroda

5. **Accountability**
   - Powiedz komuś o swoim planie
   - Dołącz do grupy programistycznej
   - Pokaż swoje projekty

6. **GitHub streak**
   - Commituj codziennie - nawet 1 linia kodu
   - Zobacz swój progres na profilu GitHub

7. **Before/After**
   - Porównuj kod z miesiąca temu
   - Widoczny progres = motywacja!

---

### 🐛 Co robić gdy coś nie działa?

**Strategia debugowania (w kolejności):**

**1. Przeczytaj błąd**
```
NameError: name 'produkty' is not defined
→ Zapomniałeś stworzyć zmienną 'produkty'
```

**2. print() debugging**
```python
print(f"klient_id: {klient_id}")
print(f"produkt_id: {produkt_id}")
```

**3. Google błędu**
- Skopiuj error message
- Dodaj "python" na początku
- Stack Overflow ma 99% odpowiedzi

**4. Uproszczenie**
```python
# Zamiast złożonego kodu:
result = complex_function(a, b, c, d)

# Testuj krok po kroku:
result = simple_function(a)  # Działa?
result = simple_function(a, b)  # Działa?
# Itd.
```

**5. Restart**
- Zamknij terminal
- Uruchom na nowo
- Czasem to pomaga!

**6. Poproś o pomoc (po 30 min walki)**
- Stack Overflow
- Reddit r/learnpython
- Discord serwery programistyczne

---

### 🔍 Jak szukać pomocy?

**Dobre pytanie na Stack Overflow:**

```
Tytuł: "Python pyodbc - connection timeout to SQL Server Express"

Pytanie:
Próbuję połączyć się z SQL Server Express używając pyodbc.

KOD:
[wklej minimalny kod reprodukujący problem]

BŁĄD:
[wklej pełny error message]

CO PRÓBOWAŁEM:
- SQL Server działa (sprawdzone)
- TCP/IP włączone
- Firewall wyłączony
- Connection string: "DRIVER={ODBC Driver 17...}"

SYSTEM:
Windows 11, Python 3.11, pyodbc 4.0.39, SQL Server Express 2019

Czy ktoś wie co może być nie tak?
```

**Złe pytanie:**
```
"pyodbc nie działa help"
```

---

### 📊 Jak śledzić postępy?

**1. Tygodniowy Review (każda niedziela, 15 min):**

```markdown
## Tydzień 1 Review - 7 Grudnia 2025

### Co zrobiłem:
- [x] Lista zakupów - działa!
- [x] Dodano usuwanie produktów
- [ ] Sortowanie (w trakcie)

### Czego się nauczyłem:
- Listy są super do przechowywania wielu elementów
- append() dodaje, remove() usuwa
- f-stringi czytelniejsze niż .format()

### Co było trudne:
- Sortowanie - muszę poćwiczyć
- Debugging - uczę się czytać błędy

### Plan na następny tydzień:
- Dokończyć sortowanie
- Zacząć tydzień 2 (funkcje)
```

**2. Miesięczny Milestone:**
- Napisz CHANGELOG.md
- Commituj do GitHub
- Pokaż projekt komuś

**3. Portfolio (od tygodnia 8):**
- Każdy projekt → GitHub repo
- README.md z opisem
- Screenshot
- Link w CV

**4. Blog/Notatki (opcjonalnie):**
- Notion / Obsidian
- "Dziś nauczyłem się X"
- Utrwala wiedzę!

---

### ⚠️ Częste Pułapki

**❌ Pułapka 1: Tutorial Hell**
- Problem: Oglądasz 10 tutoriali, nie piszesz kodu
- Rozwiązanie: **80% pisz kod, 20% oglądaj**

**❌ Pułapka 2: Perfectionism**
- Problem: "Kod musi być idealny zanim zapiszę"
- Rozwiązanie: **Ugly code that works > perfect code that doesn't exist**

**❌ Pułapka 3: Jumping ahead**
- Problem: "SQL nudne, przeskoczę do AI/ML"
- Rozwiązanie: **Fundamenty = fundament**

**❌ Pułapka 4: Copy-paste**
- Problem: Kopiujesz kod bez zrozumienia
- Rozwiązanie: **Przepisuj ręcznie, dodawaj komentarze**

**❌ Pułapka 5: Nie proszenie o pomoc**
- Problem: 5h nad jednym błędem
- Rozwiązanie: **Po 30 min → Google/Stack Overflow**

**❌ Pułapka 6: Brak prерw**
- Problem: 3h non-stop → burnout
- Rozwiązanie: **Pomodoro (25 min + 5 min przerwa)**

---

### 🎯 Zasada 3 Dni

**Jeśli utknąłeś na więcej niż 3 dni:**

- **Dzień 1:** Próbujesz sam (Google, dokumentacja)
- **Dzień 2:** Upraszczasz problem, prosisz AI o hint
- **Dzień 3:** Stack Overflow / forum / mentor
- **Dzień 4:** SKIP i wróć za tydzień

**Nie blokuj się - postęp > perfekcja**

---

## 📁 Kluczowe Pliki Projektu

Po zakończeniu nauki będziesz rozumiał **każdą linię** w tych plikach:

### 1. `system_automatyzacji_sqlserver.py` (2385 linii)
**Sekcje:**
- Linie 1-53: Importy, konfiguracja UTF-8
- Linie 58-113: Konstruktor (config.ini)
- Linie 116-163: Connection string builder
- Linie 166-410: Inicjalizacja bazy (CREATE DATABASE, TABLE)
- Linie 1015-1080: generate_sales_report()
- Linie 1083-1137: generate_inventory_report()
- Linie 1140-1211: generate_customer_report()
- Linie 1282-1369: create_order() **← TRANSAKCJA!**
- Linie 1370-1449: save_report_to_excel()
- Linie 1631-1673: GUI - Notebook, zakładki
- Linie 1675-1902: create_reports_tab()
- Linie 1904-2051: create_shop_tab()
- Linie 2053-2182: create_database_tab()
- Linie 2184-2311: Callbacki (messagebox)
- Linie 2313-2385: Main - punkt startowy

### 2. `config.ini` - Konfiguracja
### 3. `README.md` - Dokumentacja
### 4. `prd_markdown_doc.md` - Specyfikacja (PRD)

---

## 📊 Podsumowanie

**Czas całkowity:** 180-270 godzin
**Linie kodu napisane:** ~10,000+ (własnoręcznie!)
**Projekty:** 10 (8 mini + 2 główne)
**Rezultat:** Praca inżynierska + portfolio GitHub

**Timeline:**
```
START: 1 Grudnia 2025
META:  30 Września 2026
CEL:   System Automatyzacji Raportów + Obrona
```

---

## 🎓 Ostatnia Rada

> **"Nie próbuj być perfekcyjny. Próbuj być konsekwentny."**

**60 minut dziennie × 270 dni = MASTER LEVEL**

**60 minut co 3 dni × 90 dni = BEGINNER**

**Wybór jest Twój.**

---

## 🎯 Twoja Deklaracja

Wypełnij poniższe zobowiązanie:

```
Ja, [TWOJE IMIĘ], zobowiązuję się do nauki programowania
przez 60 minut dziennie przez najbliższe 9 miesięcy.

Cel: Praca inżynierska - System Automatyzacji Raportów

Data rozpoczęcia: 1 Grudnia 2025
Data zakończenia: 30 Września 2026

Podpis: ___________________
```

---

## 📞 Wsparcie

**Masz pytania? Utknąłeś?**

- 📧 Stack Overflow: [stackoverflow.com](https://stackoverflow.com)
- 💬 Reddit: [r/learnpython](https://reddit.com/r/learnpython)
- 🎮 Discord: Python Discord Server
- 📖 Dokumentacja: Zawsze pierwszy krok!

**Pamiętaj:**
- Ten plan jest wytyczną, nie więzieniem
- Możesz wrócić do poprzednich tygodni
- Możesz powtórzyć trudne sekcje
- Możesz dostosować tempo
- Możesz pominąć opcjonalne rozszerzenia

**Najważniejsze:**
- ✍️ **PISZ KOD CODZIENNIE** (nawet 10 linii)
- 🚫 **NIE KOPIUJ** - przepisuj ze zrozumieniem
- 🙋 **PYTAJ O POMOC** - nie siedź 5h nad błędem

---

## 🚀 Gotowy?

**Data startu: 1 GRUDNIA 2025**

**Pierwsza linia kodu: JUTRO!**

Za 9 miesięcy będziesz w zupełnie innym miejscu.

**See you on the other side! 🎓**

---

**Powodzenia w nauce! 🚀**

*Plan stworzony: 30 Listopada 2025*
*Ostatnia aktualizacja: 30 Listopada 2025*
