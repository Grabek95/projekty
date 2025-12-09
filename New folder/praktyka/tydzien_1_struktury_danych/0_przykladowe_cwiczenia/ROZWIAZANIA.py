"""
ROZWIĄZANIA - Ćwiczenia przykładowe
====================================

Ten plik zawiera kompletne rozwiązania wszystkich 3 ćwiczeń.

WAŻNE: Spróbuj najpierw sam! Zaglądaj tu tylko gdy utkniesz.
"""


def rozwiazanie_1():
    """
    ROZWIĄZANIE ĆWICZENIA 1: Lista owoców
    """
    print("=== LISTA OWOCÓW ===\n")

    # Tworzenie pustej listy
    owoce = []

    # Zbieranie 3 owoców
    owoc1 = input("Podaj pierwszy owoc: ")
    owoce.append(owoc1)

    owoc2 = input("Podaj drugi owoc: ")
    owoce.append(owoc2)

    owoc3 = input("Podaj trzeci owoc: ")
    owoce.append(owoc3)

    # Wyświetlenie listy
    print("\nTwoja lista owoców:")
    print(owoce)

    # BONUS: Wyświetlenie z numerami
    print("\nTwoje owoce (ponumerowane):")
    for index, owoc in enumerate(owoce, start=1):
        print(f"{index}. {owoc}")


def rozwiazanie_2():
    """
    ROZWIĄZANIE ĆWICZENIA 2: Ulubione kolory
    """
    print("=== ULUBIONE KOLORY ===")
    print("Podaj maksymalnie 5 kolorów (wpisz 'stop' aby zakończyć)\n")

    kolory = []

    # Pętla maksymalnie 5 razy
    for i in range(5):
        kolor = input(f"Podaj kolor {i+1}: ")

        # Sprawdzenie czy użytkownik chce zakończyć
        if kolor.lower() == "stop":
            print("Zakończono zbieranie kolorów.")
            break

        kolory.append(kolor)

    # Wyświetlenie zebranych kolorów
    print("\n" + "="*30)
    print("Twoje kolory:")
    for kolor in kolory:
        print(f"- {kolor}")

    # BONUS: Sprawdzenie czy czerwony jest na liście
    print("\n" + "="*30)
    if "czerwony" in kolory:
        print("Czerwony jest na Twojej liście!")
    else:
        print("Czerwony NIE jest na Twojej liście.")


def rozwiazanie_3():
    """
    ROZWIĄZANIE ĆWICZENIA 3: Kalkulator liczb
    """
    print("=== KALKULATOR LICZB ===")
    print("Podawaj liczby (wpisz 0 aby zakończyć)\n")

    liczby = []

    # Pętla nieskończona
    while True:
        liczba = float(input("Podaj liczbę: "))

        # Sprawdzenie warunku zakończenia
        if liczba == 0:
            print("Zakończono zbieranie liczb.\n")
            break

        liczby.append(liczba)

    # Sprawdzenie czy lista nie jest pusta
    if len(liczby) == 0:
        print("Nie podałeś żadnych liczb!")
        return

    # Obliczenia i wyświetlenie statystyk
    print("="*40)
    print("STATYSTYKI:")
    print("="*40)

    suma = sum(liczby)
    print(f"Suma:          {suma:.2f}")

    srednia = suma / len(liczby)
    print(f"Średnia:       {srednia:.2f}")

    najmniejsza = min(liczby)
    print(f"Najmniejsza:   {najmniejsza:.2f}")

    najwieksza = max(liczby)
    print(f"Największa:    {najwieksza:.2f}")

    # BONUS
    print(f"Ilość liczb:   {len(liczby)}")


# ============================================
# ALTERNATYWNE ROZWIĄZANIE ĆWICZENIA 1
# (bardziej kompaktowe - używa pętli)
# ============================================

def rozwiazanie_1_alternatywne():
    """
    ALTERNATYWNE ROZWIĄZANIE: Lista owoców (z pętlą)
    """
    print("=== LISTA OWOCÓW ===\n")

    owoce = []

    # Zamiast 3 osobnych input(), użyj pętli
    for i in range(3):
        owoc = input(f"Podaj owoc {i+1}: ")
        owoce.append(owoc)

    print("\nTwoja lista owoców:")
    print(owoce)

    print("\nTwoje owoce (ponumerowane):")
    for index, owoc in enumerate(owoce, start=1):
        print(f"{index}. {owoc}")


# ============================================
# MENU GŁÓWNE
# ============================================

def menu():
    """Menu do wyboru rozwiązania"""
    while True:
        print("\n" + "="*50)
        print("ROZWIĄZANIA - Ćwiczenia przykładowe")
        print("="*50)
        print("1. Rozwiązanie Ćwiczenia 1 (Lista owoców)")
        print("2. Rozwiązanie Ćwiczenia 2 (Ulubione kolory)")
        print("3. Rozwiązanie Ćwiczenia 3 (Kalkulator liczb)")
        print("4. Alternatywne rozwiązanie Ćwiczenia 1 (z pętlą)")
        print("0. Wyjście")
        print("="*50)

        wybor = input("\nWybierz opcję (0-4): ")

        if wybor == "1":
            print("\n")
            rozwiazanie_1()
        elif wybor == "2":
            print("\n")
            rozwiazanie_2()
        elif wybor == "3":
            print("\n")
            rozwiazanie_3()
        elif wybor == "4":
            print("\n")
            rozwiazanie_1_alternatywne()
        elif wybor == "0":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    menu()
