# etl_update.py
# aktualizacja istniejacych rekordow w Azure SQL Database

import pyodbc
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

print("\nAktualizacja rekordów")

try: 
    # połączenie
    print("\n Łączę się z Azure SQL...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("\n Połączono!")

    # metoda 1 - pojedynczy rekord
    print("\n Atkualizacja pojedynczego rekordu")

    # sprawdz cene przed zmiana
    cursor.execute("SELECT produkt, cena FROM TestSprzedaz WHERE produkt = 'Tablet'")
    row = cursor.fetchone()
    if row:
        print(f"Przed: {row.produkt} - cena: {row.cena}")

    # zmien cene rekordu
    query = """
        UPDATE TestSprzedaz 
        SET cena = ? 
        WHERE produkt = ?
    """

    nowa_cena = 1299.99
    produkt = 'Tablet'

    cursor.execute(query, nowa_cena, produkt)
    conn.commit()

    # sprawdz cene po zmianie
    cursor.execute("SELECT produkt, cena FROM TestSprzedaz WHERE produkt = 'Tablet'")
    row = cursor.fetchone()
    if row:
        print(f"Po: {row.produkt} - cena: {row.cena}")

    print(f"Zaktualizowano: {produkt} - cena: {nowa_cena}")

    # metoda 2 - wiele rekordów
    print("\n Aktualizacja wielu rekordów")

    # podnosimy ceny produktow > 100zł o 10%
    query = """
        UPDATE TestSprzedaz 
        SET cena = cena * 1.10
        WHERE cena > 100
    """

    cursor.execute(query)
    rows_affected = cursor.rowcount # ile wierszy zostało zmienionych
    conn.commit()

    print(f"\n Podwyższone ceny {rows_affected} produktów o 10%")

    # metoda 3 - update z wartoscia obliczona
    print("\n Atkualizacja z wartością obliczoną")

    # zmien ilosc powerbank na 10
    query = """
        UPDATE TestSprzedaz
        SET ilosc = ?
        WHERE produkt = ?
    """

    cursor.execute(query, 10, 'Powerbank')
    conn.commit()

    print("\n Zaktualizowano ilość powerbank o 10")

    # weryfikacja - pokaż zaktuazliowane dane
    print("\n Weryfikacja - wszystkie rekordy")

    cursor.execute("""
            SELECT id, produkt, ilosc, cena
            FROM TestSprzedaz
            ORDER BY id
    """)

    rows = cursor.fetchall()

    print("\nID | Produkt    | Ilość | Cena")
    print("-" * 50)
    for row in rows:
        print(f"{row.id:2} | {row.produkt:12} | {row.ilosc:5} | {row.cena:7.2f}")

    # Zamknij połączenie
    cursor.close()
    conn.close()
    print("\n Połączenie zamknięte!")

except pyodbc.Error as e:
    print(f"\n Błąd bazy: {e}")

except Exception as e:
    print(f"\n Błąd: {e}")

input("\n Naciśnij Enter aby zakończyć...")