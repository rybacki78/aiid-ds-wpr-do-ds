def zadanie_1():
    """
    Zadanie 1

    Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak,
    aby pierwsze 5 liczb zostało w oryginalnej liście, a pozostałe 5 znalazło się w nowej liście.
    """

    print("---- Zdanie 1 ----")
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = list1[5:]
    list1 = list1[:5]
    print(list1)
    print(list2)

    print("-" * 18)


def zadanie_2():
    """
    Zadanie 2

    Połącz te listy ponownie. Dodaj do listy wartość „0” na początku. Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco.
    """

    print("---- Zdanie 2 ----")
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = list1[5:]
    list1 = list1[:5]
    list1 = list1 + list2
    list1.insert(0, 0)
    list3 = (
        list1.copy()
    )  # płytka kopia kopiuje tylko referencje listy pierwszego poziomu

    # kopia głęboka
    from copy import deepcopy

    list4 = deepcopy(list1)  # głęboka kopia kopiuje wszystkie elementy listy
    ###############

    list3.sort(reverse=True)
    print(list3)

    print("-" * 18)


def zadanie_4():
    """
    Zadanie 4"
    Stwórz słownik gdzie kluczami będą numery miesięcy (rozpoczynając od 1), a wartościami nazwy polskich miesięcy.
    """

    print("---- Zdanie 4 ----")
    miesiace = {
        1: "Styczeń",
        2: "Luty",
        3: "Marzec",
        4: "Kwiecień",
        5: "Maj",
        6: "Czerwiec",
        7: "Lipiec",
        8: "Sierpień",
        9: "Wrzesień",
        10: "Październik",
        11: "Listopad",
        12: "Grudzień",
    }
    print(miesiace)

    print("-" * 18)


def zadanie_5():
    """
    Zadanie 5

    Stwórz podobny słownik jak w zadaniu 4, ale z angielskimi nazwami miesięcy.
    Połącz teraz słowniki tak, żeby przykładowo dla kwietnia, dostać się poprzez wyrażenie: months['pl'][4] a dla wersji angielskiej poprzez months['en'][4].
    """

    print("---- Zdanie 5 ----")
    miesiace = {
        1: "Styczeń",
        2: "Luty",
        3: "Marzec",
        4: "Kwiecień",
        5: "Maj",
        6: "Czerwiec",
        7: "Lipiec",
        8: "Sierpień",
        9: "Wrzesień",
        10: "Październik",
        11: "Listopad",
        12: "Grudzień",
    }
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    miesiace_pl_en = {"pl": miesiace, "en": months}
    print(miesiace_pl_en["pl"][4])
    print(miesiace_pl_en["en"][4])

    print("-" * 18)


def zadanie_6():
    """
    Zadanie 6

    Wykorzystując ciąg tekstowy 'Marianna' oraz metodę fromkeys() dla słowników stwórz słownik,
    który będzie zawierał jako klucze unikalne litery w/w imienia a jako wartość każdy klucz będzie miał przypisaną wartość 1.
    Poprawne wyjście: {'M': 1, 'a': 1, 'r': 1, 'i': 1, 'n': 1}
    """

    print("---- Zdanie 6 ----")
    imie = "Marianna"
    slownik = dict.fromkeys(imie, 1)
    print(slownik)

    print("-" * 18)


def main():
    zadanie_1()
    zadanie_2()
    zadanie_4()
    zadanie_5()
    zadanie_6()


if __name__ == "__main__":
    main()
