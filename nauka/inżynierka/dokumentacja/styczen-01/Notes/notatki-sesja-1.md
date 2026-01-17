# Sesja 1 - Setup Azure i pierwsze połączenie

**Data:** 16.01.2026  
**Czas:** ~3h (2 sesje)

## Co zrobiłem

### Azure Setup

- Utworzono Resource Group: rg-praca-inzynierska
- Utworzono SQL Server: sql-praca-mateusz.database.windows.net
- Utworzono SQL Database: db-praca-inzynierska (Basic tier, ~$5/month)
- Konfiguracja firewall: Azure services + domowe IP (xxx.xxx.xxx.xxx)
- Budget: $20/month z alertami 80% i 100%

### Narzędzia

- SSMS - połączenie działa
- Python biblioteki: pyodbc, pandas, sqlalchemy, azure-storage-blob

### Kod

- `test_azure_connection.py` - pierwszy działający skrypt
- SELECT z Azure SQL do pandas DataFrame

### Dane

- Tabela TestSprzedaz z 5 rekordami testowymi

## Lekcje i obserwacje

1. **IP lokalne vs publiczne**:
   - ipconfig pokazuje IP lokalne (192.168.x.x)
   - Azure widzi IP publiczne (xxx.xxx.xxx.xxx)
   - Do firewall trzeba dodać IP publiczne!

2. **Datetime precyzja**:
   - .877 to milisekundy
   - SQL Server DATETIME: ~3.33ms precyzji
   - Ważne dla audytu i timestamp'ów

3. **Przepisywanie kodu**:
   - Lepiej przepisać niż copy-paste
   - Rozumiesz każdą linię
   - Uczysz się debugowania

## Problemy i rozwiązania

**Problem:** f-string z podwójnymi klamrami `{{}}` w connection string
**Rozwiązanie:** Użyć konkatenacji stringów zamiast f-string

## Screenshoty

- azure-sql-database-overview.png
- ssms-tabela-testsprzedaz.png  
- python-skrypt-dzialajacy.png
- azure-budget-ustawienia.png
