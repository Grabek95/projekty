"""
ĆWICZENIE 2: Ulubione kolory
============================

POZIOM: ŚREDNIE
CZAS: 10-15 minut

CEL:
Nauczyć się:
- Pętli for z range()
- Warunków if i instrukcji break
- Sprawdzania czy element jest w liście (operator 'in')

ZADANIE:
Program pyta użytkownika maksymalnie 5 razy o ulubiony kolor.
Jeśli użytkownik wpisze "stop", program kończy zbieranie danych wcześniej.
Na koniec wyświetl wszystkie zebrane kolory i sprawdź czy "czerwony" jest na liście.
"""


def main():
    """Główna funkcja programu"""

    print("=== ULUBIONE KOLORY ===")
    print("Podaj maksymalnie 5 kolorów (wpisz 'stop' aby zakończyć)\n")

    # TODO: Stwórz pustą listę 'kolory'
    kolory = []

    # TODO: Stwórz pętlę for która wykona się 5 razy
    # Wskazówka: for i in range(5):
    for i in range(5):

        # TODO: Zapytaj użytkownika o kolor
        kolor = input("Podaj kolor: ").lower()

        # TODO: Sprawdź czy użytkownik wpisał "stop"
        # Jeśli tak, przerwij pętlę (break)
        if kolor == "stop": 
            break

        # TODO: Dodaj kolor do listy
        kolory.append(kolor)


    # TODO: Wyświetl separator i komunikat
    print("\n" + "="*30)
    print("Twoje kolory:")

    # TODO: Wyświetl wszystkie kolory używając pętli for
    # Wskazówka: for kolor in kolory:
    for kolor in kolory:
        print(f"{kolor}")

    # BONUS:
    # TODO: Sprawdź czy "czerwony" jest w liście
    # Wskazówka: if "czerwony" in kolory:
    # Jeśli tak - wyświetl "Czerwony jest na Twojej liście!"
    # Jeśli nie - wyświetl "Czerwony NIE jest na Twojej liście."
    if "czerwony" in kolory:
        print("\nCzerwony jest na Twojej liście!")
    else:
        print("\nCzerwony NIE jest na Twojej liście.")


if __name__ == "__main__":
    main()
