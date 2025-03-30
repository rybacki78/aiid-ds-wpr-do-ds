def zadanie_1():
    """
    Zadanie 1

    Napisz skrypt, który pobiera od użytkownika zdanie i liczy w nim spacje. Wynik wyświetla na ekranie (użyj instrukcji input).
    """

    tekst = input("Podaj jakis tekst:\n")
    spacje = 0

    for znak in tekst:
        if znak == " ":
            spacje += 1

    print("Liczba spacji:", spacje)

    ### alternatywnie
    spacje = tekst.count(" ")

    print("Liczba spacji:", spacje)


def zadanie_3():
    """
    Napisz skrypt, który pobiera od użytkownika trzy liczby a, b i c. Sprawdza następujące warunki:

    czy a zawiera się w przedziale (0,10]
    oraz czy jednocześnie a>b lub b>c.

    Jeśli warunki są spełnione lub nie to ma się wyświetlić odpowiedni komunikat na ekranie.
    """

    a = input("Liczba a:\n")
    b = input("liczba b:\n")
    c = input("Liczba c:\n")

    if a.isdigit() and b.isdigit() and c.isdigit():
        a = int(a)
        b = int(b)
        c = int(c)
        if (0 < a <= 10) and (a > b or b > c):
            print(
                f"{a} jest w przedziale (0,10) oraz {a} jest większe od {b} lub {b} jest wieksze od {c} "
            )
        else:
            print("Twoje liczby nie spełniają warunków z treści zadania.")

    else:
        print("Hej, nie wpisałeś trzech liczb!")


def zadanie_4():
    """
    Napisz pętlę, która wyświetla liczby podzielne przez 5 z zakresu [0,50]
    """

    for liczba in range(51):  # 51 iteracji
        if liczba % 5 == 0:
            print(liczba)

    ### alternatywnie - mniej iteracji tylko 11
    for liczba in range(0, 51, 5):
        print(liczba)


def zadanie_5():
    """
    Napisz pętle (while), która pobiera liczby od użytkownika i wyświetla ich kwadraty na ekranie. Liczby pobierane są w postaci oddzielonej spacjami. Pętla kończy działanie po wpisaniu słowa quit.
    """

    # dobre ale nie zakłada spacji tylko pojedyncze cyfry
    while True:

        liczba = input("Podaj liczbę:\n")

        if liczba == "quit":
            break
        elif liczba.isdigit():
            liczba = int(liczba)
            print(f"{liczba} do kwadratu to {liczba ** 2}")
        else:
            print("To nie jest liczba!")

    # poprawnie z trescia zadania
    while True:

        liczby = input("Podaj liczby:\n")

        if liczby == "quit":
            break

        liczby = liczby.split()
        for liczba in liczby:
            # sprawdzenie czy to są liczby
            if not liczba.isdigit():
                continue
            else:
                liczba = int(liczba)
                print(f"Kwadrat liczby {liczba} to {liczba ** 2}")


def zadanie_7():
    """
    Napisz skrypt, który odczytuje od użytkownika liczbę wielocyfrową i sumuje jej cyfry. Wynik wyświetla na ekranie. Napisz dwa rozwiązania: jedno z uzyciem pętli for a drugie z użyciem pętli while.
    """

    # pętla for
    wejscie = input("Podaj liczbe:\n")

    suma = 0

    for znak in wejscie:
        suma += int(znak)

    print(f"Suma to: {suma}")

    # pętla while
    index = 0
    suma_wh = 0

    while index < len(wejscie):
        suma_wh = suma_wh + int(wejscie[index])
        index += 1

    print(f"suma z while: {suma_wh}")


def zadanie_9():
    """
    Napisz skrypt, który wyświetla i oblicza tabliczkę mnożenia od 1 do 100 w formie znanej z lekcji matematyki w szkole podstawowej. W formie ładnej :) tabeli
    """

    n = 20

    max_digits = len(str(n ** 2)) + 1

    print(' ' * max_digits, end='')
    for naglowek in range(1, n + 1):
        print(f'{naglowek:>{max_digits}}', end='')
    print()

    for wiersz in range(1, n + 1):
        print(f'{wiersz:>{max_digits}}', end='')
        for kolumna in range(1, n + 1):
            print(f'{wiersz * kolumna:>{max_digits}}', end='')
        print()


def main():
    # zadanie_1()
    # zadanie_3()
    # zadanie_4()
    # zadanie_5()
    # zadanie_7()
    zadanie_9()


if __name__ == "__main__":
    main()
