# etl_isnert.py
# insert nowych rekordow do Azure SQL Database

import pyodbc
from datetime import datetime

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

print("INSERT - dodawanie nowych rekordów")

try: 
    # połączenie
    print ("\n Łącze się z Azure SQL Database...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Połączono!")

    # metoda 1 - insert pojedynczego rekordu
    print("\n Pojedynczy INSERT")

    query = """
        INSERT INTO TestSprzedaz (produkt, ilosc, cena)
        VALUES (?, ?, ?)
    """
    # DANE
    produkt = 'Tablet'
    ilosc = 2
    cena = 1499.49

    cursor.execute(query, produkt, ilosc, cena)
    conn.commit() # potrzebne do zapisywania danych

    print(f"Dodano: {produkt}, ilość: {ilosc}, cena: {cena}")


    # metoda 2 - insert wielu rekordów (lista)
    print("\n Multiple INSERT")

    nowe_produkty = [
        ('Drukarka', 1, 599.99),
        ('Webcam', 3, 149.99),
        ('Mikrofon', 2, 299.99),
        ('Powerbank', 5, 79.99)
    ]

    cursor.executemany(query, nowe_produkty)
    conn.commit()

    print(f"Dodano {len(nowe_produkty)} produktów!")

    # weryfikacja - sprawdzenie co zostało dodane
    print("\n Weryfikacja ostatnich 5 rekordów")

    cursor.execute("""
        SELECT TOP 5 * FROM TestSprzedaz 
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    print("\nID | Produkt      | Ilość | Cena    | Data")
    print("-" * 60)
    for row in rows:
        print(f"{row.id:2} | {row.produkt:12} | {row.ilosc:5} | {row.cena:7.2f} | {row.data_sprzedazy}")

    # zamknij połączenie
    cursor.close()
    conn.close()
    print("\nPołączenie zamknięte!")

except pyodbc.Error as e:
    print(f"\n Błąd bazy danych: {e}")

except Exception as e:
    print(f"\n Błąd: {e}")

input("\nNaciśnij Enter aby zakończyć...")