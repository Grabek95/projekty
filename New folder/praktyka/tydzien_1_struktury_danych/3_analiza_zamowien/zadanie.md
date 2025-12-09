# 📝 ZADANIE 1.3: Analiza zamówień

## 🎯 Cel
Nauczyć się pracy z **tuple** (krotkami) i wykonywania analiz statystycznych na danych.

---

## 📋 Specyfikacja

Masz listę zamówień. Każde zamówienie to **tuple** z 3 elementami:
```python
(nazwa_produktu, cena_jednostkowa, ilość)
```

Przykład:
```python
zamowienia = [
    ("Laptop", 3500.00, 2),
    ("Mysz", 45.50, 5),
    ("Klawiatura", 120.00, 3),
    ("Monitor", 890.00, 1),
    ("Słuchawki", 180.00, 4)
]
```

### Zadanie:
Napisz program który **analizuje** listę zamówień i wyświetla:

1. **Liczbę zamówień** - ile pozycji jest na liście
2. **Sumę cen jednostkowych** - suma wszystkich cen (bez uwzględniania ilości)
3. **Średnią cenę produktu** - średnia z cen jednostkowych
4. **Najtańszy produkt** - produkt o najniższej cenie jednostkowej
5. **Najdroższy produkt** - produkt o najwyższej cenie jednostkowej
6. **Całkowitą wartość zamówień** - suma (cena × ilość) dla wszystkich pozycji
7. **Najczęściej zamawiany produkt** - produkt o największej ilości

---

## 🎨 Przykładowy output programu

```
=== ANALIZA ZAMÓWIEŃ ===

LISTA ZAMÓWIEŃ:
1. Laptop: 3500.00 PLN x 2 szt. = 7000.00 PLN
2. Mysz: 45.50 PLN x 5 szt. = 227.50 PLN
3. Klawiatura: 120.00 PLN x 3 szt. = 360.00 PLN
4. Monitor: 890.00 PLN x 1 szt. = 890.00 PLN
5. Słuchawki: 180.00 PLN x 4 szt. = 720.00 PLN

========================================
STATYSTYKI:
========================================
Liczba zamówień:              5
Suma cen jednostkowych:       4735.50 PLN
Średnia cena produktu:        947.10 PLN
Najtańszy produkt:            Mysz (45.50 PLN)
Najdroższy produkt:           Laptop (3500.00 PLN)
Całkowita wartość zamówień:   9197.50 PLN
Najczęściej zamawiany:        Mysz (5 szt.)
```

---

## ✅ Kryteria akceptacji

Program działa poprawnie jeśli:
- [ ] Wyświetla wszystkie zamówienia w czytelnej formie
- [ ] Oblicza liczbę zamówień (ile pozycji)
- [ ] Oblicza sumę cen jednostkowych
- [ ] Oblicza średnią cenę produktu
- [ ] Znajduje najtańszy produkt
- [ ] Znajduje najdroższy produkt
- [ ] Oblicza całkowitą wartość (suma cena × ilość)
- [ ] Znajduje produkt o największej ilości
- [ ] Wszystkie liczby są sformatowane z 2 miejscami po przecinku

---

## 💡 Wskazówki

### Czym jest tuple?
Tuple to **niezmienne** listy. Używa się nawiasów okrągłych `()`:
```python
produkt = ("Laptop", 3500.00, 2)

# Dostęp do elementów (jak w liście):
nazwa = produkt[0]    # "Laptop"
cena = produkt[1]     # 3500.00
ilosc = produkt[2]    # 2

# Rozpakowanie (unpacking):
nazwa, cena, ilosc = produkt
```

### Iteracja po liście tuple
```python
zamowienia = [
    ("Laptop", 3500.00, 2),
    ("Mysz", 45.50, 5)
]

for zamowienie in zamowienia:
    nazwa = zamowienie[0]
    cena = zamowienie[1]
    ilosc = zamowienie[2]
    print(f"{nazwa}: {cena} PLN x {ilosc} szt.")

# Lub krócej (z rozpakowaniem):
for nazwa, cena, ilosc in zamowienia:
    print(f"{nazwa}: {cena} PLN x {ilosc} szt.")
```

### Obliczenia

**Liczba zamówień:**
```python
liczba = len(zamowienia)
```

**Suma cen (tylko ceny, bez ilości):**
```python
suma_cen = 0
for nazwa, cena, ilosc in zamowienia:
    suma_cen += cena

# Lub krócej:
suma_cen = sum(cena for nazwa, cena, ilosc in zamowienia)
```

**Średnia:**
```python
srednia = suma_cen / len(zamowienia)
```

**Najtańszy produkt:**
```python
# Metoda 1: Ręcznie
min_cena = float('inf')  # Nieskończoność
min_nazwa = ""
for nazwa, cena, ilosc in zamowienia:
    if cena < min_cena:
        min_cena = cena
        min_nazwa = nazwa

# Metoda 2: Funkcja min() z kluczem
najtanszy = min(zamowienia, key=lambda x: x[1])
# najtanszy to cały tuple, x[1] to cena
min_nazwa = najtanszy[0]
min_cena = najtanszy[1]
```

**Całkowita wartość (cena × ilość):**
```python
total = 0
for nazwa, cena, ilosc in zamowienia:
    total += cena * ilosc

# Lub krócej:
total = sum(cena * ilosc for nazwa, cena, ilosc in zamowienia)
```

**Produkt o największej ilości:**
```python
# Metoda 1: Ręcznie
max_ilosc = 0
max_nazwa = ""
for nazwa, cena, ilosc in zamowienia:
    if ilosc > max_ilosc:
        max_ilosc = ilosc
        max_nazwa = nazwa

# Metoda 2: Funkcja max()
najczestszy = max(zamowienia, key=lambda x: x[2])
# x[2] to ilość
```

---

## 🚨 Typowe problemy i rozwiązania

### Problem 1: Nie wiem co to lambda
**Wyjaśnienie:** Lambda to anonimowa funkcja (poznasz ją później)
**Rozwiązanie na teraz:** Użyj metody ręcznej (pętli for) zamiast lambda

### Problem 2: Błąd przy rozpakowywaniu
```
ValueError: too many values to unpack
```
**Przyczyna:** Próbujesz rozpakować tuple do niewłaściwej liczby zmiennych
**Rozwiązanie:**
```python
# ŹLE: Tuple ma 3 elementy, rozpakowujesz do 2
nazwa, cena = ("Laptop", 3500, 2)

# DOBRZE:
nazwa, cena, ilosc = ("Laptop", 3500, 2)
```

### Problem 3: Średnia się nie zgadza
**Przyczyna:** Dzielisz przez złą liczbę
**Rozwiązanie:** Średnia = suma_cen / len(zamowienia), NIE / suma_ilosci

---

## 🎓 Czego się nauczysz?

Po wykonaniu tego zadania będziesz potrafił:
- ✅ Używać tuple do przechowywania danych
- ✅ Rozpakowywać tuple (unpacking)
- ✅ Iterować po liście tuple
- ✅ Obliczać statystyki (suma, średnia, min, max)
- ✅ Znajdować elementy spełniające warunki
- ✅ Wykonywać obliczenia na zagnieżdżonych strukturach
- ✅ Rozumieć różnicę między listą a tuple

---

## 🤔 Dlaczego tuple zamiast listy?

### Lista (zmienne):
```python
zamowienie = ["Laptop", 3500.00, 2]
zamowienie[0] = "Monitor"  # Można zmienić - RYZYKO!
```

### Tuple (niezmienne):
```python
zamowienie = ("Laptop", 3500.00, 2)
zamowienie[0] = "Monitor"  # BŁĄD! TypeError
```

**Wniosek:** Gdy dane NIE POWINNY się zmieniać (np. zamówienie już złożone), używaj tuple!

---

## 🚀 Rozszerzenia (opcjonalne)

1. **Sortowanie:** Wyświetl zamówienia posortowane od najdroższego
2. **Filtrowanie:** Pokaż tylko zamówienia o wartości > 500 PLN
3. **Statystyki ilości:** Całkowita liczba wszystkich produktów (suma ilości)
4. **Kategorie cenowe:**
   - Tanie (< 100 PLN)
   - Średnie (100-1000 PLN)
   - Drogie (> 1000 PLN)
5. **Interaktywność:** Pozwól użytkownikowi dodać nowe zamówienie

---

## 📁 Pliki

- `zadanie.md` ← jesteś tutaj
- `szablon.py` ← tu piszesz kod
- `dane_testowe.py` ← przykładowe dane (możesz użyć lub stworzyć własne)
- `rozwiazanie.py` ← rozwiązanie (tylko gdy utkniesz!)

---

**Powodzenia!** 🎯

💡 **Tip:** To zadanie jest trudniejsze niż poprzednie. Nie zrażaj się - rób krok po kroku!
