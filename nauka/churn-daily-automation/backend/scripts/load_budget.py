# -*- coding: utf-8 -*-
"""
Wgrywanie budżetu churn z Excela do pliku budget.xlsx
Uruchomienie: python load_budget.py
Zapisuje do: backend/credentials/budget.xlsx
"""

import pandas as pd
import openpyxl
import os

# KONFIGURACJA 
ROK = 2026 # podaj rok

# Ścieżka do pliku Excel z budżetem
excel_file = r'\\polkomtel\pliki\PO_DABiW\ZZZDiOKP_Analitycy\RAPORTY\Churn\CHURN DZIENNY\Cele_DWN_churn_ 2026_T10_0305.xlsx'

# Mapowanie: produkt → wiersz w Excelu (wiersz BUDŻETU)
MAPPING = {
    'PLK': {
        'IND': 7,
        'MIX': 12,
        'BIZ': 17,
        'DATA': 22
    },
    'CP': {
        'IN': 32,
        'TV': 37
    },
    'NETIA': {
        'BB ONNET': 42,
        'BB OFFNET': 47,
        'TV': 52,
        'VOICE ONNET': 57,
        'VOICE OFFNET': 62,
        'MOBILE': 67
    }
}

def get_kolumny_dla_roku(rok, prognoza_po_miesiacu=1):
    """
    Zwraca listę kolumn dla budżetów danego roku.
    
    Args:
        rok: Rok budżetu (2026, 2027, etc.)
        prognoza_po_miesiacu: Po którym miesiącu jest prognoza (1=Sty, 3=Mar, etc.)
    
    13 kolumn na rok
    """
    kolumna_start = 84 + (rok - 2026) * 13
    
    # Indeks prognozy w Excelu
    indeks_prognozy = prognoza_po_miesiacu  # Po styczniu=1, po marcu=3
    
    # Buduj listę kolumn pomijając prognozę i sumę (12)
    kolumny = []
    for i in range(13):  # 12 miesięcy (0-11)
        if i != indeks_prognozy:  # Pomiń prognozę
            kolumny.append(kolumna_start + i)
    
    return kolumny

# GŁÓWNA LOGIKA

# Wczytaj Excel
wb = openpyxl.load_workbook(excel_file)
ws = wb.active

# Pobierz kolumny dla danego roku
kolumny = get_kolumny_dla_roku(ROK, prognoza_po_miesiacu=3)  # Po marcu! - 1, 2, 3 - miesiace po ktorych jest prognoza, wybrac aby pominac progrnoze

# Lista na dane budżetu
budget_data = []

# Iteruj po miesiącach i kolumnach
for miesiac_nr, kolumna in enumerate(kolumny, start=1):
    rok_msc = f"{ROK}{miesiac_nr:02d}"  # Format: YYYYMM
    
    # Iteruj po spółkach i produktach
    for spolka, produkty in MAPPING.items():
        for produkt, wiersz in produkty.items():
            # Odczytaj wartość budżetu z Excela
            wartosc = ws.cell(row=wiersz, column=kolumna).value
            
            # Dodaj do listy
            budget_data.append((rok_msc, spolka, produkt, wartosc))

# Stwórz DataFrame
df = pd.DataFrame(budget_data, columns=['ROK_MSC', 'SPOLKA', 'PRODUKT', 'WARTOSC'])

# Zapisz do pliku
script_dir = os.path.dirname(__file__)
output_path = os.path.join(script_dir, '..', 'credentials', 'budget.xlsx')
df.to_excel(output_path, index=False)

print(f"Zapisano {len(df)} wierszy budżetu do: {output_path}")
print(f"Rok: {ROK}")
print(f"Miesiące: {len(kolumny)}")
print("\nPierwsze 5 wierszy:")
print(df.head())