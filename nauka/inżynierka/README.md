# Praca Inżynierska - Automatyczna integracja danych w Azure

**Temat:** Automatyczna integracja, przetwarzanie i raportowanie danych z MSSQL z wykorzystaniem Pythona w chmurze Azure

**Autor:** Mateusz Grabiński  
**Start projektu:** 16 stycznia 2026  
**Termin obrony:** Wrzesień 2026

---

## Technologie

- **Baza danych:** Microsoft SQL Server (lokalny + Azure SQL Database)
- **Język programowania:** Python 3.x
- **Chmura:** Microsoft Azure (SQL Database, Blob Storage, Functions)
- **Narzędzia:** SSMS, VS Code, Power BI Desktop
- **Biblioteki:** pyodbc, sqlalchemy, pandas, azure-storage-blob

---

## Zakres projektu

System automatycznej integracji danych składający się z:

1. **Pipeline ETL** - ekstrakcja, transformacja, ładowanie danych
2. **Azure SQL Database** - magazyn danych w chmurze
3. **Azure Functions** - automatyzacja procesów (timer triggers)
4. **Azure Blob Storage** - przechowywanie plików
5. **Raportowanie** - Excel, Email, Power BI Dashboard

---

## Struktura projektu

```
inzynierka/
├── diagramy/               # Diagramy architektury (draw.io)
├── dokumentacja/           # Screenshoty i notatki
│   ├── styczen-01/
│   ├── luty-02/
│   └── FINALNA/            # Materiały do pracy pisemnej
├── kod/                    # Kod źródłowy Python
│   ├── styczen-01/         # ETL scripts
│   ├── luty-02-functions/  # Azure Functions
│   └── produkcja/          # Finalne wersje
├── praca-pisemna/          # Dokumenty Word/LaTeX
└── raporty/                # raporty z dashboardem

---

## Obecnie zaimplementowane (Luty 2026)

### Milestone 1: Fundament Azure (100%)

- Azure SQL Database skonfigurowana
- SSMS połączenie działające
- Python połączenie z Azure SQL
- Pierwsze dane w chmurze (1000+ rekordów)

### Milestone 2: Pipeline Python ETL (100%)

- **INSERT:** Pojedynczy i bulk (executemany)
- **UPDATE:** Różne metody (WHERE, obliczenia)
- **DELETE:** Z walidacją i warunkami
- **Error handling:** try/except/finally, rollback
- **Bulk operations:** 1000+ rekordów w ~3 sekundy
- **db_utils.py:** Helper functions, context manager

## Milestone 3: Automatyzacja (Azure Functions)

### Azure Functions - Serverless ETL Pipeline

**Data:** 31.01.2026 - 01.02.2026

**Technologie:**

- Azure Functions Core Tools 4.6.0
- Python 3.11
- Flex Consumption Plan
- pymssql (SQL connectivity)
- Timer Trigger + HTTP Trigger

**Funkcje:**

1. **TimerPipeline** - Automatyczne uruchamianie (CRON: codziennie 9:00)

2. **HttpPipeline** - Uruchamianie na żądanie (HTTP API)

**Pipeline workflow:**

```

Timer/HTTP → Blob Storage (raw) → Parse CSV → Azure SQL INSERT → Blob (processed)

```

**Deployment:**

- VS Code Azure Functions Extension
- Zmienne środowiskowe w Azure Portal
- Monitoring przez Application Insights

**Rezultat:**

- Pipeline wykonuje się automatycznie
- 0.7s execution time
- Serverless (pay-per-execution)
- ~$0.50/miesiąc koszt

---

## Milestone 4: Power BI - Wizualizacja (50%)

### Power BI Desktop Dashboard

**Data:** 01.02.2026

**Technologie:**

- Power BI Desktop
- DAX (Data Analysis Expressions)
- DirectQuery do Azure SQL

**Dashboard zawiera:**

- Wykres słupkowy: Top produkty (ilość)
- KPI Cards: Przychód (8.84M zł), Średnia cena (1.52K)
- Pie chart: Udział produktów w sprzedaży
- Top 5 produktów według wartości
- Slicer: Interaktywny filtr produktów
- Tabela szczegółowa

**Calculated columns:**

- Wartość = cena × ilość

**Insights:**

- 1,111 transakcji
- 5,894 produktów sprzedanych
- iPhone 15 - największy przychód (~15K zł)
- Procesor - najpopularniejszy produkt (400 szt)

**Plik:** `raporty/Dashboard_Sprzedazy_Produktow.pbix`

---

## TODO - Pozostałe kroki

- [ ] Power BI Service - publikacja w chmurze
- [ ] Scheduled refresh - automatyczna aktualizacja danych
- [ ] Power BI Embedded - osadzenie w aplikacji

## Timeline

- **Styczeń 2026:** Setup Azure + Python ETL ✅
- **Luty 2026:** Automatyzacja (Azure Functions, Blob Storage) ✅
- **Marzec 2026:** Raportowanie (Excel, Email, Power BI)
- **Kwiecień 2026:** Optymalizacja i rozszerzenia
- **Maj-Czerwiec 2026:** Pisanie pracy
- **Lipiec 2026:** Oddanie pracy
- **Wrzesień 2026:** Obrona

---

## Budżet

- **Kredyt:** $100 (Azure for Students)
- **Miesięczny limit:** $20
- **Dotychczas wykorzystano:** ~$0-5
- **Szacowany koszt projektu:** $60-70 (9 miesięcy)

---

## Dokumentacja

- **Azure:** <https://docs.microsoft.com/azure/>
- **Python pyodbc:** <https://github.com/mkleehammer/pyodbc>
- **Pandas:** <https://pandas.pydata.org/docs/>

---

## 🎯 Progress

```

████████░░░░░░░░░░ 44% (3,5/8 milestones)

✅ Milestone 1: Fundament Azure
✅ Milestone 2: Pipeline Python ETL
✅ Milestone 3: Automatyzacja
[50%] Milestone 4: Raportowanie
⬜ Milestone 5: Optymalizacja
⬜ Milestone 6: Dokumentacja
⬜ Milestone 7: Finalizacja
⬜ Milestone 8: Obrona

```

---

## Kontakt

**Email:** <grabinskimateusz@gmail.com>

---

**Ostatnia aktualizacja:** 07 luty 2026
