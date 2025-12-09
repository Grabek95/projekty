"""
ĆWICZENIE 1: Lista owoców
=========================

POZIOM: ŁATWE
CZAS: 5-10 minut

CEL:
Nauczyć się podstaw pracy z listami:
- Tworzenie pustej listy
- Dodawanie elementów metodą append()
- Wyświetlanie zawartości listy

ZADANIE:
Zapytaj użytkownika o 3 owoce, dodaj je do listy i wyświetl całą listę.
"""


def main():
    """Główna funkcja programu"""

    print("=== LISTA OWOCÓW ===\n")

    # TODO: Stwórz pustą listę o nazwie 'owoce'
    owoce = []

    # TODO: Zapytaj użytkownika o pierwszy owoc i dodaj go do listy
    # Wskazówka: użyj input() i append()
    owoc1 = input("Podaj pierwszy owoc: ")
    owoce.append(owoc1)
    print(f"Dodano do listy: {owoc1}\n")

    # TODO: Zapytaj użytkownika o drugi owoc i dodaj go do listy
    owoc2 = input("Podaj drugi owoc: ")
    owoce.append(owoc2)
    print(f"Dodano do listy: {owoc2}\n")

    # TODO: Zapytaj użytkownika o trzeci owoc i dodaj go do listy
    owoc3 = input("Podaj trzeci owoc: ")
    owoce.append(owoc3)
    print(f"Dodano do listy: {owoc3}\n")

    # TODO: Wyświetl komunikat "Twoja lista owoców:"
    print(f"Twoja lista owoców:")

    # TODO: Wyświetl całą listę
    # Wskazówka: po prostu print(owoce)
    print(f"{owoce}\n")

    # BONUS (opcjonalnie):
    # TODO: Wyświetl każdy owoc w osobnej linii z numerem
    # Wskazówka: użyj pętli for z enumerate()
    # Przykład: for index, owoc in enumerate(owoce, start=1):
    for index, owoc in enumerate(owoce, start=1):
        print(f"{index}. {owoc}")



if __name__ == "__main__":
    main()
