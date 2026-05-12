# etl_update.py
# aktualizacja istniejacych rekordow w Azure SQL Database

import pyodbc
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

print("UPDATE - modifying existing records")

try:
    # polaczenie
    print("\nConnecting to Azure SQL...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Connected!")

    # metoda 1: pojedynczy rekord
    print("\nSingle record UPDATE:")

    # sprawdz cene przed
    cursor.execute("SELECT produkt, cena FROM TestSprzedaz WHERE produkt = 'Tablet'")
    row = cursor.fetchone()
    if row:
        print(f"Before: {row.produkt} - price: {row.cena}")

    # zmien cene
    query = """
        UPDATE TestSprzedaz 
        SET cena = ? 
        WHERE produkt = ?
    """

    nowa_cena = 1299.99
    produkt = 'Tablet'

    cursor.execute(query, nowa_cena, produkt)
    conn.commit()

    # sprawdz po
    cursor.execute("SELECT produkt, cena FROM TestSprzedaz WHERE produkt = 'Tablet'")
    row = cursor.fetchone()
    if row:
        print(f"After: {row.produkt} - price: {row.cena}")

    print(f"Updated: {produkt} - new price: {nowa_cena}")

    # metoda 2: wiele rekordow
    print("\nBulk UPDATE:")

    # podnies ceny > 100 PLN o 10%
    query = """
        UPDATE TestSprzedaz 
        SET cena = cena * 1.10
        WHERE cena > 100
    """

    cursor.execute(query)
    rows_affected = cursor.rowcount
    conn.commit()

    print(f"Increased prices for {rows_affected} products by 10%")

    # metoda 3: update z wartoscia obliczona
    print("\nCalculated value UPDATE:")

    query = """
        UPDATE TestSprzedaz
        SET ilosc = ?
        WHERE produkt = ?
    """

    cursor.execute(query, 10, 'Powerbank')
    conn.commit()

    print("Updated Powerbank quantity to 10")

    # weryfikacja
    print("\nVerification - all records:")

    cursor.execute("""
        SELECT id, produkt, ilosc, cena
        FROM TestSprzedaz
        ORDER BY id
    """)

    rows = cursor.fetchall()

    print("\nID | Product      | Qty   | Price")
    print("-" * 50)
    for row in rows:
        print(f"{row.id:2} | {row.produkt:12} | {row.ilosc:5} | {row.cena:7.2f}")

    # zamknij
    cursor.close()
    conn.close()
    print("\nConnection closed!")

except pyodbc.Error as e:
    print(f"\nDatabase error: {e}")

except Exception as e:
    print(f"\nError: {e}")

input("\nPress Enter to exit...")