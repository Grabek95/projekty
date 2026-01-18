# etl_with_error_handling.py
# etl z obsługą błędów

import pyodbc
import sys
from datetime import datetime

# konfiguracja
server = 'sql-praca-mateusz.database.windows.net'
database = 'db-praca-inzynierska'
username = 'sqladmin' 
password = 'haslo' # wpisać właściwe hasło

# Connection string
conn_str = (
    f'Driver={{ODBC Driver 18 for SQL Server}};'
    f'Server=tcp:{server},1433;'
    f'Database={database};'
    f'Uid={username};'
    f'Pwd={password};'
    f'Encrypt=yes;'
    f'TrustServerCertificate=no;'
    f'Connection Timeout=30;'
)

print("ETL z obsługa błędów")

# inicjowanie zmiennych
conn = None
cursor = None

try:
    print ("\nPróba połączenia z Azure SQL Database...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Połączono!")

    # operacja 1 - insert z walidacją
    print("\nINSERT z walidacją")

    produkt = 'Tablet'
    ilosc = 3
    cena = 1999.99

    # walidacja danych
    if ilosc <= 0:
        raise ValueError("Ilość musi być większa niż 0!")
    
    if cena <= 0:
        raise ValueError("Cena musi być większa niż 0!")
    
    # insert
    query = "INSERT INTO TestSprzedaz (produkt, ilosc, cena) VALUES (?, ?, ?)"
    cursor.execute(query, produkt, ilosc, cena)
    conn.commit()

    print(f"Dodano: {produkt}, ilość: {ilosc}, cena: {cena}")

    # operacja 2 - UPDATE z walidacją czy rekord istnieje
    print("\nUPDATE z walidacją")

    produkt_do_zmiany = "Monitor"
    nowa_cena = 1099.99

    # sprawdz czy produkt istnieje
    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz WHERE produkt = ?", produkt_do_zmiany)
    count = cursor.fetchone()[0]

    if count == 0:
        print(f"Produkt '{produkt_do_zmiany}' nie istnieje - pomijam UPDATE")
    else:
        cursor.execute("UPDATE TestSprzedaz SET cena = ?, produkt = ?", nowa_cena, produkt_do_zmiany)
        conn.commit()
        print(f"Zaktualizowano produkt {produkt_do_zmiany} o nową cenę: {nowa_cena}")

    # delete z potwierdzeniem
    print("\nDELETE z potwierdzeniem")

    produkt_do_usuniecia = "XYZ" # produkt który nie istnieje

    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz WHERE produkt = ?", produkt_do_usuniecia)
    count = cursor.fetchone()[0]

    if count == 0:
        print(f"Produkt {produkt_do_usuniecia} nie istnieje - nie można usunąć")
    else:
        cursor.execute("DELETE FROM TestSprzedaz WHERE produkt = ?", produkt_do_usuniecia)
        conn.commit()
        print(f"Usunięto: {produkt_do_usuniecia}")

    # weryfikacja końcowa
    print("\nWeryfikacja końcowa - wszystkie rekordy")

    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
    total_count = cursor.fetchone()[0]
    print(f"\nŁączna liczba rekordów: {total_count}")

    cursor.execute("""
        SELECT id, produkt, ilosc, cena
        FROM TestSprzedaz
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    print("\nID | Produkt      | Ilość | Cena")
    print("=" * 50)
    for row in rows[:5]: # pokaż tylkko 5 ostatnich
        print(f"{row.id:2} | {row.produkt:12} | {row.ilosc:5} | {row.cena:7.2f}")

    print("\nWszystkie operacje zakończone pomyślnie!")

except pyodbc.Error as db_error: # błędy bazy danych
    print(f"\nBłąd bazy danych!")
    print(f"    Typ błędu: {type(db_error).__name__}")
    print(f"    Szczegóły: {db_error}")

    # rollback jeśli połączenie istnieje
    if conn:
        conn.rollback()
        print("Wykonano rollback - cofnięto niezatwierdzone zmiany")

    sys.exit(1) # zakończ program z kodem błędu

except ValueError as val_error:
    # błędy walidacji danych
    print(f"\nBłąd walidacji danych!")
    print(f"    Szczegóły: {val_error}")
    sys.exit(1)

except Exception as general_error:
    # inne oczekiwane błędy
    print(f"\nNieoczekiwany błąd!")
    print(f"    Typ: {type(general_error).__name__}")
    print(f"    Szczegóły: {general_error}")

    if conn:
        conn.rollback()
        print("Wykonano rollback!")

finally:
    # ten blok zawsze się wykona niezależnie od wyniku - sukces lub błąd
    print("\nSprzątanie zasobów")

    if cursor:
        cursor.close()
        print("Cursor zamknięty")

    if conn:
        conn.close()
        print("Połączenie zamknięte")

    print(f"\nZakończono: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    input("\nNaciśnij Enter aby zakończyć...")