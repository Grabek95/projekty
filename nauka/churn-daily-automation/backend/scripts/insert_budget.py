# -*- coding: utf-8 -*-
"""
Wgrywanie budżetu churn do tabeli db_work_dwn.Churn_Daily_BU
"""

import pandas as pd
import pyodbc
import os

def get_db_connection():
    """Połączenie z Teradata"""
    script_dir = os.path.dirname(__file__)
    credentials_path = os.path.join(script_dir, '..', 'credentials', 'Pass.xlsx')
    
    hasla = pd.read_excel(credentials_path)
    credentials = {}
    for _, row in hasla.iterrows():
        credentials[row['Co']] = row['wartosc']
    
    conn = pyodbc.connect(
        f"DRIVER={{Teradata Database ODBC Driver 16.20}};"
        f"DBCNAME={credentials['dbc']};"
        f"UID={credentials['teralog']};"
        f"PWD={credentials['terapas']};"
        f"QUIETMODE=YES;"
    )
    conn.autocommit = True
    return conn

def load_budget_from_excel():
    """
    Wczytaj budżet z Excela
    Zakładam strukturę: ROK_MSC, SPOLKA, PRODUKT, WARTOSC
    """
    script_dir = os.path.dirname(__file__)
    excel_file = os.path.join(script_dir, '..', 'credentials', 'budget.xlsx')
    
    df = pd.read_excel(excel_file)
    
    # Sprawdź czy są wymagane kolumny
    required_cols = ['ROK_MSC', 'SPOLKA', 'PRODUKT', 'WARTOSC']
    if not all(col in df.columns for col in required_cols):
        print(f"BŁĄD: Excel musi mieć kolumny: {required_cols}")
        print(f"Masz kolumny: {df.columns.tolist()}")
        return None
    
    return df

def insert_budget(conn, df):
    """Wstaw budżet do tabeli"""
    cursor = conn.cursor()
    
    # Wyczyść tabelę (opcjonalnie - jeśli chcesz przeładować dane)
    # cursor.execute("DELETE FROM db_work_dwn.Churn_Daily_BU")
    # print("Wyczyszczono tabelę Churn_Daily_BU")
    
    inserted = 0
    updated = 0
    
    for _, row in df.iterrows():
        rok_msc = str(row['ROK_MSC'])
        spolka = row['SPOLKA']
        produkt = row['PRODUKT']
        wartosc = int(row['WARTOSC']) if pd.notna(row['WARTOSC']) else 0
        
        # Sprawdź czy istnieje
        check_sql = """
            SELECT COUNT(*) FROM db_work_dwn.Churn_Daily_BU
            WHERE ROK_MSC = ? AND SPOLKA = ? AND PRODUKT = ?
        """
        cursor.execute(check_sql, (rok_msc, spolka, produkt))
        exists = cursor.fetchone()[0]
        
        if exists == 0:
            # INSERT
            insert_sql = """
                INSERT INTO db_work_dwn.Churn_Daily_BU (ROK_MSC, SPOLKA, PRODUKT, WARTOSC)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(insert_sql, (rok_msc, spolka, produkt, wartosc))
            inserted += 1
        else:
            # UPDATE
            update_sql = """
                UPDATE db_work_dwn.Churn_Daily_BU
                SET WARTOSC = ?
                WHERE ROK_MSC = ? AND SPOLKA = ? AND PRODUKT = ?
            """
            cursor.execute(update_sql, (wartosc, rok_msc, spolka, produkt))
            updated += 1
    
    cursor.close()
    print(f"\nWstawiono: {inserted}, Zaktualizowano: {updated}")

if __name__ == "__main__":
    print("=== Wgrywanie budżetu churn ===\n")
    
    # Wczytaj dane z Excela
    df_budget = load_budget_from_excel()
    if df_budget is None:
        exit()
    
    print(f"Wczytano {len(df_budget)} wierszy z Excela")
    print(f"Kolumny: {df_budget.columns.tolist()}\n")
    print("Przykładowe dane:")
    print(df_budget.head())
    
    # Połącz z bazą
    conn = get_db_connection()
    if conn is None:
        print("Nie można połączyć z bazą!")
        exit()
    
    # Wstaw dane
    insert_budget(conn, df_budget)
    
    conn.close()
    print("\nGotowe!")