# bulk_insert.py
# test wydajności - INSERRT 1000 rekordów

import pyodbc
import random
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

print("BULK INSERT - 1000 rekordów")

# lista produktów do losowania
produkty = [
    'Laptop', 'Mysz', 'Klawiatura', 'Monitor', 'Słuchawki',
    'Tablet', 'Drukarka', 'Webcam', 'Mikrofon', 'Powerbank',
    'Router', 'Switch', 'Pendrive', 'Dysk SSD', 'RAM',
    'Procesor', 'Karta graficzna', 'Zasilacz', 'Obudowa', 'Wentylator'
]

try:
    # połączenie
    print ("\nŁączę się z Azure SQL Database...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Połączono!")

    # sprawdź ile mamy przed
    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
    count_before = cursor.fetchone()[0]
    print(f"\nRekordów przed: {count_before}")

    # generuj 1000 rekordów
    print("\nGeneruję 1000 rekordów...")

    dane = []
    for i in range(1000):
        produkt = random.choice(produkty)
        ilosc = random.randint(1, 10)
        cena = round(random.uniform(49.99, 2999.99), 2)
        dane.append((produkt, ilosc, cena))

    print("Wygenerowano 1000 rekordów")

    # bulk insert
    print("\n Wstawiam do bazy (bulk)...")
    start_time = datetime.now()

    query = "INSERT INTO TestSprzedaz (produkt, ilosc, cena) VALUES (?, ?, ?)"
    cursor.executemany(query, dane)
    conn.commit()

    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds()

    print(f"Wstawiono 1000 rekordów w {elapsed:.2f} sekund")
    print(f"Wydajność: {1000/elapsed:.0f} rekordów/sekund")

    # sprawdz ile mamy po
    cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
    count_after = cursor.fetchone()[0]
    print(f"\nRekordów po: {count_after}")
    print(f"Dodano: {count_after - count_before}")

    # statystyki
    print("\nStatystyki")

    cursor.execute("""
        SELECT
            COUNT(*) as liczba_rekordow,
            AVG(cena) as srednia_cena,
            MIN(cena) as min_cena,
            MAX(cena) as max_cena,
            SUM(ilosc * cena) as wartosc_calkowita
        FROM TestSprzedaz
    """)

    row = cursor.fetchone()
    print(f"Liczba rekordów: {row.liczba_rekordow}")
    print(f"Średnia cena: {row.srednia_cena:.2f} zł")
    print(f"Min cena: {row.min_cena:.2f} zł")
    print(f"Max cena: {row.max_cena:.2f} zł")
    print(f"Wartość całkowita: {row.wartosc_calkowita:.2f} zł")

    # top 5 produktów
    print("\nTop 5 produktów")

    cursor.execute("""
        SELECT TOP 5
            produkt,
            COUNT(*) as liczba_transakcji,
            SUM(ilosc) as suma_ilosci,
            SUM(ilosc * cena) as wartosc
        FROM TestSprzedaz
        GRUPY BY produkt
        ORDER BY wartosc DESC
    """)

    rows = cursor.fetchall()
    print("\nProdukt          | Transakcje | Ilość | Wartość")
    print("-" * 55)
    for row in rows:
        print(f"{row.produkt:15} | {row.liczba_transakcji:10} | {row.suma_ilosci:5} | {row.wartosc:10.2f}")
    
    # zamknij polaczernie
    cursor.close()
    conn.close()
    print("\n Połączenie zamknięte")

except Exception as e:
    print(f"\n Błąd: {e}")
    if conn:
        conn.rollback()

input("\nNaciśnij Enter aby zakończyć...")