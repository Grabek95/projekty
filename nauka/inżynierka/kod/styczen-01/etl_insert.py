# etl_insert.py
# insert nowych rekordow do Azure SQL Database
# skrypt testowy - testy lokalne

import pyodbc
from datetime import datetime

# konfiguracja polaczenia
server = 'sql-praca-mateusz.database.windows.net'
database = 'db-praca-inzynierska'
username = 'sqladmin' 
password = 'YOUR_PASSWORD' # tylko dla testow lokalnych

# conn string (pyodbc - wymaga ODBC driver 18)
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

print("INSERT - adding new records to the database")

try: 
    # polaczenie
    print ("\nConnecting to Azure SQL Database...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Connected!")

    # insert pojedynczego rekordu
    print("\nSingle INSERT")

    query = """
        INSERT INTO TestSprzedaz (produkt, ilosc, cena)
        VALUES (?, ?, ?)
    """
    # dane
    produkt = 'Tablet'
    ilosc = 2
    cena = 1499.49

    cursor.execute(query, produkt, ilosc, cena)
    conn.commit() 

    print(f"Added: {produkt}, ilość: {ilosc}, cena: {cena}")


    # insert wielu rekordow
    print("\nBulk INSERT:")

    nowe_produkty = [
        ('Drukarka', 1, 599.99),
        ('Webcam', 3, 149.99),
        ('Mikrofon', 2, 299.99),
        ('Powerbank', 5, 79.99)
    ]

    cursor.executemany(query, nowe_produkty)
    conn.commit()

    print(f"Added {len(nowe_produkty)} products!")

    # weryfikacja
    print("\n Verification - last 5 records")

    cursor.execute("""
        SELECT TOP 5 * FROM TestSprzedaz 
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    print("\nID | Product      | Quantity | Price    | Date")
    print("-" * 60)
    for row in rows:
        print(f"{row.id:2} | {row.produkt:12} | {row.ilosc:5} | {row.cena:7.2f} | {row.data_sprzedazy}")

    # zamknij polaczenie
    cursor.close()
    conn.close()
    print("\nConnection closed!")

except pyodbc.Error as e:
    print(f"\nDatabase error: {e}")

except Exception as e:
    print(f"\nError: {e}")

input("\Press Enter to exit...")