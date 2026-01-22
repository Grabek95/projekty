# 🎓 Praca Inżynierska - Automatyczna integracja danych w Azure

**Temat:** Automatyczna integracja, przetwarzanie i raportowanie danych z MSSQL z wykorzystaniem Pythona w chmurze Azure

**Autor:** Mateusz Grabiński  
**Start projektu:** 16 stycznia 2026  
**Termin obrony:** Wrzesień 2026

---

## 📊 Technologie

- **Baza danych:** Microsoft SQL Server (lokalny + Azure SQL Database)
- **Język programowania:** Python 3.x
- **Chmura:** Microsoft Azure (SQL Database, Blob Storage, Functions)
- **Narzędzia:** SSMS, VS Code, Power BI Desktop
- **Biblioteki:** pyodbc, sqlalchemy, pandas, azure-storage-blob

---

## 🎯 Zakres projektu

System automatycznej integracji danych składający się z:

1. **Pipeline ETL** - ekstrakcja, transformacja, ładowanie danych
2. **Azure SQL Database** - magazyn danych w chmurze
3. **Azure Functions** - automatyzacja procesów (timer triggers)
4. **Azure Blob Storage** - przechowywanie plików
5. **Raportowanie** - Excel, Email, Power BI Dashboard

---

## 📁 Struktura projektu

```
inzynierka/
├── diagramy/              # Diagramy architektury (draw.io)
├── dokumentacja/          # Screenshoty i notatki
│   ├── styczen-01/
│   ├── luty-02/
│   └── FINALNA/          # Materiały do pracy pisemnej
├── kod/                   # Kod źródłowy Python
│   ├── styczen-01/       # ETL scripts
│   └── produkcja/        # Finalne wersje
└── praca-pisemna/        # Dokumenty Word/LaTeX
```

---

## 🚀 Obecnie zaimplementowane (Styczeń 2026)

### ✅ Milestone 1: Fundament Azure (100%)

- Azure SQL Database skonfigurowana
- SSMS połączenie działające
- Python połączenie z Azure SQL
- Pierwsze dane w chmurze (1000+ rekordów)

### ✅ Milestone 2: Pipeline Python ETL (100%)

- **INSERT:** Pojedynczy i bulk (executemany)
- **UPDATE:** Różne metody (WHERE, obliczenia)
- **DELETE:** Z walidacją i warunkami
- **Error handling:** try/except/finally, rollback
- **Bulk operations:** 1000+ rekordów w ~3 sekundy
- **db_utils.py:** Helper functions, context manager

---

## 📦 Pliki w projekcie

### Kod Python (`/kod/styczen-01/`)

| Plik | Opis | Status |
|------|------|--------|
| `test_azure_connection.py` | Pierwsze połączenie, SELECT | ✅ Działa |
| `etl_insert.py` | INSERT pojedynczy i multiple | ✅ Działa |
| `etl_update.py` | UPDATE (3 metody) | ✅ Działa |
| `etl_delete.py` | DELETE z walidacją | ✅ Działa |
| `etl_with_error_handling.py` | Profesjonalny error handling | ✅ Działa |
| `bulk_insert.py` | Test wydajności (1000 rek) | ✅ Działa |
| `db_utils.py` | Helper functions, AzureSQLConnection class | ✅ Działa |
| `etl_insert_refactored.py` | INSERT z db_utils (DRY) | ✅ Działa |

---

## 🔧 Jak uruchomić

### Wymagania

```bash
pip install pyodbc sqlalchemy pandas azure-storage-blob openpyxl
```

### Konfiguracja

1. Utwórz plik `credentials.txt` (ignorowany przez Git):

```
server=sql-praca-mateusz.database.windows.net
database=db-praca-inzynierska
username=sqladmin
password=TWOJE_HASLO
```

1. Uzupełnij hasło w skryptach Python (oznaczone `YOUR_PASSWORD_HERE`)

### Uruchomienie

```bash
cd kod/styczen-01
python etl_insert_refactored.py
```

---

## 📊 Dane w bazie

**Tabela:** `TestSprzedaz`  
**Rekordów:** 1006 (dane testowe)  
**Kolumny:** id, produkt, ilosc, cena, data_sprzedazy

**Statystyki:**

- Średnia cena: ~1507 zł
- Min cena: 64 zł
- Max cena: 2999 zł
- Wartość całkowita: ~842,352 zł

---

## 🗓️ Timeline

- **Styczeń 2026:** Setup Azure + Python ETL ✅
- **Luty 2026:** Automatyzacja (Azure Functions, Blob Storage)
- **Marzec 2026:** Raportowanie (Excel, Email, Power BI)
- **Kwiecień 2026:** Optymalizacja i rozszerzenia
- **Maj-Czerwiec 2026:** Pisanie pracy
- **Lipiec 2026:** Oddanie pracy
- **Wrzesień 2026:** Obrona

---

## 💰 Budżet

- **Kredyt:** $100 (Azure for Students)
- **Miesięczny limit:** $20
- **Dotychczas wykorzystano:** ~$0-5
- **Szacowany koszt projektu:** $60-70 (9 miesięcy)

---

## 📚 Dokumentacja

- **Azure:** <https://docs.microsoft.com/azure/>
- **Python pyodbc:** <https://github.com/mkleehammer/pyodbc>
- **Pandas:** <https://pandas.pydata.org/docs/>

---

## 🎯 Progress

```
████████░░░░░░░░░░ 25% (2/8 milestones)

✅ Milestone 1: Fundament Azure
✅ Milestone 2: Pipeline Python ETL
⬜ Milestone 3: Automatyzacja
⬜ Milestone 4: Raportowanie
⬜ Milestone 5: Optymalizacja
⬜ Milestone 6: Dokumentacja
⬜ Milestone 7: Finalizacja
⬜ Milestone 8: Obrona
```

---

## 📧 Kontakt

**Email:** <grabinskimateusz@gmail.com>  
**Uczelnia:** <grabinsm@office.wit.edu.pl>

---

**Ostatnia aktualizacja:** 22 stycznia 2026
