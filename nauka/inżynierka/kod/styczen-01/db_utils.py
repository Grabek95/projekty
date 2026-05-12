# db_utils.py
# funkcje pomocnicze do pracy z Azure SQL Database

import pyodbc
from typing import List, Tuple, Optional

class AzureSQLConnection:
    """
    Context manager dla Azure SQL Database.
    Automatyczne zamykanie polaczenia i commit/rollback.
    
    Uzycie:
        with AzureSQLConnection(server, db, user, pass) as db:
            db.execute_query(...)
    """

    def __init__(self, server: str, database: str, username: str, password: str):
        """Inicjalizacja parametrow polaczenia"""
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = None
        self.cursor = None

    def __enter__(self):
        """Otwiera polaczenie (with statement)"""
        conn_str = (
            'Driver={ODBC Driver 17 for SQL Server};'
            f'Server=tcp:{self.server},1433;'
            f'Database={self.database};'
            f'Uid={self.username};'
            f'Pwd={self.password};'
            'Encrypt=yes;'
            'TrustServerCertificate=no;'
            'Connection Timeout=30;'
        )
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Zamyka polaczenie, commit lub rollback"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            if exc_type:
                self.conn.rollback()
            else:
                self.conn.commit()
            self.conn.close()
    
    def execute_query(self, query: str, params: Optional[Tuple] = None):
        """
        Wykonaj zapytanie SQL
        Returns: liczba zmienionych wierszy
        """
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.rowcount
    
    def fetch_all(self, query: str, params: Optional[Tuple] = None):
        """
        SELECT - pobierz wszystkie wyniki
        Returns: lista wierszy
        """
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def fetch_one(self, query: str, params: Optional[Tuple] = None):
        """
        SELECT - pobierz jeden wynik
        Returns: jeden wiersz lub None
        """
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def bulk_insert(self, table: str, columns: List[str], data: List[Tuple]):
        """
        Bulk INSERT wielu rekordow
        Returns: liczba wstawionych wierszy
        """
        placeholders = ', '.join(['?'] * len(columns))
        columns_str = ', '.join(columns)
        query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
        
        self.cursor.executemany(query, data)
        return len(data)
    
    def get_count(self, table: str, where: Optional[str] = None):
        """
        Policz rekordy w tabeli
        Returns: liczba rekordow
        """
        query = f"SELECT COUNT(*) FROM {table}"
        if where:
            query += f" WHERE {where}"
        
        result = self.fetch_one(query)
        return result[0] if result else 0


# funkcje pomocnicze

def get_credentials_from_file(filepath: str = "credentials.txt") -> dict:
    """
    Wczytaj credentials z pliku tekstowego
    
    Format:
        server=sql-server.database.windows.net
        database=db-name
        username=user
        password=pass
    
    Returns: slownik z danymi logowania
    """
    credentials = {}
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if '=' in line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    credentials[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"File {filepath} not found!")
        return None
    
    return credentials


def print_table(rows, headers: List[str], widths: Optional[List[int]] = None):
    """
    Wyswietl wyniki w formie tabeli

    Args:
        rows: lista wierszy (Row objects lub tuples)
        headers: nazwy kolumn
        widths: szerokosci kolumn (opcjonalnie)
    """
    if not widths:
        widths = [15] * len(headers)
    
    # naglowek
    header_str = " | ".join([h.ljust(w) for h, w in zip(headers, widths)])
    print(header_str)
    print("=" * len(header_str))
    
    # wiersze
    for row in rows:
        values = [str(getattr(row, h, '')) if hasattr(row, h) else str(row[i])
                for i, h in enumerate(headers)]
        row_str = " | ".join([v.ljust(w)[:w] for v, w in zip(values, widths)])
        print(row_str)


# przyklad uzycia
if __name__ == "__main__":
    print("db_utils.py - Test funkcji pomocniczych")
    
    # dane logowania
    SERVER = 'sql-praca-mateusz.database.windows.net'
    DATABASE = 'db-praca-inzynierska'
    USERNAME = 'sqladmin'
    PASSWORD = 'YourPasswordHere'
    
    try:
        # test context manager
        with AzureSQLConnection(SERVER, DATABASE, USERNAME, PASSWORD) as db:
            print("\nConnected to Azure SQL!")
            
            # test 1: count
            count = db.get_count('TestSprzedaz')
            print(f"\nTotal records: {count}")
            
            # test 2: top 5
            rows = db.fetch_all("""
                SELECT TOP 5 id, produkt, ilosc, cena
                FROM TestSprzedaz
                ORDER BY id DESC
            """)
            
            print(f"\nTop 5 records:")
            print_table(rows, ['id', 'produkt', 'ilosc', 'cena'], [5, 20, 8, 10])
            
            # test 3: stats
            stats = db.fetch_one("""
                SELECT
                    AVG(cena) as avg_price,
                    MIN(cena) as min_price,
                    MAX(cena) as max_price
                FROM TestSprzedaz
            """)
            
            print("\nStatistics:")
            print(f"  Average price: {stats.avg_price:.2f} PLN")
            print(f"  Min price: {stats.min_price:.2f} PLN")
            print(f"  Max price: {stats.max_price:.2f} PLN")
        
        print("\nTest completed successfully!")
    
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPress Enter to exit...")