# modele pydantic
from pydantic import BaseModel
from typing import Optional

class ChurnRecord(BaseModel):
    """Model pojedynczego rekordu churn"""
    DATA_RAPORTU: str   # Format: '2026-03-01'
    SPOLKA: str         # 'PLK', 'CP', 'NETIA'
    PRODUKT: str        # Nazwa produktu
    WARTOSC: int        # Wartosc churn
    MIESIAC: str        # Format: '202603'

class ChurnResponse(BaseModel):
    """Odpowiedź API z listą rekordów"""
    records: list[ChurnRecord]
    total: int          # ile rekordów

class PLKManualInput(BaseModel):
    """Ręczne wprowadzanie danych PLK"""
    biz: Optional[int] = None
    data: Optional[int] = None
    data_ftth: Optional[int] = None
    ind: Optional[int] = None
    mix: Optional[int] = None