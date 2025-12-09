# System Automatyzacji Raportów z Interfejsem Sklepu - SQL Server

**Wersja:** 2.0
**Data:** 16 listopada 2025
**Baza danych:** Microsoft SQL Server

---

## 📋 Spis treści

1. [Opis projektu](#opis-projektu)
2. [Wymagania systemowe](#wymagania-systemowe)
3. [Instalacja krok po kroku](#instalacja-krok-po-kroku)
4. [Konfiguracja](#konfiguracja)
5. [Pierwsze uruchomienie](#pierwsze-uruchomienie)
6. [Używanie aplikacji](#używanie-aplikacji)
7. [Rozwiązywanie problemów](#rozwiązywanie-problemów)
8. [Struktura projektu](#struktura-projektu)

---

## 📝 Opis projektu

System automatyzacji raportów sprzedażowych z wbudowanym interfejsem do zarządzania zamówieniami, wykorzystujący Microsoft SQL Server jako bazę danych.

### Główne funkcje:

✅ **3 typy raportów:**
- Raport sprzedaży (wszystkie zamówienia)
- Raport magazynowy (stany i wartości produktów)
- Raport klientów (podsumowanie aktywności)

✅ **Sklep internetowy:**
- Składanie zamówień przez GUI
- Automatyczna aktualizacja stanów magazynowych
- Walidacja dostępności produktów

✅ **Statystyki w czasie rzeczywistym:**
- Liczba klientów, produktów, zamówień
- Wartość magazynu i zamówień
- Top 3 najczęściej kupowane produkty

✅ **Eksport do Excel:**
- Wszystkie raporty zapisywane jako .xlsx
- Automatyczne nazewnictwo z timestamp
- Pełne wsparcie polskich znaków

---

## 💻 Wymagania systemowe

### Minimalne:
- **System operacyjny:** Windows 10+ (lub Linux z ODBC Driver)
- **Python:** 3.7 lub nowszy
- **SQL Server:** 2016+ (lub Express Edition - darmowa)
- **ODBC Driver:** ODBC Driver 17 for SQL Server
- **RAM:** 256 MB
- **Dysk:** 50 MB (aplikacja) + 500 MB (SQL Server Express)

### Zalecane:
- **System operacyjny:** Windows 11
- **Python:** 3.9+
- **SQL Server:** 2019+ (lub Express 2019)
- **ODBC Driver:** ODBC Driver 18 for SQL Server
- **RAM:** 512 MB
- **Dysk:** SSD dla lepszej wydajności

---

## 🚀 Instalacja krok po kroku

### Krok 1: Instalacja SQL Server

#### Opcja A: SQL Server Express (ZALECANA - DARMOWA)

1. **Pobierz SQL Server Express 2019:**
   - Wejdź na: https://www.microsoft.com/pl-pl/sql-server/sql-server-downloads
   - Kliknij "Download now" w sekcji Express
   - Pobierz plik instalacyjny (~10 MB)

2. **Uruchom instalator:**
   - Kliknij dwukrotnie pobrany plik
   - Wybierz "Basic" (podstawowa instalacja)
   - Zaakceptuj licencję
   - Wybierz lokalizację instalacji (domyślna: C:\Program Files\Microsoft SQL Server)
   - Kliknij "Install"

3. **Zanotuj nazwę instancji:**
   - Po instalacji zobaczysz: **Connection String**
   - Przykład: `localhost\SQLEXPRESS`
   - Zapisz tę nazwę - będzie potrzebna w konfiguracji!

4. **Włącz protokoły (WAŻNE!):**
   - Otwórz "SQL Server Configuration Manager"
   - Przejdź do: SQL Server Network Configuration → Protocols for SQLEXPRESS
   - Kliknij prawym na "TCP/IP" → Enable
   - Kliknij prawym na "Named Pipes" → Enable
   - Zrestartuj usługę SQL Server (SQLEXPRESS) w "SQL Server Services"

#### Opcja B: Pełna wersja SQL Server

Jeśli masz już zainstalowany SQL Server (Developer, Standard, Enterprise):
1. Sprawdź nazwę serwera: `SELECT @@SERVERNAME` w SQL Server Management Studio
2. Upewnij się, że masz uprawnienia CREATE DATABASE

### Krok 2: Instalacja ODBC Driver

#### Windows:

1. **Pobierz ODBC Driver 17:**
   - Wejdź na: https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
   - Wybierz "Download ODBC Driver 17 for SQL Server"
   - Pobierz wersję dla Windows (msi)

2. **Zainstaluj:**
   - Uruchom pobrany plik .msi
   - Kliknij "Next" → "I accept" → "Next" → "Install"
   - Kliknij "Finish"

3. **Weryfikacja instalacji:**
   - Otwórz: Panel sterowania → Narzędzia administracyjne → ODBC Data Sources (64-bit)
   - Zakładka "Drivers" → powinien być widoczny "ODBC Driver 17 for SQL Server"

#### Linux (Ubuntu/Debian):

```bash
# Dodaj klucz Microsoft
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

# Dodaj repozytorium
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list

# Zaktualizuj listę pakietów
sudo apt-get update

# Zainstaluj ODBC Driver
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Zainstaluj narzędzia (opcjonalnie)
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools
```

### Krok 3: Instalacja Python

1. **Pobierz Python:**
   - Wejdź na: https://www.python.org/downloads/
   - Pobierz najnowszą wersję (3.9+ zalecane)

2. **Zainstaluj:**
   - Uruchom instalator
   - **WAŻNE:** Zaznacz "Add Python to PATH" ☑️
   - Kliknij "Install Now"

3. **Weryfikacja:**
   ```cmd
   python --version
   ```
   Powinno wyświetlić: `Python 3.x.x`

### Krok 4: Instalacja bibliotek Python

1. **Otwórz terminal/cmd** w katalogu projektu (c:\projekty\Sklep)

2. **Zainstaluj zależności:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Weryfikacja instalacji:**
   ```cmd
   python -c "import pyodbc; print('pyodbc:', pyodbc.version)"
   python -c "import pandas; print('pandas:', pandas.__version__)"
   python -c "import openpyxl; print('openpyxl:', openpyxl.__version__)"
   ```

---

## ⚙️ Konfiguracja

### Metoda 1: Użycie pliku config.ini (ZALECANA)

1. **Otwórz plik `config.ini`** w edytorze tekstowym

2. **Edytuj sekcję [DATABASE]:**

   **Przykład 1 - Lokalne SQL Server Express z Windows Authentication (najprostszy):**
   ```ini
   [DATABASE]
   Server = localhost\SQLEXPRESS
   Database = SklepDB
   Username =
   Password =
   ```

   **Przykład 2 - SQL Server z uwierzytelnianiem SQL:**
   ```ini
   [DATABASE]
   Server = localhost\SQLEXPRESS
   Database = SklepDB
   Username = sa
   Password = TwojeHaslo123!
   ```

   **Przykład 3 - Zdalny SQL Server:**
   ```ini
   [DATABASE]
   Server = 192.168.1.100
   Database = SklepDB
   Username = sklepuser
   Password = TwojeHaslo123!
   ```

   **Przykład 4 - Azure SQL Database:**
   ```ini
   [DATABASE]
   Server = yourserver.database.windows.net
   Database = SklepDB
   Username = azureuser
   Password = TwojeHaslo123!
   ```

3. **Zapisz plik**

### Metoda 2: Bezpośrednia edycja kodu (alternatywna)

Jeśli nie chcesz używać config.ini, możesz edytować bezpośrednio plik Python:

1. Otwórz `system_automatyzacji_sqlserver.py`
2. Znajdź linię 73-78 (konstruktor `__init__`)
3. Edytuj wartości domyślne:
   ```python
   self.server = 'localhost\\SQLEXPRESS'  # Twoja nazwa serwera
   self.database = 'SklepDB'              # Nazwa bazy
   self.username = ''                     # Puste = Windows Auth
   self.password = ''                     # Puste = Windows Auth
   ```

### Jak znaleźć nazwę swojego SQL Server?

**Metoda 1 - SQL Server Management Studio (SSMS):**
```sql
SELECT @@SERVERNAME
```

**Metoda 2 - Command Line:**
```cmd
sqlcmd -L
```
Wyświetli listę wszystkich dostępnych instancji SQL Server w sieci.

**Metoda 3 - SQL Server Configuration Manager:**
- Otwórz Configuration Manager
- Przejdź do "SQL Server Services"
- Nazwa instancji jest w nawiasach, np. `SQL Server (SQLEXPRESS)`

---

## 🎯 Pierwsze uruchomienie

### 1. Sprawdź konfigurację

Upewnij się, że:
- ✅ SQL Server działa (sprawdź w Services.msc: "SQL Server (SQLEXPRESS)")
- ✅ ODBC Driver zainstalowany
- ✅ Python i biblioteki zainstalowane
- ✅ Plik config.ini wypełniony poprawnymi danymi

### 2. Uruchom aplikację

W terminalu/cmd w katalogu projektu:

```cmd
python system_automatyzacji_sqlserver.py
```

### 3. Co się stanie przy pierwszym uruchomieniu?

Aplikacja **AUTOMATYCZNIE**:
1. Połączy się z SQL Server
2. Utworzy bazę danych `SklepDB` (jeśli nie istnieje)
3. Utworzy 4 tabele: `klienci`, `produkty`, `ceny`, `zamowienia`
4. Wypełni tabele przykładowymi danymi:
   - 3 klientów (Firma ABC, Jan Kowalski, Hurtownia XYZ)
   - 5 produktów (Laptop, Monitor, Klawiatura, Mysz, Słuchawki)
   - 5 cen dla produktów
5. Otworzy okno GUI aplikacji

### 4. Komunikaty w konsoli

Powinieneś zobaczyć:
```
============================================================
System Automatyzacji Raportów - SQL Server
Wersja 2.0
============================================================

Tworzenie bazy danych SklepDB...
Baza danych SklepDB została utworzona.
Tworzenie tabel...
Tabele utworzone pomyślnie.
Wypełnianie bazy przykładowymi danymi...
Dane przykładowe zostały dodane.
Inicjalizacja bazy danych zakończona pomyślnie.
```

### 5. Okno aplikacji

Zobaczysz okno z 3 zakładkami:
- 📊 **Raporty** - generowanie raportów
- 🛒 **Sklep** - składanie zamówień
- 💾 **Baza danych** - statystyki

---

## 📖 Używanie aplikacji

### Zakładka "Raporty"

1. **Raport Sprzedaży:**
   - Kliknij przycisk "📊 Raport Sprzedaży"
   - Zobaczysz listę wszystkich zamówień
   - Raport automatycznie zapisze się jako `raport_sprzedazy_YYYYMMDD_HHMMSS.xlsx`

2. **Raport Magazynowy:**
   - Kliknij "📦 Raport Magazynowy"
   - Zobaczysz stany magazynowe i ceny produktów
   - Zapisze się jako `raport_magazynowy_YYYYMMDD_HHMMSS.xlsx`

3. **Raport Klientów:**
   - Kliknij "👥 Raport Klientów"
   - Zobaczysz podsumowanie aktywności klientów
   - Zapisze się jako `raport_klientow_YYYYMMDD_HHMMSS.xlsx`

### Zakładka "Sklep"

1. **Składanie zamówienia:**
   - Wybierz klienta z listy rozwijanej
   - Wybierz produkt (zobaczysz aktualną cenę i stan)
   - Ustaw ilość (1-100)
   - Kliknij "🛒 Złóż zamówienie"

2. **Walidacja:**
   - System sprawdzi czy produkt jest dostępny
   - Jeśli stan niewystarczający → komunikat błędu
   - Jeśli OK → zamówienie zostanie zapisane, stan magazynowy zmniejszony

3. **Odświeżanie:**
   - Kliknij "🔄 Odśwież dane" aby przeładować listy produktów/klientów

### Zakładka "Baza danych"

1. **Statystyki:**
   - Liczba klientów, produktów, zamówień
   - Łączna wartość zamówień
   - Wartość magazynu
   - Top 3 produkty

2. **Odświeżanie:**
   - Kliknij "🔄 Odśwież statystyki" aby zaktualizować dane

---

## 🔧 Rozwiązywanie problemów

### Problem 1: "Cannot open database 'SklepDB'"

**Przyczyna:** Brak uprawnień do tworzenia bazy danych

**Rozwiązanie:**
1. Sprawdź czy SQL Server działa:
   ```cmd
   services.msc
   ```
   Znajdź "SQL Server (SQLEXPRESS)" → powinno być "Running"

2. Sprawdź uprawnienia:
   - Jeśli używasz Windows Authentication - Twoje konto Windows musi mieć uprawnienia
   - Jeśli używasz SQL Authentication - użytkownik musi mieć rolę `dbcreator`

3. Ręcznie utwórz bazę (jeśli problem persystuje):
   ```sql
   CREATE DATABASE SklepDB
   ```

### Problem 2: "ODBC Driver not found"

**Komunikat błędu:**
```
pyodbc.Error: ('01000', "[01000] [unixODBC][Driver Manager]Can't open lib 'ODBC Driver 17 for SQL Server'")
```

**Rozwiązanie:**
1. Sprawdź czy ODBC Driver zainstalowany:
   - Windows: Panel sterowania → ODBC Data Sources → Drivers
   - Linux: `odbcinst -q -d`

2. Jeśli nie ma - zainstaluj (patrz: Krok 2 instalacji)

3. Sprawdź wersję drivera w kodzie:
   - Linia 107 w `system_automatyzacji_sqlserver.py`
   - Zmień z `ODBC Driver 17` na `ODBC Driver 18` jeśli masz nowszą wersję

### Problem 3: Polskie znaki wyświetlają się jako "?"

**Przyczyna:** Niewłaściwe kodowanie

**Rozwiązanie:**
1. Upewnij się, że wszystkie tabele używają NVARCHAR (nie VARCHAR)
2. Sprawdź kodowanie pliku Python (powinno być UTF-8)
3. W SQL Server Management Studio ustaw: Tools → Options → Query Results → Results to Grid → "Include column headers when copying"

### Problem 4: "Login failed for user"

**Komunikat błędu:**
```
pyodbc.Error: ('28000', "[28000] [Microsoft][ODBC Driver 17 for SQL Server]Login failed for user 'username'")
```

**Rozwiązanie:**
1. Sprawdź nazwę użytkownika i hasło w config.ini
2. Sprawdź czy SQL Server Authentication jest włączone:
   - SSMS → Kliknij prawym na serwer → Properties
   - Security → "SQL Server and Windows Authentication mode"
3. Restart SQL Server po zmianie

### Problem 5: "Cannot connect to localhost\SQLEXPRESS"

**Rozwiązanie:**
1. Sprawdź nazwę serwera:
   ```cmd
   sqlcmd -L
   ```
2. Włącz TCP/IP i Named Pipes (patrz: Krok 1, punkt 4)
3. Sprawdź firewall (port 1433)
4. Spróbuj użyć `(local)\SQLEXPRESS` zamiast `localhost\SQLEXPRESS`

### Problem 6: Błąd przy eksporcie do Excel

**Komunikat:**
```
ModuleNotFoundError: No module named 'openpyxl'
```

**Rozwiązanie:**
```cmd
pip install openpyxl
```

---

## 📁 Struktura projektu

```
c:\projekty\Sklep\
│
├── system_automatyzacji_sqlserver.py  # Główna aplikacja (1862 linii)
│   ├── SEKCJA 1: Importy bibliotek
│   ├── SEKCJA 2: Klasa ReportAutomationSystem (backend)
│   ├── SEKCJA 3: Metody generowania raportów
│   ├── SEKCJA 4: Metody modułu sklepu
│   ├── SEKCJA 5: Klasa ShopGUI (interfejs)
│   ├── SEKCJA 6: Metody callback GUI
│   └── SEKCJA 7: Punkt startowy
│
├── config.ini                          # Konfiguracja połączenia
│   ├── [DATABASE] - parametry SQL Server
│   └── [REPORTS] - ustawienia raportów
│
├── requirements.txt                    # Zależności Python
│   ├── pyodbc>=4.0.35
│   ├── pandas>=1.3.0
│   └── openpyxl>=3.0.9
│
├── README.md                           # Ten plik - dokumentacja
│
├── prd_markdown_doc.md                 # Pełna specyfikacja PRD
│
└── sql/                                # Skrypty SQL (opcjonalne)
    ├── create_database.sql             # Ręczne tworzenie bazy
    └── create_indexes.sql              # Optymalizacja wydajności
```

### Pliki generowane przez aplikację:

```
c:\projekty\Sklep\
├── raport_sprzedazy_20251116_143052.xlsx
├── raport_magazynowy_20251116_143128.xlsx
└── raport_klientow_20251116_143145.xlsx
```

---

## 📊 Struktura bazy danych

### Tabela: `klienci`
```sql
CREATE TABLE klienci (
    id INT IDENTITY(1,1) PRIMARY KEY,    -- Auto-increment ID
    nazwa NVARCHAR(255) NOT NULL,        -- Nazwa klienta/firmy
    email NVARCHAR(255),                 -- Email
    telefon NVARCHAR(50),                -- Telefon
    adres NVARCHAR(500)                  -- Pełny adres
)
```

### Tabela: `produkty`
```sql
CREATE TABLE produkty (
    id INT IDENTITY(1,1) PRIMARY KEY,    -- Auto-increment ID
    nazwa NVARCHAR(255) NOT NULL,        -- Nazwa produktu
    kategoria NVARCHAR(100),             -- Kategoria (np. Elektronika)
    opis NVARCHAR(1000),                 -- Opis produktu
    stan_magazynowy INT DEFAULT 0        -- Ile sztuk w magazynie
)
```

### Tabela: `ceny`
```sql
CREATE TABLE ceny (
    id INT IDENTITY(1,1) PRIMARY KEY,    -- Auto-increment ID
    produkt_id INT,                      -- Odniesienie do produkty.id
    cena DECIMAL(10,2) NOT NULL,         -- Wartość ceny
    data_od DATE,                        -- Od kiedy obowiązuje
    data_do DATE,                        -- Do kiedy obowiązuje
    FOREIGN KEY (produkt_id) REFERENCES produkty(id)
)
```

### Tabela: `zamowienia`
```sql
CREATE TABLE zamowienia (
    id INT IDENTITY(1,1) PRIMARY KEY,         -- Auto-increment ID
    klient_id INT,                            -- Odniesienie do klienci.id
    produkt_id INT,                           -- Odniesienie do produkty.id
    ilosc INT,                                -- Ile sztuk zamówiono
    cena_jednostkowa DECIMAL(10,2),           -- Cena w momencie zamówienia
    data_zamowienia DATETIME DEFAULT GETDATE(), -- Kiedy złożono
    status NVARCHAR(50) DEFAULT 'nowe',       -- Status zamówienia
    FOREIGN KEY (klient_id) REFERENCES klienci(id),
    FOREIGN KEY (produkt_id) REFERENCES produkty(id)
)
```

---

## 🎓 Dla programistów

### Każda linijka kodu jest skomentowana!

Plik `system_automatyzacji_sqlserver.py` zawiera **szczegółowe komentarze** dla każdej linii kodu, wyjaśniające:
- Co robi dana instrukcja
- Dlaczego jest potrzebna
- Jakie parametry przyjmuje
- Co zwraca

Przykład:
```python
# Nawiązujemy połączenie z bazą danych SQL Server
conn = pyodbc.connect(self.build_connection_string())

# Tworzymy cursor - obiekt do wykonywania zapytań SQL
cursor = conn.cursor()

# SELECT - pobieramy ID i nazwę wszystkich klientów
cursor.execute("""
    SELECT id, nazwa
    FROM klienci
    ORDER BY nazwa  -- Sortowanie alfabetyczne
""")
```

### Architektura kodu:

- **Backend (ReportAutomationSystem):** Logika biznesowa, połączenie z SQL Server
- **Frontend (ShopGUI):** Interfejs Tkinter, obsługa zdarzeń
- **Separacja odpowiedzialności:** GUI nie wie o SQL Server, backend nie wie o GUI
- **Obsługa błędów:** Try-except w każdej metodzie
- **Transakcje SQL:** COMMIT/ROLLBACK dla atomowości operacji

---

## 🔐 Bezpieczeństwo

### Best Practices:

✅ **Parametryzowane zapytania:**
```python
# DOBRZE ✅
cursor.execute("SELECT * FROM klienci WHERE id = ?", (klient_id,))

# ŹLE ❌ (SQL Injection!)
cursor.execute(f"SELECT * FROM klienci WHERE id = {klient_id}")
```

✅ **Windows Authentication (zalecane):**
```ini
Username =
Password =
```

✅ **Hasła nie w kodzie:**
- Używaj config.ini (NIE commituj do git!)
- Lub zmiennych środowiskowych

❌ **NIE HARDCODUJ HASEŁ:**
```python
# ŹLE ❌
self.password = 'TajneHaslo123'
```

---

## 📞 Wsparcie

### Dokumentacja:
- **SQL Server:** https://docs.microsoft.com/sql/
- **pyodbc:** https://github.com/mkleehammer/pyodbc/wiki
- **pandas:** https://pandas.pydata.org/docs/
- **tkinter:** https://docs.python.org/3/library/tkinter.html

### Często zadawane pytania:

Sprawdź plik `prd_markdown_doc.md`, sekcja 16 (FAQ).

---

## 📝 Licencja

Ten projekt jest przykładową aplikacją edukacyjną.

---

## ✨ Autor

System Automatyzacji Raportów v2.0 - SQL Server Edition
Data utworzenia: 16 listopada 2025

---

**Powodzenia w używaniu systemu! 🚀**

Jeśli masz pytania lub problemy, sprawdź sekcję "Rozwiązywanie problemów" powyżej.
