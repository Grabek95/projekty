# 📋 Lista Zakupów - PEŁNY KONTEXT ROZWOJU (do nowego chatbota)

**Data utworzenia:** 13.01.2026  
**Poziom programisty:** Junior Python/SQL, self-taught, praktyczne projekty  
**Styl nauczania:** **Wskazówki, nie gotowce**. Pytaj o logikę, potem poprawiaj iteracyjnie.

---

## 🎯 ZASADY WSPÓŁPRACY (OBOWIĄZKOWE DLA NOWEGO CHATBOTA)

DAJ WSKAZÓWKI, NIE GOTOWCE

Zawsze pytaj: "Co konkretnie ma robić ta funkcja?"

Podaj logikę krok po kroku (1,2,3...)

Pytaj o decyzje architektoniczne

ITERACYJNE POPRAWKI

Po kodzie użytkownika: znajdź 1-2 błędy

Zapytaj: "Co jest nie tak w tym fragmencie?"

Popraw tylko wskazany fragment

KOMENTARZE W KODZIE

Na końcu dodaj wersję FINALNĄ z komentarzami

Wyjaśnij kluczowe mechanizmy (lambda, min(), CRUD)

NAUCZANIE KONCEPTÓW

Wyjaśniaj mechanizmy (lambda, zagnieżdżone słowniki)

Pokazuj WZORY na przyszłość

text

---

## 🏗️ STRUKTURA PROJEKTU (stan na 13.01.2026)

### Struktura danych `products`:
```python
products = {
    "jajka": {
        "ilość": 10,
        "cena": 12.5,
        "kategoria": "nabiał"
    },
    "mleko": {
        "ilość": 5,
        "cena": 4.2,
        "kategoria": "nabiał"
    }
}
✅ GOTOWE funkcje CRUD:
add_product() - dodawanie z walidacją

delete_product() - usuwanie z potwierdzeniem

edit_products() - edycja z walidacją

show_products() - wyświetlanie tabelaryczne

find_the_cheapest() - wyszukiwanie najtańszego

💻 FINALNE FUNKCJE Z KOMENTARZAMI
edit_products() - Edycja
python
def edit_products():
    product = input("Podaj nazwę produktu: ").lower().strip()
    if product not in products:
        print("Produkt nie istnieje!")
        return
    
    # Walidacja jak w add_product
    try:
        quantity = int(input("Nowa ilość: "))
        if quantity <= 0: return
        price = float(input("Nowa cena: "))
        if price <= 0: return
    except ValueError:
        print("Błędne dane!")
        return
    
    category = input("Nowa kategoria: ").lower().strip()
    
    # NADPISUJEMY konkretne pola
    products[product]["ilość"] = quantity
    products[product]["cena"] = price
    products[product]["kategoria"] = category
    
    print("Edycja OK!")
find_the_cheapest() - Najtańszy produkt
python
def find_the_cheapest(products):
    if not products:
        print("Brak produktów!")
        return
    
    # min() + lambda: porównuje po products[nazwa]["cena"]
    cheapest = min(products, key=lambda p: products[p]["cena"])
    price = products[cheapest]["cena"]
    
    print(f"Najtańszy: {cheapest} - {price:.2f} PLN")
🧠 KLUCZOWE KONCEPTY (WZORY NA PRZYSZŁOŚĆ)
1. Lambda z min/max/sorted
python
# Wzorzec dla zagnieżdżonego słownika
min(słownik, key=lambda klucz: słownik[klucz]["pole"])
max(słownik, key=lambda klucz: słownik[klucz]["pole"])
sorted(słownik, key=lambda klucz: słownik[klucz]["pole"])
2. Walidacja input
python
try:
    value = int(input("..."))
    if value <= 0: return
except ValueError:
    print("Błąd!")
    return
3. CRUD operations
text
CREATE → add_product()
READ   → show_products(), find_the_cheapest()
UPDATE → edit_products()  
DELETE → delete_product()
🚀 NASTĘPNE KROKI PROJEKTU (propozycje)
text
1. ZAPIS/ODCZYT DO PLIKU (JSON/CSV)
2. MENU GŁÓWNE z pętlą while
3. FILTROWANIE po kategorii
4. SORTowanie po cenie/ilości
5. Całkowity koszt listy zakupów
6. Usuwanie pustych produktów (ilość=0)
📝 PRZYKŁAD SESJI (jak powinieneś odpowiadać)
Użytkownik:

text
def moja_funkcja():
    x = input("...")
    # zły kod
Twoja odpowiedź:

text
Dobra próba, ale tu jest problem z [KONKRETNY BŁĄD].

1. Co konkretnie ma robić ta funkcja?
2. W tej linijce [WYJAŚNIJ BŁĄD]
3. Spróbuj poprawić tylko [KONKRETNY FRAGMENT]

Wklej swoją wersję, poprawimy iteracyjnie.