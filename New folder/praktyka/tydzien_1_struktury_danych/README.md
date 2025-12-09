# 📚 TYDZIEŃ 1: STRUKTURY DANYCH

## 🎯 Cel tygodnia
Opanować podstawowe struktury danych w Python: **listy, słowniki, tuple, sets**

---

## 📋 Plan tygodnia

### 🔰 Etap 1: Ćwiczenia rozgrzewkowe (1-2 dni)
**Folder:** `0_przykladowe_cwiczenia/`

Trzy proste ćwiczenia na rozgrzewkę:
- [ ] Ćwiczenie 1: Lista owoców (ŁATWE, 5-10 min)
- [ ] Ćwiczenie 2: Ulubione kolory (ŚREDNIE, 10-15 min)
- [ ] Ćwiczenie 3: Kalkulator liczb (TRUDNIEJSZE, 15-20 min)

**Czego się nauczysz:**
- Tworzenie list: `lista = []`
- Dodawanie elementów: `append()`
- Pętle: `for`, `while`
- Pobieranie danych: `input()`
- Warunki: `if`, `break`

---

### 💪 Etap 2: Zadania główne (3-5 dni)

#### Zadanie 1.1: Lista zakupów
**Folder:** `1_lista_zakupow/`
**Czas:** 30-60 min
**Poziom:** ⭐⭐☆☆☆

Program z interaktywnym menu:
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl listę
4. Posortuj alfabetycznie
5. Wyjście

**Naucz się:** listy, menu, pętle nieskończone, `sort()`

---

#### Zadanie 1.2: Słownik produktów
**Folder:** `2_slownik_produktow/`
**Czas:** 45-90 min
**Poziom:** ⭐⭐⭐☆☆

Program zarządzający produktami (nazwa → cena):
- Dodaj produkt
- Usuń produkt
- Znajdź najtańszy
- Znajdź najdroższy
- Wyświetl wszystkie

**Naucz się:** słowniki `{}`, `.keys()`, `.values()`, `.items()`, `min()`, `max()`

---

#### Zadanie 1.3: Analiza zamówień
**Folder:** `3_analiza_zamowien/`
**Czas:** 60-120 min
**Poziom:** ⭐⭐⭐⭐☆

Analiza listy zamówień (tuple):
```python
zamowienia = [
    ("Laptop", 3500.00, 2),
    ("Mysz", 45.50, 5),
    ("Klawiatura", 120.00, 3),
    ...
]
```

Oblicz:
- Suma wszystkich zamówień
- Średnia cena produktu
- Najczęściej zamawiany produkt
- Całkowita wartość zamówień (cena × ilość)

**Naucz się:** tuple `()`, iteracja, agregacje, `sum()`, statystyki

---

## 📖 Jak korzystać z materiałów?

### Krok 1: Przeczytaj zadanie
Otwórz plik `zadanie.md` w folderze zadania

### Krok 2: Otwórz szablon
Otwórz plik `szablon.py` - to tam będziesz pisać kod

### Krok 3: Szukaj TODO
W szablonie znajdziesz komentarze:
```python
# TODO: Stwórz pustą listę zakupów
# TODO: Wyświetl menu z opcjami
```

### Krok 4: Wypełnij TODO
**WAŻNE:** Nie kopiuj gotowych rozwiązań! Spróbuj sam, nawet jeśli będzie błąd.

### Krok 5: Testuj
Uruchom program:
```bash
python szablon.py
```

### Krok 6: Poproś o review
Gdy skończysz, wskaż ścieżkę do pliku i poproś o sprawdzenie:
```
Sprawdź mój kod: C:\projekty\praktyka\tydzien_1_struktury_danych\1_lista_zakupow\szablon.py
```

### Krok 7: (Ostateczność) Rozwiązanie
Jeśli **kompletnie** utkniesz, możesz zajrzeć do `rozwiazanie.py`
**Ale spróbuj najpierw sam!**

---

## 🎓 Teoria - Struktury Danych

### Lista `[]`
```python
# Tworzenie
lista = []
lista = ["jabłko", "banan", "gruszka"]

# Operacje
lista.append("pomarańcza")  # Dodaj na koniec
lista.remove("banan")       # Usuń element
lista.sort()                # Sortuj alfabetycznie
len(lista)                  # Długość listy
```

### Słownik `{}`
```python
# Tworzenie
slownik = {}
slownik = {"jabłko": 3.50, "banan": 2.00}

# Operacje
slownik["gruszka"] = 4.20   # Dodaj/zmień
del slownik["banan"]        # Usuń
slownik.keys()              # Wszystkie klucze
slownik.values()            # Wszystkie wartości
slownik.items()             # Pary klucz-wartość
```

### Tuple `()`
```python
# Tworzenie (niezmienne!)
krotka = ("Laptop", 3500, 2)
produkt, cena, ilosc = krotka  # Rozpakowanie

# Dostęp
krotka[0]  # "Laptop"
krotka[1]  # 3500
```

### Set `{}`
```python
# Tworzenie (unikalne wartości)
zbior = {1, 2, 3, 3, 3}  # {1, 2, 3}

# Operacje
zbior.add(4)
zbior.remove(2)
```

---

## 💡 Wskazówki ogólne

### Debugowanie
Jeśli coś nie działa:
1. **Przeczytaj błąd** - Python dokładnie mówi co jest nie tak
2. **print()** - dodaj `print()` w różnych miejscach żeby zobaczyć wartości
3. **Sprawdź wcięcia** - Python wymaga poprawnych wcięć (4 spacje lub Tab)
4. **Literówki** - sprawdź czy nazwy zmiennych są poprawne

### Częste błędy
```python
# ŹLE: Lista nie istnieje
produkty.append("jabłko")  # NameError

# DOBRZE: Najpierw stwórz
produkty = []
produkty.append("jabłko")

# ŹLE: Próba modyfikacji tuple
zamowienie = ("Laptop", 3500)
zamowienie[1] = 4000  # TypeError: tuple object does not support item assignment

# DOBRZE: Użyj listy jeśli chcesz modyfikować
zamowienie = ["Laptop", 3500]
zamowienie[1] = 4000
```

---

## 📊 Tracking postępów

Zaznacz po ukończeniu:

### Ćwiczenia rozgrzewkowe:
- [ ] cwiczenie_1_owoce.py
- [ ] cwiczenie_2_kolory.py
- [ ] cwiczenie_3_liczby.py

### Zadania główne:
- [ ] Zadanie 1.1: Lista zakupów
- [ ] Zadanie 1.2: Słownik produktów
- [ ] Zadanie 1.3: Analiza zamówień

### Zrozumienie koncepcji:
- [ ] Rozumiem czym jest lista i jak jej używać
- [ ] Rozumiem czym jest słownik i kiedy go stosować
- [ ] Rozumiem różnicę między listą a tuple
- [ ] Potrafię iterować po strukturach danych
- [ ] Potrafię używać podstawowych funkcji (len, sum, min, max)

---

## 🔗 Linki do materiałów

### Dokumentacja:
- [Python Docs: Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [W3Schools: Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [W3Schools: Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)

### Kursy:
- [Real Python: Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [Real Python: Dictionaries](https://realpython.com/python-dicts/)

---

## 🚀 Co dalej?

Po ukończeniu Tygodnia 1:
1. ✅ Sprawdź czy zaznaczyłeś wszystkie checkboxy
2. ✅ Przejrzyj swój kod sprzed tygodnia - co możesz poprawić?
3. ✅ Przejdź do **Tydzień 2: Funkcje i Moduły**

---

## 💪 Pamiętaj!

> **"Programowanie to umiejętność praktyczna - nie wystarczy czytać, musisz PISAĆ KOD!"**

- Błędy to część nauki
- Każdy programista Google'uje problemy
- Konsystencja > intensywność (30 min dziennie lepsze niż 5h raz w tygodniu)
- Nie kopiuj gotowych rozwiązań - próbuj sam!

**Powodzenia!** 🎯
