"""
ĆWICZENIE 3: Kalkulator liczb
==============================

POZIOM: TRUDNIEJSZE
CZAS: 15-20 minut

CEL:
Nauczyć się:
- Pętli nieskończonej (while True)
- Konwersji typów (float)
- Funkcji matematycznych: sum(), min(), max()
- Obliczania średniej

ZADANIE:
Program w pętli zbiera liczby od użytkownika.
Gdy użytkownik wpisze 0, program kończy zbieranie i wyświetla statystyki:
- Suma wszystkich liczb
- Średnia arytmetyczna
- Najmniejsza liczba
- Największa liczba
"""


def main():
    """Główna funkcja programu"""

    print("=== KALKULATOR LICZB ===")
    print("Podawaj liczby (wpisz 0 aby zakończyć)\n")

    # TODO: Stwórz pustą listę 'liczby'
    liczby = []

    # TODO: Stwórz nieskończoną pętlę
    # Wskazówka: while True:
    while True:

        # TODO: Zapytaj użytkownika o liczbę i zamień ją na float
        # Wskazówka: liczba = float(input("Podaj liczbę: "))
        liczba = float(input("Podaj liczbę: "))

        # TODO: Sprawdź czy liczba == 0
        # Jeśli tak, przerwij pętlę (break)
        if liczba == 0:
            break

        # TODO: Dodaj liczbę do listy
        liczby.append(liczba)


    # Sprawdzenie czy lista nie jest pusta
    if len(liczby) == 0:
        print("Nie podałeś żadnych liczb!")
        return

    # TODO: Wyświetl separator
    print("\n" + "="*40)
    print("STATYSTYKI:")
    print("="*40)

    # TODO: Oblicz i wyświetl sumę wszystkich liczb
    # Wskazówka: suma = sum(liczby)
    suma = sum(liczby)
    print(f"Suma liczb wynosi: {suma}")

    # TODO: Oblicz i wyświetl średnią
    # Wskazówka: srednia = sum(liczby) / len(liczby)
    srednia = suma / len(liczby)
    print(f"Średnia liczb jest równa {srednia}")

    # TODO: Znajdź i wyświetl najmniejszą liczbę
    # Wskazówka: min(liczby)
    minimum = min(liczby)
    print(f"Najmniejsza liczba to: {minimum}")

    # TODO: Znajdź i wyświetl największą liczbę
    # Wskazówka: max(liczby)
    maximum = max(liczby)
    print(f"Największa liczba to: {maximum}")

    # BONUS:
    # TODO: Wyświetl ile liczb zostało podanych
    # Wskazówka: len(liczby)
    if len(liczby) == 1:
        print(f"Została podana {len(liczby)} liczba.")
    elif 2 <= len(liczby) <= 4: # można też użyć in [2, 3, 4]
        print(f"Zostały podane {len(liczby)} liczby.")
    else:
        print(f"Zostały podane {len(liczby)} liczb.")

if __name__ == "__main__":
    main()
