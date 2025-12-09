# 🚨 BŁĄD: Nie można połączyć z SQL Server

## Problem
Aplikacja nie może połączyć się z SQL Server. Błąd:
```
SQL Server Network Interfaces: Error Locating Server/Instance Specified
```

## Przyczyna
**SQL Server NIE JEST zainstalowany** lub nie działa na Twoim komputerze.

---

## ✅ ROZWIĄZANIE: Zainstaluj SQL Server Express (DARMOWY)

### Krok 1: Pobierz SQL Server Express

1. Otwórz przeglądarkę
2. Wejdź na: **https://www.microsoft.com/pl-pl/sql-server/sql-server-downloads**
3. Przewiń w dół do sekcji **"Express"**
4. Kliknij **"Download now"** (pobierz teraz)
5. Zapisz plik (około 10 MB)

### Krok 2: Zainstaluj SQL Server Express

1. **Uruchom pobrany plik** (SQL2019-SSEI-Expr.exe lub podobny)
2. Wybierz **"Basic"** (Podstawowa instalacja)
3. Kliknij **"Accept"** (Zaakceptuj licencję)
4. Wybierz lokalizację instalacji (lub zostaw domyślną)
5. Kliknij **"Install"**
6. **Poczekaj** 5-10 minut na instalację

### Krok 3: Zanotuj dane połączenia

Po instalacji zobaczysz ekran z informacjami:
```
Connection String:
Server=localhost\SQLEXPRESS;...
```

**ZANOTUJ:** `localhost\SQLEXPRESS` - to nazwa Twojego serwera!

### Krok 4: Włącz protokoły sieciowe (WAŻNE!)

1. Otwórz **"SQL Server Configuration Manager"**
   - Start → wpisz: "SQL Server Configuration Manager"

2. Przejdź do: **SQL Server Network Configuration** → **Protocols for SQLEXPRESS**

3. **Włącz TCP/IP:**
   - Kliknij prawym na "TCP/IP" → **Enable**

4. **Włącz Named Pipes:**
   - Kliknij prawym na "Named Pipes" → **Enable**

5. **Zrestartuj SQL Server:**
   - Przejdź do: **SQL Server Services**
   - Kliknij prawym na **"SQL Server (SQLEXPRESS)"** → **Restart**

### Krok 5: Sprawdź czy SQL Server działa

1. Naciśnij **Windows + R**
2. Wpisz: `services.msc`
3. Naciśnij **Enter**
4. Znajdź **"SQL Server (SQLEXPRESS)"**
5. Status powinien być: **"Running"** (Uruchomiona)

Jeśli NIE działa:
- Kliknij prawym → **Start**

---

## 🔄 Po instalacji SQL Server

### Uruchom ponownie aplikację:

```cmd
python system_automatyzacji_sqlserver.py
```

### Co powinno się stać:

✅ Aplikacja połączy się z SQL Server
✅ Automatycznie utworzy bazę danych `SklepDB`
✅ Utworzy tabele (klienci, produkty, ceny, zamowienia)
✅ Wypełni przykładowymi danymi
✅ Otworzy okno GUI

---

## ❓ Nadal nie działa?

### Sprawdź nazwę serwera:

Otwórz **Command Prompt** i wpisz:
```cmd
sqlcmd -L
```

To pokaże listę dostępnych instancji SQL Server.

### Edytuj config.ini:

Otwórz plik `config.ini` i upewnij się, że nazwa serwera jest poprawna:

```ini
[DATABASE]
Server = localhost\SQLEXPRESS    ← Twoja nazwa serwera
Database = SklepDB
Username =
Password =
```

---

## 🆘 Alternatywy (jeśli nie chcesz instalować SQL Server)

### Opcja 1: Użyj SQLite (lżejsza wersja)

Jeśli nie chcesz instalować SQL Server, mogę przygotować wersję aplikacji dla SQLite (bez instalacji serwera bazy danych).

### Opcja 2: Użyj SQL Server w Docker

Jeśli masz Docker:
```bash
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=YourStrong@Passw0rd" -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server:2019-latest
```

Wtedy w `config.ini`:
```ini
Server = localhost
Username = sa
Password = YourStrong@Passw0rd
```

---

## 📞 Potrzebujesz pomocy?

1. Sprawdź pełną dokumentację w pliku **README.md**
2. Sekcja "Rozwiązywanie problemów" zawiera więcej rozwiązań
3. Upewnij się, że masz zainstalowany **ODBC Driver 17 for SQL Server**

---

**Po zainstalowaniu SQL Server Express aplikacja będzie działać poprawnie!** 🚀
