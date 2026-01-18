# 🎓 Roadmapa Pracy Inżynierskiej - Automatyczna Integracja Danych w Azure

**Temat:** "Automatyczna integracja, przetwarzanie i raportowanie danych z MSSQL z wykorzystaniem Pythona w chmurze Azure"

**Autor:** Mateusz Grabiński  
**Termin oddania:** Lipiec 2026  
**Termin obrony:** Wrzesień 2026  
**Start projektu:** Styczeń 2026

---

## 📊 OVERVIEW - Zakres projektu

### Technologie

- **Baza danych:** MSSQL (lokalny + Azure SQL Database)
- **Język:** Python 3.x
- **Chmura:** Microsoft Azure
- **Narzędzia:** SSMS, VS Code, Power BI Desktop
- **Biblioteki:** pyodbc, sqlalchemy, pandas, azure-storage-blob, openpyxl

### Budżet

- **Kredyt Azure for Students:** $85
- **Budget miesięczny:** $20/month
- **Szacowany koszt projektu:** ~$60-70 (9 miesięcy)

### Główne komponenty

1. Azure SQL Database (Basic tier)
2. Azure Blob Storage
3. Azure Functions (automatyzacja)
4. Python ETL scripts
5. Power BI Dashboard
6. Automatyczne raportowanie (Excel/Email)

---

## 🎯 MILESTONE'Y PROJEKTU

### ✅ MILESTONE 1: Fundament Azure (DONE - 16.01.2026)

- Azure Account + SQL Server + Database
- SSMS połączenie
- Python połączenie
- Pierwsze dane w chmurze

### 🎯 MILESTONE 2: Pipeline Local → Azure (Luty 2026)

- Lokalna baza MSSQL
- Skrypt ETL: kopiowanie danych
- Transformacje podstawowe

### 🎯 MILESTONE 3: Automatyzacja (Marzec 2026)

- Azure Functions (Timer trigger)
- Harmonogram dzienny
- Blob Storage integracja

### 🎯 MILESTONE 4: Raportowanie (Kwiecień 2026)

- Generowanie Excel
- Email notifications
- Power BI Dashboard

### 🎯 MILESTONE 5: Optymalizacja (Maj 2026)

- Performance tuning
- Error handling
- Monitoring (Application Insights)

### 🎯 MILESTONE 6: Dokumentacja (Czerwiec 2026)

- Część teoretyczna
- Diagramy architektury
- Instrukcje deployment

### 🎯 MILESTONE 7: Finalizacja (Lipiec 2026)

- Ostatnie testy
- Korekta pracy
- Oddanie pracy

### 🎯 MILESTONE 8: Obrona (Wrzesień 2026)

- Prezentacja
- Demo live
- Obrona

---

## 📅 SZCZEGÓŁOWA ROADMAPA

---

## STYCZEŃ 2026 - Fundament i Setup

### ✅ TYDZIEŃ 1 (6-12.01) - Azure Setup i pierwsze połączenie [DONE!]

**Cel:** Działające środowisko Azure + pierwsze połączenie

**Zadania:**

- [x] Założenie konta Azure for Students
- [x] Utworzenie Resource Group (rg-praca-inzynierska)
- [x] Utworzenie SQL Server (sql-praca-mateusz)
- [x] Utworzenie SQL Database (db-praca-inzynierska, Basic tier)
- [x] Konfiguracja Firewall (Azure services + domowe IP)
- [x] Utworzenie Budget ($20/month z alertami)
- [x] Połączenie przez SSMS
- [x] Utworzenie tabeli TestSprzedaz + dane testowe
- [x] Instalacja bibliotek Python (pyodbc, pandas, sqlalchemy)
- [x] Pierwszy skrypt Python → Azure SQL (SELECT)

**Rezultat:**

```
✅ Azure SQL Database gotowa
✅ SSMS działa
✅ Python działa
✅ Pierwsze dane w chmurze
```

**Czas:** ~3h (2 sesje)  
**Status:** ✅ COMPLETE

---

### 📍 TYDZIEŃ 2 (13-19.01) - Python ETL Podstawy

**Cel:** INSERT, UPDATE, DELETE przez Python

**Zadania:**

- [ ] Skrypt: INSERT nowych rekordów przez Python
- [ ] Skrypt: UPDATE istniejących rekordów
- [ ] Skrypt: DELETE rekordów
- [ ] Error handling (try-except)
- [ ] Logging do pliku
- [ ] Funkcje pomocnicze (connect_to_db, execute_query)
- [ ] Test: bulk insert (100+ rekordów)

**Do stworzenia:**

- `etl_insert.py` - dodawanie danych
- `etl_update.py` - aktualizacja danych
- `etl_delete.py` - usuwanie danych
- `db_utils.py` - funkcje pomocnicze

**Rezultat:**

```
✅ Pełna kontrola nad danymi przez Python
✅ Obsługa błędów
✅ Logi operacji
```

**Czas:** ~4-5h  
**Deadline:** 19.01.2026

---

### 📍 TYDZIEŃ 3 (20-26.01) - Lokalna baza + pipeline

**Cel:** Kopiowanie danych z lokalnego MSSQL do Azure

**Zadania:**

- [ ] Setup lokalnego MSSQL (lub testowa instancja)
- [ ] Utworzenie testowej tabeli lokalnej z danymi
- [ ] Skrypt: read z lokalnego MSSQL
- [ ] Skrypt: write do Azure SQL
- [ ] Pipeline: local → Azure (pełny ETL)
- [ ] Porównanie danych (walidacja)
- [ ] Test na większym zbiorze (1000+ rekordów)

**Do stworzenia:**

- `local_to_azure_pipeline.py` - główny pipeline
- `config.py` - connection strings (local + Azure)
- `validate_data.py` - porównanie źródło vs cel

**Rezultat:**

```
✅ Działający pipeline local → Azure
✅ Walidacja danych
✅ Skalowalne do większych zbiorów
```

**Czas:** ~5-6h  
**Deadline:** 26.01.2026

---

### 📍 TYDZIEŃ 4 (27.01-02.02) - Transformacje danych

**Cel:** Czyszczenie i transformacje w pandas

**Zadania:**

- [ ] Czyszczenie danych (null values, duplikaty)
- [ ] Agregacje (GROUP BY w pandas)
- [ ] Joiny między tabelami
- [ ] Obliczenia (nowe kolumny)
- [ ] Filtrowanie i sortowanie
- [ ] Export do CSV (backup)
- [ ] Pipeline z transformacjami: local → transform → Azure

**Do stworzenia:**

- `data_transformations.py` - logika transformacji
- `etl_with_transforms.py` - pełny pipeline

**Rezultat:**

```
✅ Dane czyszczone i transformowane
✅ Logika biznesowa w pandas
✅ Pipeline z walidacją
```

**Czas:** ~5-6h  
**Deadline:** 02.02.2026

**🎊 KONIEC STYCZNIA - Status:** Podstawowy pipeline działa!

---

## LUTY 2026 - Automatyzacja i Blob Storage

### 📍 TYDZIEŃ 1 (03-09.02) - Azure Blob Storage

**Cel:** Przechowywanie plików w chmurze

**Zadania:**

- [ ] Utworzenie Storage Account
- [ ] Utworzenie Container (raw-data, processed-data)
- [ ] Instalacja azure-storage-blob
- [ ] Upload CSV/Excel do Blob
- [ ] Download z Blob do pandas
- [ ] Pipeline: Blob → transform → Azure SQL
- [ ] Organizacja plików (foldery: /year/month/day/)

**Do stworzenia:**

- `blob_utils.py` - funkcje do Blob Storage
- `blob_to_sql_pipeline.py` - pipeline Blob → SQL

**Rezultat:**

```
✅ Dane w Blob Storage
✅ Pipeline Blob → SQL działa
✅ Archiwizacja danych
```

**Czas:** ~4-5h  
**Deadline:** 09.02.2026

---

### 📍 TYDZIEŃ 2 (10-16.02) - Azure Functions Setup

**Cel:** Pierwsza Azure Function (Hello World)

**Zadania:**

- [ ] Instalacja Azure Functions Core Tools
- [ ] Utworzenie pierwszego projektu (Python)
- [ ] Timer trigger - test lokalny
- [ ] Deploy pierwszej funkcji do Azure
- [ ] Test wykonania w chmurze
- [ ] Logi w Azure Portal
- [ ] Application Insights - podstawy

**Do stworzenia:**

- `function_app/` - katalog projektu
- `__init__.py` - funkcja główna
- `function.json` - konfiguracja triggera

**Rezultat:**

```
✅ Pierwsza funkcja w Azure
✅ Harmonogram działa
✅ Logi widoczne
```

**Czas:** ~5-6h  
**Deadline:** 16.02.2026

---

### 📍 TYDZIEŃ 3 (17-23.02) - Azure Function ETL Pipeline

**Cel:** Automatyczny pipeline w Azure Function

**Zadania:**

- [ ] Przeniesienie kodu ETL do Azure Function
- [ ] Konfiguracja connection strings (environment variables)
- [ ] Timer trigger: codziennie o 6:00
- [ ] Test wykonania automatycznego
- [ ] Error handling w funkcji
- [ ] Email notification przy błędzie (opcjonalnie)

**Do stworzenia:**

- `etl_function/` - funkcja ETL
- `requirements.txt` - zależności
- `local.settings.json` - konfiguracja lokalna

**Rezultat:**

```
✅ Automatyczny pipeline działa
✅ Harmonogram: codziennie 6:00
✅ Obsługa błędów
```

**Czas:** ~6-7h  
**Deadline:** 23.02.2026

---

### 📍 TYDZIEŃ 4 (24.02-02.03) - Monitoring i Logi

**Cel:** Śledzenie wykonań i błędów

**Zadania:**

- [ ] Application Insights - szczegółowa konfiguracja
- [ ] Custom logs w funkcji
- [ ] Dashboard w Azure Portal
- [ ] Alerty przy błędach
- [ ] Query logs (Kusto)
- [ ] Metryki wydajności

**Rezultat:**

```
✅ Pełny monitoring
✅ Alerty działają
✅ Analiza logów
```

**Czas:** ~4-5h  
**Deadline:** 02.03.2026

**🎊 KONIEC LUTEGO - Status:** Automatyczny pipeline + monitoring!

---

## MARZEC 2026 - Raportowanie i Power BI

### 📍 TYDZIEŃ 1 (03-09.03) - Konsultacja z promotorem

**Cel:** Prezentacja postępów i ustalenie szczegółów pracy

**Zadania:**

- [ ] Przygotowanie prezentacji postępów
- [ ] Demo działającego pipeline'u
- [ ] Konsultacja zakresu pracy
- [ ] Ustalenie struktury dokumentu
- [ ] Feedback i ewentualne zmiany

**Rezultat:**

```
✅ Promotor zapoznany z projektem
✅ Zakres zatwierdzony
✅ Uwagi uwzględnione
```

**Czas:** ~2-3h (przygotowanie + spotkanie)  
**Deadline:** 09.03.2026

---

### 📍 TYDZIEŃ 2 (10-16.03) - Excel Automation

**Cel:** Generowanie raportów Excel automatycznie

**Zadania:**

- [ ] Instalacja openpyxl / xlsxwriter
- [ ] Skrypt: DataFrame → Excel
- [ ] Formatowanie (nagłówki, szerokość kolumn)
- [ ] Wykresy w Excel (słupkowe, liniowe)
- [ ] Multiple sheets
- [ ] Zapis do Blob Storage
- [ ] Integracja z Azure Function

**Do stworzenia:**

- `excel_generator.py` - generowanie raportów
- `report_templates.py` - szablony raportów

**Rezultat:**

```
✅ Automatyczne raporty Excel
✅ Wykresy i formatowanie
✅ Zapisywane w Blob Storage
```

**Czas:** ~5-6h  
**Deadline:** 16.03.2026

---

### 📍 TYDZIEŃ 3 (17-23.03) - Email Notifications

**Cel:** Wysyłanie raportów mailem

**Zadania:**

- [ ] Konfiguracja SMTP / SendGrid
- [ ] Test wysyłki maila
- [ ] Attach Excel do maila
- [ ] HTML email template
- [ ] Alerty przy przekroczeniu progów
- [ ] Lista odbiorców (konfiguracja)
- [ ] Integracja z Azure Function

**Do stworzenia:**

- `email_sender.py` - wysyłka maili
- `email_templates.py` - szablony HTML

**Rezultat:**

```
✅ Automatyczne maile z raportami
✅ Alerty działają
✅ Profesjonalne HTML templates
```

**Czas:** ~4-5h  
**Deadline:** 23.03.2026

---

### 📍 TYDZIEŃ 4 (24-30.03) - Power BI Desktop

**Cel:** Pierwszy dashboard w Power BI

**Zadania:**

- [ ] Instalacja Power BI Desktop
- [ ] Połączenie z Azure SQL Database
- [ ] Import danych
- [ ] Podstawowe wizualizacje (3-4 wykresy)
- [ ] Filtry i slicery
- [ ] Formatowanie
- [ ] Refresh data (ręcznie)

**Do stworzenia:**

- `Dashboard.pbix` - plik Power BI

**Rezultat:**

```
✅ Działający dashboard
✅ Połączenie z Azure SQL
✅ 3-4 wizualizacje gotowe
```

**Czas:** ~4-5h  
**Deadline:** 30.03.2026

**🎊 KONIEC MARCA - Status:** Raportowanie + Power BI działa!

---

## KWIECIEŃ 2026 - Rozszerzenia i Optymalizacja

### 📍 TYDZIEŃ 1 (31.03-06.04) - Power BI rozszerzenie

**Cel:** Dopracowanie dashboardu

**Zadania:**

- [ ] Dodanie bardziej zaawansowanych wizualizacji
- [ ] DAX measures (opcjonalnie)
- [ ] Bookmarks i page navigation
- [ ] Publish do Power BI Service (jeśli masz Pro)
- [ ] Scheduled refresh (jeśli masz Pro)
- [ ] Export do PDF

**Rezultat:**

```
✅ Kompletny dashboard
✅ Gotowy do prezentacji
```

**Czas:** ~4-5h  
**Deadline:** 06.04.2026

---

### 📍 TYDZIEŃ 2 (07-13.04) - Optymalizacja SQL

**Cel:** Poprawa wydajności zapytań

**Zadania:**

- [ ] Analiza execution plans
- [ ] Dodanie indeksów
- [ ] Optymalizacja JOIN'ów
- [ ] Partycjonowanie tabel (opcjonalnie)
- [ ] Statistics update
- [ ] Query tuning

**Rezultat:**

```
✅ Zapytania szybsze
✅ Indeksy dodane
✅ Execution plans poprawione
```

**Czas:** ~4-5h  
**Deadline:** 13.04.2026

---

### 📍 TYDZIEŃ 3 (14-20.04) - Error Handling & Retry Logic

**Cel:** Stabilność pipeline'u

**Zadania:**

- [ ] Comprehensive try-except blocks
- [ ] Retry logic (3 próby)
- [ ] Exponential backoff
- [ ] Dead letter queue (opcjonalnie)
- [ ] Graceful degradation
- [ ] Health check endpoint

**Rezultat:**

```
✅ Pipeline odporny na błędy
✅ Automatyczne retry
✅ Logi szczegółowe
```

**Czas:** ~5-6h  
**Deadline:** 20.04.2026

---

### 📍 TYDZIEŃ 4 (21-27.04) - Testy End-to-End

**Cel:** Weryfikacja całego systemu

**Zadania:**

- [ ] Test scenariusz 1: Pełny pipeline
- [ ] Test scenariusz 2: Duże dane (10k+ rekordów)
- [ ] Test scenariusz 3: Błędy sieci
- [ ] Test scenariusz 4: Raportowanie
- [ ] Dokumentacja testów
- [ ] Fix bugów

**Rezultat:**

```
✅ System przetestowany
✅ Bugi naprawione
✅ Dokumentacja testów gotowa
```

**Czas:** ~5-6h  
**Deadline:** 27.04.2026

**🎊 KONIEC KWIETNIA - Status:** System kompletny i zoptymalizowany!

---

## MAJ 2026 - Pisanie Pracy (Część Teoretyczna)

### 📍 TYDZIEŃ 1 (28.04-04.05) - Rozdział 1 i 2

**Cel:** Wstęp + Przegląd literatury

**Zadania:**

- [ ] Rozdział 1: Wstęp
  - [ ] 1.1 Uzasadnienie tematu
  - [ ] 1.2 Cel pracy
  - [ ] 1.3 Zakres pracy
  - [ ] 1.4 Struktura pracy
- [ ] Rozdział 2: Przegląd literatury
  - [ ] 2.1 ETL i procesy integracji danych
  - [ ] 2.2 Chmura Azure - charakterystyka
  - [ ] 2.3 Automatyzacja procesów
  - [ ] 2.4 Raportowanie biznesowe

**Rezultat:**

```
✅ Rozdziały 1-2 napisane (~10-15 stron)
✅ Bibliografia wstępna (10+ pozycji)
```

**Czas:** ~10-12h  
**Deadline:** 04.05.2026

---

### 📍 TYDZIEŃ 2 (05-11.05) - Rozdział 3

**Cel:** Opis technologii

**Zadania:**

- [ ] Rozdział 3: Opis technologii
  - [ ] 3.1 Microsoft Azure
    - [ ] 3.1.1 Azure SQL Database
    - [ ] 3.1.2 Azure Blob Storage
    - [ ] 3.1.3 Azure Functions
  - [ ] 3.2 Python i biblioteki
    - [ ] 3.2.1 pyodbc i sqlalchemy
    - [ ] 3.2.2 pandas
    - [ ] 3.2.3 azure-storage-blob
  - [ ] 3.3 SQL Server
  - [ ] 3.4 Power BI

**Rezultat:**

```
✅ Rozdział 3 napisany (~15-20 stron)
✅ Screenshoty z dokumentacji
```

**Czas:** ~10-12h  
**Deadline:** 11.05.2026

---

### 📍 TYDZIEŃ 3 (12-18.05) - Rozdział 4 (Architektura)

**Cel:** Architektura rozwiązania

**Zadania:**

- [ ] Rozdział 4: Architektura rozwiązania
  - [ ] 4.1 Wymagania funkcjonalne
  - [ ] 4.2 Wymagania niefunkcjonalne
  - [ ] 4.3 Architektura systemu
    - [ ] Diagramy (draw.io / Visio)
    - [ ] Przepływ danych
  - [ ] 4.4 Komponenty systemu
  - [ ] 4.5 Bezpieczeństwo i networking

**Rezultat:**

```
✅ Rozdział 4 napisany (~10-15 stron)
✅ Diagramy architektury gotowe
✅ Screenshoty z Azure Portal
```

**Czas:** ~10-12h  
**Deadline:** 18.05.2026

---

### 📍 TYDZIEŃ 4 (19-25.05) - Dokumentacja techniczna

**Cel:** Przygotowanie materiałów technicznych

**Zadania:**

- [ ] Connection strings i konfiguracja
- [ ] Screenshoty wszystkich komponentów
- [ ] Diagramy ERD (bazy danych)
- [ ] Flow charts (pipeline'y)
- [ ] Przykłady kodów (sformatowane)
- [ ] Tabele z parametrami

**Rezultat:**

```
✅ Wszystkie materiały techniczne gotowe
✅ Screenshoty i diagramy
```

**Czas:** ~8-10h  
**Deadline:** 25.05.2026

**🎊 KONIEC MAJA - Status:** Część teoretyczna gotowa!

---

## CZERWIEC 2026 - Pisanie Pracy (Implementacja + Finalizacja)

### 📍 TYDZIEŃ 1 (26.05-01.06) - Rozdział 5 (Implementacja)

**Cel:** Opis implementacji

**Zadania:**

- [ ] Rozdział 5: Implementacja
  - [ ] 5.1 Konfiguracja środowiska Azure
  - [ ] 5.2 Implementacja bazy danych
  - [ ] 5.3 Pipeline ETL
    - [ ] Kod źródłowy z komentarzami
    - [ ] Transformacje danych
  - [ ] 5.4 Azure Functions
  - [ ] 5.5 Raportowanie
  - [ ] 5.6 Power BI Dashboard

**Rezultat:**

```
✅ Rozdział 5 napisany (~20-25 stron)
✅ Fragmenty kodu z wyjaśnieniami
```

**Czas:** ~12-15h  
**Deadline:** 01.06.2026

---

### 📍 TYDZIEŃ 2 (02-08.06) - Rozdział 6 (Testy i Wyniki)

**Cel:** Dokumentacja testów

**Zadania:**

- [ ] Rozdział 6: Testy i wyniki
  - [ ] 6.1 Scenariusze testowe
  - [ ] 6.2 Testy funkcjonalne
  - [ ] 6.3 Testy wydajnościowe
  - [ ] 6.4 Wyniki testów
    - [ ] Tabele z danymi
    - [ ] Wykresy
  - [ ] 6.5 Analiza kosztów
  - [ ] 6.6 Power BI - screenshoty

**Rezultat:**

```
✅ Rozdział 6 napisany (~10-15 stron)
✅ Wyniki testów udokumentowane
```

**Czas:** ~10-12h  
**Deadline:** 08.06.2026

---

### 📍 TYDZIEŃ 3 (09-15.06) - Rozdział 7 + Zakończenie

**Cel:** Podsumowanie pracy

**Zadania:**

- [ ] Rozdział 7: Podsumowanie
  - [ ] 7.1 Osiągnięte cele
  - [ ] 7.2 Wnioski
  - [ ] 7.3 Problemy i rozwiązania
  - [ ] 7.4 Możliwości rozwoju
- [ ] Bibliografia (kompletna)
- [ ] Spis treści (automatyczny)
- [ ] Spis tabel
- [ ] Spis rysunków
- [ ] Streszczenie PL
- [ ] Abstract EN

**Rezultat:**

```
✅ Praca KOMPLETNA
✅ Wszystkie rozdziały gotowe
```

**Czas:** ~10-12h  
**Deadline:** 15.06.2026

---

### 📍 TYDZIEŃ 4 (16-22.06) - Korekta i Formatowanie

**Cel:** Finalna wersja pracy

**Zadania:**

- [ ] Korekta językowa
- [ ] Korekta merytoryczna
- [ ] Formatowanie (marginesy, czcionki)
- [ ] Numeracja stron
- [ ] Sprawdzenie bibliografii
- [ ] Sprawdzenie spisu treści
- [ ] Generowanie PDF
- [ ] Backup pracy (3 kopie!)

**Rezultat:**

```
✅ Praca gotowa do oddania
✅ PDF wygenerowany
✅ Backup'y zrobione
```

**Czas:** ~8-10h  
**Deadline:** 22.06.2026

**🎊 KONIEC CZERWCA - Status:** Praca GOTOWA!

---

## LIPIEC 2026 - Oddanie Pracy

### 📍 TYDZIEŃ 1 (23-29.06) - Konsultacja finalna

**Zadania:**

- [ ] Wysłanie wersji PDF do promotora
- [ ] Konsultacja finalna
- [ ] Poprawki (jeśli są)
- [ ] Finalna wersja

**Deadline:** 29.06.2026

---

### 📍 TYDZIEŃ 2-3 (30.06-13.07) - Druk i Oddanie

**Zadania:**

- [ ] Wydruk pracy (2-3 egzemplarze)
- [ ] Oprawa twarda
- [ ] Płyta CD z kodem źródłowym (jeśli wymagana)
- [ ] Oświadczenia (antyplagiat)
- [ ] **ODDANIE PRACY** 🎓

**Deadline:** ~15.07.2026 (dokładny termin z promotorem)

---

## SIERPIEŃ 2026 - Przygotowanie do Obrony

### 📍 Cały miesiąc (30.07-31.08)

**Zadania:**

- [ ] Prezentacja PowerPoint (15-20 slajdów)
  - [ ] Slajd 1: Tytuł
  - [ ] Slajd 2-3: Cel i zakres
  - [ ] Slajd 4-5: Architektura
  - [ ] Slajd 6-10: Implementacja (z kodem)
  - [ ] Slajd 11-13: Wyniki i testy
  - [ ] Slajd 14-15: Demo + podsumowanie
- [ ] Przygotowanie demo live (5-10 min)
  - [ ] Azure Portal
  - [ ] SSMS
  - [ ] Uruchomienie pipeline'u
  - [ ] Power BI Dashboard
- [ ] Ćwiczenie prezentacji
- [ ] Przewidywanie pytań komisji
- [ ] Przygotowanie odpowiedzi

**Rezultat:**

```
✅ Prezentacja gotowa
✅ Demo działa
✅ Pytania przećwiczone
```

**Czas:** ~15-20h (rozłożone na miesiąc)

---

## WRZESIEŃ 2026 - Obrona

### 🎓 OBRONA PRACY

**Format:**

- Prezentacja: 10-15 minut
- Demo live: 5 minut
- Pytania komisji: 10-15 minut

**Przygotowanie w dniu obrony:**

- [ ] Laptop naładowany
- [ ] Internet działający (hotspot backup)
- [ ] Azure Portal zalogowany
- [ ] SSMS połączony
- [ ] Power BI otwarte
- [ ] Prezentacja gotowa
- [ ] Zapasowa wersja offline

**✅ SUKCES!** 🎊

---

## 📊 TRACKING POSTĘPÓW

### Status Milestone'ów

```
✅ MILESTONE 1: Fundament Azure (DONE - 16.01.2026)
⬜ MILESTONE 2: Pipeline Local → Azure (Luty 2026)
⬜ MILESTONE 3: Automatyzacja (Marzec 2026)
⬜ MILESTONE 4: Raportowanie (Kwiecień 2026)
⬜ MILESTONE 5: Optymalizacja (Maj 2026)
⬜ MILESTONE 6: Dokumentacja (Czerwiec 2026)
⬜ MILESTONE 7: Finalizacja (Lipiec 2026)
⬜ MILESTONE 8: Obrona (Wrzesień 2026)
```

### Postęp ogólny

```
████░░░░░░░░░░░░░░░░ 12.5% (1/8 milestone'ów)
```

### Czas zainwestowany

```
Styczeń Tydzień 1: 3h ✅
Styczeń Tydzień 2: 0h
Styczeń Tydzień 3: 0h
Styczeń Tydzień 4: 0h
---
TOTAL: 3h / ~200h (szacowany czas całego projektu)
```

---

## 🎯 KLUCZOWE DATY (PODSUMOWANIE)

| Data | Wydarzenie | Status |
|------|-----------|--------|
| 16.01.2026 | START projektu + MILESTONE 1 | ✅ DONE |
| 02.02.2026 | MILESTONE 2: Pipeline działa | ⬜ TODO |
| 02.03.2026 | MILESTONE 3: Automatyzacja | ⬜ TODO |
| Marzec 2026 | Konsultacja z promotorem | ⬜ TODO |
| 30.03.2026 | MILESTONE 4: Raportowanie + Power BI | ⬜ TODO |
| 27.04.2026 | MILESTONE 5: System kompletny | ⬜ TODO |
| 25.05.2026 | MILESTONE 6: Część teoretyczna | ⬜ TODO |
| 22.06.2026 | MILESTONE 7: Praca gotowa | ⬜ TODO |
| ~15.07.2026 | **ODDANIE PRACY** 🎓 | ⬜ TODO |
| Wrzesień 2026 | **OBRONA** 🎊 | ⬜ TODO |

---

## 📚 MATERIAŁY I ZASOBY

### Dokumentacja

- Azure Documentation: <https://docs.microsoft.com/azure/>
- Python pyodbc: <https://github.com/mkleehammer/pyodbc>
- Pandas: <https://pandas.pydata.org/docs/>
- Power BI: <https://docs.microsoft.com/power-bi/>

### Kursy (opcjonalnie)

- Microsoft Learn: Azure Fundamentals
- Microsoft Learn: Azure SQL Database
- Microsoft Learn: Azure Functions
- Microsoft Learn: Power BI

### Narzędzia

- Azure Portal: <https://portal.azure.com>
- VS Code: <https://code.visualstudio.com/>
- SSMS: <https://docs.microsoft.com/sql/ssms/>
- Power BI Desktop: <https://powerbi.microsoft.com/desktop/>
- Draw.io: <https://app.diagrams.net/> (diagramy)

---

## 💾 BACKUP STRATEGY

### Kod źródłowy

- [ ] GitHub private repository
- [ ] Backup lokalny (dysk zewnętrzny)
- [ ] OneDrive / Google Drive

### Praca pisemna

- [ ] OneDrive (auto-sync)
- [ ] Google Drive (backup)
- [ ] Lokalny dysk
- [ ] Email do siebie (wersje milestone'ów)

### Azure

- [ ] Export konfiguracji (ARM templates)
- [ ] Backup bazy danych (Azure)
- [ ] Export danych (CSV backup)

**Zasada 3-2-1:**

- 3 kopie
- 2 różne media
- 1 kopia off-site

---

## 🎓 STRUKTURA PRACY PISEMNEJ (Wstępna)

```
1. WSTĘP (5-7 stron)
   1.1 Uzasadnienie tematu
   1.2 Cel pracy
   1.3 Zakres pracy
   1.4 Struktura pracy

2. PRZEGLĄD LITERATURY (10-15 stron)
   2.1 ETL i procesy integracji danych
   2.2 Chmura obliczeniowa - koncepcje
   2.3 Microsoft Azure - charakterystyka
   2.4 Automatyzacja procesów biznesowych
   2.5 Raportowanie i Business Intelligence

3. OPIS TECHNOLOGII (15-20 stron)
   3.1 Microsoft Azure
       3.1.1 Azure SQL Database
       3.1.2 Azure Blob Storage
       3.1.3 Azure Functions
       3.1.4 Application Insights
   3.2 Python i biblioteki
       3.2.1 pyodbc i sqlalchemy
       3.2.2 pandas
       3.2.3 azure-storage-blob
   3.3 Microsoft SQL Server
   3.4 Power BI

4. ARCHITEKTURA ROZWIĄZANIA (10-15 stron)
   4.1 Wymagania funkcjonalne
   4.2 Wymagania niefunkcjonalne
   4.3 Architektura systemu
   4.4 Komponenty systemu
   4.5 Przepływ danych
   4.6 Bezpieczeństwo i networking

5. IMPLEMENTACJA (20-25 stron)
   5.1 Konfiguracja środowiska Azure
   5.2 Implementacja bazy danych
   5.3 Pipeline ETL
   5.4 Azure Functions
   5.5 Raportowanie
   5.6 Power BI Dashboard

6. TESTY I WYNIKI (10-15 stron)
   6.1 Metodyka testowania
   6.2 Testy funkcjonalne
   6.3 Testy wydajnościowe
   6.4 Wyniki testów
   6.5 Analiza kosztów
   6.6 Dashboard - prezentacja wyników

7. PODSUMOWANIE (5-7 stron)
   7.1 Osiągnięte cele
   7.2 Wnioski
   7.3 Napotkane problemy i rozwiązania
   7.4 Możliwości rozwoju systemu

BIBLIOGRAFIA
SPISY (treści, tabel, rysunków)
STRESZCZENIE (PL + EN)
ZAŁĄCZNIKI (kod źródłowy - wybrane fragmenty)
```

**Szacowana objętość:** 80-100 stron (bez załączników)

---

## 💡 WSKAZÓWKI I BEST PRACTICES

### Podczas programowania

- ✅ Commituj kod często (GitHub)
- ✅ Dodawaj komentarze w kodzie
- ✅ Używaj meaningful variable names
- ✅ Rób backup przed większymi zmianami
- ✅ Testuj na małych zbiorach danych najpierw

### Podczas pisania pracy

- ✅ Pisz na bieżąco (nie zostawiaj na koniec!)
- ✅ Rób screenshoty już teraz
- ✅ Notuj problemy i rozwiązania
- ✅ Zbieraj bibliografię na bieżąco
- ✅ Używaj narzędzi do zarządzania bibliografią

### Zarządzanie projektem

- ✅ Cotygodniowe review postępów
- ✅ Update tego pliku po każdym milestone
- ✅ Nie zostawiaj zadań na ostatnią chwilę
- ✅ Komunikuj się z promotorem regularnie
- ✅ Proś o feedback wcześnie

### Zarządzanie kosztami Azure

- ✅ Sprawdzaj budżet co tydzień
- ✅ Wyłączaj zasoby gdy nie używasz (weekend)
- ✅ Używaj Basic tier gdzie możliwe
- ✅ Monitoruj alerty mailowe
- ✅ Eksportuj dane regularnie (backup)

---

## 🚨 RISK MANAGEMENT

### Potencjalne problemy

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitigation |
|--------|-------------------|-------|------------|
| Przekroczenie budżetu Azure | Średnie | Wysoki | Monitoring codzienny, alerty, backup plan |
| Problemy techniczne (Azure down) | Niskie | Średni | Backup lokalny danych, alternatywne demo |
| Brak czasu na pisanie | Średnie | Wysoki | Pisanie na bieżąco, nie zostawiać na koniec |
| Choroba / problemy osobiste | Niskie | Wysoki | Buffer 2 tygodnie przed deadline |
| Zmiany zakresu przez promotora | Średnie | Średni | Elastyczna architektura, modularne komponenty |
| Problemy z VPN/siecią służbową | Niskie | Niski | Praca z domu, hotspot mobilny |

---

## 📞 KONTAKTY

### Promotor

- Imię i nazwisko: [DO UZUPEŁNIENIA w marcu]
- Email: [DO UZUPEŁNIENIA]
- Konsultacje: [DO UZUPEŁNIENIA]

### Uczelnia

- Dziekanat: [DO UZUPEŁNIENIA]
- Terminy: [DO UZUPEŁNIENIA]

### Azure Support

- Student Support: <https://aka.ms/azureforeducation>
- Documentation: <https://docs.microsoft.com/azure/>

---

## 📝 NOTATKI I UWAGI

### Sesja 1 (16.01.2026)

- Utworzono Azure Account (Azure for Students, $85 kredytu)
- Resource Group: rg-praca-inzynierska
- SQL Server: sql-praca-mateusz.database.windows.net
- SQL Database: db-praca-inzynierska (Basic tier, ~$5/month)
- Budget: $20/month z alertami na 80% i 100%
- Emails: uczelniany + Gmail

### Sesja 2 (16.01.2026)

- Dodano domowe IP do firewall
- SSMS połączenie działa
- Utworzono tabelę TestSprzedaz z 5 rekordami
- Zainstalowano biblioteki Python (pyodbc, pandas, sqlalchemy)
- Pierwszy skrypt Python → Azure SQL działa!
- SELECT przez Python - dane pobrane do DataFrame

**Czas łączny:** ~3h  
**Status:** MILESTONE 1 - COMPLETE! ✅

### Lekcje i obserwacje

- Przepisywanie kodu > copy-paste (lepsze zrozumienie)
- Datetime w SQL Server: milisekundy (.877) dla precyzji
- IP lokalne vs publiczne - ważne dla firewall rules
- f-strings + double braces problematyczne w pyodbc

---

## ✅ QUICK CHECKLIST - Co mam zrobione?

```
INFRASTRUKTURA:
✅ Azure Account
✅ Resource Group
✅ SQL Server
✅ SQL Database (Basic tier)
✅ Firewall rules (Azure services + domowe IP)
✅ Budget i alerty

NARZĘDZIA:
✅ SSMS zainstalowane i działające
✅ Python + biblioteki (pyodbc, pandas, sqlalchemy)
✅ Connection string do Azure SQL

DANE:
✅ Tabela TestSprzedaz z danymi testowymi
✅ SELECT przez SSMS działa
✅ SELECT przez Python działa

KOD:
✅ test_azure_connection.py - pierwszy skrypt

DOKUMENTACJA:
✅ Roadmapa projektu (ten plik!)
✅ Screenshoty z pierwszej sesji
✅ Connection details zapisane

NASTĘPNE KROKI:
⬜ INSERT przez Python
⬜ UPDATE przez Python
⬜ DELETE przez Python
⬜ Lokalna baza MSSQL
⬜ Pipeline local → Azure
```

---

## 🎯 NASTĘPNA SESJA - Plan

**Kiedy:** Gdy będziesz gotowy (weekend / wieczór)

**Zadania (Tydzień 2 - część 1):**

1. [ ] Skrypt: INSERT nowych rekordów przez Python (30 min)
2. [ ] Skrypt: UPDATE istniejących rekordów (20 min)
3. [ ] Skrypt: DELETE rekordów (20 min)
4. [ ] Error handling - try-except (20 min)
5. [ ] Test: bulk insert (100 rekordów) (30 min)

**Czas:** ~2h  
**Rezultat:** Pełna kontrola nad danymi przez Python ✅

---

## 📌 PRZYPOMNIENIE - Kluczowe terminy

- **Konsultacja z promotorem:** Marzec 2026
- **Oddanie pracy:** ~15 Lipca 2026
- **Obrona:** Wrzesień 2026

**Dni do oddania:** ~180 dni (6 miesięcy)  
**Dni do obrony:** ~240 dni (8 miesięcy)

**MASZ CZAS! Ale nie zwlekaj - regular progress = sukces!** 💪

---

## 🎊 PODSUMOWANIE

**Status projektu:** W trakcie realizacji ✅  
**Postęp:** 12.5% (1/8 milestone'ów)  
**Następny milestone:** Pipeline Local → Azure (Luty 2026)  
**Budżet wykorzystany:** $0 / $85 (0%)  
**Czas zainwestowany:** 3h / ~200h (1.5%)

**Prognoza:** Na dobrej drodze! 🚀

---

**Dokument utworzony:** 16.01.2026  
**Ostatnia aktualizacja:** 16.01.2026  
**Wersja:** 1.0  
**Autor:** Mateusz Grabiński

---

## 🔄 HISTORIA ZMIAN

| Data | Wersja | Zmiany |
|------|--------|--------|
| 16.01.2026 | 1.0 | Utworzenie dokumentu roadmapy |

---

**POWODZENIA! DASZ RADĘ! 💪🎓**
