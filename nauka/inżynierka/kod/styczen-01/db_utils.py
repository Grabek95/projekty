# db_utils.py
# funkcje pomocnicze do pracy z Azure SQL Database

import pyodbc
from typing import list, Tuple, Optional # import type odpowiednio: Lista, Krotka, Opcjonalny

class AzureSQLConnection: # utworzenie klasy = szablon do tworzenia obiektów połączeń
    """
    Klasa do zarządzania połączeniem z Azure SQL Database.
    Automatycznie zamyka połączenie po użyciu (context manager).
    """

    def __init__(self, server: str, database: str, username: str, password: str):
        # konstruktor - uruchamia się automatycznie gdy tworzymy obiekt
        # self = ten konkretny obiekt
        # str = type hint (podpowiedż, że jest to string)
        """
        Inicjalizacja połączenia.

        Args:
            server: Nazwa serwera
            database: Nazwa bazy danych
            username: Login użytkownika
            password: Hasło
        """
        self.server = server # zapisz serwer na tym obiekcie
        self.database = database
        self.username = username
        self.password = password
        self.conn = None # na razie połączenie nie istnieje
        self.cursor = None

    def __enter__(self): # specjalna metoda - uruchamia się gdy robimy: with ... as db:
        """Otwórz połączenie (używane z 'with')"""
        conn_str = (
            'Driver={ODBC Driver 17 for SQL Server};'
            f'Server=tcp:{self.server},1433;' # wstaw self.server do stringa
            f'Database={self.database};'
            f'Uid={self.username};'
            f'Pwd={self.password};'
            'Encrypt=yes;'
            'TrustServerCertificate=no;'
            'Connection Timeout=30;'
        )

        self.conn = pyodbc.connect(conn_str) # otwórz połączenie i zapisz w self.conn
        self.cursor = self.conn.cursor() # utwórz kursor do wykonywania zapytań
        return self # zwróć self (siebie) - to będzie przypisane do 'db'
    
    def __exit__(self, exc_type, exc_val, exc_tb): # specjalna metoda - uruchamia się, gdy kończy się blok with
        # exc_type = typ błędu (jeśl był), None jeśli sukces
        """Zamknij połączenie (używane z 'with')"""
        if self.cursor:
            self.cursor.close() # jeśli kursor istnieje, zamknij go
        if self.conn:
            if exc_type:
                # jeśli błąd --> rollback czyli cofinj zmiany
                self.conn.rollback()
            else:
                # jeśli sukces --> commit czyli zatwierdz zmiany
                self.conn.commit()
            self.conn.close()
    
    def execute_query(self, query: str, params: Optional[Tuple] = None): # query: str = query to string 
        # params to Tuple lub None, None - domyślna wartość jeśli nie podamy params
        """
        Wykonaj zapytanie SQL.

        Args:
            query: Zapytanie SQL
            params: Parametry zapytania (opcjonalnie)

        Returns:
            Liczba zmienionych wierszy
        """
        if params: # jeśli params podane
            self.cursor.execute(query, params)
        else: # jeśli params nie podane
            self.cursor.execute(query)
        return self.cursor.rowcount # zwróć ile wierszy zostało zmienionych
    
    def fetch_all(self, query: str, params: Optional[Tuple] = None): # podobnie jak execute_query
        """
        Wykonaj SELECT i pobierz wszystkie wyniki.
        
        Args:
            query: Zapytanie SELECT
            params: Parametry zapytania (opcjonalnie)

        Returns:
            Lista wierszy
        """
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall() # zwróć wszystkie wiersze
    
    def fetch_one(self, query: str, params: Optional[Tuple] = None): # podobnie jak fetch_all, execute_query
        """
        Wykonaj SELECT i pobierz jeden wynik

        Args:
            query: Zapytanie SELECT
            params: Parametry zapytania (opcjonalnie)

        Returns:
            Jeden wiersz lub None
        """
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchone() # zwróć jeden wiersz
    
    def bulk_insert(self, table: str, columns: list[str], data: list[Tuple]): # columns: List[str] = lista stringów
        # data: List[Tuple] = lista krotek
        """
        Bulk INSERT wielu rekordów naraz.

        Args:
            table: Nazwa tabeli
            columns: Lista nazw kolumn
            data: Lista tuple'i z danymi

        Returns:
            Liczba wstawionych wierszy
        """
        placeholders = ', '.join(['?'] * len(columns))
        # utwórz "?, ?, ?" (tyle '?' ile kolumn)
        # Przykład: ['?', '?', '?'] → "?, ?, ?"
        columns_str = ', '.join(columns)
        # połącz nazwy kolumn przecinkami - stąd też spacja po przecinku, tak jak w zapytaniu SQL
        # przykład: ['produkt', 'ilosc', 'cena'] czyli "produkt, ilosc, cena"
        query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
        # wstaw zmienne do zapytania
        # wynik: "INSERT INTO TestSprzedaz (produkt, ilosc, cena) VALUES (?, ?, ?)"

        self.cursor.executemany(query, data)
        # wykonaj insert dla kazdego tuple w data
        return len(data)
        # zwróc ile rekordów wstawiono
    
    def get_count(self, table: str, where: Optional[str] = None): # nazwa tabeli: string
        # warunek WHERE (string lub None), domyślnie None
        """
        Policz rekordy w tabeli

        Args:
            table: Nazwa tabeli
            where: warunek WHERE (opcjonalny)

        Returns:
            Liczba rekordów
        """
        query = f"SELECT COUNT(*) FROM {table}" # wstawia nazwę tabeli
        if where: # jeśli where jest podane (nie None i nie pusty string)
            query += f" WHERE {where}" # dodaje do query (konkatenacja) - czyli query + WHERE ...

        result = self.fetch_one(query) # wywołuje metode fetch_one, zwraca tylko jeden wiersz
        return result[0] if result else 0 # jeśli result istnieje zwróć result[0], jeśli None zwraca 0 - result[0] to pierwsza wartość, patrzymy po indeksie
    

# FUNKCJE POMOCNICZE

def get_credentials_from_file(filepath: str = "credentials.txt") -> dict:
    # filepath: str = domyślnie "credentials.txt"
    # -> dict - funkcja zwraca słownik
    """
    Wczytaj credentials z pliku tekstowego.

    Format pliku:
    server=sql-praca.mateusz.database.windows.net
    database=db-praca-inzynierska
    username=sqladmin
    password=Twoje_Haslo

    Args:
        filepath: Ścieżka do pliku z credentials

    Returns:
        Słownik z danymi logowania
    """
    credentials = {} # tworzymy pusty słownik

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # otwórz plik do odczytu ('r' = read)
            # encoding='utf-8' = obsługa polskich znaków
            # with = automatyczne zamknięcie pliku
            for line in f:
                line = line.strip() # line,strip() - usuń puste znaki z początku i końca
                if '=' in line and not line.startswith('#'):
                # jeśli linia zawiera '=' i nie zaczyna się od '#' - komentarza
                    key, value = line.split('=', 1)
                    # split() podziel string na '=' i max 1 podział
                    # Dlaczego 1?
                    # "a=b=c".split('=', 1) → ["a", "b=c"] (tylko pierwszy =)
                    # "a=b=c".split('=')    → ["a", "b", "c"] (wszystkie =)
                    credentials[key.strip()] = value.strip()
                    # zapisz w słowniku, key.strip() - usuń spacje z klucza, value.strip() - usuń spacje z wartości
    except:
        print(f"Plik {filepath} nie istnieje!")
        return None
        
    return credentials
    
def print_table(rows, headers: list[str], widths: Optional[list[int]] = None):
    """
    Wyświetl wyniki w formnie ładnej tabeli

    Args:
        rows: Lista wierszy (Row object lub tuple)
        headers: Nazwy kolumn
        widths: Szerokości kolumn (opcjonalnie)
    """
    if not widths:
        widths = [15] * len(headers)

    # nagłowek
    header_str = " | ".join([h.ljust(w) for h, w in zip(headers, widths)]) # h, w - to naglowki i szerokosc, join zaś łączy stringi uzywając "|" jako seperatora
    # zip(headers, widths) - Połącz dwie listy w pary:
    # [('id', 5), ('produkt', 20), ('ilosc', 8), ('cena', 10)]
    # h.ljust(w) - 'left justify' czyli wyrównanie do lewej, wypełnij spacjali do szerokości w
    print(header_str)
    print("=" * len(header_str))

    # wiersze
    for row in rows:
        values = [str(getattr(row, h, '')) if hasattr(row, h) else str(row[i])
            # hasattr(row, h) - sprawdza czy obiekt row ma aytrubut o naziwe h, czyli hasattr(row, 'produkt') → True (row.produkt istnieje)
            # getattr(row, h, '') - pobiera wartości atrybutu o nazwie h, jeśli nie istnieje zwraca pusty string
            for i, h in enumerate(headers)] # enumerate zwraca pary (indeks, wartość) dla każdego i, h
        row_str = " | ".join([v.ljust(w)[:w] for v, w in zip(values, widths)])
        # podobnie jak header_str
        print(row_str)

# PRZYKŁAD UŻYCIA
if __name__ == "__main__":
    print("-" * 60)
    print("db.utils.py - Test funkcji pomocniczych")
    print("-" * 60)

    # dane logowania
    SERVER = 'sql-praca-mateusz.database.windows.net'
    DATABASE = 'db-praca-inzynierska'
    USERNAME = 'sqladmin'
    PASSWORD = 'YOUR_PASSWORD_HERE'  # uzupełnić

    try:
        #użycie context managera (automatyczne zamknięcie) z with
        with AzureSQLConnection(SERVER, DATABASE, USERNAME, PASSWORD) as db:
            # python wywołuje __enter__() czyli wywołuje połączenie
            # db = self (zwrócone przez __enter__)
            print("\nPołączona z Azure SQL!")

            # Test 1: policz rekordy
            count = db.get_count('TestSprzedaz')
            print(f"\nLiczba rekordów: {count}")

            # Test 2: Pobierz TOP 5
            rows = db.fetch_all("""
                SELECT TOP 5 id, produkt, ilosc, cena
                FROM TestSprzedaz
                ORDER BY id DESC
            """)

            print(f"\nTOP 5 rekordów:")
            print_table(rows, ['id', 'produkt', 'ilosc', 'cena'], [5, 20, 8, 10])

            # Test 3: Statystyki
            stats = db.fetch_one("""
                SELECT
                    AVG(cena) as avg_price,
                    MIN(cena) as min_price,
                    MAX(cena) as max_price
                FROM TestSprzedaz
            """)

            print("\nStatystyki:")
            print(f"    Średnia cena: {stats.avg_price:.2f} zł")
            print(f"    Min cena: {stats.min_price:.2f} zł")
            print(f"    Max cena: {stats.max_price:.2f} zł")

        print("\nTest zakończony pomyślnie!")
    
    except Exception as e:
        print(f"Błąd: {e}")

    input("\nNaciśnij Enter aby zakończyć...")