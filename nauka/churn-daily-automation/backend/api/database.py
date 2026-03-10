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
        script_dir = os.path.dirname(__file__)
        credentials_path = os.path.join(script_dir, '..', 'credentials', 'Pass.xlsx')
        hasla = pd.read_excel(credentials_path)

        credentials = {}
        for _, row in hasla.iterrows(): # Ignoruję index, biorę tylko row
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
    
    except Exception as e:
        print(f"DEBUG: BŁĄD - {type(e).__name__}: {e}")
        return None