# etl_delete.py
# delete rekordow z Azure SQL Database

import pyodbc


# konfiguracja
server = 'sql-praca-mateusz.database.windows.net'
database = 'db-praca-inzynierska'
username = 'sqladmin' 
password = 'YOUR_PASSWORD' # wpisać właściwe hasło

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

print("DELETE - usuwanie rekordów")

try:
    # połączenie
    print("\nŁączę się z Azure SQL Database...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Połączono!")

    # sprawdzanie ile rekordów mamy przed operacja
    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
    count_before = cursor.fetchone()[0]
    print(f"\n Liczba rekordów przed: {count_before}")

    # metoda 1 = delete pojedynczego rekordu
    print("\nPojedynczy DELETE")

    # sprawdzamy czy produkt istnieje
    cursor.execute("SELECT id, produkt FROM TestSprzedaz WHERE produkt = ?", 'Powerbank')
    row = cursor.fetchone()

    if row:
        print(f"Znaleziono ID={row.id}, Produkt={row.produkt}")

        # usuń
        cursor.execute("DELETE FROM TestSprzedaz WHERE Produkt = ?", 'Powerbank')
        conn.commit()
        print(f"Usnięto produkt: Powerbank")
    else:
        print("Produkt 'Powerbank' nie istnieje!")

    # metoda 2 - delete z warunkiem
    print("\n DELETE z warunkiem")

    # usuń produkty > 1000 zł
    cursor.execute("DELETE FROM TestSprzedaz WHERE cena > ?", 1000)
    rows_deleted = cursor.rowcount
    conn.commit()

    print(f"Usunięto {rows_deleted} produktów droższych niż 1000 zł")

    # metoda 3 - delete wielu rekordów (lista ID)
    print("\n DELETE wielu rekordów o konkretnych ID")

    # usuń produkty o ID 2, 3 - jeśli istnieją
    ids_to_delete = [2, 3]
    deleted_count = 0

    for product_id in ids_to_delete:
        cursor.execute("DELETE FROM TestSprzedaz WHERE id = ?", product_id)
        if cursor.rowcount > 0:
            deleted_count += 1

    conn.commit()
    print(f"Usunięto {deleted_count} produktów (sprawdzono ID: {ids_to_delete})")

    # sprawdz ile rekordow zostało po operacji
    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
    count_after = cursor.fetchone()[0]
    print(f"\n Liczna rekordów po: {count_after}")
    print(f"Łącznie usunięto: {count_before - count_after} rekordów")

    # weryfikacja - pokaż co zostało
    print("\n Pozostałe rekordy")

    cursor.execute("""
        SELECT id, produkt, ilosc, cena
        FROM TestSprzedaz
        ORDER BY id
    """)

    rows = cursor.fetchall()

    if rows:
        print("\nID | Produkt     | Ilość | Cena")
        print("-" * 50)
        for row in rows:
            print(f"{row.id:2} | {row.produkt:12} | {row.ilosc:5} | {row.cena:7.2f}")
        else:
            print("\n Brak rekordów w tabeli")

    # zamknij połączenie
    cursor.close()
    conn.close()
    print("\n Połączenie zamknięte.")

except pyodbc.Error as e:
    print(f"\nBłąd bazy danych: {e}")

except Exception as e:
    print(f"\nBłąd: {e}")

input("\nNaciśnij Enter aby zakończyć...")