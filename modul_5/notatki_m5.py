# Python comprehensions

# zamiast pisać w pętli
lista = []
for element in range(5):
    if element > 0:
        lista.append(element * element)

# możemy zapisać w jednej linijce
lista = [element * element for element in range(5) if element > 0]
# co - jak - warunki


wejscie = input()
liczby = []

# zagnieżdżone
for liczba in wejscie.split():
    if liczba.isdigit():
        liczby.append(int(liczba))

# flat - płaskie
liczby = [int(liczba) for liczba in wejscie.split() if liczba.isdigit()]


# przykłady
A = [x**2 for x in range(10)]
B = [3**i for i in range(6)]
C = [x for x in A if x % 2 != 0]

print(A)
print(B)
print(C)

# chcemy uzyskać liczby parzyste z podanego zakresu
# wersja z pętlą
liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = []

for i in liczby:
    if i % 2 == 0:
        lista.append(i)

print("Liczby parzyste uzyskane z wykorystaniem pętli")
print(lista)

# wersja z Python comprehension
lista2 = [i for i in liczby if i % 2 == 0]
print(lista2)


# zagnieżdżanie
# zamiast pisać tak:
lista = []
for i in [1, 2, 3]:
    for j in [4, 5, 6]:
        if i != j:
            lista.append((i, j))
print(lista)

# można to zrobić krócej
lista2 = [(i, j) for i in [1, 2, 3] for j in [4, 5, 6] if i != j]
print(lista2)

# słowniki i zamiana klucza z wartością
skroty = {"PZU": "Państwowy zakład Ubezpieczeń",
"ZUS": "Zakład Ubezpieczeń Społecznych",
"PKO": "Powszechna Kasa Oszczędności"}
odwrocone = {value: key for key, value in skroty.items()}

print("Oryginalny słownik")
print(skroty)
print("Słownik odwrócony")
print(odwrocone)


## Funkcje
# 
# def nazwa_funkcji(arg_pozycyjny, arg_domyslny=wartosc, *arg_4, **arg_5):
#     instrukcje
#     ...
#     [ return wartość ] # opcjonalne
#
# *arg_4 dowolna liczna argumentów przekazywana jako krotka do funkcji
# **arg_5 dowolna ilosc argumentów i przechowuje w słowniku