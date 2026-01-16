# test_azure_connection.py
# Pierwszy skrypt łączący się z Azure SQL Database

import pyodbc
import pandas as pd

# KONFIGURACJA POŁĄCZENIA
server = 'sql-praca-mateusz.database.windows.net'
database = 'db-praca-inzynierska'
username = 'sqladmin'
password = 'b64#ZkpR_37TnLsD'

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

print("Łącze się z Azure SQL Database...")

try:
    # Połączenie
    conn = pyodbc.connect(conn_str)
    print("Połączono!")

    # Zapytanie SQL
    query = "SELECT * FROM TestSprzedaz"

    # Wczytaj pandas dataframe
    df = pd.read_sql(query, conn)

    print("\n Dane z tabeli TestSprzedaz:")
    print(df)

    print("\nStatystyki:")
    print(f" Liczba rekordów: {len(df)}")
    suma = (df['ilosc'] * df['cena']).sum()
    print(f"   Suma wartości sprzedaży: {suma:.2f} PLN")

    # Zamknij połączenie
    conn.close()
    print("\n Połączenie zamknięte!")

except Exception as e:
    print(f"\n Błąd: {e}")

input("\n Naciśnij Enter aby zakończyć...")