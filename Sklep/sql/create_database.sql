-- ====================================================================
-- SKRYPT RĘCZNEGO TWORZENIA BAZY DANYCH
-- ====================================================================
-- Ten skrypt można wykonać w SQL Server Management Studio (SSMS)
-- aby ręcznie utworzyć bazę danych i tabele.
--
-- UWAGA: Aplikacja Python tworzy bazę automatycznie!
-- Ten skrypt jest potrzebny tylko jeśli chcesz utworzyć bazę ręcznie.
-- ====================================================================

-- ====================================================================
-- KROK 1: UTWORZENIE BAZY DANYCH
-- ====================================================================

-- Sprawdzamy czy baza już istnieje
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'SklepDB')
BEGIN
    -- Jeśli nie istnieje - tworzymy nową bazę danych
    CREATE DATABASE SklepDB

    -- Wyświetlamy komunikat
    PRINT 'Baza danych SklepDB została utworzona.'
END
ELSE
BEGIN
    -- Jeśli już istnieje - informujemy o tym
    PRINT 'Baza danych SklepDB już istnieje.'
END
GO

-- ====================================================================
-- KROK 2: PRZEŁĄCZAMY SIĘ NA NASZĄ BAZĘ DANYCH
-- ====================================================================

-- Wszystkie kolejne polecenia będą wykonywane w kontekście SklepDB
USE SklepDB
GO

-- ====================================================================
-- KROK 3: UTWORZENIE TABELI 'klienci'
-- ====================================================================

-- Sprawdzamy czy tabela już istnieje
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'klienci')
BEGIN
    -- Tworzymy tabelę klienci
    CREATE TABLE klienci (
        -- id - klucz główny, automatycznie inkrementowany
        -- IDENTITY(1,1) - zaczyna od 1, zwiększa o 1
        id INT IDENTITY(1,1) PRIMARY KEY,

        -- nazwa - nazwa klienta lub firmy
        -- NVARCHAR - typ tekstowy Unicode (wspiera polskie znaki: ą, ę, ł, ć, etc.)
        -- NOT NULL - pole wymagane, nie może być puste
        nazwa NVARCHAR(255) NOT NULL,

        -- email - adres email klienta
        -- NULL dozwolone - pole opcjonalne
        email NVARCHAR(255),

        -- telefon - numer telefonu
        telefon NVARCHAR(50),

        -- adres - pełny adres pocztowy
        adres NVARCHAR(500)
    )

    -- Komunikat o utworzeniu tabeli
    PRINT 'Tabela klienci została utworzona.'
END
ELSE
BEGIN
    -- Tabela już istnieje
    PRINT 'Tabela klienci już istnieje.'
END
GO

-- ====================================================================
-- KROK 4: UTWORZENIE TABELI 'produkty'
-- ====================================================================

-- Sprawdzamy czy tabela już istnieje
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'produkty')
BEGIN
    -- Tworzymy tabelę produkty
    CREATE TABLE produkty (
        -- id - klucz główny, auto-increment
        id INT IDENTITY(1,1) PRIMARY KEY,

        -- nazwa - nazwa produktu
        -- NVARCHAR dla polskich znaków
        nazwa NVARCHAR(255) NOT NULL,

        -- kategoria - kategoria produktu (np. Elektronika, Audio, Akcesoria)
        kategoria NVARCHAR(100),

        -- opis - szczegółowy opis produktu
        opis NVARCHAR(1000),

        -- stan_magazynowy - ile sztuk produktu jest w magazynie
        -- INT - liczba całkowita
        -- DEFAULT 0 - wartość domyślna to 0 jeśli nie podano innej
        stan_magazynowy INT DEFAULT 0
    )

    PRINT 'Tabela produkty została utworzona.'
END
ELSE
BEGIN
    PRINT 'Tabela produkty już istnieje.'
END
GO

-- ====================================================================
-- KROK 5: UTWORZENIE TABELI 'ceny'
-- ====================================================================

-- Sprawdzamy czy tabela już istnieje
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'ceny')
BEGIN
    -- Tworzymy tabelę ceny
    CREATE TABLE ceny (
        -- id - klucz główny
        id INT IDENTITY(1,1) PRIMARY KEY,

        -- produkt_id - odniesienie do tabeli produkty
        -- Przechowuje ID produktu dla którego określamy cenę
        produkt_id INT,

        -- cena - wartość ceny produktu
        -- DECIMAL(10,2) - liczba dziesiętna z 10 cyframi łącznie i 2 po przecinku
        -- Przykład: 1234.56 lub 99999999.99
        -- DECIMAL zapewnia dokładność (w przeciwieństwie do FLOAT)
        cena DECIMAL(10,2) NOT NULL,

        -- data_od - od kiedy cena obowiązuje
        -- DATE - tylko data (bez godziny)
        data_od DATE,

        -- data_do - do kiedy cena obowiązuje
        data_do DATE,

        -- FOREIGN KEY - klucz obcy
        -- Łączy tabelę ceny z tabelą produkty
        -- Zapewnia integralność danych - nie można dodać ceny dla nieistniejącego produktu
        FOREIGN KEY (produkt_id) REFERENCES produkty(id)
    )

    PRINT 'Tabela ceny została utworzona.'
END
ELSE
BEGIN
    PRINT 'Tabela ceny już istnieje.'
END
GO

-- ====================================================================
-- KROK 6: UTWORZENIE TABELI 'zamowienia'
-- ====================================================================

-- Sprawdzamy czy tabela już istnieje
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'zamowienia')
BEGIN
    -- Tworzymy tabelę zamowienia
    CREATE TABLE zamowienia (
        -- id - klucz główny
        id INT IDENTITY(1,1) PRIMARY KEY,

        -- klient_id - ID klienta który złożył zamówienie
        klient_id INT,

        -- produkt_id - ID zamówionego produktu
        produkt_id INT,

        -- ilosc - ile sztuk produktu zamówiono
        ilosc INT,

        -- cena_jednostkowa - cena za 1 sztukę w momencie składania zamówienia
        -- Zapisujemy cenę w zamówieniu aby zachować historyczną wartość
        -- (cena w tabeli ceny może się zmienić, ale zamówienie musi pamiętać starą cenę)
        cena_jednostkowa DECIMAL(10,2),

        -- data_zamowienia - kiedy zamówienie zostało złożone
        -- DATETIME - data i godzina
        -- DEFAULT GETDATE() - automatycznie ustawia aktualną datę i czas przy INSERT
        data_zamowienia DATETIME DEFAULT GETDATE(),

        -- status - status zamówienia (np. 'nowe', 'wysłane', 'dostarczone', 'anulowane')
        -- DEFAULT 'nowe' - nowe zamówienia domyślnie mają status 'nowe'
        status NVARCHAR(50) DEFAULT 'nowe',

        -- FOREIGN KEY - łączy z tabelą klienci
        -- Zapewnia że zamówienie może być tylko dla istniejącego klienta
        FOREIGN KEY (klient_id) REFERENCES klienci(id),

        -- FOREIGN KEY - łączy z tabelą produkty
        -- Zapewnia że zamówienie może być tylko dla istniejącego produktu
        FOREIGN KEY (produkt_id) REFERENCES produkty(id)
    )

    PRINT 'Tabela zamowienia została utworzona.'
END
ELSE
BEGIN
    PRINT 'Tabela zamowienia już istnieje.'
END
GO

-- ====================================================================
-- KROK 7: WYPEŁNIENIE PRZYKŁADOWYMI DANYMI
-- ====================================================================

-- Sprawdzamy czy tabela klienci jest pusta
-- COUNT(*) zlicza liczbę rekordów
IF (SELECT COUNT(*) FROM klienci) = 0
BEGIN
    -- Tabela jest pusta - dodajemy przykładowe dane

    PRINT 'Dodawanie przykładowych klientów...'

    -- ================================================================
    -- INSERT - wstawianie nowych rekordów do tabeli
    -- ================================================================

    -- Klient 1: Firma ABC
    INSERT INTO klienci (nazwa, email, telefon, adres)
    VALUES (
        'Firma ABC Sp. z o.o.',              -- nazwa
        'kontakt@abc.pl',                    -- email
        '+48 123 456 789',                   -- telefon
        'ul. Przykładowa 1, 00-001 Warszawa' -- adres
    )

    -- Klient 2: Jan Kowalski
    INSERT INTO klienci (nazwa, email, telefon, adres)
    VALUES (
        'Jan Kowalski',
        'jan.kowalski@email.pl',
        '+48 987 654 321',
        'ul. Testowa 5, 30-001 Kraków'
    )

    -- Klient 3: Hurtownia XYZ
    INSERT INTO klienci (nazwa, email, telefon, adres)
    VALUES (
        'Hurtownia XYZ',
        'biuro@xyz.com',
        '+48 555 123 456',
        'ul. Handlowa 10, 50-001 Wrocław'
    )

    PRINT 'Dodano 3 przykładowych klientów.'

    -- ================================================================
    -- PRODUKTY
    -- ================================================================

    PRINT 'Dodawanie przykładowych produktów...'

    -- Produkt 1: Laptop
    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
    VALUES (
        'Laptop Dell XPS 15',                           -- nazwa
        'Elektronika',                                  -- kategoria
        'Wysokowydajny laptop do pracy i rozrywki',     -- opis
        15                                              -- stan (15 sztuk)
    )

    -- Produkt 2: Monitor
    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
    VALUES (
        'Monitor Samsung 27"',
        'Elektronika',
        'Monitor LED 27 cali Full HD',
        25
    )

    -- Produkt 3: Klawiatura
    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
    VALUES (
        'Klawiatura mechaniczna',
        'Akcesoria',
        'Klawiatura mechaniczna z podświetleniem RGB',
        50
    )

    -- Produkt 4: Mysz
    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
    VALUES (
        'Mysz bezprzewodowa',
        'Akcesoria',
        'Mysz optyczna bezprzewodowa 2.4GHz',
        100
    )

    -- Produkt 5: Słuchawki
    INSERT INTO produkty (nazwa, kategoria, opis, stan_magazynowy)
    VALUES (
        'Słuchawki Sony WH-1000XM4',
        'Audio',
        'Słuchawki bezprzewodowe z redukcją szumów',
        30
    )

    PRINT 'Dodano 5 przykładowych produktów.'

    -- ================================================================
    -- CENY PRODUKTÓW
    -- ================================================================

    PRINT 'Dodawanie cen dla produktów...'

    -- Produkty mają ID od 1 do 5 (IDENTITY zaczyna od 1)

    -- Cena dla Laptopa (produkt_id = 1)
    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
    VALUES (
        1,              -- ID produktu (Laptop)
        4999.00,        -- cena w PLN
        '2025-01-01',   -- obowiązuje od 1 stycznia 2025
        '2025-12-31'    -- obowiązuje do 31 grudnia 2025
    )

    -- Cena dla Monitora (produkt_id = 2)
    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
    VALUES (2, 1299.00, '2025-01-01', '2025-12-31')

    -- Cena dla Klawiatury (produkt_id = 3)
    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
    VALUES (3, 449.00, '2025-01-01', '2025-12-31')

    -- Cena dla Myszy (produkt_id = 4)
    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
    VALUES (4, 129.00, '2025-01-01', '2025-12-31')

    -- Cena dla Słuchawek (produkt_id = 5)
    INSERT INTO ceny (produkt_id, cena, data_od, data_do)
    VALUES (5, 1499.00, '2025-01-01', '2025-12-31')

    PRINT 'Dodano ceny dla wszystkich produktów.'
    PRINT 'Baza danych została pomyślnie zainicjalizowana!'
END
ELSE
BEGIN
    -- Tabela klienci nie jest pusta - dane już istnieją
    PRINT 'Baza zawiera już dane. Pomijam dodawanie przykładowych rekordów.'
END
GO

-- ====================================================================
-- KROK 8: WERYFIKACJA - WYŚWIETLENIE PODSUMOWANIA
-- ====================================================================

PRINT ''
PRINT '===================================================================='
PRINT 'PODSUMOWANIE BAZY DANYCH'
PRINT '===================================================================='
PRINT ''

-- Zliczamy klientów
DECLARE @liczba_klientow INT
SELECT @liczba_klientow = COUNT(*) FROM klienci
PRINT 'Liczba klientów: ' + CAST(@liczba_klientow AS NVARCHAR(10))

-- Zliczamy produkty
DECLARE @liczba_produktow INT
SELECT @liczba_produktow = COUNT(*) FROM produkty
PRINT 'Liczba produktów: ' + CAST(@liczba_produktow AS NVARCHAR(10))

-- Zliczamy ceny
DECLARE @liczba_cen INT
SELECT @liczba_cen = COUNT(*) FROM ceny
PRINT 'Liczba rekordów cenowych: ' + CAST(@liczba_cen AS NVARCHAR(10))

-- Zliczamy zamówienia
DECLARE @liczba_zamowien INT
SELECT @liczba_zamowien = COUNT(*) FROM zamowienia
PRINT 'Liczba zamówień: ' + CAST(@liczba_zamowien AS NVARCHAR(10))

PRINT ''
PRINT 'Baza danych SklepDB jest gotowa do użycia!'
PRINT '===================================================================='
GO

-- ====================================================================
-- KONIEC SKRYPTU
-- ====================================================================
--
-- INSTRUKCJA UŻYCIA:
-- 1. Otwórz SQL Server Management Studio (SSMS)
-- 2. Połącz się z instancją SQL Server
-- 3. Otwórz ten plik (File → Open → File)
-- 4. Kliknij "Execute" (F5) lub przycisk ▶
-- 5. Sprawdź Messages - powinny pojawić się komunikaty o utworzeniu tabel
--
-- WERYFIKACJA:
-- Po wykonaniu skryptu możesz sprawdzić dane:
--
-- SELECT * FROM klienci
-- SELECT * FROM produkty
-- SELECT * FROM ceny
-- SELECT * FROM zamowienia
--
-- ====================================================================
