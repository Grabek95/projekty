# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:17:31 2026

@author: mateusz.grabinski
"""

import win32com.client
from datetime import datetime
import pandas as pd
import lxml
import pyodbc
import os
import warnings
warnings.filterwarnings('ignore')

def outlook_connect():
    try:
        # połączenie z outlook
        outlook = win32com.client.Dispatch("Outlook.Application")
        namespace = outlook.GetNameSpace("MAPI")
        # Dostęp do folderu Inbox
        inbox = namespace.GetDefaultFolder(6) # 6 = Inbox
        return inbox
    except Exception as e:
        print(f"Błąd połączenia z outlookiem: {e}")
        return None

def Teradata_connect():
    try:
        if os.getlogin() == 'mateusz.grabinski':
            hasla = pd.read_excel(r'C:\Users\mateusz.grabinski\Desktop\Pass.xlsx')         
            start = 0
            koniec = hasla.index.max()
            while start <= koniec:
                pas = hasla.loc[start, 'Co']
                globals()[pas] = hasla.loc[start, 'wartosc']
                start = start + 1
            del pas, start, koniec, hasla
        conn = pyodbc.connect('DRIVER={Teradata Database ODBC Driver 16.20};DBCNAME={dbc};UID=' + teralog + ';PWD=' + terapas + ';QUIETMODE=YES;')
        conn.autocommit = True
        return conn
    except Exception as e:
        print(f"Błąd połączenia: {e}")
        return None

def pobierz_plk():
    try:
        # Filtr dla PLK
        temat_plk = f"RaportyDWN PLK Churn {dzis}"
        filtr_plk = f"[Subject] = '{temat_plk}'"
        maile_plk = inbox.Items.Restrict(filtr_plk)
        if len(maile_plk) == 0:
            print("Brak maila!")
            return None
        mail_plk = maile_plk[0]
        html_content = mail_plk.HTMLBody
        # pandas automatycznie wyciąga WSZYSTKIE tabele z HTML
        tabele = pd.read_html(html_content)
        # Pokazmy 1 tabele
        if len(tabele) > 0:
            df_plk = tabele[0]                
            # Wyciągamy wartości z kolumny "Wykonanie"
            biz = df_plk.loc[df_plk['Linia'] == 'BIZ', 'Wykonanie'].values[0]
            data = df_plk.loc[df_plk['Linia'] == 'DATA', 'Wykonanie'].values[0]
            data_ftth = df_plk.loc[df_plk['Linia'] == 'DATA_FTTH', 'Wykonanie'].values[0]
            ind = df_plk.loc[df_plk['Linia'] == 'IND', 'Wykonanie'].values[0]
            mix = df_plk.loc[df_plk['Linia'] == 'MIX', 'Wykonanie'].values[0]
            # Sumujemy DATA + DATA_FTTH
            data_total = data + data_ftth
            print("\n--- Wartości CHURN PLK ---")
            print(f"DATA (osobno): {data}")
            print(f"MIX: {mix}")
            print(f"IND: {ind}")
            print(f"DATA_FTTH (osobno): {data_ftth}")
            print(f"BIZ: {biz}")
            print(f"\nDATA (łącznie z FTTH): {data_total}")

            return biz, data, data_ftth, ind, mix
            
    except Exception as e:
        print(f"Błąd: {e}")
        return None

def pobierz_cp(conn):
    try:
        cursor = conn.cursor()
        rok_biezacy = datetime.now().year # Bieżący rok i miesiąc
        query_cp = f"""
        SELECT CAST((DataZdarzenia (FORMAT 'yyyymm')) AS CHAR(6)) Msc
        ,SUM(CASE WHEN TypKontraktu='Kontrakt TV' THEN 1 ELSE 0 END) TV
        ,SUM(CASE WHEN TypKontraktu='Internet' THEN 1 ELSE 0 END) "IN"
        FROM VD_US_DM_RODOS_CP.RPT_FT_Dezaktywacje
        WHERE RodzajZdarzenia='Churn windykacyjny'
        AND CzyChurnAnulowany=0
        AND CzyGieldowy=1
        AND DataZdarzenia >= '{rok_biezacy}-01-01'
        GROUP BY 1
        ORDER BY 1
        """

        # Wykonanie zapytania
        df_cp = pd.read_sql(query_cp, conn)
        if len(df_cp) < 2:
            print("Błąd w zapytaniu - sprawdź SQL")
            return None
        # bierzemy ostatni miesiąc
        cp_ostatni = df_cp.iloc[-2]
        tv_cp_0 = cp_ostatni['TV']
        in_cp_0 = cp_ostatni['IN']
        miesiac_cp_0 = cp_ostatni['Msc']
        # Bierzemy aktualny miesiąc (najnowszy)
        cp_aktualny = df_cp.iloc[-1]
        tv_cp = cp_aktualny['TV']
        in_cp = cp_aktualny['IN']
        miesiac_cp = cp_aktualny['Msc']

        print("\n--- Wartości CHURN CP (najnowszy miesiąc) ---")
        print(f"Miesiąc: {miesiac_cp}")
        print(f"TV: {tv_cp}")
        print(f"IN: {in_cp}")
        print("\n--- Wartości CHURN CP (poprzedni miesiąc) ---")
        print(f"Miesiąc: {miesiac_cp_0}")
        print(f"TV: {tv_cp_0}")
        print(f"IN: {in_cp_0}")

        return  cp_ostatni, cp_aktualny
    
    except Exception as e:
        print(f"Błąd: {e}")
        return None
    finally:
        try:
            cursor.close()
        except:
            pass

def pobierz_netia():
    try:
        # Filtra dla Netia
        temat_netia = f"CHURN WINDYKACYJNY NETIA - WYKONANIE: {dzis}"
        filtr_netia = f"[Subject] = '{temat_netia}'"
        maile_netia = inbox.Items.Restrict(filtr_netia)

        if len(maile_netia) == 0:
            print("Brak maila!")
            return None
        mail_netia = maile_netia[0]
        html_content_netia = mail_netia.HTMLBody
        tabele_netia = pd.read_html(html_content_netia)
        # Bierzemy pierwszą tabelę
        df_netia = tabele_netia[0]
        # Szukamy kolumny z datą (format YYYY-MM-DD w poziomie 0)
        kolumny_dat = [col for col in df_netia.columns 
            if col[0] not in ['OKRES', 'TOTAL'] and '-' in str(col[0])]
        # Bierzemy pierwszą (lub najnowszą) datę
        if len(kolumny_dat) == 0:
            print("Nie znaleziono kolumny z datą!")
            return None       
        kolumna_z_data_biezacy = kolumny_dat[-1]  # Ostatnia = najnowsza data  
        kolumna_z_data_poprzedni = kolumny_dat[-2] if len(kolumny_dat) > 1 else None  # Przedostatnia     
        # Kolumna z nazwami produktów
        kolumna_produkt = ('OKRES', 'PRODUKT')
        # Usuwamy wiersz TOTAL
        df_netia_clean = df_netia[df_netia[kolumna_produkt] != 'TOTAL'].copy()
        # Wyciągamy wartości dla każdego produktu
        bb_offnet = df_netia_clean.loc[df_netia_clean[kolumna_produkt] == 'BB OFFNET', kolumna_z_data_biezacy].values[0]
        bb_onnet = df_netia_clean.loc[df_netia_clean[kolumna_produkt] == 'BB ONNET', kolumna_z_data_biezacy].values[0]
        mobile = df_netia_clean.loc[df_netia_clean[kolumna_produkt] == 'MOBILE', kolumna_z_data_biezacy].values[0]
        tv = df_netia_clean.loc[df_netia_clean[kolumna_produkt] == 'TV', kolumna_z_data_biezacy].values[0]
        voice_offnet = df_netia_clean.loc[df_netia_clean[kolumna_produkt] == 'VOICE OFFNET', kolumna_z_data_biezacy].values[0]
        voice_onnet = df_netia_clean.loc[df_netia_clean[kolumna_produkt] == 'VOICE ONNET', kolumna_z_data_biezacy].values[0]
        if kolumna_z_data_poprzedni is not None:
            bb_offnet_last = df_netia_clean.loc[df_netia_clean[kolumna_produkt] == 'BB OFFNET', kolumna_z_data_poprzedni].values[0]
            bb_onnet_last = df_netia_clean.loc[df_netia_clean[kolumna_produkt] == 'BB ONNET', kolumna_z_data_poprzedni].values[0]
            mobile_last = df_netia_clean.loc[df_netia_clean[kolumna_produkt] == 'MOBILE', kolumna_z_data_poprzedni].values[0]
            tv_last = df_netia_clean.loc[df_netia_clean[kolumna_produkt] == 'TV', kolumna_z_data_poprzedni].values[0]
            voice_offnet_last = df_netia_clean.loc[df_netia_clean[kolumna_produkt] == 'VOICE OFFNET', kolumna_z_data_poprzedni].values[0]
            voice_onnet_last = df_netia_clean.loc[df_netia_clean[kolumna_produkt] == 'VOICE ONNET', kolumna_z_data_poprzedni].values[0]

        print("\n--- Wartości CHURN NETIA ---")
        print(f"Data: {kolumna_z_data_biezacy[0]}")
        print(f"BB OFFNET: {bb_offnet}")
        print(f"BB ONNET: {bb_onnet}")
        print(f"MOBILE: {mobile}")
        print(f"TV: {tv}")
        print(f"VOICE OFFNET: {voice_offnet}")
        print(f"VOICE ONNET: {voice_onnet}")

        return (bb_offnet, bb_onnet, mobile, tv, voice_offnet, voice_onnet), (bb_offnet_last, bb_onnet_last, mobile_last, tv_last, voice_offnet_last, voice_onnet_last), kolumna_z_data_biezacy, kolumna_z_data_poprzedni
    except Exception as e:
        print(f"Błąd: {e}")
        return None


def zapisz_do_bazy(conn, dane_plk, dane_cp, dane_netia):
    try:
        cursor = conn.cursor()
        dane = []
        if dane_plk is not None:
            biz, data, data_ftth, ind, mix = dane_plk
            dane.append((dzis, 'PLK', 'BIZ',       int(biz),        str(datetime.now().strftime("%Y%m"))))
            dane.append((dzis, 'PLK', 'DATA',       int(data), str(datetime.now().strftime("%Y%m"))))
            dane.append((dzis, 'PLK', 'DATA_FTTH',  int(data_ftth), str(datetime.now().strftime("%Y%m"))))
            dane.append((dzis, 'PLK', 'IND',        int(ind),        str(datetime.now().strftime("%Y%m"))))
            dane.append((dzis, 'PLK', 'MIX',        int(mix),        str(datetime.now().strftime("%Y%m"))))
        if dane_cp is not None:
            cp_ostatni, cp_aktualny = dane_cp
            dane.append((dzis, 'CP', 'TV', int(cp_aktualny['TV']), str(cp_aktualny['Msc'])))
            dane.append((dzis, 'CP', 'IN', int(cp_aktualny['IN']), str(cp_aktualny['Msc'])))
        if dane_netia is not None:
            dane_biezace, dane_poprzednie, kolumna_z_data_biezacy, kolumna_z_data_poprzedni = dane_netia
            dzien_dzis = datetime.now().day
            if dzien_dzis >= 10:
                bb_offnet, bb_onnet, mobile, tv, voice_offnet, voice_onnet = dane_biezace            
                miesiac_netia = kolumna_z_data_biezacy[0][:7].replace('-','')
                dane.append((dzis, 'NETIA', 'BB OFFNET',  int(bb_offnet),   miesiac_netia))
                dane.append((dzis, 'NETIA', 'BB ONNET',   int(bb_onnet),    miesiac_netia))
                dane.append((dzis, 'NETIA', 'MOBILE',     int(mobile),      miesiac_netia))
                dane.append((dzis, 'NETIA', 'TV',         int(tv),          miesiac_netia))
                dane.append((dzis, 'NETIA', 'VOICE OFFNET', int(voice_offnet), miesiac_netia))
                dane.append((dzis, 'NETIA', 'VOICE ONNET',  int(voice_onnet),  miesiac_netia))
        if len(dane) == 0:
            print("Brak danych do zapisania!")
            return
        current_month = datetime.now().strftime('%Y%m')
        query_check = f"SELECT COUNT(*) FROM db_work_dwn.Churn_Daily WHERE MIESIAC = '{current_month}'"
        cursor.execute(query_check)
        count_records = cursor.fetchone()[0]

        if count_records == 0:
            insert_sql = "INSERT INTO db_work_dwn.Churn_Daily VALUES (?,?,?,?,?)"
            cursor.executemany(insert_sql, dane)
            print(f"\nWrzucono {len(dane)} wierszy do Churn_Daily!")
        else:
            dane_update = [(wartosc, data_raportu, spolka, produkt, miesiac) 
                for (data_raportu, spolka, produkt, wartosc, miesiac) in dane]
            update_sql = """UPDATE db_work_dwn.Churn_Daily 
                            SET WARTOSC = ?, DATA_RAPORTU = ?
                            WHERE SPOLKA = ?
                            AND PRODUKT = ?
                            AND MIESIAC = ?
                            """
            cursor.executemany(update_sql, dane_update)
            print(f"\nZaktualizowano {len(dane_update)} wierszy!")
    except Exception as e:
        print(f"Błąd: {e}")
        return None
    finally:
        try:
            cursor.close()
        except:
            pass

def update_last_cp(conn, dane_cp):
    try:
        cursor = conn.cursor()
        if dane_cp is None:
            return
        cp_ostatni, cp_aktualny = dane_cp

        dane_update = [
            (int(cp_ostatni['TV']), 'CP', 'TV', str(cp_ostatni['Msc'])),
            (int(cp_ostatni['IN']), 'CP', 'IN', str(cp_ostatni['Msc']))
        ]
        update_sql = """UPDATE db_work_dwn.Churn_Daily 
        SET WARTOSC = ?
        WHERE SPOLKA = ?
        AND PRODUKT = ?
        AND MIESIAC = ?
        """
        cursor.executemany(update_sql, dane_update)
        print("Zaktualizowano poprzedni msc dla CP!")
    except Exception as e:
        print(f"Błąd: {e}")
        return None
    finally:
        try:
            cursor.close()
        except:
            pass

def update_last_netia(conn, dane_netia):
    try:
        if dane_netia is None:
            return
        cursor = conn.cursor()
        dane = []
        dane_biezace, dane_poprzednie, kolumna_z_data_biezacy, kolumna_z_data_poprzedni = dane_netia
        bb_offnet_last, bb_onnet_last, mobile_last, tv_last, voice_offnet_last, voice_onnet_last = dane_poprzednie  # ← Wartości POPRZEDNIEGO miesiąca!
        if kolumna_z_data_poprzedni is None:
            return    
        miesiac_netia = kolumna_z_data_poprzedni[0][:7].replace('-','')
        dane.append((int(bb_offnet_last), 'NETIA', 'BB OFFNET', miesiac_netia))
        dane.append((int(bb_onnet_last), 'NETIA', 'BB ONNET', miesiac_netia))
        dane.append((int(mobile_last), 'NETIA', 'MOBILE', miesiac_netia))
        dane.append((int(tv_last), 'NETIA', 'TV', miesiac_netia))
        dane.append((int(voice_offnet_last), 'NETIA', 'VOICE OFFNET', miesiac_netia))
        dane.append((int(voice_onnet_last), 'NETIA', 'VOICE ONNET', miesiac_netia))
        update_sql = """UPDATE db_work_dwn.Churn_Daily 
        SET WARTOSC = ?
        WHERE SPOLKA = ?
        AND PRODUKT = ?
        AND MIESIAC = ?
        """
        cursor.executemany(update_sql, dane)
        print("Zaktualizowano poprzedni msc dla Netii!")
    except Exception as e:
        print(f"Błąd: {e}")
        return None
    finally:
        try:
            cursor.close()
        except:
            pass




if __name__ == "__main__":
    dzis = datetime.now().strftime("%Y-%m-%d")
    inbox = outlook_connect()
    if inbox is None:
        print("Nie można połączyć z Outlook!")
        exit()
    conn = Teradata_connect()
    if conn is None:
        print("Nie można połączyć z Teradata!")
        exit()
    dane_plk = pobierz_plk()
    dane_cp = pobierz_cp(conn)
    dane_netia = pobierz_netia()
    zapisz_do_bazy(conn, dane_plk, dane_cp, dane_netia)
    update_last_cp(conn, dane_cp)
    update_last_netia(conn, dane_netia)
    conn.close()


