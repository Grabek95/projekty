# etl_with_error_handling.py
# etl z obsluga bledow

import pyodbc
import sys
from datetime import datetime

# konfiguracja
server = 'sql-praca-mateusz.database.windows.net'
database = 'db-praca-inzynierska'
username = 'sqladmin'
password = 'YOUR_PASSWORD'

# connection string
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

print("ETL with error handling")

# inicjalizacja zmiennych
conn = None
cursor = None

try:
    print("\nAttempting connection to Azure SQL...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Connected!")

    # operacja 1: insert z walidacja
    print("\nINSERT with validation:")

    produkt = 'Tablet'
    ilosc = 3
    cena = 1999.99

    # walidacja danych
    if ilosc <= 0:
        raise ValueError("Quantity must be greater than 0!")

    if cena <= 0:
        raise ValueError("Price must be greater than 0!")

    # insert
    query = "INSERT INTO TestSprzedaz (produkt, ilosc, cena) VALUES (?, ?, ?)"
    cursor.execute(query, produkt, ilosc, cena)
    conn.commit()

    print(f"Added: {produkt}, quantity: {ilosc}, price: {cena}")

    # operacja 2: update z walidacja
    print("\nUPDATE with validation:")

    produkt_do_zmiany = "Monitor"
    nowa_cena = 1099.99

    # sprawdz czy istnieje
    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz WHERE produkt = ?", produkt_do_zmiany)
    count = cursor.fetchone()[0]

    if count == 0:
        print(f"Product '{produkt_do_zmiany}' does not exist - skipping UPDATE")
    else:
        cursor.execute("UPDATE TestSprzedaz SET cena = ? WHERE produkt = ?", nowa_cena, produkt_do_zmiany)
        conn.commit()
        print(f"Updated {produkt_do_zmiany} with new price: {nowa_cena}")

    # operacja 3: delete z potwierdzeniem
    print("\nDELETE with confirmation:")

    produkt_do_usuniecia = "XYZ"  # nie istnieje

    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz WHERE produkt = ?", produkt_do_usuniecia)
    count = cursor.fetchone()[0]

    if count == 0:
        print(f"Product '{produkt_do_usuniecia}' does not exist - cannot delete")
    else:
        cursor.execute("DELETE FROM TestSprzedaz WHERE produkt = ?", produkt_do_usuniecia)
        conn.commit()
        print(f"Deleted: {produkt_do_usuniecia}")

    # weryfikacja koncowa
    print("\nFinal verification - all records:")

    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
    total_count = cursor.fetchone()[0]
    print(f"\nTotal records: {total_count}")

    cursor.execute("""
        SELECT id, produkt, ilosc, cena
        FROM TestSprzedaz
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    print("\nID | Product      | Qty   | Price")
    print("=" * 50)
    for row in rows[:5]:  # pokaz 5 ostatnich
        print(f"{row.id:2} | {row.produkt:12} | {row.ilosc:5} | {row.cena:7.2f}")

    print("\nAll operations completed successfully!")

except pyodbc.Error as db_error:
    print(f"\nDatabase error!")
    print(f"  Type: {type(db_error).__name__}")
    print(f"  Details: {db_error}")

    if conn:
        conn.rollback()
        print("Rollback executed - reverted uncommitted changes")

    sys.exit(1)

except ValueError as val_error:
    print(f"\nValidation error!")
    print(f"  Details: {val_error}")
    sys.exit(1)

except Exception as general_error:
    print(f"\nUnexpected error!")
    print(f"  Type: {type(general_error).__name__}")
    print(f"  Details: {general_error}")

    if conn:
        conn.rollback()
        print("Rollback executed!")

    sys.exit(1)

finally:
    # zawsze wykonany - cleanup
    print("\nCleaning up resources...")

    if cursor:
        cursor.close()
        print("Cursor closed")

    if conn:
        conn.close()
        print("Connection closed")

    print(f"\nCompleted: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

input("\nPress Enter to exit...")