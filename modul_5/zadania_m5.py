def zadanie_1():
    """
    Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
    A={1/x: x∈<1,10>}
    B={1, 2, 4, 8,…, $2^{10}$}
    C={x: x∈ B i x jest liczbą podzielną przez 4}
    """

    A = [1 / x for x in range(1, 11)]
    print(A)

    B = [2**i for i in range(11)]
    print(B)

    B = [x for x in B if x % 4 == 0]
    print(B)


def zadanie_2():
    """
    Wygeneruj macierz (lista dwupoziomowa) losowych wartości (sprawdź pakiet random) o rozmiarach 4x4 i wykorzystując Python Comprehension zdefiniuj zmienną typu list, która będzie zawierała tylko elementy znajdujące się na przekątnej tej macierzy.
    """

    import random as rd

    matrix = [[rd.randint(1, 100) for _ in range(4)] for _ in range(4)]
    print(matrix)

    list = [matrix[idx][idx] for idx in range(len(matrix))]
    print(list)


def main():
    # zadanie_1()
    zadanie_2()


if __name__ == "__main__":
    main()
