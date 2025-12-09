# 📚 ĆWICZENIA - APPEND() I LISTY

## 🎯 Cel
Nauczyć się dodawania elementów do listy używając metody `append()`

---

## 📋 Jak korzystać z tych ćwiczeń?

### Krok 1: Zacznij od Ćwiczenia 1
```bash
python cwiczenie_1_owoce.py
```

### Krok 2: Przeczytaj komentarze TODO
W każdym pliku są komentarze `# TODO:` - to miejsca gdzie musisz dopisać kod

### Krok 3: Uzupełnij brakujący kod
Nie kopiuj! Spróbuj napisać sam, nawet jeśli nie wiesz czy będzie dobrze

### Krok 4: Uruchom i testuj
Uruchom program i zobacz czy działa. Jeśli nie - to świetnie! Błędy uczą najwięcej!

### Krok 5: Sprawdź rozwiązanie (tylko jeśli utkniesz)
```bash
python ROZWIAZANIA.py
```

---

## 📝 Ćwiczenia

### ✅ Ćwiczenie 1: Lista owoców (ŁATWE)
**Plik:** `cwiczenie_1_owoce.py`
**Czas:** 5-10 minut
**Czego się nauczysz:**
- Tworzenie pustej listy: `lista = []`
- Pobieranie danych: `input()`
- Dodawanie do listy: `lista.append(element)`
- Wyświetlanie: `print()`

**Co musisz zrobić:**
1. Zapytać użytkownika o 3 owoce
2. Dodać je do listy
3. Wyświetlić całą listę

---

### ✅ Ćwiczenie 2: Ulubione kolory (ŚREDNIE)
**Plik:** `cwiczenie_2_kolory.py`
**Czas:** 10-15 minut
**Czego się nauczysz:**
- Pętla `for` z `range()`
- Warunek `if` i `break`
- Sprawdzanie czy element jest w liście: `if x in lista`

**Co musisz zrobić:**
1. Pętla 5 razy pyta o kolor
2. Jeśli użytkownik wpisze "stop" - przerwij
3. Dodaj kolory do listy
4. Wyświetl wszystkie kolory
5. BONUS: Sprawdź czy "czerwony" jest na liście

---

### ✅ Ćwiczenie 3: Kalkulator liczb (TRUDNIEJSZE)
**Plik:** `cwiczenie_3_liczby.py`
**Czas:** 15-20 minut
**Czego się nauczysz:**
- Pętla `while True`
- Konwersja typu: `float()`
- Funkcje matematyczne: `sum()`, `min()`, `max()`
- Obliczanie średniej

**Co musisz zrobić:**
1. Pętla nieskończona zbiera liczby
2. Jeśli użytkownik wpisze 0 - zakończ
3. Dodaj liczby do listy
4. Oblicz sumę, średnią, min, max
5. Wyświetl wyniki

---

## 💡 Wskazówki

### Podstawowe polecenia które musisz znać:

```python
# 1. Tworzenie pustej listy
moja_lista = []

# 2. Dodawanie elementu
moja_lista.append("element")

# 3. Pobieranie od użytkownika
zmienna = input("Podaj coś: ")

# 4. Wyświetlanie
print(moja_lista)

# 5. Długość listy
dlugosc = len(moja_lista)

# 6. Pętla po liście
for element in moja_lista:
    print(element)

# 7. Sprawdzanie czy element jest w liście
if "cos" in moja_lista:
    print("Jest!")
```

---

## 🚨 Częste błędy (i jak je naprawić)

### Błąd 1: Lista nie istnieje
```python
# ŹLE:
lista.append("element")  # NameError: name 'lista' is not defined

# DOBRZE:
lista = []  # Najpierw stwórz listę!
lista.append("element")
```

### Błąd 2: Zapomniałeś nawiasów
```python
# ŹLE:
lista.append "element"  # SyntaxError

# DOBRZE:
lista.append("element")
```

### Błąd 3: Próbujesz dodać do stringa zamiast listy
```python
# ŹLE:
lista = ""
lista.append("x")  # AttributeError: 'str' object has no attribute 'append'

# DOBRZE:
lista = []  # Lista to [], nie ""
lista.append("x")
```

---

## ✅ Sprawdzian - czy rozumiesz?

Po zrobieniu ćwiczeń, odpowiedz na pytania:

1. **Co robi `append()`?**
   - Odpowiedź: Dodaje element na koniec listy

2. **Jak stworzyć pustą listę?**
   - Odpowiedź: `lista = []`

3. **Jak sprawdzić ile elementów jest w liście?**
   - Odpowiedź: `len(lista)`

4. **Jak wyświetlić wszystkie elementy?**
   - Odpowiedź: `for element in lista: print(element)`

Jeśli znasz odpowiedzi - **gratulacje!** Rozumiesz podstawy! 🎉

---

## 🚀 Co dalej?

Po ukończeniu tych 3 ćwiczeń:

1. ✅ Przejdź do [ZADANIA_TYDZIEN_1.py](../Sklep/ZADANIA_TYDZIEN_1.py)
2. ✅ Spróbuj samodzielnie napisać prosty program
3. ✅ Jutro: Naucz się słowników (dictionary)

---

## 📊 Tracking postępów

Zaznacz gdy ukończysz:

- [x] Ćwiczenie 1 (owoce)
- [x] Ćwiczenie 2 (kolory)
- [x] Ćwiczenie 3 (liczby)
- [x] Zrozumiałem `append()`
- [x] Potrafię użyć tego w swoim kodzie

---

## 💪 Pamiętaj!

> **"Błędy to nie porażki - to lekcje!"**

Jeśli coś nie działa:
1. Przeczytaj komunikat błędu
2. Sprawdź czy nie ma literówki
3. Porównaj z przykładem
4. Google'uj błąd
5. Sprawdź rozwiązanie

**Powodzenia!** 🚀
