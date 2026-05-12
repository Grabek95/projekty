# etl_insert_refactored.py
# INSERT z uzyciem db_utils.py (refactored version)

from db_utils import AzureSQLConnection

print("=" * 60)
print("INSERT - Refactored version (with db_utils)")
print("=" * 60)

# konfiguracja
SERVER = 'sql-praca-mateusz.database.windows.net'
DATABASE = 'db-praca-inzynierska'
USERNAME = 'sqladmin'
PASSWORD = 'YOUR_PASSWORD'

try:
    # context manager z db_utils
    with AzureSQLConnection(SERVER, DATABASE, USERNAME, PASSWORD) as db:
        print("\nConnected to Azure SQL!")

        # metoda 1: pojedynczy insert
        print("\nSingle INSERT:")

        query = "INSERT INTO TestSprzedaz (produkt, ilosc, cena) VALUES (?, ?, ?)"
        db.execute_query(query, ('Tablet Pro', 2, 2499.99))

        print("Added: Tablet Pro, quantity: 2, price: 2499.99")

        # metoda 2: bulk insert
        print("\nBulk INSERT:")

        data = [
            ('iPhone 15', 3, 4999.00),
            ('AirPods Pro 3', 5, 1099.00),
            ('iPad Air', 2, 2999.00),
            ('Apple Watch', 4, 1899.00)
        ]

        count = db.bulk_insert(
            table='TestSprzedaz',
            columns=['produkt', 'ilosc', 'cena'],
            data=data
        )

        print(f"Added {count} products!")

        # weryfikacja
        print("\nVerification - last 5 records:")

        total = db.get_count('TestSprzedaz')
        print(f"\nTotal records: {total}")

        rows = db.fetch_all("""
            SELECT TOP 5 id, produkt, ilosc, cena
            FROM TestSprzedaz
            ORDER BY id DESC
        """)

        print("\nID   | Product          | Qty   | Price")
        print("-" * 55)
        for row in rows:
            print(f"{row.id:4} | {row.produkt:15} | {row.ilosc:5} | {row.cena:7.2f}")

        print("\nAll operations completed successfully!")
        print("Connection closed automatically (context manager)")

except Exception as e:
    print(f"\nError: {e}")

input("\nPress Enter to exit...")