# Teradata connect

import pyodbc
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """
    Tworzy połączenie z Teradata.
    """
    try:
        print("DEBUG: Próba połączenia z bazą...")

        print("DEBUG: Wczytuję Pass.xlsx...")
        hasla = pd.read_excel(r'C:\Users\mateusz.grabinski\Desktop\Pass.xlsx')

        print("DEBUG: Przetwarzam credentials...")
        credentials = {}
        for _, row in hasla.iterrows(): # Ignoruję index, biorę tylko row
            credentials[row['Co']] = row['wartosc']
        print(f"DEBUG: Credentials: {list(credentials.keys())}")
        
        print("DEBUG: Tworzę połączenie...")
        conn = pyodbc.connect(
            f"DRIVER={{Teradata Database ODBC Driver 16.20}};"
            f"DBCNAME={credentials['dbc']};"
            f"UID={credentials['teralog']};"
            f"PWD={credentials['terapas']};"
            f"QUIETMODE=YES;"
        )
        conn.autocommit = True

        print("DEBUG: Połączenie OK!")
        return conn
    except Exception as e:
        print(f"DEBUG: BŁĄD - {type(e).__name__}: {e}")
        return None