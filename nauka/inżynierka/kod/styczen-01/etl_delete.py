# etl_delete.py
# usuwanie rekordow z Azure SQL Database

import pyodbc

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

print("DELETE - removing records")

try:
    # polaczenie
    print("\nConnecting to Azure SQL...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Connected!")

    # count przed
    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
    count_before = cursor.fetchone()[0]
    print(f"\nRecords before: {count_before}")

    # metoda 1: delete pojedynczego rekordu
    print("\nSingle record DELETE:")

    cursor.execute("SELECT id, produkt FROM TestSprzedaz WHERE produkt = ?", 'Powerbank')
    row = cursor.fetchone()

    if row:
        print(f"Found: ID={row.id}, Product={row.produkt}")

        cursor.execute("DELETE FROM TestSprzedaz WHERE produkt = ?", 'Powerbank')
        conn.commit()
        print(f"Deleted product: Powerbank")
    else:
        print("Product 'Powerbank' does not exist!")

    # metoda 2: delete z warunkiem
    print("\nConditional DELETE:")

    cursor.execute("DELETE FROM TestSprzedaz WHERE cena > ?", 1000)
    rows_deleted = cursor.rowcount
    conn.commit()

    print(f"Deleted {rows_deleted} products with price > 1000 PLN")

    # metoda 3: delete wielu (lista ID)
    print("\nMultiple DELETE by ID:")

    ids_to_delete = [2, 3]
    deleted_count = 0

    for product_id in ids_to_delete:
        cursor.execute("DELETE FROM TestSprzedaz WHERE id = ?", product_id)
        if cursor.rowcount > 0:
            deleted_count += 1

    conn.commit()
    print(f"Deleted {deleted_count} products (checked IDs: {ids_to_delete})")

    # count po
    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
    count_after = cursor.fetchone()[0]
    print(f"\nRecords after: {count_after}")
    print(f"Total deleted: {count_before - count_after}")

    # weryfikacja
    print("\nRemaining records:")

    cursor.execute("""
        SELECT id, produkt, ilosc, cena
        FROM TestSprzedaz
        ORDER BY id
    """)

    rows = cursor.fetchall()

    if rows:
        print("\nID | Product      | Qty   | Price")
        print("-" * 50)
        for row in rows:
            print(f"{row.id:2} | {row.produkt:12} | {row.ilosc:5} | {row.cena:7.2f}")
    else:
        print("\nNo records in table!")

    # zamknij
    cursor.close()
    conn.close()
    print("\nConnection closed!")

except pyodbc.Error as e:
    print(f"\nDatabase error: {e}")

except Exception as e:
    print(f"\nError: {e}")

input("\nPress Enter to exit...")