# PRD (Product Requirements Document)
## System Automatyzacji Raportów z Interfejsem Sklepu - SQL Server

---

### 📋 Informacje podstawowe

**Nazwa projektu:** System Automatyzacji Raportów z Interfejsem Sklepu (SQL Server)  
**Wersja:** 2.0  
**Data utworzenia:** 16 listopada 2025  
**Autor:** System automatyzacji biznesowej  
**Baza danych:** Microsoft SQL Server

---

## 1. Wprowadzenie

### 1.1 Cel dokumentu
Dokument określa wymagania funkcjonalne i techniczne dla systemu automatyzacji raportów sprzedażowych z wbudowanym interfejsem do zarządzania zamówieniami, wykorzystującego Microsoft SQL Server jako bazę danych.

### 1.2 Cel projektu
Stworzenie zautomatyzowanego systemu, który:
- Eliminuje ręczne przetwarzanie danych
- Generuje raporty biznesowe jednym kliknięciem
- Umożliwia zarządzanie zamówieniami przez prosty interfejs graficzny
- Zapewnia spójność danych w bazie SQL Server
- Integruje się z istniejącą infrastrukturą SQL Server w organizacji

### 1.3 Zakres projektu
System obejmuje:
- Automatyczne generowanie 3 typów raportów
- Interfejs graficzny do składania zamówień
- Zarządzanie bazą danych SQL Server (klienci, produkty, ceny, zamówienia)
- Eksport raportów do formatu Excel
- Obsługa Windows Authentication i SQL Server Authentication

---

## 2. Wymagania funkcjonalne

### 2.1 Moduł raportowania

#### RF-01: Raport sprzedaży
**Priorytet:** Wysoki  
**Opis:** System musi generować raport zawierający wszystkie zamówienia z SQL Server

**Szczegóły:**
- Lista zamówień z pełnymi informacjami
- Dane klienta dla każdego zamówienia
- Szczegóły produktu (nazwa, kategoria)
- Ilość i cena jednostkowa
- Wartość całkowita zamówienia
- Data i status zamówienia
- Sortowanie od najnowszych
- Zapytanie SQL z JOIN-ami dla optymalnej wydajności

**Akceptacja:**
- Raport zawiera wszystkie pola
- Dane są poprawnie połączone z tabel SQL Server
- Eksport do Excel działa prawidłowo
- Czas generowania < 3 sekundy dla 10000 rekordów

#### RF-02: Raport magazynowy
**Priorytet:** Wysoki  
**Opis:** System musi generować raport stanów magazynowych z SQL Server

**Szczegóły:**
- Lista wszystkich produktów
- Kategoria produktu
- Aktualny stan magazynowy
- Aktualna cena produktu (tylko aktywne ceny)
- Wartość magazynowa (stan × cena)
- Grupowanie po kategoriach
- Użycie `GETDATE()` dla aktualnych cen

**Akceptacja:**
- Wyświetlane są tylko ceny aktualne na dzień dzisiejszy
- Wartości są prawidłowo kalkulowane w SQL
- Sortowanie po kategorii i nazwie
- Obsługa produktów bez cen

#### RF-03: Raport klientów
**Priorytet:** Średni  
**Opis:** System musi generować raport podsumowujący aktywność klientów

**Szczegóły:**
- Lista wszystkich klientów z SQL Server
- Dane kontaktowe (email, telefon)
- Liczba złożonych zamówień
- Łączna wartość zakupów
- Sortowanie od najcenniejszych klientów
- Użycie `ISNULL` dla klientów bez zamówień

**Akceptacja:**
- Agregacja danych jest poprawna
- Klienci bez zamówień mają wartość 0
- Eksport zawiera wszystkie dane
- Kodowanie NVARCHAR dla polskich znaków

#### RF-04: Eksport raportów
**Priorytet:** Wysoki  
**Opis:** Wszystkie raporty muszą być eksportowane do Excel

**Szczegóły:**
- Format pliku: .xlsx
- Nazewnictwo: `{typ_raportu}_{YYYYMMDD_HHMMSS}.xlsx`
- Automatyczne zapisywanie w katalogu roboczym
- Potwierdzenie sukcesu z nazwą pliku
- Obsługa polskich znaków (NVARCHAR)

**Akceptacja:**
- Pliki są czytelne w Excel/LibreOffice
- Timestamp jest unikalny
- Komunikat potwierdza zapisanie
- Polskie znaki wyświetlają się poprawnie

### 2.2 Moduł sklepu

#### RF-05: Składanie zamówień
**Priorytet:** Wysoki  
**Opis:** Użytkownik musi móc składać zamówienia przez interfejs z zapisem do SQL Server

**Szczegóły:**
- Wybór klienta z listy rozwijanej
- Wybór produktu z dostępnych na stanie
- Określenie ilości (1-100 sztuk)
- Automatyczne pobieranie aktualnej ceny z SQL Server
- Walidacja stanu magazynowego
- Transakcyjność operacji (COMMIT/ROLLBACK)

**Akceptacja:**
- Niemożliwe zamówienie więcej niż stan magazynowy
- Cena pobierana automatycznie z tabeli ceny
- Komunikat sukcesu/błędu
- Atomowość transakcji (zamówienie + aktualizacja stanu)

#### RF-06: Zarządzanie stanem magazynowym
**Priorytet:** Wysoki  
**Opis:** System automatycznie aktualizuje stany magazynowe w SQL Server

**Szczegóły:**
- Zmniejszenie stanu po złożeniu zamówienia
- Blokada zamówienia przy niewystarczającym stanie
- Wyświetlanie aktualnego stanu przy produktach
- Użycie UPDATE w ramach transakcji

**Akceptacja:**
- Stan zmniejsza się o zamówioną ilość
- Komunikat przy braku towaru
- Synchronizacja między modułami
- Rollback przy błędach

#### RF-07: Odświeżanie danych
**Priorytet:** Średni  
**Opis:** Użytkownik może odświeżyć listy klientów i produktów

**Szczegóły:**
- Przycisk "Odśwież dane"
- Przeładowanie list wyboru z SQL Server
- Aktualizacja stanów magazynowych

**Akceptacja:**
- Dane aktualizują się natychmiast
- Widoczne zmiany po złożeniu zamówienia
- Poprawna obsługa błędów połączenia

### 2.3 Moduł bazy danych

#### RF-08: Statystyki bazy danych
**Priorytet:** Niski  
**Opis:** System wyświetla statystyki w czasie rzeczywistym z SQL Server

**Szczegóły:**
- Liczba klientów, produktów, zamówień
- Łączna wartość zamówień
- Wartość magazynu
- Top 3 najczęściej kupowane produkty (TOP 3 w SQL Server)

**Akceptacja:**
- Statystyki aktualizują się po zmianach
- Wartości są poprawnie kalkulowane
- Użycie agregacji SQL dla wydajności

#### RF-09: Zarządzanie połączeniem z SQL Server
**Priorytet:** Krytyczny  
**Opis:** System musi niezawodnie zarządzać połączeniami z SQL Server

**Szczegóły:**
- Support dla Windows Authentication
- Support dla SQL Server Authentication
- Automatyczne tworzenie bazy danych jeśli nie istnieje
- Komunikaty błędów przy problemach z połączeniem
- Connection string builder

**Akceptacja:**
- Jasne komunikaty o błędach połączenia
- Wsparcie obu metod autentykacji
- Automatyczna konfiguracja bazy

---

## 3. Wymagania niefunkcjonalne

### 3.1 Wydajność
- **NFR-01:** Generowanie raportu < 3 sekundy dla 10000 rekordów z SQL Server
- **NFR-02:** Zapisywanie zamówienia < 1 sekunda
- **NFR-03:** Odświeżanie interfejsu < 0.5 sekundy
- **NFR-04:** Otwieranie połączenia z SQL Server < 2 sekundy

### 3.2 Użyteczność
- **NFR-05:** Intuicyjny interfejs nie wymagający szkolenia
- **NFR-06:** Komunikaty w języku polskim
- **NFR-07:** Ikony emoji dla lepszej identyfikacji funkcji
- **NFR-08:** Jasne komunikaty błędów SQL Server

### 3.3 Niezawodność
- **NFR-09:** Obsługa błędów z komunikatami dla użytkownika
- **NFR-10:** Walidacja danych wejściowych
- **NFR-11:** Zabezpieczenie przed duplikacją plików (timestamp)
- **NFR-12:** Transakcyjność operacji bazodanowych
- **NFR-13:** Rollback przy błędach SQL
- **NFR-14:** Graceful degradation przy braku połączenia

### 3.4 Kompatybilność
- **NFR-15:** Python 3.7+
- **NFR-16:** SQL Server 2016+ (zalecane 2019+)
- **NFR-17:** ODBC Driver 17 for SQL Server
- **NFR-18:** System operacyjny: Windows, Linux (z odpowiednim ODBC)
- **NFR-19:** Eksport kompatybilny z Excel 2010+

### 3.5 Bezpieczeństwo
- **NFR-20:** Wsparcie Windows Authentication (zalecane)
- **NFR-21:** Opcjonalne SQL Server Authentication
- **NFR-22:** Brak hardcoded credentials w kodzie
- **NFR-23:** Connection string w zmiennych konfiguracyjnych

---

## 4. Architektura systemu

### 4.1 Struktura bazy danych SQL Server

#### Tabela: `klienci`
```sql
CREATE TABLE klienci (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nazwa NVARCHAR(255) NOT NULL,
    email NVARCHAR(255),
    telefon NVARCHAR(50),
    adres NVARCHAR(500)
)
```

#### Tabela: `produkty`
```sql
CREATE TABLE produkty (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nazwa NVARCHAR(255) NOT NULL,
    kategoria NVARCHAR(100),
    opis NVARCHAR(1000),
    stan_magazynowy INT DEFAULT 0
)
```

#### Tabela: `ceny`
```sql
CREATE TABLE ceny (
    id INT IDENTITY(1,1) PRIMARY KEY,
    produkt_id INT,
    cena DECIMAL(10,2) NOT NULL,
    data_od DATE,
    data_do DATE,
    FOREIGN KEY (produkt_id) REFERENCES produkty(id)
)
```

#### Tabela: `zamowienia`
```sql
CREATE TABLE zamowienia (
    id INT IDENTITY(1,1) PRIMARY KEY,
    klient_id INT,
    produkt_id INT,
    ilosc INT,
    cena_jednostkowa DECIMAL(10,2),
    data_zamowienia DATETIME DEFAULT GETDATE(),
    status NVARCHAR(50) DEFAULT 'nowe',
    FOREIGN KEY (klient_id) REFERENCES klienci(id),
    FOREIGN KEY (produkt_id) REFERENCES produkty(id)
)
```

### 4.2 Kluczowe różnice SQL Server vs SQLite

| Funkcjonalność | SQL Server | SQLite (poprzednia wersja) |
|----------------|-----------|---------------------------|
| Auto-increment | `IDENTITY(1,1)` | `AUTOINCREMENT` |
| Tekst Unicode | `NVARCHAR(n)` | `TEXT` |
| Liczby dziesiętne | `DECIMAL(10,2)` | `REAL` |
| Data aktualna | `GETDATE()` | `date('now')` |
| Top N rekordów | `TOP N` | `LIMIT N` |
| NULL handling | `ISNULL()` | `COALESCE()` |
| Sprawdzanie istnienia | `IF EXISTS` | Custom logic |

### 4.3 Komponenty systemu

```
┌─────────────────────────────────────────────────┐
│         Interfejs GUI (Tkinter)                 │
│  ┌──────────┬──────────┬──────────────┐        │
│  │ Raporty  │  Sklep   │  Baza danych │        │
│  └──────────┴──────────┴──────────────┘        │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│    ReportAutomationSystem (Logika biznesowa)    │
│  • generate_sales_report()                      │
│  • generate_inventory_report()                  │
│  • generate_customer_report()                   │
│  • create_order()                               │
│  • save_report_to_excel()                       │
│  • build_connection_string()                    │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│              pyodbc Driver                      │
│  • Connection pooling                           │
│  • Transaction management                       │
│  • Error handling                               │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│         Microsoft SQL Server                    │
│  • Database: SklepDB                            │
│  • Server: localhost\SQLEXPRESS lub custom      │
│  • Auth: Windows lub SQL Server                 │
└─────────────────────────────────────────────────┘
```

### 4.4 Connection String Management

**Windows Authentication (zalecane):**
```python
DRIVER={ODBC Driver 17 for SQL Server};
SERVER=localhost\SQLEXPRESS;
DATABASE=SklepDB;
Trusted_Connection=yes;
```

**SQL Server Authentication:**
```python
DRIVER={ODBC Driver 17 for SQL Server};
SERVER=localhost\SQLEXPRESS;
DATABASE=SklepDB;
UID=username;
PWD=password;
```

### 4.5 Przepływ danych

**Generowanie raportu:**
1. Użytkownik klika przycisk raportu
2. System otwiera połączenie z SQL Server (pyodbc)
3. Wykonuje zapytanie SQL z JOIN-ami
4. Dane przekształcane do DataFrame (pandas)
5. Wyświetlenie w interfejsie
6. Zapis do Excel z timestampem
7. Zamknięcie połączenia
8. Komunikat sukcesu

**Składanie zamówienia (transakcja):**
1. Użytkownik wybiera klienta i produkt
2. Określa ilość
3. System otwiera połączenie
4. **BEGIN TRANSACTION**
5. Sprawdza stan magazynowy (SELECT)
6. Pobiera aktualną cenę (SELECT)
7. Tworzy rekord w `zamowienia` (INSERT)
8. Aktualizuje `stan_magazynowy` (UPDATE)
9. **COMMIT** (lub **ROLLBACK** przy błędzie)
10. Zamknięcie połączenia
11. Komunikat sukcesu/błędu

---

## 5. Interfejs użytkownika

### 5.1 Zakładka "Raporty"

**Layout:**
- Nagłówek: "Generowanie Raportów"
- 3 przyciski z ikonami:
  - 📊 Raport Sprzedaży
  - 📦 Raport Magazynowy
  - 👥 Raport Klientów
- Obszar podglądu (Text widget ze scrollbarem)

**Interakcje:**
- Klik na przycisk → połączenie SQL Server → generowanie + podgląd
- Automatyczny zapis do Excel
- Popup z potwierdzeniem lub błędem połączenia

### 5.2 Zakładka "Sklep"

**Layout:**
- Nagłówek: "Składanie Zamówień"
- Formularz:
  - Combobox: Wybór klienta (z SQL Server)
  - Combobox: Wybór produktu (z ceną i stanem z SQL Server)
  - Spinbox: Ilość (1-100)
  - Przycisk: 🛒 Złóż zamówienie
- Przycisk: 🔄 Odśwież dane

**Interakcje:**
- Wybór z list rozwijanych (dane live z SQL Server)
- Walidacja przed zapisem
- Popup z rezultatem transakcji

### 5.3 Zakładka "Baza danych"

**Layout:**
- Nagłówek: "Informacje o Bazie Danych (SQL Server)"
- Text widget z statystykami
- Przycisk: 🔄 Odśwież statystyki
- Info o połączeniu (serwer, baza)

**Wyświetlane informacje:**
- Liczba klientów/produktów/zamówień
- Łączna wartość zamówień
- Wartość magazynu
- Top 3 produkty (TOP 3 SQL Server)
- Status połączenia

---

## 6. Zależności techniczne

### 6.1 Biblioteki Python

```python
# Standardowe
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os

# Zewnętrzne (wymagają instalacji)
import pyodbc         # pip install pyodbc
import pandas         # pip install pandas
import openpyxl       # pip install openpyxl
```

### 6.2 Wymagania ODBC Driver

**Windows:**
- Pobierz: [ODBC Driver 17 for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)
- Instalacja: uruchom MSI installer

**Linux (Ubuntu/Debian):**
```bash
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
```

### 6.3 Wymagania systemowe

**Minimalne:**
- Python 3.7+
- SQL Server 2016+ (lub Express)
- ODBC Driver 17 for SQL Server
- 50 MB przestrzeni dyskowej (aplikacja)
- 256 MB RAM
- Połączenie z SQL Server (lokalnie lub sieć)

**Zalecane:**
- Python 3.9+
- SQL Server 2019+ (lub Express 2019)
- ODBC Driver 18 for SQL Server
- 500 MB przestrzeni dyskowej
- 512 MB RAM
- SSD dla lepszej wydajności SQL Server

---

## 7. Konfiguracja i instalacja

### 7.1 Instalacja zależności

```bash
# Krok 1: Zainstaluj Python libraries
pip install pyodbc pandas openpyxl

# Krok 2: Zainstaluj ODBC Driver (jeśli nie zainstalowany)
# Windows: Pobierz MSI z Microsoft
# Linux: Zobacz sekcja 6.2
```

### 7.2 Konfiguracja SQL Server

**Opcja A: SQL Server Express (za darmo)**
1. Pobierz SQL Server Express 2019
2. Zainstaluj z domyślnymi ustawieniami
3. Nazwa instancji: `SQLEXPRESS`
4. Enable: TCP/IP, Named Pipes

**Opcja B: Istniejący SQL Server**
1. Sprawdź nazwę serwera: `SELECT @@SERVERNAME`
2. Upewnij się, że masz uprawnienia CREATE DATABASE

### 7.3 Konfiguracja aplikacji

**Edytuj w kodzie:**
```python
class ReportAutomationSystem:
    def __init__(self):
        # KONFIGURACJA - ZMIEŃ NA SWOJE WARTOŚCI
        self.server = 'localhost\\SQLEXPRESS'  # Twój serwer
        self.database = 'SklepDB'              # Nazwa bazy
        self.username = ''  # Puste dla Windows Auth
        self.password = ''  # Puste dla Windows Auth
```

**Przykłady konfiguracji:**

1. **Lokalne SQL Server Express (Windows Auth):**
   ```python
   self.server = 'localhost\\SQLEXPRESS'
   self.username = ''
   self.password = ''
   ```

2. **Zdalny SQL Server (SQL Auth):**
   ```python
   self.server = '192.168.1.100'
   self.username = 'sa'
   self.password = 'YourStrongPassword123!'
   ```

3. **Named instance:**
   ```python
   self.server = 'DESKTOP-ABC123\\SQLEXPRESS'
   self.username = ''
   self.password = ''
   ```

### 7.4 Pierwsze uruchomienie

1. Uruchom aplikację:
   ```bash
   python system_automatyzacji_sqlserver.py
   ```

2. System automatycznie:
   - Utworzy bazę `SklepDB` (jeśli nie istnieje)
   - Utworzy tabele
   - Wypełni przykładowymi danymi

3. Jeśli błąd połączenia:
   - Sprawdź czy SQL Server działa
   - Sprawdź nazwę serwera w SQL Server Management Studio
   - Sprawdź firewall (port 1433)
   - Sprawdź czy TCP/IP jest włączony

---

## 8. Dane początkowe

### 8.1 Przykładowi klienci (3)
- Firma ABC Sp. z o.o. (kontakt@abc.pl)
- Jan Kowalski (jan.kowalski@email.pl)
- Hurtownia XYZ (biuro@xyz.com)

### 8.2 Przykładowe produkty (5)
- Laptop Dell XPS 15 (Elektronika, 4999 zł, stan: 15)
- Monitor Samsung 27" (Elektronika, 1299 zł, stan: 25)
- Klawiatura mechaniczna (Akcesoria, 449 zł, stan: 50)
- Mysz bezprzewodowa (Akcesoria, 129 zł, stan: 100)
- Słuchawki Sony WH-1000XM4 (Audio, 1499 zł, stan: 30)

### 8.3 Inicjalizacja
System automatycznie:
- Sprawdza istnienie bazy danych
- Tworzy tabele jeśli nie istnieją (IF NOT EXISTS)
- Wypełnia przykładowymi danymi przy pierwszym uruchomieniu
- Używa NVARCHAR dla wsparcia polskich znaków

---

## 9. Scenariusze użycia

### 9.1 UC-01: Wygenerowanie raportu sprzedaży

**Aktor:** Użytkownik biznesowy  
**Cel:** Otrzymanie raportu wszystkich zamówień z SQL Server

**Warunki wstępne:**
- SQL Server działa
- Aplikacja ma połączenie z bazą
- Istnieją zamówienia w bazie

**Przebieg główny:**
1. Użytkownik otwiera zakładkę "Raporty"
2. Klika przycisk "📊 Raport Sprzedaży"
3. System łączy się z SQL Server
4. System wykonuje zapytanie SQL z JOIN-ami
5. Raport wyświetla się w podglądzie
6. System zapisuje raport do Excel
7. Pojawia się komunikat z nazwą pliku

**Przebieg alternatywny:**
- 3a. Brak połączenia z SQL Server
  - System wyświetla komunikat błędu z opisem problemu
  - Użytkownik może sprawdzić konfigurację

- 4a. Brak zamówień w bazie
  - System wyświetla komunikat "Brak zamówień"
  - Nie tworzy pliku Excel

### 9.2 UC-02: Złożenie zamówienia

**Aktor:** Pracownik sprzedaży  
**Cel:** Utworzenie zamówienia dla klienta w SQL Server

**Warunki wstępne:**
- SQL Server działa
- Istnieją klienci i produkty w bazie
- Produkt ma stan > 0

**Przebieg główny:**
1. Użytkownik otwiera zakładkę "Sklep"
2. Wybiera klienta z listy (pobrane z SQL Server)
3. Wybiera produkt z listy (z aktualną ceną)
4. Ustawia ilość
5. Klika "🛒 Złóż zamówienie"
6. System rozpoczyna transakcję SQL
7. Weryfikuje dostępność produktu
8. Pobiera aktualną cenę
9. Tworzy zamówienie (INSERT)
10. Aktualizuje stan magazynowy (UPDATE)
11. System wykonuje COMMIT
12. Pojawia się komunikat sukcesu

**Przebieg alternatywny:**
- 6a. Niewystarczający stan magazynowy
  - System wykonuje ROLLBACK
  - Wyświetla komunikat błędu z dostępnym stanem
  - Zamówienie nie zostaje utworzone

- 8a. Brak aktualnej ceny
  - System wykonuje ROLLBACK
  - Wyświetla komunikat błędu
  - Zamówienie nie zostaje utworzone

- 11a. Błąd SQL podczas COMMIT
  - System wykonuje ROLLBACK
  - Wyświetla komunikat błędu SQL
  - Stan bazy pozostaje niezmieniony

### 9.3 UC-03: Sprawdzenie statystyk

**Aktor:** Manager  
**Cel:** Przegląd kluczowych wskaźników z SQL Server

**Przebieg główny:**
1. Użytkownik otwiera zakładkę "Baza danych"
2. System łączy się z SQL Server
3. Wykonuje zapytania agregacyjne
4. Wyświetla statystyki
5. [Opcjonalnie] Użytkownik klika "🔄 Odśwież statystyki"
6. System ponownie pobiera dane

**Przebieg alternatywny:**
- 2a. Brak połączenia
  - System wyświetla "Brak połączenia z bazą danych"
  - Użytkownik może sprawdzić konfigurację

### 9.4 UC-04: Konfiguracja połączenia z SQL Server

**Aktor:** Administrator systemu  
**Cel:** Skonfigurowanie połączenia z SQL Server

**Przebieg główny:**
1. Administrator otwiera plik Python
2. Znajduje sekcję konfiguracji
3. Wprowadza nazwę serwera
4. Wybiera metodę autentykacji (Windows/SQL)
5. [Opcjonalnie] Wprowadza username/password
6. Zapisuje plik
7. Uruchamia aplikację
8. System testuje połączenie

**Przebieg alternatywny:**
- 8a. Błąd połączenia
  - System wyświetla szczegółowy komunikat błędu
  - Administrator weryfikuje konfigurację

---

## 10. Testowanie

### 10.1 Przypadki testowe

#### TC-01: Połączenie z SQL Server (Windows Auth)
- **Warunek:** SQL Server działa, Windows Auth włączona
- **Kroki:** Uruchom aplikację
- **Oczekiwany rezultat:** Połączenie nawiązane, statystyki widoczne

#### TC-02: Połączenie z SQL Server (SQL Auth)
- **Warunek:** Uzupełnione username/password
- **Kroki:** Uruchom aplikację
- **Oczekiwany rezultat:** Połączenie nawiązane, statystyki widoczne

#### TC-03: Błąd połączenia
- **Warunek:** Nieprawidłowa nazwa serwera
- **Kroki:** Uruchom aplikację
- **Oczekiwany rezultat:** Jasny komunikat błędu

#### TC-04: Generowanie raportu z dużej tabeli
- **Warunek:** 10000+ rekordów w zamowieniach
- **Kroki:** Kliknij "Raport Sprzedaży"
- **Oczekiwany rezultat:** Raport w < 3 sekundy

#### TC-05: Transakcja - sukces
- **Warunek:** Produkt ma stan > ilość zamówienia
- **Kroki:** Złóż zamówienie
- **Oczekiwany rezultat:** Zamówienie utworzone, stan zmniejszony

#### TC-06: Transakcja - rollback
- **Warunek:** Próba zamówienia więcej niż stan
- **Kroki:** Złóż zamówienie
- **Oczekiwany rezultat:** Rollback, komunikat błędu, stan niezmieniony

#### TC-07: Polskie znaki (NVARCHAR)
- **Warunek:** Klient z polskimi znakami (ą, ę, etc.)
- **Kroki:** Dodaj klienta, wygeneruj raport
- **Oczekiwany rezultat:** Znaki wyświetlają się poprawnie

#### TC-08: Automatyczne tworzenie bazy
- **Warunek:** Baza `SklepDB` nie istnieje
- **Kroki:** Uruchom aplikację
- **Oczekiwany rezultat:** Baza utworzona automatycznie

### 10.2 Testy akceptacyjne

- [ ] Połączenie z SQL Server działa (Windows Auth)
- [ ] Połączenie z SQL Server działa (SQL Auth)
- [ ] Wszystkie raporty generują się poprawnie
- [ ] Pliki Excel można otworzyć i odczytać
- [ ] Zamówienia aktualizują stan magazynowy
- [ ] Transakcje są atomowe (COMMIT/ROLLBACK)
- [ ] Walidacja działa poprawnie
- [ ] Polskie znaki wyświetlają się poprawnie
- [ ] Interfejs jest responsywny
- [ ] Komunikaty błędów SQL są zrozumiałe
- [ ] Automatyczne tworzenie bazy działa
- [ ] Top 3 produkty wyświetlają się poprawnie

### 10.3 Testy wydajnościowe

#### Benchmark 1: Raport sprzedaży
- **Dane:** 1000 zamówień
- **Oczekiwany czas:** < 1 sekunda
- **Metryka:** Czas wykonania zapytania SQL + pandas processing

#### Benchmark 2: Raport sprzedaży (duża tabela)
- **Dane:** 10000 zamówień
- **Oczekiwany czas:** < 3 sekundy
- **Metryka:** Czas całkowity generowania raportu

#### Benchmark 3: Złożenie zamówienia
- **Operacje:** INSERT + UPDATE w transakcji
- **Oczekiwany czas:** < 1 sekunda
- **Metryka:** Od kliknięcia przycisku do komunikatu

---

## 11. Wdrożenie

### 11.1 Plan wdrożenia

#### Faza 1: Przygotowanie środowiska (Dzień 1)
1. Zainstaluj SQL Server (jeśli nie zainstalowany)
2. Skonfiguruj Windows Authentication lub SQL Authentication
3. Włącz TCP/IP w SQL Server Configuration Manager
4. Zainstaluj ODBC Driver 17 for SQL Server
5. Zainstaluj Python 3.7+
6. Zainstaluj biblioteki: `pip install pyodbc pandas openpyxl`

#### Faza 2: Konfiguracja aplikacji (Dzień 1)
1. Pobierz kod aplikacji
2. Edytuj parametry połączenia (server, database, auth)
3. Uruchom aplikację testowo
4. Zweryfikuj automatyczne utworzenie bazy
5. Sprawdź przykładowe dane

#### Faza 3: Testy (Dzień 2)
1. Przeprowadź wszystkie przypadki testowe (TC-01 do TC-08)
2. Przetestuj wszystkie raporty
3. Przetestuj składanie zamówień
4. Sprawdź transakcyjność (rollback)
5. Zweryfikuj polskie znaki

#### Faza 4: Szkolenie użytkowników (Dzień 3)
1. Pokaz funkcjonalności raportów
2. Pokaz składania zamówień
3. Omówienie komunikatów błędów
4. Q&A sesja

#### Faza 5: Uruchomienie produkcyjne (Dzień 4)
1. Backup obecnych danych (jeśli migracja)
2. Import danych produkcyjnych (jeśli potrzebne)
3. Rozpoczęcie używania systemu
4. Monitoring pierwszych operacji

### 11.2 Checklist przed wdrożeniem

**Infrastruktura:**
- [ ] SQL Server zainstalowany i działa
- [ ] ODBC Driver zainstalowany
- [ ] Firewall skonfigurowany (port 1433 jeśli zdalny)
- [ ] TCP/IP włączony w SQL Server
- [ ] Python 3.7+ zainstalowany

**Uprawnienia:**
- [ ] Użytkownik ma dostęp do SQL Server
- [ ] Uprawnienia CREATE DATABASE (dla pierwszego uruchomienia)
- [ ] Uprawnienia INSERT, UPDATE, SELECT na tabelach

**Aplikacja:**
- [ ] Biblioteki Python zainstalowane
- [ ] Parametry połączenia skonfigurowane
- [ ] Testowe uruchomienie pomyślne
- [ ] Przykładowe dane widoczne

**Backup:**
- [ ] Plan backupów SQL Server skonfigurowany
- [ ] Lokalizacja zapisywanych raportów ustalona
- [ ] Procedura odzyskiwania danych ustalona

### 11.3 Migracja z SQLite (jeśli dotyczy)

Jeśli poprzednio używałeś wersji SQLite i chcesz migrować dane:

**Krok 1: Export danych z SQLite**
```python
import sqlite3
import pandas as pd

# Połącz z SQLite
conn_sqlite = sqlite3.connect('sklep_baza.db')

# Export każdej tabeli
tables = ['klienci', 'produkty', 'ceny', 'zamowienia']
data = {}
for table in tables:
    data[table] = pd.read_sql_query(f"SELECT * FROM {table}", conn_sqlite)
    data[table].to_csv(f'{table}_export.csv', index=False)

conn_sqlite.close()
```

**Krok 2: Import do SQL Server**
```python
import pyodbc
import pandas as pd

# Połącz z SQL Server
conn_sqlserver = pyodbc.connect(your_connection_string)

# Import każdej tabeli
for table in ['klienci', 'produkty', 'ceny', 'zamowienia']:
    df = pd.read_csv(f'{table}_export.csv')
    # Usuń kolumnę id (będzie automatycznie generowana przez IDENTITY)
    if 'id' in df.columns:
        df = df.drop('id', axis=1)
    # Import do SQL Server
    df.to_sql(table, conn_sqlserver, if_exists='append', index=False)

conn_sqlserver.close()
```

---

## 12. Backup i recovery

### 12.1 Strategia backupów

#### Backup bazy danych SQL Server
```sql
-- Full backup (wykonuj codziennie)
BACKUP DATABASE SklepDB
TO DISK = 'C:\Backups\SklepDB_Full.bak'
WITH FORMAT, INIT, NAME = 'Full Backup of SklepDB';

-- Differential backup (wykonuj co godzinę w godzinach pracy)
BACKUP DATABASE SklepDB
TO DISK = 'C:\Backups\SklepDB_Diff.bak'
WITH DIFFERENTIAL, NAME = 'Differential Backup of SklepDB';
```

#### Automatyczny backup (SQL Server Agent Job)
1. Otwórz SQL Server Management Studio
2. Idź do: SQL Server Agent → Jobs
3. Utwórz nowy Job: "Daily SklepDB Backup"
4. Schedule: codziennie o 23:00
5. Step: wykonaj skrypt BACKUP DATABASE

#### Backup raportów Excel
- Zalecane: kopiowanie katalogu z raportami do chmury (OneDrive, Dropbox)
- Częstotliwość: automatyczne synchronizowanie
- Retencja: 30 dni

### 12.2 Procedura odzyskiwania

**Scenariusz 1: Przywrócenie bazy danych**
```sql
-- Zamknij wszystkie połączenia
ALTER DATABASE SklepDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;

-- Przywróć backup
RESTORE DATABASE SklepDB
FROM DISK = 'C:\Backups\SklepDB_Full.bak'
WITH REPLACE;

-- Przywróć tryb multi-user
ALTER DATABASE SklepDB SET MULTI_USER;
```

**Scenariusz 2: Odzyskiwanie pojedynczej tabeli**
```sql
-- Przywróć backup do nowej bazy
RESTORE DATABASE SklepDB_Recovery
FROM DISK = 'C:\Backups\SklepDB_Full.bak';

-- Skopiuj dane z tabeli
INSERT INTO SklepDB.dbo.zamowienia
SELECT * FROM SklepDB_Recovery.dbo.zamowienia
WHERE data_zamowienia >= '2025-11-15';

-- Usuń tymczasową bazę
DROP DATABASE SklepDB_Recovery;
```

---

## 13. Rozwój przyszły

### 13.1 Funkcje do rozważenia (Faza 2)

#### RF-10: Import danych z CSV/Excel
**Priorytet:** Średni  
**Opis:** Możliwość importu masowego klientów/produktów z plików

**Szczegóły:**
- Upload CSV lub Excel
- Mapowanie kolumn
- Walidacja przed importem
- Bulk INSERT do SQL Server

#### RF-11: Filtrowanie raportów po datach
**Priorytet:** Wysoki  
**Opis:** Raporty za wybrany okres czasu

**Szczegóły:**
- Date picker (od-do)
- Filtrowanie w SQL WHERE clause
- Porównania rok do roku

#### RF-12: Wykresy i wizualizacje
**Priorytet:** Średni  
**Opis:** Graficzne przedstawienie danych

**Szczegóły:**
- Wykres sprzedaży w czasie (matplotlib)
- Top produkty - wykres słupkowy
- Rozkład sprzedaży po kategoriach - wykres kołowy
- Export wykresów do raportów Excel

#### RF-13: Edycja danych przez UI
**Priorytet:** Niski  
**Opis:** CRUD operations dla klientów i produktów

**Szczegóły:**
- Formularze dodawania/edycji
- UPDATE statements do SQL Server
- Walidacja danych
- Audit trail (kto, kiedy zmienił)

#### RF-14: Historia zmian cen
**Priorytet:** Średni  
**Opis:** Pełna historia cenowa produktów

**Szczegóły:**
- Archiwizacja starych cen
- Raport zmian cen w czasie
- Analiza trendów cenowych

#### RF-15: Powiadomienia email
**Priorytet:** Niski  
**Opis:** Automatyczne wysyłanie raportów emailem

**Szczegóły:**
- SMTP configuration
- Scheduled reports (cron/task scheduler)
- Załączniki Excel
- Lista odbiorców

#### RF-16: Eksport do PDF
**Priorytet:** Niski  
**Opis:** Profesjonalne raporty PDF

**Szczegóły:**
- Template PDF (reportlab)
- Logo firmy
- Stopka, nagłówki
- Export obok Excel

#### RF-17: Multi-user support
**Priorytet:** Średni  
**Opis:** Role użytkowników (admin, pracownik, viewer)

**Szczegóły:**
- Login screen
- Role w SQL Server lub aplikacji
- Permissions na operacjach
- Audit log

#### RF-18: REST API
**Priorytet:** Niski  
**Opis:** Integracja z innymi systemami

**Szczegóły:**
- Flask/FastAPI backend
- Endpoints: /orders, /products, /reports
- JWT authentication
- API documentation (Swagger)

#### RF-19: Web interface
**Priorytet:** Średni  
**Opis:** Dostęp przez przeglądarkę

**Szczegóły:**
- Flask/Django backend
- React/Vue frontend
- Responsive design
- Ten sam SQL Server backend

### 13.2 Ulepszenia techniczne

#### Optymalizacja SQL Server
- **Indeksy:** Dodaj indeksy na często używane kolumny
  ```sql
  CREATE INDEX idx_zamowienia_data 
  ON zamowienia(data_zamowienia);
  
  CREATE INDEX idx_ceny_daty 
  ON ceny(data_od, data_do);
  ```

- **Stored Procedures:** Przenieś logikę do SQL Server
  ```sql
  CREATE PROCEDURE sp_GetSalesReport
  AS
  BEGIN
      SELECT z.id, k.nazwa, p.nazwa, ...
      FROM zamowienia z
      JOIN klienci k ON z.klient_id = k.id
      JOIN produkty p ON z.produkt_id = p.id
      ORDER BY z.data_zamowienia DESC;
  END
  ```

- **Views:** Materialized views dla często używanych raportów
  ```sql
  CREATE VIEW v_ProductInventoryValue AS
  SELECT p.id, p.nazwa, p.stan_magazynowy,
         c.cena, (p.stan_magazynowy * c.cena) as wartosc
  FROM produkty p
  LEFT JOIN ceny c ON p.id = c.produkt_id
  WHERE GETDATE() BETWEEN c.data_od AND c.data_do;
  ```

#### Connection Pooling
```python
# Implementacja connection pool
from pyodbc import pooling

pool = pooling.SimpleConnectionPool(
    minconn=2,
    maxconn=10,
    connection_string=self.connection_string
)
```

#### Logging i monitoring
```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger.info("Raport wygenerowany: raport_sprzedazy_20251116")
logger.error(f"Błąd SQL: {str(e)}")
```

#### Async operations (dla dużych raportów)
```python
import asyncio
import aioodbc

async def generate_report_async():
    conn = await aioodbc.connect(dsn=connection_string)
    cursor = await conn.cursor()
    await cursor.execute(query)
    # ... przetwarzanie
```

---

## 14. Ryzyka i ograniczenia

### 14.1 Ryzyka

| ID | Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja |
|----|--------|-------------------|-------|-----------|
| R-01 | Utrata połączenia z SQL Server | Średnie | Wysoki | Retry logic, komunikaty błędów, backup lokalny |
| R-02 | Błąd w transakcjach | Niskie | Krytyczny | ROLLBACK, testy transakcyjności, logging |
| R-03 | SQL Injection | Bardzo niskie | Krytyczny | Parametryzowane zapytania (pyodbc `?`) |
| R-04 | Przepełnienie tabeli | Bardzo niskie | Średni | Archiwizacja starych danych, monitoring rozmiaru |
| R-05 | Niezgodność ODBC Driver | Niskie | Wysoki | Dokumentacja wymagań, wsparcie instalacji |
| R-06 | Błędy kodowania (polskie znaki) | Niskie | Średni | NVARCHAR wszędzie, testy z polskimi znakami |
| R-07 | Wolne zapytania (duże tabele) | Średnie | Średni | Indeksy, optymalizacja SQL, stored procedures |
| R-08 | Konflikt wersji SQL Server | Niskie | Średni | Kompatybilność z SQL Server 2016+ |

### 14.2 Ograniczenia

**Techniczne:**
- SQL Server Express: limit 10 GB na bazę (Full version nieograniczony)
- pyodbc: single-threaded (asyncio dla wysokiej wydajności)
- Tkinter: desktop only (web interface w przyszłości)
- Brak autentykacji w aplikacji (security w SQL Server)

**Funkcjonalne:**
- Brak kontroli wersji dokumentów (tylko timestamp)
- Single-user editing (bez conflict resolution)
- Wszystkie ceny w PLN (brak multi-currency)
- Brak workflow approval (zamówienia od razu zatwierdzone)

**Skalowanie:**
- Do ~100,000 zamówień bez problemów
- Powyżej 100,000: rozważ partycjonowanie tabel
- Powyżej 1,000,000: rozważ archiwizację starych danych

---

## 15. Bezpieczeństwo

### 15.1 Best practices

#### Połączenie z SQL Server
- **Zalecane:** Windows Authentication (Integrated Security)
- **Unikaj:** Hardcoded passwords w kodzie
- **Używaj:** Zmiennych środowiskowych lub config file

```python
# Dobra praktyka: config file
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

server = config['DATABASE']['Server']
database = config['DATABASE']['Database']
```

#### SQL Injection Prevention
```python
# ✅ DOBRZE - parametryzowane zapytanie
cursor.execute("SELECT * FROM klienci WHERE id = ?", (klient_id,))

# ❌ ŹLE - konkatenacja stringów
cursor.execute(f"SELECT * FROM klienci WHERE id = {klient_id}")
```

#### Uprawnienia SQL Server
```sql
-- Utwórz dedykowanego użytkownika aplikacji
CREATE LOGIN SklepApp WITH PASSWORD = 'StrongPassword123!';
CREATE USER SklepApp FOR LOGIN SklepApp;

-- Przydziel minimalne wymagane uprawnienia
GRANT SELECT, INSERT, UPDATE ON klienci TO SklepApp;
GRANT SELECT, INSERT, UPDATE ON produkty TO SklepApp;
GRANT SELECT, INSERT, UPDATE ON zamowienia TO SklepApp;
GRANT SELECT ON ceny TO SklepApp;

-- NIE DAWAJ: db_owner, sysadmin
```

#### Encryption (dla produkcji)
```sql
-- Włącz TLS/SSL dla połączeń
-- W connection string:
Encrypt=yes;TrustServerCertificate=no;
```

### 15.2 Audit i compliance

**Logging operacji:**
```sql
-- Tabela audit log
CREATE TABLE audit_log (
    id INT IDENTITY(1,1) PRIMARY KEY,
    tabela NVARCHAR(50),
    operacja NVARCHAR(10),
    uzytkownik NVARCHAR(100),
    data_operacji DATETIME DEFAULT GETDATE(),
    dane_przed NVARCHAR(MAX),
    dane_po NVARCHAR(MAX)
);

-- Trigger dla auditu (przykład)
CREATE TRIGGER trg_audit_zamowienia
ON zamowienia
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    INSERT INTO audit_log (tabela, operacja, uzytkownik)
    VALUES ('zamowienia', 'INSERT', SYSTEM_USER);
END
```

---

## 16. FAQ - Najczęściej zadawane pytania

### Q1: Jak sprawdzić nazwę mojego SQL Server?
**A:** W SQL Server Management Studio wykonaj:
```sql
SELECT @@SERVERNAME
```
Lub w command line:
```cmd
sqlcmd -L
```

### Q2: Błąd "Cannot open database SklepDB"
**A:** Sprawdź:
1. Czy użytkownik ma uprawnienia do CREATE DATABASE
2. Czy SQL Server działa: `services.msc` → SQL Server (SQLEXPRESS)
3. Czy w kodzie poprawna nazwa bazy

### Q3: Błąd "ODBC Driver not found"
**A:** Zainstaluj ODBC Driver 17:
- Windows: Pobierz MSI z Microsoft
- Linux: `sudo apt-get install msodbcsql17`

### Q4: Jak zmienić z Windows Auth na SQL Auth?
**A:** W kodzie ustaw:
```python
self.username = 'twoj_user'
self.password = 'twoje_haslo'
```

### Q5: Polskie znaki wyświetlają się jako "?"
**A:** Upewnij się, że:
- Używasz NVARCHAR (nie VARCHAR)
- Connection string ma właściwe kodowanie
- W Pythonie używasz UTF-8

### Q6: Jak migrować z SQLite?
**A:** Zobacz sekcja 11.3 - Migracja z SQLite

### Q7: Czy mogę używać Azure SQL Database?
**A:** Tak! Zmień connection string:
```python
self.server = 'yourserver.database.windows.net'
self.database = 'SklepDB'
self.username = 'azureuser'
self.password = 'AzurePassword123!'
```

### Q8: Jak dodać więcej użytkowników?
**A:** Obecnie single-user. Multi-user w Fazie 2 (patrz RF-17)

### Q9: Czy działa na Linux?
**A:** Tak, po zainstalowaniu:
- ODBC Driver for SQL Server (Linux)
- Python libraries
- SQL Server może być na Windows lub Linux

### Q10: Jak zoptymalizować dla dużych danych?
**A:** 
- Dodaj indeksy (sekcja 13.2)
- Użyj stored procedures
- Partycjonowanie tabel
- Archiwizuj stare dane

---

## 17. Glosariusz

| Termin | Definicja |
|--------|-----------|
| **SQL Server** | Relacyjny system zarządzania bazą danych Microsoft |
| **SSMS** | SQL Server Management Studio - narzędzie GUI dla SQL Server |
| **pyodbc** | Biblioteka Python do łączenia z bazami ODBC |
| **ODBC Driver** | Open Database Connectivity - standard dostępu do baz danych |
| **IDENTITY** | Auto-increment w SQL Server (odpowiednik AUTOINCREMENT) |
| **NVARCHAR** | Typ danych Unicode w SQL Server (wsparcie polskich znaków) |
| **GETDATE()** | Funkcja SQL Server zwracająca aktualną datę i czas |
| **Windows Authentication** | Logowanie do SQL Server używając konta Windows |
| **SQL Authentication** | Logowanie do SQL Server używając username/password |
| **Transaction** | Atomowa operacja bazodanowa (COMMIT lub ROLLBACK) |
| **Connection String** | Parametry połączenia z bazą danych |
| **DataFrame** | Struktura danych pandas do tabulacji |
| **TOP N** | SQL Server syntax dla limitowania wyników (zamiast LIMIT) |
| **ISNULL()** | Funkcja SQL Server do obsługi wartości NULL |

---

## 18. Załączniki

### 18.1 Przykładowe zapytania SQL Server

**Raport sprzedaży:**
```sql
SELECT 
    z.id as zamowienie_id,
    k.nazwa as klient,
    p.nazwa as produkt,
    p.kategoria,
    z.ilosc,
    z.cena_jednostkowa,
    (z.ilosc * z.cena_jednostkowa) as wartosc,
    z.data_zamowienia,
    z.status
FROM zamowienia z
JOIN klienci k ON z.klient_id = k.id
JOIN produkty p ON z.produkt_id = p.id
ORDER BY z.data_zamowienia DESC;
```

**Top produkty:**
```sql
SELECT TOP 3 
    p.nazwa, 
    SUM(z.ilosc) as suma
FROM zamowienia z
JOIN produkty p ON z.produkt_id = p.id
GROUP BY p.nazwa
ORDER BY suma DESC;
```

**Wartość magazynu:**
```sql
SELECT 
    SUM(p.stan_magazynowy * c.cena) as wartosc_magazynu
FROM produkty p
LEFT JOIN ceny c ON p.id = c.produkt_id 
    AND GETDATE() BETWEEN c.data_od AND c.data_do;
```

**Klienci bez zamówień:**
```sql
SELECT k.nazwa, k.email
FROM klienci k
LEFT JOIN zamowienia z ON k.id = z.klient_id
WHERE z.id IS NULL;
```

### 18.2 Przykładowy plik config.ini

```ini
[DATABASE]
Server = localhost\SQLEXPRESS
Database = SklepDB
Username = 
Password = 

[REPORTS]
OutputDirectory = C:\Raporty
ArchiveDays = 30

[EMAIL]
SMTPServer = smtp.gmail.com
SMTPPort = 587
FromEmail = system@firma.pl
```

### 18.3 Skrypt tworzenia indeksów

```sql
-- Indeksy dla lepszej wydajności
USE SklepDB;

-- Indeks na datę zamówienia (dla raportów chronologicznych)
CREATE NONCLUSTERED INDEX idx_zamowienia_data 
ON zamowienia(data_zamowienia DESC);

-- Indeks na foreign keys (dla JOIN-ów)
CREATE NONCLUSTERED INDEX idx_zamowienia_klient 
ON zamowienia(klient_id);

CREATE NONCLUSTERED INDEX idx_zamowienia_produkt 
ON zamowienia(produkt_id);

-- Indeks na daty cen (dla filtrowania aktualnych cen)
CREATE NONCLUSTERED INDEX idx_ceny_daty 
ON ceny(data_od, data_do);

-- Indeks na kategorię produktu
CREATE NONCLUSTERED INDEX idx_produkty_kategoria 
ON produkty(kategoria);
```

### 18.4 Skrypt maintenance

```sql
-- Regularne czyszczenie i optymalizacja
USE SklepDB;

-- Rebuild indeksów (wykonuj co tydzień)
ALTER INDEX ALL ON klienci REBUILD;
ALTER INDEX ALL ON produkty REBUILD;
ALTER INDEX ALL ON ceny REBUILD;
ALTER INDEX ALL ON zamowienia REBUILD;

-- Update statistics (wykonuj codziennie)
UPDATE STATISTICS klienci;
UPDATE STATISTICS produkty;
UPDATE STATISTICS ceny;
UPDATE STATISTICS zamowienia;

-- Sprawdź fragmentację indeksów
SELECT 
    OBJECT_NAME(ips.object_id) AS TableName,
    i.name AS IndexName,
    ips.avg_fragmentation_in_percent
FROM sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'LIMITED') ips
JOIN sys.indexes i ON ips.object_id = i.object_id 
    AND ips.index_id = i.index_id
WHERE ips.avg_fragmentation_in_percent > 10
ORDER BY ips.avg_fragmentation_in_percent DESC;
```

---

## 19. Kontakt i wsparcie

### 19.1 Wsparcie techniczne

**Dokumentacja SQL Server:**
- Microsoft Docs: https://docs.microsoft.com/sql/
- Connection Strings: https://www.connectionstrings.com/sql-server/

**Biblioteki Python:**
- pyodbc: https://github.com/mkleehammer/pyodbc/wiki
- pandas: https://pandas.pydata.org/docs/
- tkinter: https://docs.python.org/3/library/tkinter.html

### 19.2 Troubleshooting resources

**SQL Server błędy:**
- Error codes: https://docs.microsoft.com/sql/relational-databases/errors-events/
- Forums: https://dba.stackexchange.com/

**Python pyodbc issues:**
- GitHub Issues: https://github.com/mkleehammer/pyodbc/issues
- Stack Overflow: https://stackoverflow.com/questions/tagged/pyodbc

---

## 20. Historia zmian dokumentu

| Wersja | Data | Autor | Zmiany |
|--------|------|-------|--------|
| 1.0 | 2025-11-16 | System | Wersja początkowa (SQLite) |
| 2.0 | 2025-11-16 | System | Migracja na SQL Server, dodano sekcje bezpieczeństwa, FAQ, maintenance |

---

**Koniec dokumentu PRD v2.0 - SQL Server Edition**

*Dokument zawiera kompletną specyfikację systemu automatyzacji raportów wykorzystującego Microsoft SQL Server jako bazę danych.*