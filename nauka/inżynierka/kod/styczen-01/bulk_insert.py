# bulk_insert.py
# test wydajnosci - INSERT 1000 rekordow

import pyodbc
import random
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

print("BULK INSERT - performance test (1000 records)")

# produkty do losowania
produkty = [
    'Laptop', 'Mysz', 'Klawiatura', 'Monitor', 'Słuchawki',
    'Tablet', 'Drukarka', 'Webcam', 'Mikrofon', 'Powerbank',
    'Router', 'Switch', 'Pendrive', 'Dysk SSD', 'RAM',
    'Procesor', 'Karta graficzna', 'Zasilacz', 'Obudowa', 'Wentylator'
]

try:
    # polaczenie
    print("\nConnecting to Azure SQL Database...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Connected!")

    # sprawdz count przed
    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
    count_before = cursor.fetchone()[0]
    print(f"\nRecords before: {count_before}")

    # generuj 1000 rekordow
    print("\nGenerating 1000 records...")

    dane = []
    for i in range(1000):
        produkt = random.choice(produkty)
        ilosc = random.randint(1, 10)
        cena = round(random.uniform(49.99, 2999.99), 2)
        dane.append((produkt, ilosc, cena))

    print("Generated 1000 records")

    # bulk insert z pomiarem czasu
    print("\nInserting to database (bulk)...")
    start_time = datetime.now()

    query = "INSERT INTO TestSprzedaz (produkt, ilosc, cena) VALUES (?, ?, ?)"
    cursor.executemany(query, dane)
    conn.commit()

    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds()

    print(f"Inserted 1000 records in {elapsed:.2f} seconds")
    print(f"Performance: {1000/elapsed:.0f} records/second")

    # sprawdz count po
    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
    count_after = cursor.fetchone()[0]
    print(f"\nRecords after: {count_after}")
    print(f"Added: {count_after - count_before}")

    # statystyki
    print("\nStatistics:")

    cursor.execute("""
        SELECT
            COUNT(*) as total_records,
            AVG(cena) as avg_price,
            MIN(cena) as min_price,
            MAX(cena) as max_price,
            SUM(ilosc * cena) as total_value
        FROM TestSprzedaz
    """)

    row = cursor.fetchone()
    print(f"  Total records: {row.total_records}")
    print(f"  Average price: {row.avg_price:.2f} PLN")
    print(f"  Min price: {row.min_price:.2f} PLN")
    print(f"  Max price: {row.max_price:.2f} PLN")
    print(f"  Total value: {row.total_value:.2f} PLN")

    # top 5 produktow
    print("\nTop 5 products by value:")

    cursor.execute("""
        SELECT TOP 5
            produkt,
            COUNT(*) as transaction_count,
            SUM(ilosc) as total_quantity,
            SUM(ilosc * cena) as total_value
        FROM TestSprzedaz
        GROUP BY produkt
        ORDER BY total_value DESC
    """)

    rows = cursor.fetchall()
    print("\nProduct          | Transactions | Quantity   | Value")
    print("-" * 60)
    for row in rows:
        print(f"{row.produkt:15} | {row.transaction_count:12} | {row.total_quantity:5} | {row.total_value:10.2f}")

    # zamknij
    cursor.close()
    conn.close()
    print("\nConnection closed!")

except Exception as e:
    print(f"\nError: {e}")
    if conn:
        conn.rollback()

input("\nPress Enter to exit...")