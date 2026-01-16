# Setup Azure - [16/01/2026]

## Krok 1: Azure Portal

- Kredyt dostępny: € 85
- Region wybrany: West Europe
- Resource Group: rg-praca-inzynierska

## Krok 2: Azure SQL

- Server name: sql-praca-mateusz.database.windows.net
- Database: db-praca-inzynierska
- Admin login: sqladmin
- Password: b64#ZkpR_37TnLsD
- Resource group: rg-praca-inzynierska
- IP domowe: dodane do Firewall

- Tier: Basic (5 DTU, 2 GB)
- Cost: ~$5/month

- Firewall:
- Allow Azure services: YES
- Home IP: 213.134.162.39

- Budget: $20/month
- Alerts: 80% ($16), 100% ($20)
- Emails: uczelniany + Gmail

## Krok 3: Konfiguracja SSMS oraz utworzenie tabel

- Połączenie skonfigurowane pomyślnie
- Tabela TestSprzedaz - utworzona
- Uzupełnienie tabeli o dane

## Krok 4: Skrypt Python do łączenia się z bazą

- Instalacja wymaganych bibliotek
- Pierwszy skrypt python: test_azure_connection.py - poprawnie działający
- SELECT przez Python - dane pobrane prawidłowo

## MILESTONE 1: FUNDAMENT - GOTOWY

### Czego się dziś nauczyłem

### **Azure:**

- Tworzenie Resource Groups
- Konfiguracja SQL Server
- Zarządzanie firewall rules
- Monitoring kosztów (budgets)

### **SQL Server:**

- Połączenie SSMS z Azure
- CREATE TABLE
- INSERT danych
- SELECT queries

### **Python:**

- Instalacja bibliotek (pip)
- Connection strings
- pyodbc połączenie
- pandas DataFrame
- Debugowanie błędów

### **Networking:**

- IP lokalne vs publiczne
- Firewall rules
- VPN a połączenia
