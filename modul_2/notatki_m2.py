print("Hello, World!")

x = 1 // 2

print(x)
print(type(x))

# this is comment

print("Adam" + str(3)) # Adam3 rzutowanie 3 na string
print("Adam" * 4) # AdamAdamAdamAdam

print ("_" * 20) # 20x _

print (bool(0)) # False
print (bool(1)) # True

print ('a' in 'abc') # True
print (1 in [1,2,3]) # True

print("1" in "1111111")  # działa
# print (1 in 11111111) # nie działa

print("_" * 30)
lista = [1, 2, 3, 4, 5]
if lista:
    print("Lista nie jest pusta")
else:
    print("Lista jest pusta")

print("_" * 30)
liczba = 56.0
print(type(liczba))

print("_" * 30)
print((0.1 + 0.2) == 0.3)  # False
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")

print("_" * 30)
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True

print("_" * 30)
liczba = 1
print(liczba.__str__())  # dunders

print("_" * 30)


class Osoba:
    pass


o = Osoba()
o.__class__.__name__
print(o)  # method resolution order

print("_" * 30)
imie = "JaaAan"
a = imie.count("a")
print(a)
a = imie.lower().count("a")  # method chaining
print(a)

print("_" * 30)
imie = "a" + imie[1:]
print(imie)

print("_" * 30)  # czas wykonania operacji - fajowe
from timeit import timeit

setup = """imie = 'Alicja'"""

snippet_1 = """ 
imie = imie.lower()
"""

snippet_2 = """ 
imie = 'a' + imie[1:]
"""
snippet_3 = """ 
imie = imie[0].lower() + imie[1:]
"""
repeats = 1000000

print(timeit(snippet_1, setup=setup, number=repeats))
print(timeit(snippet_2, setup=setup, number=repeats))
print(timeit(snippet_3, setup=setup, number=repeats))

# wycinek stringa - zwraca nowy string
# wycinek zawsze zwraca nowy obiekt tego samego typu
print("_" * 30)
print(imie[::-1])  # odwrócenie stringa
print(imie[:-4:-1])  # odwrócenie stringa i wycięcie 3 ostatnich znaków

print("_" * 30)
log = "2024-03-09 12:00:00 INFO Log message"

log_date = slice(0, 10)
log_time = slice(11, 19)
log_level = slice(20, 24)
log_message = slice(25, None)

print(log[log_date])
print(log[log_time])
print(log[log_level])
print(log[log_message])

print("_" * 30)
log = """2024-03-09 12:00:00 INFO Log message
2024-03-10 12:00:00 INFO Log message
2024-03-11 12:00:00 INFO Log message
2024-03-12 12:00:00 INFO Log message
"""
log_date = slice(0, 10)
log_time = slice(11, 19)
log_level = slice(20, 24)
log_message = slice(25, None)

for log_entry in log.split("\n"):
    print(log_entry[log_date], log_entry[log_time], log_entry[log_level])

print("_" * 30)
sentence = "ala ma kota"

print(sentence.capitalize())  # zmiana pierwszej litery na wielką
print(sentence.upper())  # zmiana na wielkie litery
print(sentence.title())  # zmiana pierwszej litery każdego słowa na wielką
print(sentence.lstrip())  # usuwa białe znaki z lewej strony
print(sentence.strip())  # usuwa białe znaki z obu stron
print(sentence.replace(" ", ""))  # usuwa spacje
print(sentence.split(" "))  # dzieli zdanie na słowa
print(sentence.isalnum())  # sprawdza czy zdanie składa się z liter i cyfr
print(sentence.isdigit())  # sprawdza czy zdanie składa się z samych cyfr

print("|".join(sentence))  # łączy znaki w zdaniu za pomocą znaku "|"


print("_" * 30)
# imie, wiek, punkty
row = "Alicja, 25, 100"

print(row.split(","))  # dzieli zdanie na słowa

# print i f-string
print("_" * 30)
print("Adam ma ", 23, "lata.")
print(5, end="")  # nie dodaje znaku nowej linii
print(5, 6, 7, sep="|", end="")  # separator i brak nowej linii
print()

imie = "Adam"
print(imie)
print(*imie)  # rozbija stringa na pojedyncze znaki. sequence unpacking

print(f"{imie} ma 23 lata.")  # f-string

num = 3.33333333333333333333333333
print(f"{num:.2f}")  # zaokrąglenie do 2 miejsc po przecinku
print(f"{num:.2e}")  # zapis w notacji naukowej
print(f"{num:2.5f}")  # 2 miejsca przed przecinkiem i 5 po
print(f"{num:^20}")  # wyśrodkowanie w 20 znakach
print(f"{num:_>30}")  # wypełnienie znakiem _ do 20 znaków

from datetime import datetime

data_dz = datetime.now()
print(data_dz)  # data i czas
print(f"{data_dz:%Y-%m-%d %H:%M:%S}")  # formatowanie daty

# sekwencje sterujące
print("_" * 30)
print("\sciezka\rok\numer\task") # \n nowa linia, \t tabulator
print("\\sciezka\\rok\\numer\\task") # backslash
print(r"\sciezka\rok\numer\task") # raw string

print ("elo\r", end="") # \r - powrót karetki

print("elo2")

# znaki specjalne
print("_" * 30)
print("\u2764") # serce
print("\U0001F600") # uśmiech
print("\U00000041") # A