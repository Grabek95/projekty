# 📝 ZADANIE 1.1: Lista zakupów

## 🎯 Cel
Stworzyć interaktywny program do zarządzania listą zakupów z menu wyboru opcji.

---

## 📋 Specyfikacja

Program wyświetla menu z 5 opcjami i wykonuje wybrane operacje w pętli nieskończonej, aż użytkownik wybierze "Wyjście".

### Menu:
```
=== LISTA ZAKUPÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl listę
4. Posortuj alfabetycznie
5. Wyjście

Wybierz opcję (1-5):
```

### Funkcjonalność opcji:

**1. Dodaj produkt**
- Zapytaj użytkownika: "Podaj nazwę produktu: "
- Dodaj produkt do listy
- Wyświetl: "Dodano produkt: {nazwa}"

**2. Usuń produkt**
- Jeśli lista jest pusta → wyświetl "Lista jest pusta!"
- W przeciwnym razie:
  - Zapytaj: "Podaj nazwę produktu do usunięcia: "
  - Jeśli produkt istnieje → usuń go i wyświetl "Usunięto produkt: {nazwa}"
  - Jeśli nie istnieje → wyświetl "Produkt nie znaleziony!"

**3. Wyświetl listę**
- Jeśli lista jest pusta → wyświetl "Lista jest pusta!"
- W przeciwnym razie:
  ```
  Twoja lista zakupów:
  1. Mleko
  2. Chleb
  3. Masło
  ```

**4. Posortuj alfabetycznie**
- Posortuj listę alfabetycznie (A-Z)
- Wyświetl: "Lista została posortowana!"

**5. Wyjście**
- Wyświetl "Do widzenia!"
- Zakończ program (break)

---

## 🎨 Przykładowe działanie programu

```
=== LISTA ZAKUPÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl listę
4. Posortuj alfabetycznie
5. Wyjście

Wybierz opcję (1-5): 1
Podaj nazwę produktu: Mleko
Dodano produkt: Mleko

=== LISTA ZAKUPÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl listę
4. Posortuj alfabetycznie
5. Wyjście

Wybierz opcję (1-5): 1
Podaj nazwę produktu: Chleb
Dodano produkt: Chleb

=== LISTA ZAKUPÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl listę
4. Posortuj alfabetycznie
5. Wyjście

Wybierz opcję (1-5): 3
Twoja lista zakupów:
1. Mleko
2. Chleb

=== LISTA ZAKUPÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl listę
4. Posortuj alfabetycznie
5. Wyjście

Wybierz opcję (1-5): 4
Lista została posortowana!

=== LISTA ZAKUPÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl listę
4. Posortuj alfabetycznie
5. Wyjście

Wybierz opcję (1-5): 3
Twoja lista zakupów:
1. Chleb
2. Mleko

=== LISTA ZAKUPÓW ===
1. Dodaj produkt
2. Usuń produkt
3. Wyświetl listę
4. Posortuj alfabetycznie
5. Wyjście

Wybierz opcję (1-5): 5
Do widzenia!
```

---

## ✅ Kryteria akceptacji

Program działa poprawnie jeśli:
- [ ] Menu wyświetla się w pętli po każdej operacji
- [ ] Opcja 1 dodaje produkty do listy
- [ ] Opcja 2 usuwa produkty z listy (z obsługą błędów)
- [ ] Opcja 3 wyświetla listę z numerami
- [ ] Opcja 4 sortuje listę alfabetycznie
- [ ] Opcja 5 kończy program
- [ ] Program obsługuje pustą listę (nie wysypuje się)
- [ ] Program obsługuje nieprawidłowy wybór (nie opcja 1-5)

---

## 💡 Wskazówki

### Struktura programu
```python
# 1. Stwórz pustą listę zakupów
zakupy = []

# 2. Pętla nieskończona
while True:
    # 3. Wyświetl menu
    # 4. Pobierz wybór użytkownika
    # 5. Obsłuż wybór (if/elif/else)
```

### Przydatne metody i funkcje

**Dodawanie do listy:**
```python
lista.append(element)
```

**Usuwanie z listy:**
```python
lista.remove(element)  # Usuwa element (jeśli istnieje)
```

**Sortowanie:**
```python
lista.sort()  # Sortuje w miejscu (modyfikuje listę)
```

**Sprawdzanie czy lista pusta:**
```python
if len(lista) == 0:
    print("Lista pusta")
# lub krócej:
if not lista:
    print("Lista pusta")
```

**Sprawdzanie czy element jest w liście:**
```python
if produkt in lista:
    print("Produkt istnieje")
```

**Wyświetlanie z numerami:**
```python
for index, produkt in enumerate(lista, start=1):
    print(f"{index}. {produkt}")
```

---

## 🚨 Typowe problemy i rozwiązania

### Problem 1: Program się kończy po jednej operacji
**Przyczyna:** Brak pętli `while True`
**Rozwiązanie:** Owiń całą logikę menu w `while True:`

### Problem 2: ValueError przy usuwaniu
```
ValueError: list.remove(x): x not in list
```
**Przyczyna:** Próba usunięcia produktu którego nie ma
**Rozwiązanie:** Sprawdź `if produkt in zakupy:` PRZED usunięciem

### Problem 3: Menu wyświetla się cały czas
**Przyczyna:** Brak `input()` - program nie czeka na użytkownika
**Rozwiązanie:** Dodaj `wybor = input("Wybierz opcję: ")`

### Problem 4: Nieprawidłowy wybór powoduje błąd
**Przyczyna:** Brak obsługi dla opcji innych niż 1-5
**Rozwiązanie:** Dodaj ostatnie `else:` które wyświetli "Nieprawidłowy wybór"

---

## 🎓 Czego się nauczysz?

Po wykonaniu tego zadania będziesz potrafił:
- ✅ Tworzyć interaktywne menu w pętli
- ✅ Obsługiwać wybór użytkownika (if/elif/else)
- ✅ Dodawać i usuwać elementy z listy
- ✅ Sortować listę
- ✅ Walidować dane (sprawdzać czy element istnieje)
- ✅ Obsługiwać edge cases (pusta lista)
- ✅ Formatować output (enumerate)

---

## 🚀 Rozszerzenia (opcjonalne)

Jeśli chcesz dodać więcej funkcjonalności:

1. **Podwójne produkty:** Nie pozwalaj dodać produktu który już istnieje
2. **Licznik:** Wyświetl ile produktów jest na liście
3. **Wyczyść listę:** Dodaj opcję 6 która czyści całą listę
4. **Zapisz do pliku:** Dodaj opcję zapisu listy do pliku .txt
5. **Case-insensitive:** Traktuj "Mleko" i "mleko" jako ten sam produkt

---

## 📁 Pliki

- `zadanie.md` ← jesteś tutaj
- `szablon.py` ← tu piszesz kod
- `rozwiazanie.py` ← rozwiązanie (tylko gdy utkniesz!)

---

**Powodzenia! Pamiętaj - najpierw spróbuj sam, potem pytaj o pomoc!** 💪
