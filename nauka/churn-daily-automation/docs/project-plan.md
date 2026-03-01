# Aplikacja Churn Daily - Plan Projektu

## 📋 Przegląd

Aplikacja webowa do zarządzania i wizualizacji danych churn dla spółek: PLK, Netia, CP.

---

## 🎯 Funkcjonalności

### 1. Dashboard z danymi

- Wyświetlanie danych churn w formie tabel i wykresów
- Dane z wszystkich trzech spółek (PLK, Netia, CP)
- Aktualne wartości oraz dane historyczne

### 2. Przyciski do ręcznej aktualizacji

- **CP** - uruchomienie funkcji `update_last_cp()` (poprzedni miesiąc)
- **Netia** - uruchomienie funkcji `update_last_netia()` (poprzedni miesiąc)
- **PLK - ręczne wpisywanie wartości:**
  - Formularz z polami: BIZ, DATA, DATA_FTTH, IND, MIX
  - Wartości docelowe są w osobnym Excelu
  - Opcjonalnie: funkcja odczytująca wartości z Excela i przekształcająca je

### 3. Porównania miesiąc do miesiąca

- Trendy (wzrost/spadek)
- Różnice między miesiącami
- Sumy i agregaty

### 4. SQL Playground

- Okno do pisania własnych zapytań SQL
- Bezpośrednie sprawdzanie wartości w bazie Teradata
- Wyświetlanie wyników w formie tabeli

---

## 🏗️ Architektura

### Stack Technologiczny

- **Frontend:** React
- **Backend:** FastAPI (Python)
- **Baza danych:** Teradata
- **Wykresy:** Recharts (React)

### Komunikacja

```
React (Frontend)          FastAPI (Backend)          Teradata
     |                          |                        |
     |---> GET /api/churn ----->|---> SELECT * -------->|
     |<--- JSON ----------------|                        |
     |                          |                        |
     |---> POST /api/update --->|---> UPDATE ---------->|
```

---

## 🔌 Backend API (FastAPI)

### Endpointy do zaimplementowania

#### 1. Pobieranie danych

```
GET /api/churn/all
- Zwraca wszystkie dane churn (wszystkie spółki, wszystkie miesiące)

GET /api/churn/{spolka}
- Zwraca dane dla konkretnej spółki (PLK/CP/NETIA)

GET /api/churn/{spolka}/{miesiac}
- Zwraca dane dla konkretnej spółki i miesiąca (np. /api/churn/PLK/202603)
```

#### 2. Aktualizacje

```
POST /api/update/cp
- Uruchamia funkcję update_last_cp()
- Aktualizuje poprzedni miesiąc CP

POST /api/update/netia
- Uruchamia funkcję update_last_netia()
- Aktualizuje poprzedni miesiąc Netii

POST /api/plk/manual
Body: {
  "biz": 295,
  "data": 1257,
  "data_ftth": 251,
  "ind": 4150,
  "mix": 25
}
- Ręczne wpisanie wartości PLK
- INSERT do bazy dla bieżącego miesiąca
```

#### 3. Porównania

```
GET /api/compare/{miesiac1}/{miesiac2}
- Porównanie danych między dwoma miesiącami
- Zwraca różnice, procentowe zmiany

GET /api/trends/{spolka}?months=6
- Dane trendów dla ostatnich N miesięcy
```

#### 4. SQL Playground

```
POST /api/sql/execute
Body: {
  "query": "SELECT * FROM db_work_dwn.Churn_Daily WHERE MIESIAC='202603'"
}
- Wykonuje zapytanie SQL
- Zwraca wyniki w JSON
- UWAGA: Tylko SELECT (bezpieczeństwo!)
```

---

## 🎨 Frontend (React)

### Główne komponenty

#### 1. Dashboard

- Karty z podsumowaniem dla każdej spółki
- Wykresy liniowe (trendy)
- Tabele z danymi

#### 2. Przyciski akcji

- Sekcja z przyciskami do aktualizacji
- Formularz dla ręcznego wprowadzania PLK
- Potwierdzenia akcji (modals)

#### 3. Porównania

- Selektor miesiąca (dropdown)
- Tabele porównawcze
- Wykresy słupkowe (porównanie miesiąc do miesiąca)

#### 4. SQL Console

- Edytor tekstowy (textarea)
- Przycisk "Wykonaj"
- Tabela z wynikami

---

## 📝 Plan implementacji

### Faza 1: Backend (FastAPI)

1. ✅ Struktura projektu
2. ✅ Połączenie z Teradata
3. ✅ Endpoint GET /api/churn/all
4. ✅ Endpoint POST /api/update/cp
5. ✅ Endpoint POST /api/update/netia
6. ✅ Endpoint POST /api/plk/manual
7. ✅ Testowanie API (Postman/curl)

### Faza 2: Frontend (React)

1. ✅ Setup projektu React
2. ✅ Komponent Dashboard
3. ✅ Integracja z API (pobieranie danych)
4. ✅ Wykresy (Recharts)
5. ✅ Przyciski aktualizacji
6. ✅ Formularz PLK
7. ✅ SQL Playground

### Faza 3: Deployment

1. ✅ Konfiguracja serwera
2. ✅ CORS i bezpieczeństwo
3. ✅ Testy końcowe

---

## 🔒 Uwagi bezpieczeństwa

- SQL Playground: **tylko SELECT**, blokada INSERT/UPDATE/DELETE
- Autoryzacja: rozważyć dodanie logowania (opcjonalnie)
- CORS: ograniczyć dostęp do frontendu
- Walidacja danych wejściowych (FastAPI Pydantic models)

---

## 📂 Struktura plików (propozycja)

```
churn-app/
├── backend/
│   ├── main.py              # FastAPI app
│   ├── database.py          # Połączenie z Teradata
│   ├── models.py            # Pydantic models
│   ├── routes/
│   │   ├── churn.py         # Endpointy churn
│   │   ├── update.py        # Endpointy update
│   │   └── sql.py           # SQL playground
│   └── utils.py             # Funkcje pomocnicze
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── UpdateButtons.jsx
│   │   │   ├── PLKForm.jsx
│   │   │   ├── Comparison.jsx
│   │   │   └── SQLConsole.jsx
│   │   ├── App.jsx
│   │   └── index.js
│   └── package.json
│
└── README.md
```

---

## 🚀 Następne kroki

**Krok 1:** Stworzenie struktury projektu FastAPI
**Krok 2:** Implementacja połączenia z Teradata
**Krok 3:** Pierwszy endpoint (GET /api/churn/all)

---

**Status:** 🟢 Gotowy do startu!
**Ostatnia aktualizacja:** 2026-03-01
