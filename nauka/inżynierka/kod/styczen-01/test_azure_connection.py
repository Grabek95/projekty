# test_azure_connection.py
# pierwszy skrypt laczacy sie z Azure SQL Database

import pyodbc
import pandas as pd

# konfiguracja polaczenia
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

print("Connecting to Azure SQL Database...")

try:
    # polaczenie
    conn = pyodbc.connect(conn_str)
    print("Connected!")

    # sql
    query = "SELECT * FROM TestSprzedaz"

    # wczytaj do pandas dataframe
    df = pd.read_sql(query, conn)

    print("\nData from TestSprzedaz:")
    print(df)

    print("\nStatistics:")
    print(f"  Total records: {len(df)}")
    suma = (df['ilosc'] * df['cena']).sum()
    print(f"  Total sales value: {suma:.2f} PLN")

    # zamknij polaczenie
    conn.close()
    print("\nConnection closed!")

except Exception as e:
    print(f"\nError: {e}")

input("\nPress Enter to exit...")