-- ====================================================================
-- SKRYPT TWORZENIA INDEKSÓW DLA OPTYMALIZACJI WYDAJNOŚCI
-- ====================================================================
-- Ten skrypt tworzy indeksy na kluczowych kolumnach aby przyspieszyć
-- zapytania SQL używane w aplikacji.
--
-- KIEDY WYKONAĆ:
-- - Po utworzeniu bazy danych i tabel
-- - Gdy baza zawiera dużo danych (1000+ rekordów)
-- - Gdy zauważysz spowolnienie raportów
--
-- UWAGA: Indeksy przyspieszają SELECT, ale spowalniają INSERT/UPDATE
-- W małych bazach (<10000 rekordów) różnica może być niewyczuwalna
-- ====================================================================

-- ====================================================================
-- KROK 1: PRZEŁĄCZAMY SIĘ NA BAZĘ DANYCH
-- ====================================================================

-- Upewniamy się że pracujemy na właściwej bazie
USE SklepDB
GO

PRINT '===================================================================='
PRINT 'TWORZENIE INDEKSÓW DLA OPTYMALIZACJI WYDAJNOŚCI'
PRINT '===================================================================='
PRINT ''

-- ====================================================================
-- KROK 2: INDEKSY DLA TABELI 'zamowienia'
-- ====================================================================

-- --------------------------------------------------------------------
-- INDEKS 1: idx_zamowienia_data
-- --------------------------------------------------------------------
-- CEL: Przyspieszenie sortowania zamówień po dacie (ORDER BY data_zamowienia DESC)
-- UŻYWANY W: Raport sprzedaży, lista najnowszych zamówień
-- --------------------------------------------------------------------

-- Sprawdzamy czy indeks już istnieje
IF NOT EXISTS (
    SELECT * FROM sys.indexes
    WHERE name = 'idx_zamowienia_data'
    AND object_id = OBJECT_ID('zamowienia')
)
BEGIN
    -- Tworzymy indeks na kolumnie data_zamowienia
    -- NONCLUSTERED - indeks pomocniczy (nie zmienia fizycznej kolejności danych)
    -- DESC - sortowanie malejące (najnowsze najpierw)
    CREATE NONCLUSTERED INDEX idx_zamowienia_data
    ON zamowienia(data_zamowienia DESC)

    PRINT '✓ Utworzono indeks: idx_zamowienia_data'
    PRINT '  Przyspiesza: Sortowanie zamówień po dacie'
    PRINT ''
END
ELSE
BEGIN
    PRINT '○ Indeks idx_zamowienia_data już istnieje'
END
GO

-- --------------------------------------------------------------------
-- INDEKS 2: idx_zamowienia_klient
-- --------------------------------------------------------------------
-- CEL: Przyspieszenie JOIN-ów z tabelą klienci
-- UŻYWANY W: Raport sprzedaży, statystyki klientów
-- --------------------------------------------------------------------

IF NOT EXISTS (
    SELECT * FROM sys.indexes
    WHERE name = 'idx_zamowienia_klient'
    AND object_id = OBJECT_ID('zamowienia')
)
BEGIN
    -- Indeks na kolumnie klient_id (foreign key)
    -- Przyspiesza zapytania typu: JOIN klienci ON zamowienia.klient_id = klienci.id
    CREATE NONCLUSTERED INDEX idx_zamowienia_klient
    ON zamowienia(klient_id)

    PRINT '✓ Utworzono indeks: idx_zamowienia_klient'
    PRINT '  Przyspiesza: JOIN z tabelą klienci'
    PRINT ''
END
ELSE
BEGIN
    PRINT '○ Indeks idx_zamowienia_klient już istnieje'
END
GO

-- --------------------------------------------------------------------
-- INDEKS 3: idx_zamowienia_produkt
-- --------------------------------------------------------------------
-- CEL: Przyspieszenie JOIN-ów z tabelą produkty
-- UŻYWANY W: Raport sprzedaży, top produkty, statystyki
-- --------------------------------------------------------------------

IF NOT EXISTS (
    SELECT * FROM sys.indexes
    WHERE name = 'idx_zamowienia_produkt'
    AND object_id = OBJECT_ID('zamowienia')
)
BEGIN
    -- Indeks na kolumnie produkt_id (foreign key)
    -- Przyspiesza zapytania typu: JOIN produkty ON zamowienia.produkt_id = produkty.id
    CREATE NONCLUSTERED INDEX idx_zamowienia_produkt
    ON zamowienia(produkt_id)

    PRINT '✓ Utworzono indeks: idx_zamowienia_produkt'
    PRINT '  Przyspiesza: JOIN z tabelą produkty'
    PRINT ''
END
ELSE
BEGIN
    PRINT '○ Indeks idx_zamowienia_produkt już istnieje'
END
GO

-- --------------------------------------------------------------------
-- INDEKS 4: idx_zamowienia_status
-- --------------------------------------------------------------------
-- CEL: Przyspieszenie filtrowania po statusie
-- UŻYWANY W: Przyszłe funkcje (filtrowanie zamówień po statusie)
-- --------------------------------------------------------------------

IF NOT EXISTS (
    SELECT * FROM sys.indexes
    WHERE name = 'idx_zamowienia_status'
    AND object_id = OBJECT_ID('zamowienia')
)
BEGIN
    -- Indeks na kolumnie status
    -- Przyspiesza: WHERE status = 'nowe' lub WHERE status IN ('nowe', 'wysłane')
    CREATE NONCLUSTERED INDEX idx_zamowienia_status
    ON zamowienia(status)

    PRINT '✓ Utworzono indeks: idx_zamowienia_status'
    PRINT '  Przyspiesza: Filtrowanie zamówień po statusie'
    PRINT ''
END
ELSE
BEGIN
    PRINT '○ Indeks idx_zamowienia_status już istnieje'
END
GO

-- ====================================================================
-- KROK 3: INDEKSY DLA TABELI 'ceny'
-- ====================================================================

-- --------------------------------------------------------------------
-- INDEKS 5: idx_ceny_produkt_daty
-- --------------------------------------------------------------------
-- CEL: Przyspieszenie znajdowania aktualnych cen produktów
-- UŻYWANY W: Raport magazynowy, get_products(), składanie zamówień
-- KLUCZOWY INDEKS dla wydajności aplikacji!
-- --------------------------------------------------------------------

IF NOT EXISTS (
    SELECT * FROM sys.indexes
    WHERE name = 'idx_ceny_produkt_daty'
    AND object_id = OBJECT_ID('ceny')
)
BEGIN
    -- Indeks kompozytowy (złożony) na trzech kolumnach
    -- Kolejność kolumn jest WAŻNA dla wydajności!
    -- produkt_id - filtrujemy po produkcie
    -- data_od, data_do - filtrujemy po zakresie dat (GETDATE() BETWEEN data_od AND data_do)
    CREATE NONCLUSTERED INDEX idx_ceny_produkt_daty
    ON ceny(produkt_id, data_od, data_do)

    PRINT '✓ Utworzono indeks: idx_ceny_produkt_daty (KLUCZOWY!)'
    PRINT '  Przyspiesza: Wyszukiwanie aktualnych cen produktów'
    PRINT '  Używany w: Raport magazynowy, lista produktów, zamówienia'
    PRINT ''
END
ELSE
BEGIN
    PRINT '○ Indeks idx_ceny_produkt_daty już istnieje'
END
GO

-- ====================================================================
-- KROK 4: INDEKSY DLA TABELI 'produkty'
-- ====================================================================

-- --------------------------------------------------------------------
-- INDEKS 6: idx_produkty_kategoria
-- --------------------------------------------------------------------
-- CEL: Przyspieszenie grupowania i sortowania po kategoriach
-- UŻYWANY W: Raport magazynowy (ORDER BY kategoria, nazwa)
-- --------------------------------------------------------------------

IF NOT EXISTS (
    SELECT * FROM sys.indexes
    WHERE name = 'idx_produkty_kategoria'
    AND object_id = OBJECT_ID('produkty')
)
BEGIN
    -- Indeks na kolumnie kategoria
    -- Przyspiesza: ORDER BY kategoria, GROUP BY kategoria
    CREATE NONCLUSTERED INDEX idx_produkty_kategoria
    ON produkty(kategoria)

    PRINT '✓ Utworzono indeks: idx_produkty_kategoria'
    PRINT '  Przyspiesza: Grupowanie i sortowanie po kategoriach'
    PRINT ''
END
ELSE
BEGIN
    PRINT '○ Indeks idx_produkty_kategoria już istnieje'
END
GO

-- --------------------------------------------------------------------
-- INDEKS 7: idx_produkty_nazwa
-- --------------------------------------------------------------------
-- CEL: Przyspieszenie wyszukiwania produktów po nazwie
-- UŻYWANY W: Listy produktów, autocomplete (przyszłe funkcje)
-- --------------------------------------------------------------------

IF NOT EXISTS (
    SELECT * FROM sys.indexes
    WHERE name = 'idx_produkty_nazwa'
    AND object_id = OBJECT_ID('produkty')
)
BEGIN
    -- Indeks na kolumnie nazwa
    -- Przyspiesza: WHERE nazwa LIKE 'Laptop%', ORDER BY nazwa
    CREATE NONCLUSTERED INDEX idx_produkty_nazwa
    ON produkty(nazwa)

    PRINT '✓ Utworzono indeks: idx_produkty_nazwa'
    PRINT '  Przyspiesza: Wyszukiwanie i sortowanie produktów po nazwie'
    PRINT ''
END
ELSE
BEGIN
    PRINT '○ Indeks idx_produkty_nazwa już istnieje'
END
GO

-- ====================================================================
-- KROK 5: INDEKSY DLA TABELI 'klienci'
-- ====================================================================

-- --------------------------------------------------------------------
-- INDEKS 8: idx_klienci_nazwa
-- --------------------------------------------------------------------
-- CEL: Przyspieszenie sortowania klientów alfabetycznie
-- UŻYWANY W: Lista klientów w GUI (ORDER BY nazwa)
-- --------------------------------------------------------------------

IF NOT EXISTS (
    SELECT * FROM sys.indexes
    WHERE name = 'idx_klienci_nazwa'
    AND object_id = OBJECT_ID('klienci')
)
BEGIN
    -- Indeks na kolumnie nazwa
    -- Przyspiesza: ORDER BY nazwa w get_customers()
    CREATE NONCLUSTERED INDEX idx_klienci_nazwa
    ON klienci(nazwa)

    PRINT '✓ Utworzono indeks: idx_klienci_nazwa'
    PRINT '  Przyspiesza: Sortowanie klientów alfabetycznie'
    PRINT ''
END
ELSE
BEGIN
    PRINT '○ Indeks idx_klienci_nazwa już istnieje'
END
GO

-- --------------------------------------------------------------------
-- INDEKS 9: idx_klienci_email
-- --------------------------------------------------------------------
-- CEL: Przyspieszenie wyszukiwania klientów po email
-- UŻYWANY W: Przyszłe funkcje (weryfikacja unikalności, wyszukiwanie)
-- --------------------------------------------------------------------

IF NOT EXISTS (
    SELECT * FROM sys.indexes
    WHERE name = 'idx_klienci_email'
    AND object_id = OBJECT_ID('klienci')
)
BEGIN
    -- Indeks na kolumnie email
    -- Opcja UNIQUE zapewnia że email będzie unikalny (jeśli dodamy taką regułę)
    -- Przyspiesza: WHERE email = 'kontakt@abc.pl'
    CREATE NONCLUSTERED INDEX idx_klienci_email
    ON klienci(email)

    PRINT '✓ Utworzono indeks: idx_klienci_email'
    PRINT '  Przyspiesza: Wyszukiwanie klientów po email'
    PRINT ''
END
ELSE
BEGIN
    PRINT '○ Indeks idx_klienci_email już istnieje'
END
GO

-- ====================================================================
-- KROK 6: STATYSTYKI - AKTUALIZACJA
-- ====================================================================

PRINT ''
PRINT '===================================================================='
PRINT 'AKTUALIZACJA STATYSTYK TABEL'
PRINT '===================================================================='
PRINT ''
PRINT 'Aktualizacja statystyk pomaga SQL Server w optymalizacji zapytań...'
PRINT ''

-- UPDATE STATISTICS - aktualizuje statystyki dystrybucji danych
-- SQL Server używa tych statystyk do tworzenia optymalnych planów wykonania zapytań

-- Aktualizacja statystyk dla klienci
UPDATE STATISTICS klienci
PRINT '✓ Zaktualizowano statystyki tabeli: klienci'

-- Aktualizacja statystyk dla produkty
UPDATE STATISTICS produkty
PRINT '✓ Zaktualizowano statystyki tabeli: produkty'

-- Aktualizacja statystyk dla ceny
UPDATE STATISTICS ceny
PRINT '✓ Zaktualizowano statystyki tabeli: ceny'

-- Aktualizacja statystyk dla zamowienia
UPDATE STATISTICS zamowienia
PRINT '✓ Zaktualizowano statystyki tabeli: zamowienia'

PRINT ''

-- ====================================================================
-- KROK 7: PODSUMOWANIE UTWORZONYCH INDEKSÓW
-- ====================================================================

PRINT ''
PRINT '===================================================================='
PRINT 'PODSUMOWANIE INDEKSÓW W BAZIE DANYCH'
PRINT '===================================================================='
PRINT ''

-- Wyświetlamy wszystkie indeksy (oprócz Primary Key)
SELECT
    -- Nazwa tabeli
    OBJECT_NAME(i.object_id) AS 'Tabela',
    -- Nazwa indeksu
    i.name AS 'Indeks',
    -- Kolumny w indeksie
    STRING_AGG(c.name, ', ') AS 'Kolumny',
    -- Typ indeksu
    i.type_desc AS 'Typ'
FROM sys.indexes i
-- JOIN aby pobrać nazwy kolumn
INNER JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
INNER JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
WHERE
    -- Tylko nasze tabele (nie systemowe)
    OBJECT_NAME(i.object_id) IN ('klienci', 'produkty', 'ceny', 'zamowienia')
    -- Pomijamy Primary Key (są tworzone automatycznie)
    AND i.is_primary_key = 0
    -- Pomijamy wewnętrzne indeksy heap
    AND i.type > 0
GROUP BY
    i.object_id,
    i.name,
    i.type_desc
ORDER BY
    OBJECT_NAME(i.object_id),
    i.name
GO

PRINT ''
PRINT '===================================================================='
PRINT 'ZAKOŃCZONO TWORZENIE INDEKSÓW'
PRINT '===================================================================='
PRINT ''
PRINT 'ZALECENIA:'
PRINT '1. Uruchom ponownie aplikację Python aby zobaczyć różnicę w wydajności'
PRINT '2. W przypadku dużej bazy (100000+ rekordów) rozważ:'
PRINT '   - Partycjonowanie tabel'
PRINT '   - Archived data (archiwizacja starych zamówień)'
PRINT '   - Stored procedures zamiast zapytań w kodzie Python'
PRINT '3. Regularnie (co tydzień) uruchamiaj:'
PRINT '   - UPDATE STATISTICS (aktualizacja statystyk)'
PRINT '   - ALTER INDEX REBUILD (przebudowa indeksów przy fragmentacji >30%)'
PRINT ''
PRINT 'SPRAWDZENIE FRAGMENTACJI INDEKSÓW:'
PRINT 'SELECT OBJECT_NAME(ips.object_id) AS Tabela, i.name AS Indeks,'
PRINT '       ips.avg_fragmentation_in_percent AS Fragmentacja'
PRINT 'FROM sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, ''LIMITED'') ips'
PRINT 'JOIN sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id'
PRINT 'WHERE ips.avg_fragmentation_in_percent > 10'
PRINT 'ORDER BY ips.avg_fragmentation_in_percent DESC'
PRINT ''
GO

-- ====================================================================
-- KONIEC SKRYPTU
-- ====================================================================
--
-- INSTRUKCJA UŻYCIA:
-- 1. Otwórz SQL Server Management Studio (SSMS)
-- 2. Połącz się z instancją SQL Server
-- 3. Upewnij się że baza SklepDB istnieje i zawiera dane
-- 4. Otwórz ten plik (File → Open → File)
-- 5. Kliknij "Execute" (F5) lub przycisk ▶
-- 6. Sprawdź Messages - powinny pojawić się komunikaty o utworzeniu indeksów
--
-- KIEDY NIE UŻYWAĆ INDEKSÓW:
-- - Bardzo małe tabele (<100 rekordów) - indeksy mogą być wolniejsze
-- - Tabele z bardzo częstymi INSERT/UPDATE/DELETE - indeksy spowalniają zapis
-- - Kolumny z małą selektywnością (np. kolumna z 2 wartościami: tak/nie)
--
-- MONITOROWANIE WYDAJNOŚCI:
-- Po utworzeniu indeksów, możesz sprawdzić czy są używane:
--
-- SELECT
--     OBJECT_NAME(s.object_id) AS Tabela,
--     i.name AS Indeks,
--     s.user_seeks AS 'Liczba użyć (SEEK)',
--     s.user_scans AS 'Liczba skanowań',
--     s.last_user_seek AS 'Ostatnie użycie'
-- FROM sys.dm_db_index_usage_stats s
-- INNER JOIN sys.indexes i ON s.object_id = i.object_id AND s.index_id = i.index_id
-- WHERE database_id = DB_ID('SklepDB')
-- ORDER BY s.user_seeks DESC
--
-- ====================================================================
