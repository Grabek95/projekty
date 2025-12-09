# 📝 ZADANIE 1.2: Słownik produktów

## 🎯 Cel
Nauczyć się pracy ze słownikami (dictionary) - strukturą klucz-wartość.

---

## 📋 Specyfikacja

Program zarządza słownikiem produktów, gdzie:
- **Klucz** = nazwa produktu (string)
- **Wartość** = cena produktu (float)

Przykład:
```python
produkty = {
    "Mleko": 3.50,
    "Chleb": 4.20,
    "Masło": 6.50
}
```

### Menu:
```
=== SŁOWNIK PRODUKTÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl wszystkie produkty
4. Znajdź najtańszy produkt
5. Znajdź najdroższy produkt
6. Wyjście

Wybierz opcję (1-6):
```

### Funkcjonalność opcji:

**1. Dodaj produkt**
- Zapytaj o nazwę produktu
- Zapytaj o cenę produktu (zamień na float)
- Dodaj do słownika
- Wyświetl: "Dodano: {nazwa} - {cena} PLN"

**2. Usuń produkt**
- Jeśli słownik pusty → "Słownik jest pusty!"
- Zapytaj o nazwę produktu
- Jeśli produkt istnieje → usuń i wyświetl "Usunięto: {nazwa}"
- Jeśli nie istnieje → "Produkt nie znaleziony!"

**3. Wyświetl wszystkie produkty**
- Jeśli słownik pusty → "Słownik jest pusty!"
- W przeciwnym razie wyświetl wszystkie produkty:
  ```
  Lista produktów:
  - Mleko: 3.50 PLN
  - Chleb: 4.20 PLN
  - Masło: 6.50 PLN
  ```

**4. Znajdź najtańszy produkt**
- Jeśli słownik pusty → "Słownik jest pusty!"
- Znajdź produkt z najniższą ceną
- Wyświetl: "Najtańszy: {nazwa} - {cena} PLN"

**5. Znajdź najdroższy produkt**
- Jeśli słownik pusty → "Słownik jest pusty!"
- Znajdź produkt z najwyższą ceną
- Wyświetl: "Najdroższy: {nazwa} - {cena} PLN"

**6. Wyjście**
- Wyświetl "Do widzenia!"
- Zakończ program

---

## 🎨 Przykładowe działanie programu

```
=== SŁOWNIK PRODUKTÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl wszystkie produkty
4. Znajdź najtańszy produkt
5. Znajdź najdroższy produkt
6. Wyjście

Wybierz opcję (1-6): 1
Podaj nazwę produktu: Mleko
Podaj cenę produktu: 3.50
Dodano: Mleko - 3.50 PLN

=== SŁOWNIK PRODUKTÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl wszystkie produkty
4. Znajdź najtańszy produkt
5. Znajdź najdroższy produkt
6. Wyjście

Wybierz opcję (1-6): 1
Podaj nazwę produktu: Chleb
Podaj cenę produktu: 4.20
Dodano: Chleb - 4.20 PLN

=== SŁOWNIK PRODUKTÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl wszystkie produkty
4. Znajdź najtańszy produkt
5. Znajdź najdroższy produkt
6. Wyjście

Wybierz opcję (1-6): 3
Lista produktów:
- Mleko: 3.50 PLN
- Chleb: 4.20 PLN

=== SŁOWNIK PRODUKTÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl wszystkie produkty
4. Znajdź najtańszy produkt
5. Znajdź najdroższy produkt
6. Wyjście

Wybierz opcję (1-6): 4
Najtańszy: Mleko - 3.50 PLN

=== SŁOWNIK PRODUKTÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl wszystkie produkty
4. Znajdź najtańszy produkt
5. Znajdź najdroższy produkt
6. Wyjście

Wybierz opcję (1-6): 6
Do widzenia!
```

---

## ✅ Kryteria akceptacji

Program działa poprawnie jeśli:
- [ ] Opcja 1 dodaje produkty do słownika (nazwa → cena)
- [ ] Opcja 2 usuwa produkty ze słownika
- [ ] Opcja 3 wyświetla wszystkie produkty
- [ ] Opcja 4 znajduje i wyświetla najtańszy produkt
- [ ] Opcja 5 znajduje i wyświetla najdroższy produkt
- [ ] Opcja 6 kończy program
- [ ] Program obsługuje pusty słownik (nie wysypuje się)
- [ ] Ceny są wyświetlane z 2 miejscami po przecinku

---

## 💡 Wskazówki

### Operacje na słowniku

**Tworzenie pustego słownika:**
```python
produkty = {}
```

**Dodawanie elementu:**
```python
produkty["Mleko"] = 3.50
# lub z inputu:
nazwa = input("Nazwa: ")
cena = float(input("Cena: "))
produkty[nazwa] = cena
```

**Usuwanie elementu:**
```python
del produkty["Mleko"]
```

**Sprawdzanie czy klucz istnieje:**
```python
if "Mleko" in produkty:
    print("Mleko jest w słowniku")
```

**Iteracja po słowniku:**
```python
# Metoda 1: Po kluczach i wartościach
for nazwa, cena in produkty.items():
    print(f"{nazwa}: {cena} PLN")

# Metoda 2: Tylko po kluczach
for nazwa in produkty.keys():
    print(nazwa)

# Metoda 3: Tylko po wartościach
for cena in produkty.values():
    print(cena)
```

**Znalezienie min/max:**
```python
# Najtańszy (minimalna wartość)
min_cena = min(produkty.values())

# Ale jak znaleźć NAZWĘ produktu z min ceną?
# Metoda 1:
najtanszy = min(produkty, key=produkty.get)
# najtanszy to klucz (nazwa) produktu o najniższej wartości (cenie)

# Metoda 2 (bardziej zrozumiała):
min_cena = min(produkty.values())
for nazwa, cena in produkty.items():
    if cena == min_cena:
        print(f"{nazwa}: {cena}")
        break
```

**Formatowanie ceny (2 miejsca po przecinku):**
```python
cena = 3.5
print(f"{cena:.2f} PLN")  # Wyświetli: 3.50 PLN
```

---

## 🚨 Typowe problemy i rozwiązania

### Problem 1: KeyError przy usuwaniu
```
KeyError: 'Mleko'
```
**Przyczyna:** Próba usunięcia klucza którego nie ma
**Rozwiązanie:** Sprawdź `if nazwa in produkty:` PRZED `del produkty[nazwa]`

### Problem 2: ValueError przy konwersji ceny
```
ValueError: could not convert string to float: 'abc'
```
**Przyczyna:** Użytkownik wpisał tekst zamiast liczby
**Rozwiązanie (na razie):** Zakładamy że użytkownik wpisze poprawną liczbę
**Rozwiązanie (zaawansowane):** Użyj try/except (poznasz później)

### Problem 3: min() z pustego słownika
```
ValueError: min() arg is an empty sequence
```
**Przyczyna:** Próba znalezienia min/max w pustym słowniku
**Rozwiązanie:** Sprawdź `if len(produkty) == 0:` PRZED użyciem min/max

### Problem 4: Cena wyświetla się jako 3.5 zamiast 3.50
**Rozwiązanie:** Użyj formatowania `f"{cena:.2f}"`

---

## 🎓 Czego się nauczysz?

Po wykonaniu tego zadania będziesz potrafił:
- ✅ Tworzyć i używać słowników (dict)
- ✅ Dodawać i usuwać elementy ze słownika
- ✅ Iterować po słowniku (.items(), .keys(), .values())
- ✅ Znajdować minimum i maximum w słowniku
- ✅ Konwertować typy (float)
- ✅ Formatować liczby zmiennoprzecinkowe (.2f)
- ✅ Rozumieć różnicę między listą a słownikiem

---

## 🤔 Dlaczego słownik zamiast listy?

### Lista:
```python
produkty = ["Mleko", "Chleb", "Masło"]
ceny = [3.50, 4.20, 6.50]
# Musisz pamiętać że produkty[0] odpowiada ceny[0]
# Niewygodne!
```

### Słownik:
```python
produkty = {
    "Mleko": 3.50,
    "Chleb": 4.20,
    "Masło": 6.50
}
# Logiczne powiązanie: nazwa -> cena
# Łatwy dostęp: produkty["Mleko"]
```

**Wniosek:** Gdy masz pary klucz-wartość, używaj słownika!

---

## 🚀 Rozszerzenia (opcjonalne)

1. **Aktualizacja ceny:** Dodaj opcję zmiany ceny istniejącego produktu
2. **Sortowanie:** Wyświetl produkty posortowane alfabetycznie po nazwie
3. **Średnia cena:** Oblicz średnią cenę wszystkich produktów
4. **Filtrowanie:** Wyświetl tylko produkty droższe niż X PLN
5. **Zniżka:** Dodaj opcję obniżenia wszystkich cen o 10%

---

## 📁 Pliki

- `zadanie.md` ← jesteś tutaj
- `szablon.py` ← tu piszesz kod
- `rozwiazanie.py` ← rozwiązanie (tylko gdy utkniesz!)

---

**Powodzenia!** 🎯
