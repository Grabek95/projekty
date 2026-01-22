# etl_insert_refactored.py
# INSERT z użyciem db_utils.py (refactored version)

from db_utils import AzureSQLConnection

print("=" * 60)
print("INSERT - Wersja refactored (z db_utils)")
print("=" * 60)

# konfiguracja
SERVER = 'sql-praca-mateusz.database.windows.net'
DATABASE = 'db-praca-inzynierska'
USERNAME = 'sqladmin' 
PASSWORD = 'b64#ZkpR_37TnLsD' # wpisać właściwe hasło

try:
    # użycie context manager z db_utils - prostsze!
    with AzureSQLConnection(SERVER, DATABASE, USERNAME, PASSWORD) as db:
        print("\nPołączono z Azure SQL!")

        # metoda 1 - pojedynczy INSERT
        print("\nPojedynczy INSERT")

        query = "INSERT INTO TestSprzedaz (produkt, ilosc, cena) VALUES (?, ?, ?)"
        db.execute_query(query, ('Tablet Pro', 2, 2499.99))
        # nie trzeba ręcznego commita, bo db_utils robi to automatycznie!

        print("Dodano Tablet Pro, ilość: 2, cena: 2499.99")

        # metoda 2 - bulk INSERT
        print("\nBulk INSERT")

        data = [
            ('iPhone 15', 3, 4999.00),
            ('AirPods Pro 3', 5, 1099.00),
            ('iPad Air', 2, 2999.00),
            ('Apple Watch', 4, 1899.00)
        ]

        count = db.bulk_insert(
            table = 'TestSprzedaz',
            columns = ['produkt', 'ilosc', 'cena'],
            data = data
        )

        print(f"Dodano {count} produktów!")

        # weryfikacja
        print("\nWeryfikacja - 5 ostatnich rekordów")

        total = db.get_count('TestSprzedaz')
        print(f"\nŁączna liczba rekordów: {total}")

        rows = db.fetch_all("""
            SELECT TOP 5 id, produkt, ilosc, cena
            FROM TestSprzedaz
            ORDER BY id DESC
        """)

        print("\nID   | Produkt          | Ilość | Cena")
        print("-" * 55)
        for row in rows:
            print(f"{row.id:4} | {row.produkt:15} | {row.ilosc:5} | {row.cena:7.2f}")

        # tutaj __exit__ robi autoamtycznie:
        # commit
        # zamyka cursor
        # zamyka connection

        print("\nWszystkie operacje zakończone pomyślnie!")
        print("Połączenie zamknięte automatycznie (context manager)")

except Exception as e:
    print(f"\nBłąd: {e}")

input("\nNaciśnij Enter aby zakończyć...")