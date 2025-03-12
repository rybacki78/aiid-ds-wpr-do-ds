def zadanie1():
    """
    ## Zadanie 1

    Napisz fragment kodu, który wczyta trzy zmienne ze standardowego wejścia (np. funkcja input()):

    * linię danych rozdzielonych jakimś separatorem (spacja, średnik, itd.)
    * separator źródłowy
    * separator docelowy

    Następnie zaimplementuj z użyciem metod str.split() oraz str.join()
    podzielenie danych wejściowych pierwszym separatorem,
    połączenie i wypisanie danych połączonych drugim separatorem.
    Czy można to zrobić prościej wykorzystując inne wbudowane metody?
    """

    print("---- Zdanie 1 ----")
    daneWe = input("Podaj dane wejściowe:\n")
    sepZrd = input("Podaj separator źródłowy:\n")
    sepDoc = input("Podaj separator docelowy:\n")

    daneSplit = daneWe.split(sepZrd)
    daneJoin = sepDoc.join(daneSplit)
    print(daneJoin)

    # druga, prostsza metoda
    daneZmienione = daneWe.replace(sepZrd, sepDoc)
    print(daneZmienione)

    print("-" * 18)


def zadanie2():
    """
    ## Zadanie 2

    Użyj funkcji input() aby pobrać łańcuch znaków z klawiatury i z użyciem wycinków (slice) wykonaj:

    * podziel łańcuch na dwie części, w miarę możliwości równe, ale jeżeli długość łańcucha jest nieparzysta, np. 11 znaków to pierwszy ma długość 5, a drugi 6. Wyświetl te łańcuchy w oknie konsoli.
    * wyświetl łańcuch składający się z co drugiego znaku licząc od końca łańcucha
    """

    print("---- Zdanie 2 ----")
    daneWe = input("Podaj dane wejściowe:\n")

    slice = len(daneWe) // 2
    print(daneWe[slice:])
    print(daneWe[:slice])
    print(daneWe[::-2])

    print("-" * 18)


def zadanie3():
    """
    Zadanie 3

    Wyświetl na konsoli dowolny ciąg znaków i wykorzystaj wbudowane metody:
       * title(),
       * capitalize(),
       * zfill(),
       * upper(),
       * count(),
       * center().
    """

    print("---- Zdanie 3 ----")
    daneWe = "Ala ma kota."

    print(daneWe.title())
    print(daneWe.capitalize())
    print(daneWe.zfill(30))
    print(daneWe.upper())
    print(daneWe.count("a"))
    print(daneWe.center(50))

    print("-" * 18)


def zadanie4():
    """
    Zadanie 4

    Wprowadź z klawiatury dowolny łańcuch znaków i zapisz go do zmiennej.

    Następnie bazując na przykładzie poniżej zapisz również wyniki dla metod isalpha(), isascii(), isprintable(), istitle(), isupper().

    wejscie = input() print(f"Łańcuch {wejscie} isdecimal: {wejscie.isdecimal()}").
    """

    print("---- Zdanie 4 ----")
    daneWe = input("Podaj ciąg znaków:\n")

    print(f"Łańcuch {daneWe} isaplha(): {daneWe.isalpha()}")
    print(f"Łańcuch {daneWe} isascii(): {daneWe.isascii()}")
    print(f"Łańcuch {daneWe} isprintable(): {daneWe.isprintable()}")
    print(f"Łańcuch {daneWe} istitle(): {daneWe.istitle()}")
    print(f"Łańcuch {daneWe} isupper(): {daneWe.isupper()}")

    print("-" * 18)


def zadanie5():
    """
    Zadanie 5

    Przejdź na stronę https://pyformat.info/,
    a następnie zapisz w oddzielnym pliku .py i wykonaj 5 wybranych przykładów formatowania ciągów oznaczonego jako „New”,
    których nie było w przykładach z tego podrozdziału (np. z wyrównaniem do prawej lub lewej strony, ilością pozycji liczby,
    znakiem, wypełnieniem spacji itp.). Przerób zaprezentowane tam przykłady na postać z użyciem f-string.
    """

    print("---- Zdanie 5 ----")

    ciag = "Ala ma kota."
    print(f"{ciag:>20}")  # wyrównanie do prawej
    print(f"{ciag:<20}")  # wyrównanie do lewej
    liczba = 1234567890
    print(f"{liczba:,}")  # separator tysięcy
    pozycje = 40
    print(f"{liczba:0{pozycje}d}")

    print("-" * 18)


def zadanie6():
    """
    Zadanie 6

    Wykorzystując listing 10 wypisz na konsoli 10 wybranych znaków niestandardowych
    (np. litery z alfabetu greckiego, symbole walut - (funt, bitcoin)) wypisując jednocześnie jego kod z tablicy unicode.
    """

    print("---- Zdanie 6 ----")
    print("\u20bf")  # bitcoin
    print("\u2764")  # serce
    print("\U0001f600")  # uśmiech
    print("\U0001f616")  # zły
    print("\U0001f528")  # młotek
    print("\U0001f170")  # A
    print("\U0001f0a3")  # domino
    print("\u20a4")  # funt
    print("\u03b1") # mała alfa
    print("\u03a9")  # omega


    print("-" * 18)


def main():
    zadanie1()
    zadanie2()
    zadanie3()
    zadanie4()
    zadanie5()
    zadanie6()


if __name__ == "__main__":
    main()
