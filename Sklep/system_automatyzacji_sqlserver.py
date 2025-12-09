# -*- coding: utf-8 -*-
# ====================================================================
# SYSTEM AUTOMATYZACJI RAPORTÓW Z INTERFEJSEM SKLEPU - SQL SERVER
# ====================================================================
# Wersja: 2.0
# Data: 16 listopada 2025
# Baza danych: Microsoft SQL Server
# ====================================================================

# ====================================================================
# SEKCJA 1: IMPORTY BIBLIOTEK
# ====================================================================

# Importowanie biblioteki sys do konfiguracji kodowania konsoli
import sys
# Importowanie biblioteki os do obsługi zmiennych środowiskowych
import os

# Konfiguracja kodowania UTF-8 dla konsoli Windows
# Zapewnia poprawne wyświetlanie polskich znaków (ą, ę, ł, ć, ń, ó, ś, ź, ż)
if sys.platform == 'win32':
    # Ustawiamy zmienną środowiskową PYTHONIOENCODING na UTF-8
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    # Próba zmiany strony kodowej konsoli na UTF-8 (65001)
    try:
        os.system('chcp 65001 >nul 2>&1')
    except:
        pass  # Ignorujemy błędy jeśli nie można zmienić strony kodowej

# Importowanie biblioteki do łączenia z bazami danych ODBC (SQL Server)
import pyodbc

# Importowanie biblioteki do przetwarzania danych tabelarycznych
import pandas as pd

# Importowanie biblioteki do pracy z datami i czasem
from datetime import datetime

# Importowanie głównej klasy Tkinter do tworzenia okien GUI
import tkinter as tk

# Importowanie dodatkowych widgetów Tkinter (themed widgets)
from tkinter import ttk

# Importowanie modułu do wyświetlania okien dialogowych (komunikaty, błędy)
from tkinter import messagebox

# Importowanie modułu do parsowania plików konfiguracyjnych INI
import configparser

# Moduł os został już zaimportowany na początku pliku (linia 17)


# ====================================================================
# SEKCJA 2: KLASA GŁÓWNA - LOGIKA BIZNESOWA I BAZA DANYCH
# ====================================================================

class ReportAutomationSystem:
    """
    Klasa główna systemu automatyzacji raportów.
    Zarządza połączeniem z SQL Server, generowaniem raportów i operacjami sklepu.
    """

    def __init__(self):
        """
        Konstruktor klasy - inicjalizuje parametry połączenia z SQL Server.
        Parametry połączenia są wczytywane z pliku config.ini lub używane domyślne.
        """

        # Tworzenie obiektu parsera konfiguracji
        config = configparser.ConfigParser()

        # Próba wczytania pliku konfiguracyjnego
        try:
            # Odczytanie pliku config.ini z bieżącego katalogu
            # encoding='utf-8' - używamy kodowania UTF-8 dla polskich znaków
            config.read('config.ini', encoding='utf-8')

            # Wczytanie nazwy serwera SQL Server z sekcji DATABASE
            # Domyślnie: localhost\SQLEXPRESS (lokalne SQL Server Express)
            self.server = config.get('DATABASE', 'Server', fallback='localhost\\SQLEXPRESS')

            # Wczytanie nazwy bazy danych
            # Domyślnie: SklepDB
            self.database = config.get('DATABASE', 'Database', fallback='SklepDB')

            # Wczytanie nazwy użytkownika
            # Puste = Windows Authentication (zalecane)
            self.username = config.get('DATABASE', 'Username', fallback='')

            # Wczytanie hasła użytkownika
            # Puste = Windows Authentication (zalecane)
            self.password = config.get('DATABASE', 'Password', fallback='')

        except Exception as e:
            # W przypadku błędu wczytywania pliku, użyj wartości domyślnych
            print(f"Nie można wczytać config.ini, używam wartości domyślnych: {e}")

            # Nazwa serwera SQL Server - localhost\SQLEXPRESS dla lokalnego
            self.server = 'localhost\\SQLEXPRESS'

            # Nazwa bazy danych którą utworzymy
            self.database = 'SklepDB'

            # Nazwa użytkownika (puste = Windows Authentication)
            self.username = ''

            # Hasło użytkownika (puste = Windows Authentication)
            self.password = ''

        # Wywołanie metody inicjalizującej bazę danych
        # Utworzy bazę i tabele jeśli nie istnieją, wstawi przykładowe dane
        self.initialize_database()


    def build_connection_string(self):
        """
        Metoda budująca connection string dla połączenia z SQL Server.
        Obsługuje zarówno Windows Authentication jak i SQL Server Authentication.

        Returns:
            str: Connection string gotowy do użycia z pyodbc
        """

        # Sprawdzamy czy pole username jest puste
        # Jeśli puste - używamy Windows Authentication
        if not self.username:
            # ========================================================
            # WINDOWS AUTHENTICATION (ZALECANE)
            # ========================================================

            # Budowanie connection string dla Windows Authentication
            connection_string = (
                # DRIVER - sterownik ODBC dla SQL Server wersja 17
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                # SERVER - adres i nazwa instancji SQL Server
                f"SERVER={self.server};"
                # DATABASE - nazwa bazy danych do której się łączymy
                f"DATABASE={self.database};"
                # Trusted_Connection - używamy uwierzytelnienia Windows
                f"Trusted_Connection=yes;"
            )
        else:
            # ========================================================
            # SQL SERVER AUTHENTICATION
            # ========================================================

            # Budowanie connection string dla SQL Server Authentication
            connection_string = (
                # DRIVER - sterownik ODBC dla SQL Server wersja 17
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                # SERVER - adres i nazwa instancji SQL Server
                f"SERVER={self.server};"
                # DATABASE - nazwa bazy danych do której się łączymy
                f"DATABASE={self.database};"
                # UID - User ID (nazwa użytkownika SQL Server)
                f"UID={self.username};"
                # PWD - Password (hasło użytkownika SQL Server)
                f"PWD={self.password};"
            )

        # Zwracamy zbudowany connection string
        return connection_string


    def initialize_database(self):
        """
        Metoda inicjalizująca bazę danych SQL Server.
        Tworzy bazę danych (jeśli nie istnieje), tabele i wypełnia przykładowymi danymi.
        """

        # Rozpoczynamy blok try-except do obsługi błędów
        try:
            # ========================================================
            # KROK 1: POŁĄCZENIE Z SQL SERVER (BEZ BAZY DANYCH)
            # ========================================================

            # Budujemy connection string dla połączenia z serwerem (bez konkretnej bazy)
            # Zastępujemy nazwę bazy na 'master' - systemowa baza zawsze dostępna
            initial_conn_string = self.build_connection_string().replace(
                f"DATABASE={self.database}",
                "DATABASE=master"
            )

            # Nawiązujemy połączenie z SQL Server (baza master)
            conn = pyodbc.connect(initial_conn_string)

            # Wyłączamy automatyczne transakcje dla CREATE DATABASE
            # CREATE DATABASE nie może być wykonane w transakcji
            conn.autocommit = True

            # Tworzymy obiekt cursor do wykonywania zapytań SQL
            cursor = conn.cursor()

            # ========================================================
            # KROK 2: UTWORZENIE BAZY DANYCH (JEŚLI NIE ISTNIEJE)
            # ========================================================

            # Sprawdzamy czy baza danych już istnieje
            cursor.execute(f"""
                -- Zapytanie sprawdzające istnienie bazy w systemowej tabeli sys.databases
                SELECT database_id
                FROM sys.databases
                WHERE name = '{self.database}'
            """)

            # Próbujemy pobrać wynik zapytania
            # Jeśli None - baza nie istnieje
            if cursor.fetchone() is None:
                # Baza nie istnieje - tworzymy ją
                print(f"Tworzenie bazy danych {self.database}...")

                # Wykonujemy polecenie CREATE DATABASE
                # Nie potrzebujemy commit - autocommit jest włączony
                cursor.execute(f"CREATE DATABASE {self.database}")

                # Komunikat o sukcesie
                print(f"Baza danych {self.database} została utworzona.")
            else:
                # Baza już istnieje
                print(f"Baza danych {self.database} już istnieje.")

            # Zamykamy połączenie z bazą master
            cursor.close()
            conn.close()

            # ========================================================
            # KROK 3: POŁĄCZENIE Z NOWO UTWORZONĄ BAZĄ DANYCH
            # ========================================================

            # Budujemy pełny connection string (z naszą bazą danych)
            conn_string = self.build_connection_string()

            # Nawiązujemy połączenie z naszą bazą danych
            conn = pyodbc.connect(conn_string)

            # Tworzymy nowy cursor do wykonywania zapytań
            cursor = conn.cursor()

            # ========================================================
            # KROK 4: UTWORZENIE TABELI 'klienci'
            # ========================================================

            print("Tworzenie tabel...")

            # Polecenie SQL tworzące tabelę klienci
            cursor.execute("""
                -- IF NOT EXISTS - tworzymy tylko jeśli tabela nie istnieje
                IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'klienci')
                BEGIN
                    CREATE TABLE klienci (
                        -- id - klucz główny, auto-increment (IDENTITY)
                        id INT IDENTITY(1,1) PRIMARY KEY,
                        -- nazwa - nazwa klienta/firmy (NVARCHAR dla polskich znaków)
                        nazwa NVARCHAR(255) NOT NULL,
                        -- email - adres email klienta
                        email NVARCHAR(255),
                        -- telefon - numer telefonu
                        telefon NVARCHAR(50),
                        -- adres - pełny adres klienta
                        adres NVARCHAR(500)
                    )
                END
            """)

            # ========================================================
            # KROK 5: UTWORZENIE TABELI 'produkty'
            # ========================================================

            # Polecenie SQL tworzące tabelę produkty
            cursor.execute("""
                -- IF NOT EXISTS - tworzymy tylko jeśli tabela nie istnieje
                IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'produkty')
                BEGIN
                    CREATE TABLE produkty (
                        -- id - klucz główny, auto-increment
                        id INT IDENTITY(1,1) PRIMARY KEY,
                        -- nazwa - nazwa produktu (NVARCHAR dla polskich znaków)
                        nazwa NVARCHAR(255) NOT NULL,
                        -- kategoria - kategoria produktu (np. Elektronika, Audio)
                        kategoria NVARCHAR(100),
                        -- opis - szczegółowy opis produktu
                        opis NVARCHAR(1000),
                        -- stan_magazynowy - ile sztuk jest w magazynie
                        stan_magazynowy INT DEFAULT 0
                    )
                END
            """)

            # ========================================================
            # KROK 6: UTWORZENIE TABELI 'ceny'
            # ========================================================

            # Polecenie SQL tworzące tabelę ceny
            cursor.execute("""
                -- IF NOT EXISTS - tworzymy tylko jeśli tabela nie istnieje
                IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'ceny')
                BEGIN
                    CREATE TABLE ceny (
                        -- id - klucz główny, auto-increment
                        id INT IDENTITY(1,1) PRIMARY KEY,
                        -- produkt_id - odniesienie do tabeli produkty (foreign key)
                        produkt_id INT,
                        -- cena - wartość ceny (DECIMAL dla dokładności finansowej)
                        cena DECIMAL(10,2) NOT NULL,
                        -- data_od - od kiedy cena obowiązuje
                        data_od DATE,
                        -- data_do - do kiedy cena obowiązuje
                        data_do DATE,
                        -- FOREIGN KEY - powiązanie z tabelą produkty
                        FOREIGN KEY (produkt_id) REFERENCES produkty(id)
                    )
                END
            """)

            # ========================================================
            # KROK 7: UTWORZENIE TABELI 'zamowienia'
            # ========================================================

            # Polecenie SQL tworzące tabelę zamowienia
            cursor.execute("""
                -- IF NOT EXISTS - tworzymy tylko jeśli tabela nie istnieje
                IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'zamowienia')
                BEGIN
                    CREATE TABLE zamowienia (
                        -- id - klucz główny, auto-increment
                        id INT IDENTITY(1,1) PRIMARY KEY,
                        -- klient_id - odniesienie do tabeli klienci (foreign key)
                        klient_id INT,
                        -- produkt_id - odniesienie do tabeli produkty (foreign key)
                        produkt_id INT,
                        -- ilosc - ile sztuk zamówiono
                        ilosc INT,
                        -- cena_jednostkowa - cena za jedną sztukę w momencie zamówienia
                        cena_jednostkowa DECIMAL(10,2),
                        -- data_zamowienia - kiedy złożono zamówienie (GETDATE() = teraz)
                        data_zamowienia DATETIME DEFAULT GETDATE(),
                        -- status - status zamówienia (np. 'nowe', 'wysłane', 'dostarczone')
                        status NVARCHAR(50) DEFAULT 'nowe',
                        -- FOREIGN KEY - powiązanie z tabelą klienci
                        FOREIGN KEY (klient_id) REFERENCES klienci(id),
                        -- FOREIGN KEY - powiązanie z tabelą produkty
                        FOREIGN KEY (produkt_id) REFERENCES produkty(id)
                    )
                END
            """)

            # Zatwierdzamy utworzenie wszystkich tabel
            conn.commit()

            print("Tabele utworzone pomyślnie.")

            # ========================================================
            # KROK 8: SPRAWDZENIE CZY DANE PRZYKŁADOWE JUŻ ISTNIEJĄ
            # ========================================================

            # Sprawdzamy czy tabela klienci jest pusta
            cursor.execute("SELECT COUNT(*) FROM klienci")

            # Pobieramy liczbę rekordów w tabeli klienci
            # fetchone() zwraca tuple, [0] pobiera pierwszą wartość
            count = cursor.fetchone()[0]

            # Jeśli tabela jest pusta (count == 0), wstawiamy przykładowe dane
            if count == 0:
                print("Wypełnianie bazy przykładowymi danymi...")

                # ========================================================
                # KROK 9: WSTAWIANIE PRZYKŁADOWYCH KLIENTÓW
                # ========================================================

                # INSERT do tabeli klienci - Klient 1: Firma ABC
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    # ? - parametry zapytania (zabezpieczenie przed SQL Injection)
                    'Firma ABC Sp. z o.o.',  # nazwa firmy
                    'kontakt@abc.pl',         # email
                    '+48 123 456 789',        # telefon
                    'ul. Przykładowa 1, 00-001 Warszawa'  # adres
                ))

                # INSERT do tabeli klienci - Klient 2: Jan Kowalski
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Jan Kowalski',           # imię i nazwisko
                    'jan.kowalski@email.pl',  # email
                    '+48 987 654 321',        # telefon
                    'ul. Testowa 5, 30-001 Kraków'  # adres
                ))

                # INSERT do tabeli klienci - Klient 3: Hurtownia XYZ
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Hurtownia XYZ',          # nazwa hurtowni
                    'biuro@xyz.com',          # email
                    '+48 555 123 456',        # telefon
                    'ul. Handlowa 10, 50-001 Wrocław'  # adres
                ))

                # INSERT do tabeli klienci - Klient 4: Anna Nowak
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Anna Nowak',             # imię i nazwisko
                    'anna.nowak@gmail.com',   # email
                    '+48 600 111 222',        # telefon
                    'ul. Słoneczna 12, 80-001 Gdańsk'  # adres
                ))

                # INSERT do tabeli klienci - Klient 5: Tech Solutions
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Tech Solutions Sp. z o.o.',  # nazwa firmy IT
                    'office@techsolutions.pl',    # email
                    '+48 22 555 6677',            # telefon
                    'ul. Nowogrodzka 47a, 00-695 Warszawa'  # adres
                ))

                # INSERT do tabeli klienci - Klient 6: Piotr Wiśniewski
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Piotr Wiśniewski',       # imię i nazwisko
                    'p.wisniewski@op.pl',     # email
                    '+48 501 222 333',        # telefon
                    'ul. Główna 88, 40-001 Katowice'  # adres
                ))

                # INSERT do tabeli klienci - Klient 7: Sklep Komputerowy MEGA
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Sklep Komputerowy MEGA',  # nazwa sklepu detalicznego
                    'zamowienia@mega.pl',      # email
                    '+48 12 333 4455',         # telefon
                    'ul. Krakowska 100, 31-062 Kraków'  # adres
                ))

                # INSERT do tabeli klienci - Klient 8: Maria Lewandowska
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Maria Lewandowska',      # imię i nazwisko
                    'mlewandowska@interia.pl', # email
                    '+48 606 777 888',        # telefon
                    'ul. Polna 7, 60-001 Poznań'  # adres
                ))

                # INSERT do tabeli klienci - Klient 9: Digital Office Sp. z o.o.
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Digital Office Sp. z o.o.',  # firma specjalizująca się w sprzęcie biurowym
                    'kontakt@digitaloffice.pl',   # email
                    '+48 61 888 9999',            # telefon
                    'ul. Śródmiejska 25, 61-001 Poznań'  # adres
                ))

                # INSERT do tabeli klienci - Klient 10: Tomasz Kamiński
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Tomasz Kamiński',        # imię i nazwisko
                    't.kaminski@yahoo.com',   # email
                    '+48 505 444 555',        # telefon
                    'ul. Morska 15, 70-001 Szczecin'  # adres
                ))

                # INSERT do tabeli klienci - Klient 11: Gaming Store PRO
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Gaming Store PRO',       # sklep z akcesoriami gamingowymi
                    'biuro@gamingpro.pl',     # email
                    '+48 71 222 3344',        # telefon
                    'ul. Grodzka 33, 50-001 Wrocław'  # adres
                ))

                # INSERT do tabeli klienci - Klient 12: Katarzyna Zielińska
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Katarzyna Zielińska',    # imię i nazwisko
                    'k.zielinska@gmail.com',  # email
                    '+48 602 888 999',        # telefon
                    'ul. Lipowa 44, 90-001 Łódź'  # adres
                ))

                # INSERT do tabeli klienci - Klient 13: Przedsiębiorstwo ELEKTRO
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Przedsiębiorstwo ELEKTRO',  # firma zajmująca się elektroniką
                    'zamowienia@elektro.com.pl', # email
                    '+48 42 555 6677',           # telefon
                    'ul. Piotrkowska 120, 90-001 Łódź'  # adres
                ))

                # INSERT do tabeli klienci - Klient 14: Marek Wójcik
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Marek Wójcik',           # imię i nazwisko
                    'm.wojcik@onet.pl',       # email
                    '+48 508 123 456',        # telefon
                    'ul. Sienkiewicza 8, 15-001 Białystok'  # adres
                ))

                # INSERT do tabeli klienci - Klient 15: Smart Electronics
                cursor.execute("""
                    INSERT INTO klienci (nazwa, email, telefon, adres)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Smart Electronics Sp. z o.o.',  # dystrybutor elektroniki
                    'info@smartelectronics.pl',     # email
                    '+48 58 777 8899',              # telefon
                    'ul. Gdańska 200, 80-001 Gdańsk'  # adres
                ))

                # ========================================================
                # KROK 10: WSTAWIANIE PRZYKŁADOWYCH PRODUKTÓW
                # ========================================================

                # INSERT do tabeli produkty - Produkt 1: Laptop Dell XPS 15
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Laptop Dell XPS 15',     # nazwa produktu
                    'Komputery',              # kategoria
                    'Wysokowydajny laptop do pracy i rozrywki',  # opis
                    15                        # stan magazynowy (15 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 2: Monitor Samsung 27"
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Monitor Samsung 27"',    # nazwa produktu
                    'Elektronika',            # kategoria
                    'Monitor LED 27 cali Full HD',  # opis
                    25                        # stan magazynowy (25 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 3: Klawiatura mechaniczna
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Klawiatura mechaniczna', # nazwa produktu
                    'Akcesoria',              # kategoria
                    'Klawiatura mechaniczna z podświetleniem RGB',  # opis
                    50                        # stan magazynowy (50 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 4: Mysz bezprzewodowa
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Mysz bezprzewodowa',     # nazwa produktu
                    'Akcesoria',              # kategoria
                    'Mysz optyczna bezprzewodowa 2.4GHz',  # opis
                    100                       # stan magazynowy (100 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 5: Słuchawki Sony WH-1000XM4
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Słuchawki Sony WH-1000XM4',  # nazwa produktu
                    'Audio',                      # kategoria
                    'Słuchawki bezprzewodowe z redukcją szumów',  # opis
                    30                            # stan magazynowy (30 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 6: Laptop HP Pavilion 15
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Laptop HP Pavilion 15',  # nazwa produktu
                    'Komputery',              # kategoria
                    'Laptop z procesorem Intel Core i5, 8GB RAM, 512GB SSD',  # opis
                    20                        # stan magazynowy (20 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 7: Monitor LG UltraWide 34"
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Monitor LG UltraWide 34"',  # nazwa produktu
                    'Elektronika',               # kategoria
                    'Monitor panoramiczny 34 cale WQHD',  # opis
                    12                           # stan magazynowy (12 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 8: Drukarka HP LaserJet Pro
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Drukarka HP LaserJet Pro',  # nazwa produktu
                    'Urządzenia biurowe',        # kategoria
                    'Drukarka laserowa monochromatyczna',  # opis
                    18                           # stan magazynowy (18 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 9: Kamera internetowa Logitech C920
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Kamera internetowa Logitech C920',  # nazwa produktu
                    'Akcesoria',                         # kategoria
                    'Kamera Full HD 1080p z mikrofonem stereo',  # opis
                    45                                   # stan magazynowy (45 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 10: Tablet Samsung Galaxy Tab S8
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Tablet Samsung Galaxy Tab S8',  # nazwa produktu
                    'Elektronika',                   # kategoria
                    'Tablet 11 cali z rysikiem S Pen',  # opis
                    22                               # stan magazynowy (22 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 11: Dysk SSD Samsung 1TB
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Dysk SSD Samsung 1TB',  # nazwa produktu
                    'Komputery',             # kategoria
                    'Dysk SSD NVMe M.2 1TB o wysokiej prędkości',  # opis
                    60                       # stan magazynowy (60 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 12: Głośnik Bluetooth JBL Charge 5
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Głośnik Bluetooth JBL Charge 5',  # nazwa produktu
                    'Audio',                           # kategoria
                    'Przenośny głośnik Bluetooth wodoodporny IP67',  # opis
                    35                                 # stan magazynowy (35 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 13: Router Wi-Fi TP-Link AX3000
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Router Wi-Fi TP-Link AX3000',  # nazwa produktu
                    'Sieć',                         # kategoria
                    'Router WiFi 6 dual-band z prędkością do 3 Gbps',  # opis
                    28                              # stan magazynowy (28 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 14: Mikrofon Blue Yeti
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Mikrofon Blue Yeti',    # nazwa produktu
                    'Audio',                 # kategoria
                    'Mikrofon pojemnościowy USB do nagrywania i streamingu',  # opis
                    16                       # stan magazynowy (16 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 15: Powerbank Anker 20000mAh
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Powerbank Anker 20000mAh',  # nazwa produktu
                    'Akcesoria',                 # kategoria
                    'Powerbank z szybkim ładowaniem Power Delivery',  # opis
                    70                           # stan magazynowy (70 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 16: Klawiatura gamingowa Razer BlackWidow
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Klawiatura gamingowa Razer BlackWidow',  # nazwa produktu
                    'Gaming',                                 # kategoria
                    'Klawiatura mechaniczna dla graczy z podświetleniem Chroma RGB',  # opis
                    25                                        # stan magazynowy (25 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 17: Mysz gamingowa Logitech G502
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Mysz gamingowa Logitech G502',  # nazwa produktu
                    'Gaming',                        # kategoria
                    'Mysz gamingowa z 11 programowalnymi przyciskami',  # opis
                    42                               # stan magazynowy (42 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 18: Słuchawki HyperX Cloud II
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Słuchawki HyperX Cloud II',  # nazwa produktu
                    'Gaming',                     # kategoria
                    'Słuchawki gamingowe z dźwiękiem 7.1 surround',  # opis
                    33                            # stan magazynowy (33 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 19: Monitor Dell 24" Full HD
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Monitor Dell 24" Full HD',  # nazwa produktu
                    'Elektronika',               # kategoria
                    'Monitor biurowy 24 cale IPS Full HD',  # opis
                    38                           # stan magazynowy (38 sztuk)
                ))

                # INSERT do tabeli produkty - Produkt 20: Laptop Lenovo ThinkPad E15
                cursor.execute("""
                    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
                    VALUES (?, ?, ?, ?)
                """, (
                    'Laptop Lenovo ThinkPad E15',  # nazwa produktu
                    'Komputery',                   # kategoria
                    'Laptop biznesowy z Intel Core i7, 16GB RAM, 512GB SSD',  # opis
                    14                             # stan magazynowy (14 sztuk)
                ))

                # ========================================================
                # KROK 11: WSTAWIANIE CEN DLA PRODUKTÓW
                # ========================================================

                # Pobieramy ID wstawionych produktów aby przypisać im ceny
                # ID produktów to 1, 2, 3, ..., 20 (IDENTITY zaczyna od 1)

                # Cena dla Produktu 1: Laptop Dell XPS 15 (produkt_id = 1)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    1,              # produkt_id (Laptop Dell XPS 15)
                    4999.00,        # cena w PLN (DECIMAL)
                    '2025-01-01',   # cena obowiązuje od 1 stycznia 2025
                    '2025-12-31'    # cena obowiązuje do 31 grudnia 2025
                ))

                # Cena dla Produktu 2: Monitor Samsung 27" (produkt_id = 2)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    2,              # produkt_id (Monitor Samsung 27")
                    1299.00,        # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 3: Klawiatura mechaniczna (produkt_id = 3)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    3,              # produkt_id (Klawiatura mechaniczna)
                    449.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 4: Mysz bezprzewodowa (produkt_id = 4)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    4,              # produkt_id (Mysz bezprzewodowa)
                    129.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 5: Słuchawki Sony WH-1000XM4 (produkt_id = 5)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    5,              # produkt_id (Słuchawki Sony WH-1000XM4)
                    1499.00,        # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 6: Laptop HP Pavilion 15 (produkt_id = 6)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    6,              # produkt_id (Laptop HP Pavilion 15)
                    3299.00,        # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 7: Monitor LG UltraWide 34" (produkt_id = 7)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    7,              # produkt_id (Monitor LG UltraWide 34")
                    2199.00,        # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 8: Drukarka HP LaserJet Pro (produkt_id = 8)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    8,              # produkt_id (Drukarka HP LaserJet Pro)
                    899.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 9: Kamera internetowa Logitech C920 (produkt_id = 9)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    9,              # produkt_id (Kamera internetowa Logitech C920)
                    349.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 10: Tablet Samsung Galaxy Tab S8 (produkt_id = 10)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    10,             # produkt_id (Tablet Samsung Galaxy Tab S8)
                    2599.00,        # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 11: Dysk SSD Samsung 1TB (produkt_id = 11)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    11,             # produkt_id (Dysk SSD Samsung 1TB)
                    449.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 12: Głośnik Bluetooth JBL Charge 5 (produkt_id = 12)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    12,             # produkt_id (Głośnik Bluetooth JBL Charge 5)
                    649.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 13: Router Wi-Fi TP-Link AX3000 (produkt_id = 13)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    13,             # produkt_id (Router Wi-Fi TP-Link AX3000)
                    499.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 14: Mikrofon Blue Yeti (produkt_id = 14)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    14,             # produkt_id (Mikrofon Blue Yeti)
                    599.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 15: Powerbank Anker 20000mAh (produkt_id = 15)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    15,             # produkt_id (Powerbank Anker 20000mAh)
                    199.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 16: Klawiatura gamingowa Razer BlackWidow (produkt_id = 16)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    16,             # produkt_id (Klawiatura gamingowa Razer BlackWidow)
                    699.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 17: Mysz gamingowa Logitech G502 (produkt_id = 17)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    17,             # produkt_id (Mysz gamingowa Logitech G502)
                    299.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 18: Słuchawki HyperX Cloud II (produkt_id = 18)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    18,             # produkt_id (Słuchawki HyperX Cloud II)
                    449.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 19: Monitor Dell 24" Full HD (produkt_id = 19)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    19,             # produkt_id (Monitor Dell 24" Full HD)
                    899.00,         # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Cena dla Produktu 20: Laptop Lenovo ThinkPad E15 (produkt_id = 20)
                cursor.execute("""
                    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
                    VALUES (?, ?, ?, ?)
                """, (
                    20,             # produkt_id (Laptop Lenovo ThinkPad E15)
                    4299.00,        # cena w PLN
                    '2025-01-01',   # cena obowiązuje od
                    '2025-12-31'    # cena obowiązuje do
                ))

                # Zatwierdzamy wszystkie INSERT-y
                conn.commit()

                print("Dane przykładowe zostały dodane.")

            # Zamykamy cursor
            cursor.close()

            # Zamykamy połączenie z bazą danych
            conn.close()

            print("Inicjalizacja bazy danych zakończona pomyślnie.")

        except pyodbc.Error as e:
            # Jeśli wystąpił błąd SQL Server
            print(f"Błąd SQL Server podczas inicjalizacji bazy: {e}")

        except Exception as e:
            # Jeśli wystąpił inny błąd
            print(f"Błąd podczas inicjalizacji bazy danych: {e}")


# ====================================================================
# SEKCJA 3: METODY GENEROWANIA RAPORTÓW
# ====================================================================

    def generate_sales_report(self):
        """
        Generuje raport sprzedaży - wszystkie zamówienia z pełnymi informacjami.

        Returns:
            pandas.DataFrame: DataFrame z danymi raportu lub None jeśli błąd
        """

        try:
            # Nawiązujemy połączenie z bazą danych SQL Server
            conn = pyodbc.connect(self.build_connection_string())

            # Zapytanie SQL pobierające dane o zamówieniach
            # JOIN łączy dane z 3 tabel: zamowienia, klienci, produkty
            query = """
                SELECT
                    -- ID zamówienia
                    z.id as zamowienie_id,
                    -- Nazwa klienta (z tabeli klienci)
                    k.nazwa as klient,
                    -- Email klienta
                    k.email as email_klienta,
                    -- Nazwa produktu (z tabeli produkty)
                    p.nazwa as produkt,
                    -- Kategoria produktu
                    p.kategoria,
                    -- Ile sztuk zamówiono
                    z.ilosc,
                    -- Cena za jedną sztukę
                    z.cena_jednostkowa,
                    -- Wartość całkowita (ilość × cena jednostkowa)
                    (z.ilosc * z.cena_jednostkowa) as wartosc_calkowita,
                    -- Data złożenia zamówienia
                    z.data_zamowienia,
                    -- Status zamówienia (np. 'nowe')
                    z.status
                FROM zamowienia z
                -- INNER JOIN - łączy zamówienia z klientami
                INNER JOIN klienci k ON z.klient_id = k.id
                -- INNER JOIN - łączy zamówienia z produktami
                INNER JOIN produkty p ON z.produkt_id = p.id
                -- Sortowanie od najnowszych zamówień
                ORDER BY z.data_zamowienia DESC
            """

            # Wykonujemy zapytanie i konwertujemy wynik do pandas DataFrame
            # read_sql - metoda pandas do odczytu danych z SQL
            df = pd.read_sql(query, conn)

            # Zamykamy połączenie z bazą danych
            conn.close()

            # Zwracamy DataFrame z wynikami
            return df

        except pyodbc.Error as e:
            # Błąd połączenia z SQL Server
            print(f"Błąd SQL Server: {e}")
            # Zwracamy None aby wskazać błąd
            return None

        except Exception as e:
            # Inny błąd (np. pandas)
            print(f"Błąd podczas generowania raportu sprzedaży: {e}")
            # Zwracamy None aby wskazać błąd
            return None


    def generate_inventory_report(self):
        """
        Generuje raport magazynowy - stany produktów z cenami i wartościami.

        Returns:
            pandas.DataFrame: DataFrame z danymi raportu lub None jeśli błąd
        """

        try:
            # Nawiązujemy połączenie z bazą danych
            conn = pyodbc.connect(self.build_connection_string())

            # Zapytanie SQL pobierające dane o produktach i cenach
            query = """
                SELECT
                    -- Nazwa produktu
                    p.nazwa as produkt,
                    -- Kategoria produktu
                    p.kategoria,
                    -- Stan magazynowy (ile sztuk)
                    p.stan_magazynowy,
                    -- Aktualna cena produktu
                    c.cena as cena_aktualna,
                    -- Wartość magazynowa (stan × cena)
                    (p.stan_magazynowy * c.cena) as wartosc_magazynowa
                FROM produkty p
                -- LEFT JOIN - pobieramy wszystkie produkty, nawet bez cen
                LEFT JOIN ceny c ON p.id = c.produkt_id
                    -- Filtrujemy tylko aktualne ceny (dzisiejsza data między data_od a data_do)
                    -- GETDATE() - funkcja SQL Server zwracająca aktualną datę i czas
                    AND GETDATE() BETWEEN c.data_od AND c.data_do
                -- Sortowanie: najpierw po kategorii, potem po nazwie
                ORDER BY p.kategoria, p.nazwa
            """

            # Wykonujemy zapytanie i konwertujemy wynik do DataFrame
            df = pd.read_sql(query, conn)

            # Zamykamy połączenie
            conn.close()

            # Zwracamy DataFrame
            return df

        except pyodbc.Error as e:
            # Błąd SQL Server
            print(f"Błąd SQL Server: {e}")
            return None

        except Exception as e:
            # Inny błąd
            print(f"Błąd podczas generowania raportu magazynowego: {e}")
            return None


    def generate_customer_report(self):
        """
        Generuje raport klientów - podsumowanie aktywności każdego klienta.

        Returns:
            pandas.DataFrame: DataFrame z danymi raportu lub None jeśli błąd
        """

        try:
            # Nawiązujemy połączenie z bazą danych
            conn = pyodbc.connect(self.build_connection_string())

            # Zapytanie SQL z agregacją danych o klientach
            query = """
                SELECT
                    -- Nazwa klienta
                    k.nazwa as klient,
                    -- Email klienta
                    k.email,
                    -- Telefon klienta
                    k.telefon,
                    -- Liczba złożonych zamówień (COUNT)
                    -- ISNULL zamienia NULL na 0 dla klientów bez zamówień
                    ISNULL(COUNT(z.id), 0) as liczba_zamowien,
                    -- Łączna wartość zakupów (SUM)
                    -- ISNULL zamienia NULL na 0 dla klientów bez zamówień
                    ISNULL(SUM(z.ilosc * z.cena_jednostkowa), 0) as laczna_wartosc
                FROM klienci k
                -- LEFT JOIN - pobieramy wszystkich klientów, nawet bez zamówień
                LEFT JOIN zamowienia z ON k.id = z.klient_id
                -- GROUP BY - grupujemy wyniki po kliencie
                -- Wymagane przy użyciu funkcji agregujących (COUNT, SUM)
                GROUP BY k.id, k.nazwa, k.email, k.telefon
                -- Sortowanie od klientów z największą wartością zakupów
                ORDER BY laczna_wartosc DESC
            """

            # Wykonujemy zapytanie i konwertujemy do DataFrame
            df = pd.read_sql(query, conn)

            # Zamykamy połączenie
            conn.close()

            # Zwracamy DataFrame
            return df

        except pyodbc.Error as e:
            # Błąd SQL Server
            print(f"Błąd SQL Server: {e}")
            return None

        except Exception as e:
            # Inny błąd
            print(f"Błąd podczas generowania raportu klientów: {e}")
            return None


    def save_report_to_excel(self, df, report_name):
        """
        Zapisuje raport DataFrame do pliku Excel z timestampem w dedykowanym katalogu.

        Args:
            df (pandas.DataFrame): DataFrame do zapisania
            report_name (str): Nazwa raportu (np. 'raport_sprzedazy')

        Returns:
            str: Pełna ścieżka do zapisanego pliku lub None jeśli błąd
        """

        try:
            # Sprawdzamy czy DataFrame nie jest pusty
            if df is None or df.empty:
                # DataFrame jest pusty - nie ma danych do zapisania
                print("Brak danych do zapisania.")
                return None

            # ========================================================
            # KROK 1: UTWORZENIE KATALOGU DLA RAPORTU
            # ========================================================

            # Tworzymy główny katalog 'raporty' jeśli nie istnieje
            # Ten katalog będzie zawierał podkatalogi dla każdego typu raportu
            main_reports_dir = "raporty"

            # Sprawdzamy czy katalog główny istnieje
            if not os.path.exists(main_reports_dir):
                # Jeśli nie istnieje - tworzymy go
                # os.makedirs tworzy katalog (wraz z katalogami nadrzędnymi jeśli potrzeba)
                os.makedirs(main_reports_dir)
                print(f"✓ Utworzono katalog główny: {main_reports_dir}")

            # Tworzymy podkatalog dla konkretnego typu raportu
            # Np. raporty/raport_sprzedazy/, raporty/raport_magazynowy/, etc.
            report_dir = os.path.join(main_reports_dir, report_name)

            # Sprawdzamy czy podkatalog istnieje
            if not os.path.exists(report_dir):
                # Tworzymy podkatalog dla tego typu raportu
                os.makedirs(report_dir)
                print(f"✓ Utworzono katalog: {report_dir}")

            # ========================================================
            # KROK 2: GENEROWANIE NAZWY PLIKU Z TIMESTAMPEM
            # ========================================================

            # Generujemy timestamp (znacznik czasu) w formacie YYYYMMDD_HHMMSS
            # datetime.now() - aktualna data i czas
            # strftime() - formatowanie daty do stringa
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Budujemy nazwę pliku: nazwa_raportu_timestamp.xlsx
            filename = f"{report_name}_{timestamp}.xlsx"

            # ========================================================
            # KROK 3: TWORZENIE PEŁNEJ ŚCIEŻKI DO PLIKU
            # ========================================================

            # Łączymy ścieżkę katalogu z nazwą pliku
            # os.path.join automatycznie używa odpowiedniego separatora (\ na Windows, / na Linux)
            # Przykład: raporty/raport_sprzedazy/raport_sprzedazy_20250116_123045.xlsx
            full_path = os.path.join(report_dir, filename)

            # ========================================================
            # KROK 4: ZAPIS DO PLIKU EXCEL
            # ========================================================

            # Zapisujemy DataFrame do pliku Excel w odpowiednim katalogu
            # index=False - nie zapisujemy indeksu DataFrame jako kolumny
            # engine='openpyxl' - używamy silnika openpyxl do zapisu .xlsx
            df.to_excel(full_path, index=False, engine='openpyxl')

            # Zwracamy pełną ścieżkę do zapisanego pliku
            return full_path

        except Exception as e:
            # Błąd podczas zapisywania pliku
            print(f"Błąd podczas zapisywania do Excel: {e}")
            return None


# ====================================================================
# SEKCJA 4: METODY MODUŁU SKLEPU
# ====================================================================

    def create_order(self, klient_id, produkt_id, ilosc):
        """
        Tworzy nowe zamówienie w bazie danych z obsługą transakcji.
        Sprawdza stan magazynowy i aktualizuje go atomowo.

        Args:
            klient_id (int): ID klienta składającego zamówienie
            produkt_id (int): ID zamawianego produktu
            ilosc (int): Ilość sztuk do zamówienia

        Returns:
            tuple: (bool, str) - (sukces, komunikat)
        """

        # Inicjalizujemy zmienną połączenia jako None
        conn = None

        try:
            # Nawiązujemy połączenie z bazą danych
            conn = pyodbc.connect(self.build_connection_string())

            # Wyłączamy autocommit - będziemy zarządzać transakcją ręcznie
            # Dzięki temu możemy zrobić ROLLBACK w razie błędu
            conn.autocommit = False

            # Tworzymy cursor
            cursor = conn.cursor()

            # ========================================================
            # KROK 1: SPRAWDZENIE STANU MAGAZYNOWEGO
            # ========================================================

            # Pobieramy aktualny stan magazynowy produktu
            cursor.execute("""
                SELECT stan_magazynowy, nazwa
                FROM produkty
                WHERE id = ?
            """, (produkt_id,))  # ? - parametr zapytania (zabezpieczenie)

            # Pobieramy wynik zapytania
            result = cursor.fetchone()

            # Sprawdzamy czy produkt istnieje
            if result is None:
                # Produkt nie istnieje w bazie
                return (False, "Produkt nie istnieje.")

            # Rozpakowujemy wynik do zmiennych
            stan_magazynowy = result[0]  # Pierwszy element tuple - stan
            nazwa_produktu = result[1]   # Drugi element tuple - nazwa

            # Sprawdzamy czy jest wystarczająca ilość na stanie
            if stan_magazynowy < ilosc:
                # Niewystarczający stan magazynowy
                return (False, f"Niewystarczający stan magazynowy. Dostępne: {stan_magazynowy} szt.")

            # ========================================================
            # KROK 2: POBRANIE AKTUALNEJ CENY
            # ========================================================

            # Pobieramy aktualną cenę produktu (obowiązującą dzisiaj)
            cursor.execute("""
                SELECT cena
                FROM ceny
                WHERE produkt_id = ?
                    -- Filtrujemy po datach (GETDATE() = dzisiaj)
                    AND GETDATE() BETWEEN data_od AND data_do
            """, (produkt_id,))

            # Pobieramy wynik
            cena_result = cursor.fetchone()

            # Sprawdzamy czy cena istnieje
            if cena_result is None:
                # Brak aktualnej ceny dla produktu
                return (False, "Brak aktualnej ceny dla tego produktu.")

            # Pobieramy cenę (pierwszy element tuple)
            cena_jednostkowa = cena_result[0]

            # ========================================================
            # KROK 3: UTWORZENIE ZAMÓWIENIA
            # ========================================================

            # INSERT - tworzymy nowy rekord w tabeli zamowienia
            cursor.execute("""
                INSERT INTO zamowienia (klient_id, produkt_id, ilosc, cena_jednostkowa)
                VALUES (?, ?, ?, ?)
            """, (
                klient_id,           # ID klienta
                produkt_id,          # ID produktu
                ilosc,               # Zamawiana ilość
                cena_jednostkowa     # Cena jednostkowa w momencie zamówienia
            ))

            # ========================================================
            # KROK 4: AKTUALIZACJA STANU MAGAZYNOWEGO
            # ========================================================

            # UPDATE - zmniejszamy stan magazynowy o zamówioną ilość
            cursor.execute("""
                UPDATE produkty
                SET stan_magazynowy = stan_magazynowy - ?
                WHERE id = ?
            """, (
                ilosc,      # O ile zmniejszamy stan
                produkt_id  # Dla którego produktu
            ))

            # ========================================================
            # KROK 5: ZATWIERDZENIE TRANSAKCJI (COMMIT)
            # ========================================================

            # Wszystko przebiegło pomyślnie - zatwierdzamy transakcję
            # COMMIT zapisuje zmiany w bazie danych
            conn.commit()

            # Zamykamy cursor
            cursor.close()

            # Zwracamy sukces z komunikatem
            return (True, f"Zamówienie zostało złożone pomyślnie!\nProdukt: {nazwa_produktu}\nIlość: {ilosc} szt.\nCena: {cena_jednostkowa} zł")

        except pyodbc.Error as e:
            # Błąd SQL Server - wycofujemy transakcję
            if conn:
                # ROLLBACK - cofa wszystkie zmiany (INSERT i UPDATE nie zostaną zapisane)
                conn.rollback()

            # Zwracamy błąd
            return (False, f"Błąd SQL Server: {e}")

        except Exception as e:
            # Inny błąd - również wycofujemy transakcję
            if conn:
                # ROLLBACK - cofa zmiany
                conn.rollback()

            # Zwracamy błąd
            return (False, f"Błąd podczas składania zamówienia: {e}")

        finally:
            # Blok finally - wykona się zawsze (nawet jeśli był błąd)
            # Zamykamy połączenie jeśli było otwarte
            if conn:
                conn.close()


    def get_customers(self):
        """
        Pobiera listę wszystkich klientów z bazy danych.

        Returns:
            list: Lista tuple (id, nazwa) lub pusta lista jeśli błąd
        """

        try:
            # Nawiązujemy połączenie
            conn = pyodbc.connect(self.build_connection_string())

            # Tworzymy cursor
            cursor = conn.cursor()

            # SELECT - pobieramy ID i nazwę wszystkich klientów
            cursor.execute("""
                SELECT id, nazwa
                FROM klienci
                ORDER BY nazwa
            """)

            # Pobieramy wszystkie wyniki jako listę tuple
            # fetchall() zwraca listę: [(1, 'Firma ABC'), (2, 'Jan Kowalski'), ...]
            customers = cursor.fetchall()

            # Zamykamy cursor
            cursor.close()

            # Zamykamy połączenie
            conn.close()

            # Zwracamy listę klientów
            return customers

        except Exception as e:
            # Błąd podczas pobierania klientów
            print(f"Błąd podczas pobierania klientów: {e}")
            # Zwracamy pustą listę
            return []


    def get_products(self):
        """
        Pobiera listę wszystkich produktów z aktualnymi cenami i stanami.

        Returns:
            list: Lista tuple (id, nazwa z ceną i stanem) lub pusta lista jeśli błąd
        """

        try:
            # Nawiązujemy połączenie
            conn = pyodbc.connect(self.build_connection_string())

            # Tworzymy cursor
            cursor = conn.cursor()

            # SELECT - pobieramy produkty z aktualnymi cenami
            cursor.execute("""
                SELECT
                    p.id,
                    -- Formatujemy wyświetlaną nazwę: "Nazwa produktu (cena zł, stan szt.)"
                    p.nazwa + ' (' +
                    CAST(ISNULL(c.cena, 0) AS NVARCHAR(20)) + ' zł, ' +
                    CAST(p.stan_magazynowy AS NVARCHAR(10)) + ' szt.)' as display_name
                FROM produkty p
                -- LEFT JOIN - pobieramy wszystkie produkty, nawet bez cen
                LEFT JOIN ceny c ON p.id = c.produkt_id
                    -- Tylko aktualne ceny (dzisiaj między data_od a data_do)
                    AND GETDATE() BETWEEN c.data_od AND c.data_do
                -- Sortowanie po nazwie produktu
                ORDER BY p.nazwa
            """)

            # Pobieramy wszystkie wyniki
            # Lista tuple: [(1, 'Laptop (4999 zł, 15 szt.)'), ...]
            products = cursor.fetchall()

            # Zamykamy cursor
            cursor.close()

            # Zamykamy połączenie
            conn.close()

            # Zwracamy listę produktów
            return products

        except Exception as e:
            # Błąd podczas pobierania produktów
            print(f"Błąd podczas pobierania produktów: {e}")
            # Zwracamy pustą listę
            return []


    def get_database_stats(self):
        """
        Pobiera statystyki bazy danych (liczby rekordów, wartości, top produkty).

        Returns:
            dict: Słownik ze statystykami lub None jeśli błąd
        """

        try:
            # Nawiązujemy połączenie
            conn = pyodbc.connect(self.build_connection_string())

            # Tworzymy cursor
            cursor = conn.cursor()

            # Inicjalizujemy słownik na statystyki
            stats = {}

            # ========================================================
            # STATYSTYKA 1: LICZBA KLIENTÓW
            # ========================================================

            # COUNT(*) - liczy wszystkie rekordy w tabeli
            cursor.execute("SELECT COUNT(*) FROM klienci")
            # fetchone()[0] - pobiera pierwszą wartość z pierwszego rekordu
            stats['liczba_klientow'] = cursor.fetchone()[0]

            # ========================================================
            # STATYSTYKA 2: LICZBA PRODUKTÓW
            # ========================================================

            cursor.execute("SELECT COUNT(*) FROM produkty")
            stats['liczba_produktow'] = cursor.fetchone()[0]

            # ========================================================
            # STATYSTYKA 3: LICZBA ZAMÓWIEŃ
            # ========================================================

            cursor.execute("SELECT COUNT(*) FROM zamowienia")
            stats['liczba_zamowien'] = cursor.fetchone()[0]

            # ========================================================
            # STATYSTYKA 4: ŁĄCZNA WARTOŚĆ ZAMÓWIEŃ
            # ========================================================

            # SUM - sumuje wartości (ilość × cena jednostkowa)
            # ISNULL - zamienia NULL na 0 (gdyby nie było zamówień)
            cursor.execute("""
                SELECT ISNULL(SUM(ilosc * cena_jednostkowa), 0)
                FROM zamowienia
            """)
            stats['laczna_wartosc_zamowien'] = cursor.fetchone()[0]

            # ========================================================
            # STATYSTYKA 5: WARTOŚĆ MAGAZYNU
            # ========================================================

            # SUM wartości wszystkich produktów (stan × cena)
            cursor.execute("""
                SELECT ISNULL(SUM(p.stan_magazynowy * c.cena), 0)
                FROM produkty p
                LEFT JOIN ceny c ON p.id = c.produkt_id
                    -- Tylko aktualne ceny
                    AND GETDATE() BETWEEN c.data_od AND c.data_do
            """)
            stats['wartosc_magazynu'] = cursor.fetchone()[0]

            # ========================================================
            # STATYSTYKA 6: TOP 3 NAJCZĘŚCIEJ KUPOWANE PRODUKTY
            # ========================================================

            # TOP 3 - SQL Server syntax dla limitowania wyników (zamiast LIMIT 3)
            cursor.execute("""
                SELECT TOP 3
                    p.nazwa,
                    SUM(z.ilosc) as suma_sprzedazy
                FROM zamowienia z
                INNER JOIN produkty p ON z.produkt_id = p.id
                -- GROUP BY - grupujemy po produkcie
                GROUP BY p.id, p.nazwa
                -- Sortujemy od największej sprzedaży
                ORDER BY suma_sprzedazy DESC
            """)

            # Pobieramy top 3 produkty jako listę tuple
            stats['top_produkty'] = cursor.fetchall()

            # Zamykamy cursor
            cursor.close()

            # Zamykamy połączenie
            conn.close()

            # Zwracamy słownik ze statystykami
            return stats

        except Exception as e:
            # Błąd podczas pobierania statystyk
            print(f"Błąd podczas pobierania statystyk: {e}")
            # Zwracamy None
            return None


# ====================================================================
# SEKCJA 5: INTERFEJS GRAFICZNY (GUI)
# ====================================================================

class ShopGUI:
    """
    Klasa interfejsu graficznego aplikacji sklepu.
    Używa biblioteki Tkinter do tworzenia okien i widgetów.
    """

    def __init__(self):
        """
        Konstruktor klasy GUI - tworzy główne okno i wszystkie zakładki.
        """

        # ========================================================
        # KROK 1: UTWORZENIE GŁÓWNEGO OKNA
        # ========================================================

        # Tworzymy główne okno aplikacji (root window)
        self.root = tk.Tk()

        # Ustawiamy tytuł okna (wyświetla się na pasku tytułowym)
        self.root.title("System Automatyzacji Raportów - SQL Server")

        # Ustawiamy rozmiar okna: szerokość x wysokość
        self.root.geometry("900x600")

        # ========================================================
        # KROK 2: UTWORZENIE SYSTEMU BACKEND
        # ========================================================

        # Tworzymy instancję klasy ReportAutomationSystem
        # To nasz backend - zarządza bazą danych i logiką biznesową
        self.system = ReportAutomationSystem()

        # ========================================================
        # KROK 3: UTWORZENIE ZAKŁADEK (NOTEBOOK)
        # ========================================================

        # Tworzymy widget Notebook - kontener na zakładki
        # ttk.Notebook - themed notebook (lepszy wygląd niż zwykły tk.Notebook)
        self.notebook = ttk.Notebook(self.root)

        # Umieszczamy notebook w oknie
        # pack() - automatyczne rozmieszczenie
        # fill=tk.BOTH - wypełnia całą dostępną przestrzeń
        # expand=True - rozszerza się gdy okno się powiększa
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # ========================================================
        # KROK 4: UTWORZENIE POSZCZEGÓLNYCH ZAKŁADEK
        # ========================================================

        # Tworzymy zakładkę "Raporty"
        self.create_reports_tab()

        # Tworzymy zakładkę "Sklep"
        self.create_shop_tab()

        # Tworzymy zakładkę "Baza danych"
        self.create_database_tab()


    def create_reports_tab(self):
        """
        Tworzy zakładkę "Raporty" z przyciskami do generowania raportów.
        """

        # Tworzymy Frame - kontener na widgety zakładki
        # Frame to podstawowy kontener w Tkinter
        tab = tk.Frame(self.notebook)

        # Dodajemy zakładkę do Notebook
        # text - nazwa zakładki wyświetlana na przycisku
        self.notebook.add(tab, text="📊 Raporty")

        # ========================================================
        # NAGŁÓWEK ZAKŁADKI
        # ========================================================

        # Tworzymy Label - etykietę tekstową (nagłówek)
        label = tk.Label(
            tab,                              # Parent - w którym kontenerze
            text="Generowanie Raportów",      # Tekst do wyświetlenia
            font=("Arial", 16, "bold")        # Czcionka: Arial, 16pt, pogrubiona
        )

        # Umieszczamy label w zakładce
        # pack() - automatyczne rozmieszczenie
        # pady=10 - padding (odstęp) 10 pikseli góra/dół
        label.pack(pady=10)

        # ========================================================
        # PRZYCISKI RAPORTÓW
        # ========================================================

        # Przycisk "Raport Sprzedaży"
        btn_sales = tk.Button(
            tab,                                    # Parent
            text="📊 Raport Sprzedaży",             # Tekst na przycisku (z emoji)
            font=("Arial", 12),                     # Czcionka
            command=self.show_sales_report,         # Funkcja wywoływana po kliknięciu
            bg="#4CAF50",                           # Kolor tła (zielony)
            fg="white",                             # Kolor tekstu (biały)
            width=30,                               # Szerokość przycisku (w znakach)
            height=2                                # Wysokość przycisku (w liniach)
        )
        # Umieszczamy przycisk
        # pady=5 - odstęp 5 pikseli góra/dół
        btn_sales.pack(pady=5)

        # Przycisk "Raport Magazynowy"
        btn_inventory = tk.Button(
            tab,
            text="📦 Raport Magazynowy",
            font=("Arial", 12),
            command=self.show_inventory_report,     # Inna funkcja callback
            bg="#2196F3",                           # Kolor niebieski
            fg="white",
            width=30,
            height=2
        )
        btn_inventory.pack(pady=5)

        # Przycisk "Raport Klientów"
        btn_customers = tk.Button(
            tab,
            text="👥 Raport Klientów",
            font=("Arial", 12),
            command=self.show_customer_report,      # Inna funkcja callback
            bg="#FF9800",                           # Kolor pomarańczowy
            fg="white",
            width=30,
            height=2
        )
        btn_customers.pack(pady=5)

        # ========================================================
        # OBSZAR PODGLĄDU RAPORTU
        # ========================================================

        # Label nad obszarem podglądu
        preview_label = tk.Label(
            tab,
            text="Podgląd raportu:",
            font=("Arial", 10)
        )
        preview_label.pack(pady=(20, 5))  # pady - tuple: (góra, dół)

        # Frame na Text widget i Scrollbar
        # Potrzebujemy Frame aby połączyć Text ze Scrollbarem
        text_frame = tk.Frame(tab)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Tworzymy Scrollbar - pasek przewijania
        scrollbar = tk.Scrollbar(text_frame)

        # Umieszczamy scrollbar po prawej stronie
        # side=tk.RIGHT - po prawej
        # fill=tk.Y - wypełnia w pionie
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Tworzymy Text widget - wieloliniowe pole tekstowe
        self.report_text = tk.Text(
            text_frame,                         # Parent
            wrap=tk.WORD,                       # Zawijanie tekstu po słowach (nie po znakach)
            font=("Courier", 9),                # Czcionka monospace (dla tabel)
            yscrollcommand=scrollbar.set        # Połączenie ze scrollbarem
        )

        # Umieszczamy Text widget
        # fill=tk.BOTH - wypełnia całą przestrzeń
        # expand=True - rozszerza się
        self.report_text.pack(fill=tk.BOTH, expand=True)

        # Konfigurujemy scrollbar aby kontrolował Text widget
        # yview - metoda Text widget do przewijania
        scrollbar.config(command=self.report_text.yview)


    def create_shop_tab(self):
        """
        Tworzy zakładkę "Sklep" z formularzem składania zamówień.
        """

        # Tworzymy Frame dla zakładki
        tab = tk.Frame(self.notebook)

        # Dodajemy zakładkę do Notebook
        self.notebook.add(tab, text="🛒 Sklep")

        # ========================================================
        # NAGŁÓWEK
        # ========================================================

        label = tk.Label(
            tab,
            text="Składanie Zamówień",
            font=("Arial", 16, "bold")
        )
        label.pack(pady=10)

        # ========================================================
        # FORMULARZ ZAMÓWIENIA
        # ========================================================

        # Frame na formularz (dla lepszego layoutu)
        form_frame = tk.Frame(tab)
        form_frame.pack(pady=20)

        # --------------------------------------------------------
        # POLE 1: WYBÓR KLIENTA
        # --------------------------------------------------------

        # Label "Klient:"
        tk.Label(
            form_frame,
            text="Klient:",
            font=("Arial", 12)
        ).grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        # grid() - układanie w siatce (row, column)
        # sticky=tk.W - wyrównanie do lewej (West)
        # padx - padding poziomy

        # Combobox - lista rozwijana do wyboru klienta
        self.customer_combo = ttk.Combobox(
            form_frame,
            state="readonly",    # readonly - użytkownik może tylko wybierać, nie pisać
            width=40             # szerokość w znakach
        )
        # Umieszczamy w siatce: wiersz 0, kolumna 1
        self.customer_combo.grid(row=0, column=1, padx=10, pady=5)

        # --------------------------------------------------------
        # POLE 2: WYBÓR PRODUKTU
        # --------------------------------------------------------

        tk.Label(
            form_frame,
            text="Produkt:",
            font=("Arial", 12)
        ).grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

        # Combobox do wyboru produktu
        self.product_combo = ttk.Combobox(
            form_frame,
            state="readonly",
            width=40
        )
        self.product_combo.grid(row=1, column=1, padx=10, pady=5)

        # --------------------------------------------------------
        # POLE 3: ILOŚĆ
        # --------------------------------------------------------

        tk.Label(
            form_frame,
            text="Ilość:",
            font=("Arial", 12)
        ).grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)

        # Spinbox - pole numeryczne z przyciskami +/-
        self.quantity_spin = tk.Spinbox(
            form_frame,
            from_=1,        # Minimalna wartość
            to=100,         # Maksymalna wartość
            increment=1,    # Krok zmiany wartości
            width=10        # Szerokość
        )
        self.quantity_spin.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)

        # ========================================================
        # PRZYCISKI AKCJI
        # ========================================================

        # Frame na przyciski
        button_frame = tk.Frame(tab)
        button_frame.pack(pady=10)

        # Przycisk "Złóż zamówienie"
        btn_order = tk.Button(
            button_frame,
            text="🛒 Złóż zamówienie",
            font=("Arial", 12, "bold"),
            command=self.place_order,     # Funkcja wywoływana po kliknięciu
            bg="#4CAF50",                 # Zielony
            fg="white",
            width=20,
            height=2
        )
        btn_order.pack(side=tk.LEFT, padx=5)  # side=tk.LEFT - obok siebie

        # Przycisk "Odśwież dane"
        btn_refresh = tk.Button(
            button_frame,
            text="🔄 Odśwież dane",
            font=("Arial", 12),
            command=self.refresh_data,    # Funkcja wywoływana po kliknięciu
            bg="#2196F3",                 # Niebieski
            fg="white",
            width=20,
            height=2
        )
        btn_refresh.pack(side=tk.LEFT, padx=5)

        # ========================================================
        # POCZĄTKOWE ZAŁADOWANIE DANYCH
        # ========================================================

        # Ładujemy klientów i produkty do Combobox-ów
        self.load_customers()
        self.load_products()


    def create_database_tab(self):
        """
        Tworzy zakładkę "Baza danych" ze statystykami.
        """

        # Tworzymy Frame dla zakładki
        tab = tk.Frame(self.notebook)

        # Dodajemy zakładkę do Notebook
        self.notebook.add(tab, text="💾 Baza danych")

        # ========================================================
        # NAGŁÓWEK
        # ========================================================

        label = tk.Label(
            tab,
            text="Informacje o Bazie Danych (SQL Server)",
            font=("Arial", 16, "bold")
        )
        label.pack(pady=10)

        # ========================================================
        # PRZYCISK ODŚWIEŻ
        # ========================================================

        btn_refresh = tk.Button(
            tab,
            text="🔄 Odśwież statystyki",
            font=("Arial", 12),
            command=self.load_stats,      # Funkcja do odświeżania statystyk
            bg="#2196F3",
            fg="white",
            width=20
        )
        btn_refresh.pack(pady=10)

        # ========================================================
        # OBSZAR WYŚWIETLANIA STATYSTYK
        # ========================================================

        # Frame na Text widget i Scrollbar
        text_frame = tk.Frame(tab)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Scrollbar
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text widget na statystyki
        self.stats_text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            font=("Courier", 11),
            yscrollcommand=scrollbar.set
        )
        self.stats_text.pack(fill=tk.BOTH, expand=True)

        # Konfiguracja scrollbar
        scrollbar.config(command=self.stats_text.yview)

        # ========================================================
        # POCZĄTKOWE ZAŁADOWANIE STATYSTYK
        # ========================================================

        # Ładujemy statystyki przy otwarciu zakładki
        self.load_stats()


# ====================================================================
# SEKCJA 6: METODY CALLBACK GUI (OBSŁUGA ZDARZEŃ)
# ====================================================================

    def show_sales_report(self):
        """
        Obsługa kliknięcia przycisku "Raport Sprzedaży".
        Generuje raport, wyświetla w GUI i zapisuje do Excel.
        """

        # Wywołujemy metodę backend generującą raport
        df = self.system.generate_sales_report()

        # Sprawdzamy czy raport został wygenerowany poprawnie
        if df is not None and not df.empty:
            # ========================================================
            # KROK 1: WYŚWIETLENIE W TEXT WIDGET
            # ========================================================

            # Czyścimy zawartość Text widget
            # "1.0" - początek (wiersz 1, znak 0)
            # tk.END - koniec
            self.report_text.delete("1.0", tk.END)

            # Konwertujemy DataFrame do czytelnego stringa
            # to_string() - formatuje DataFrame jako tabelę tekstową
            report_str = df.to_string(index=False)

            # Wstawiamy tekst do Text widget
            # "1.0" - na początku
            self.report_text.insert("1.0", report_str)

            # ========================================================
            # KROK 2: ZAPIS DO EXCEL
            # ========================================================

            # Zapisujemy raport do pliku Excel
            filename = self.system.save_report_to_excel(df, "raport_sprzedazy")

            # Sprawdzamy czy zapis się powiódł
            if filename:
                # Wyświetlamy okno dialogowe z potwierdzeniem
                # showinfo - ikona informacji
                messagebox.showinfo(
                    "Sukces",                                    # Tytuł okna
                    f"Raport zapisany jako:\n{filename}"         # Treść komunikatu
                )
        else:
            # Brak danych lub błąd
            # showwarning - ikona ostrzeżenia
            messagebox.showwarning(
                "Uwaga",
                "Brak zamówień do wyświetlenia lub wystąpił błąd."
            )


    def show_inventory_report(self):
        """
        Obsługa kliknięcia przycisku "Raport Magazynowy".
        """

        # Generujemy raport magazynowy
        df = self.system.generate_inventory_report()

        # Sprawdzamy wynik
        if df is not None and not df.empty:
            # Czyścimy Text widget
            self.report_text.delete("1.0", tk.END)

            # Konwertujemy DataFrame do stringa i wyświetlamy
            self.report_text.insert("1.0", df.to_string(index=False))

            # Zapisujemy do Excel
            filename = self.system.save_report_to_excel(df, "raport_magazynowy")

            # Komunikat o sukcesie
            if filename:
                messagebox.showinfo(
                    "Sukces",
                    f"Raport zapisany jako:\n{filename}"
                )
        else:
            # Komunikat ostrzegawczy
            messagebox.showwarning(
                "Uwaga",
                "Brak produktów do wyświetlenia lub wystąpił błąd."
            )


    def show_customer_report(self):
        """
        Obsługa kliknięcia przycisku "Raport Klientów".
        """

        # Generujemy raport klientów
        df = self.system.generate_customer_report()

        # Sprawdzamy wynik
        if df is not None and not df.empty:
            # Czyścimy Text widget
            self.report_text.delete("1.0", tk.END)

            # Wyświetlamy raport
            self.report_text.insert("1.0", df.to_string(index=False))

            # Zapisujemy do Excel
            filename = self.system.save_report_to_excel(df, "raport_klientow")

            # Komunikat o sukcesie
            if filename:
                messagebox.showinfo(
                    "Sukces",
                    f"Raport zapisany jako:\n{filename}"
                )
        else:
            # Komunikat ostrzegawczy
            messagebox.showwarning(
                "Uwaga",
                "Brak klientów do wyświetlenia lub wystąpił błąd."
            )


    def place_order(self):
        """
        Obsługa kliknięcia przycisku "Złóż zamówienie".
        Waliduje dane i tworzy zamówienie w bazie.
        """

        # ========================================================
        # KROK 1: POBRANIE WARTOŚCI Z FORMULARZA
        # ========================================================

        # Pobieramy aktualnie wybrany tekst z Combobox klienta
        # get() - zwraca aktualnie wybraną wartość
        customer_selection = self.customer_combo.get()

        # Pobieramy wybrany produkt
        product_selection = self.product_combo.get()

        # Pobieramy ilość ze Spinbox
        # get() - zwraca string, musimy przekonwertować na int
        try:
            quantity = int(self.quantity_spin.get())
        except ValueError:
            # Jeśli użytkownik wpisał niepoprawną wartość
            messagebox.showerror("Błąd", "Niepoprawna ilość.")
            return

        # ========================================================
        # KROK 2: WALIDACJA WYBORÓW
        # ========================================================

        # Sprawdzamy czy użytkownik wybrał klienta
        if not customer_selection:
            # Brak wyboru - wyświetlamy błąd
            messagebox.showerror("Błąd", "Proszę wybrać klienta.")
            return  # Przerywamy funkcję

        # Sprawdzamy czy użytkownik wybrał produkt
        if not product_selection:
            messagebox.showerror("Błąd", "Proszę wybrać produkt.")
            return

        # ========================================================
        # KROK 3: EKSTRAKCJA ID Z WYBORÓW
        # ========================================================

        # Wyciągamy ID klienta z tekstu Combobox
        # Format: "ID - Nazwa" np. "1 - Firma ABC"
        # split(" - ")[0] - bierzemy część przed " - " (czyli ID)
        try:
            customer_id = int(customer_selection.split(" - ")[0])
        except (ValueError, IndexError):
            messagebox.showerror("Błąd", "Niepoprawny format klienta.")
            return

        # Wyciągamy ID produktu
        # Format: "ID - Nazwa (cena, stan)" np. "1 - Laptop (4999 zł, 15 szt.)"
        try:
            product_id = int(product_selection.split(" - ")[0])
        except (ValueError, IndexError):
            messagebox.showerror("Błąd", "Niepoprawny format produktu.")
            return

        # ========================================================
        # KROK 4: UTWORZENIE ZAMÓWIENIA
        # ========================================================

        # Wywołujemy metodę backend do utworzenia zamówienia
        # Zwraca tuple: (bool sukces, str komunikat)
        success, message = self.system.create_order(customer_id, product_id, quantity)

        # ========================================================
        # KROK 5: WYŚWIETLENIE WYNIKU
        # ========================================================

        # Sprawdzamy czy operacja się powiodła
        if success:
            # Sukces - zielone okno informacyjne
            messagebox.showinfo("Sukces", message)

            # Odświeżamy listy produktów (bo zmienił się stan magazynowy)
            self.load_products()

        else:
            # Błąd - czerwone okno błędu
            messagebox.showerror("Błąd", message)


    def load_customers(self):
        """
        Ładuje listę klientów z bazy do Combobox.
        """

        # Pobieramy listę klientów z backend
        # Zwraca listę tuple: [(1, 'Firma ABC'), (2, 'Jan Kowalski'), ...]
        customers = self.system.get_customers()

        # Sprawdzamy czy lista nie jest pusta
        if customers:
            # Formatujemy listę do wyświetlenia w Combobox
            # Format: "ID - Nazwa"
            # List comprehension: [f"{id} - {nazwa}" for id, nazwa in customers]
            customer_list = [f"{id} - {nazwa}" for id, nazwa in customers]

            # Ustawiamy wartości w Combobox
            # values - lista opcji do wyboru
            self.customer_combo['values'] = customer_list


    def load_products(self):
        """
        Ładuje listę produktów z bazy do Combobox.
        """

        # Pobieramy listę produktów z backend
        # Zwraca: [(1, 'Laptop (4999 zł, 15 szt.)'), ...]
        products = self.system.get_products()

        # Sprawdzamy czy lista nie jest pusta
        if products:
            # Formatujemy: "ID - Nazwa (cena, stan)"
            product_list = [f"{id} - {display}" for id, display in products]

            # Ustawiamy w Combobox
            self.product_combo['values'] = product_list


    def refresh_data(self):
        """
        Odświeża listy klientów i produktów (po kliknięciu przycisku).
        """

        # Przeładowujemy klientów
        self.load_customers()

        # Przeładowujemy produkty
        self.load_products()

        # Wyświetlamy komunikat potwierdzający
        messagebox.showinfo("Sukces", "Dane zostały odświeżone.")


    def load_stats(self):
        """
        Ładuje i wyświetla statystyki bazy danych.
        """

        # Pobieramy statystyki z backend
        # Zwraca słownik lub None
        stats = self.system.get_database_stats()

        # Sprawdzamy czy statystyki zostały pobrane
        if stats:
            # ========================================================
            # FORMATOWANIE STATYSTYK DO WYŚWIETLENIA
            # ========================================================

            # Budujemy string ze statystykami
            stats_str = "=" * 60 + "\n"
            stats_str += "STATYSTYKI BAZY DANYCH\n"
            stats_str += "=" * 60 + "\n\n"

            # Liczba klientów
            stats_str += f"📊 Liczba klientów:        {stats['liczba_klientow']}\n"

            # Liczba produktów
            stats_str += f"📦 Liczba produktów:       {stats['liczba_produktow']}\n"

            # Liczba zamówień
            stats_str += f"🛒 Liczba zamówień:        {stats['liczba_zamowien']}\n\n"

            # Łączna wartość zamówień (formatujemy z 2 miejscami po przecinku)
            stats_str += f"💰 Łączna wartość zamówień: {stats['laczna_wartosc_zamowien']:.2f} zł\n"

            # Wartość magazynu
            stats_str += f"💼 Wartość magazynu:        {stats['wartosc_magazynu']:.2f} zł\n\n"

            # Separator
            stats_str += "=" * 60 + "\n"
            stats_str += "TOP 3 NAJCZĘŚCIEJ KUPOWANE PRODUKTY\n"
            stats_str += "=" * 60 + "\n\n"

            # Sprawdzamy czy są top produkty
            if stats['top_produkty']:
                # Iterujemy po liście top produktów
                # enumerate() - dodaje indeks (0, 1, 2...)
                for idx, (nazwa, suma) in enumerate(stats['top_produkty'], 1):
                    # idx+1 aby numerować od 1, nie od 0
                    stats_str += f"{idx}. {nazwa}: {suma} szt.\n"
            else:
                # Brak zamówień
                stats_str += "Brak danych o zamówieniach.\n"

            # ========================================================
            # WYŚWIETLENIE W TEXT WIDGET
            # ========================================================

            # Czyścimy Text widget
            self.stats_text.delete("1.0", tk.END)

            # Wstawiamy sformatowane statystyki
            self.stats_text.insert("1.0", stats_str)

        else:
            # Błąd pobierania statystyk
            messagebox.showerror(
                "Błąd",
                "Nie udało się pobrać statystyk z bazy danych."
            )


    def run(self):
        """
        Uruchamia główną pętlę GUI (event loop).
        Ta metoda blokuje program do czasu zamknięcia okna.
        """

        # mainloop() - główna pętla zdarzeń Tkinter
        # Czeka na akcje użytkownika (kliknięcia, wpisywanie tekstu, etc.)
        # Kończy się gdy użytkownik zamknie okno
        self.root.mainloop()


# ====================================================================
# SEKCJA 7: PUNKT STARTOWY APLIKACJI
# ====================================================================

if __name__ == "__main__":
    """
    Punkt wejścia programu.
    __name__ == "__main__" - wykonuje się tylko gdy plik uruchamiany bezpośrednio
    (nie gdy importowany jako moduł)
    """

    # Wyświetlamy komunikat startowy
    print("=" * 60)
    print("System Automatyzacji Raportów - SQL Server")
    print("Wersja 2.0")
    print("=" * 60)
    print()

    # Tworzymy instancję GUI
    app = ShopGUI()

    # Uruchamiamy aplikację (blokuje do czasu zamknięcia okna)
    app.run()

    # Po zamknięciu okna
    print("\nAplikacja zakończona.")
    print("Dziękujemy za używanie systemu!")

# ====================================================================
# KONIEC PLIKU
# ====================================================================
